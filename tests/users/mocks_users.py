payload = {
    "city_id": 1566,
    "gender_id": 1,
    "role_id": 1,
    "name": "João Victor",
    "age": "01/01/2000",
    "email": "joao2@email.com",
    "phone": "48999999999",
    "password": "teste123*A",
    "cep": "80130780",
    "street": "Almeida street",
    "district": "Capoeiras",
    "number_street": 210,
}

configs = {
    "url_base": "/inventory/",
    "url_product_code": "/inventory/1",
    "product_code": 1,
}

keys_allow_patch = [
    "cep",
    "street",
    "district",
    "number_street",
    "phone",
    "city_id",
    "gender_id",
    "role_id",
    "name",
    "email",
    "password",
]
keys_not_allow_patch = ["id"]

keys_requireds = [
    "city_id",
    "gender_id",
    "role_id",
    "name",
    "email",
    "password",
]
keys_not_requireds = ["cep", "street", "district", "number_street", "phone", "age"]


def headers(logged_in_client):
    return {"Authorization": f"Bearer {logged_in_client}"}
