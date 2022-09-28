from flask import Blueprint, abort, jsonify, request

from src.app import DB
from src.app.middlewares.auth import requires_access_level
from src.app.models.inventory import Inventory
from src.app.models.user import User
from src.app.services.inventory_service import create_product, update_product
from src.app.utils import format_currency

inventory = Blueprint("inventory", __name__, url_prefix="/inventory")


@inventory.route("/", methods=["POST"])
@requires_access_level(["WRITE"])
def add_new_product():
    """Example endpoint post in the database an inventory
    This is using docstrings for specifications.
    ---
    parameters:
      - name: product_category_id
        in: body
        type: interger
        required: true
      - name: user_id
        in: body
        type: interger
        required: false
	default: None
      - name: product_code
        in: body
        type: interger
        required: true
      - name: title
        in: body
        type: string
        required: true
      - name: value
        in: body
        type: float
        required: true
      - name: brand
        in: body
        type: string
        required: true
      - name: template
        in: body
        type: string
        required: true
      - name: description
        in: body
        type: string
        required: true
    definitions:
      id:
        type: interget
      product_category_id: 
        type: interger
      user_id:
        type: interger
      title: 
        type: string
      product_code:
        type: interger
      value:
        type: interger
      brand:
        type: string
      template:
        type: string
      description:
        type: string
    responses:
        201:
            description: Sucesso
        400:
            description: Invalido
        403:
            description: Error permission
    """
    data = request.get_json()
    response = create_product(data)
    
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 201


@inventory.route("/", methods=["GET"])
@requires_access_level(["READ"])
def get_product_by_user_name():
    """Example endpoint get in the database an inventory
    This is using docstrings for specifications.
    ---
    parameters:
      - name: name
        in: body
        type: string
        required: true
    definitions:
      id:
        type: interget
      product_category_id: 
        type: interger
      user_id:
        type: interger
      title: 
        type: string
      product_code:
        type: interger
      value:
        type: interger
      brand:
        type: string
      template:
        type: string
      description:
        type: string
    responses:
        200:
            description: Sucesso
        403:
            description: Erro permission
        204:
            description: Error não encontrado
    """
    page = request.args.get("page", 1, type=int)
    per_page = 20

    if not request.args.get("name"):
        query = DB.session.query(Inventory).slice(
            (page - 1) * per_page, page * per_page
        )
        result = []
        for product in query:
            result.append(product.format())

        if not result:
            return jsonify({"Status": "Dados não encontrados"}), 204
        else:
            return jsonify({"Status": "Sucesso", "Dados": result}), 200
    else:
        query = (
            DB.session.query(Inventory)
            .join(User)
            .filter(User.name.ilike("%" + request.args.get("name") + "%"))
            .slice((page - 1) * per_page, page * per_page)
        )
        result = []
        for item in query:
            result.append(item.format())

        if not result:
            return jsonify({"Status": "Dados não encontrados"}), 204
        else:
            return jsonify({"Status": "Sucesso", "Dados": result}), 200


@inventory.route("/results", methods=["GET"])
@requires_access_level(["READ"])
def get_all_products():
    """Example endpoint get in the database an inventory
    This is using docstrings for specifications.
    ---
    definitions:
      id:
        type: interget
      product_category_id: 
        type: interger
      user_id:
        type: interger
      title: 
        type: string
      product_code:
        type: interger
      value:
        type: interger
      brand:
        type: string
      template:
        type: string
      description:
        type: string
    responses:
        200:
            description: Sucesso
        403:
            description: Error permission
    """
    products = Inventory.query.all()
    users = User.query.all()

    resultado = {
        "numero de usuários": len(users),
        "quantidade de produtos": len(products),
        "valor total de itens": format_currency(
            sum([product.value for product in products])
        ),
        "itens emprestados": len(
            [
                product.user_id
                for product in products
                if product.user_id is not None or product.user_id == 0
            ]
        ),
    }

    return jsonify(resultado), 200


@inventory.route("/<int:id>", methods=["PATCH"])
@requires_access_level(["UPDATE"])

def patch_product(id):
    """Example endpoint PATH in the database an inventory
    This is using docstrings for specifications.
    ---
    parameters:
      - name: id
        in: body
        type: interger
        required: true
      - name: user_id
        in: body
        type: interger
        required: false
	default: None
      - name: title
        in: body
        type: string
        required: false
      - name: value
        in: body
        type: float
        required: false
      - name: brand
        in: body
        type: string
        required: false
      - name: template
        in: body
        type: string
        required: false
      - name: description
        in: body
        type: string
        required: false
    definitions:
      id:
        type: interget
      product_category_id: 
        type: interger
      user_id:
        type: interger
      title: 
        type: string
      product_code:
        type: interger
      value:
        type: interger
      brand:
        type: string
      template:
        type: string
      description:
        type: string
    responses:
        204:
            description: No Content
        400:
            description: Invalido
        403:
            description: Error permission    
    """
    if id is None or id == 0 or not request.json:
        abort(400)
    data = request.get_json()
    result = update_product(data, id)
    
    if "error" in result:
        return jsonify(result), 400
    
    return jsonify({"status": "Produto atualizado com sucesso!", "Dados": result}), 204
