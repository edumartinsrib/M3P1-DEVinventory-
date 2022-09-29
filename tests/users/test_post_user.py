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
        "number_street": 210
}

keys_requireds = ["city_id", "gender_id", "role_id", "name", "email", "password", ]
keys_not_requireds = ["cep", "street", "district", "number_street", 'phone']

def test_post_user_success(client, logged_in_client):
    """Test of the post user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}

    response = client.post("/user/", headers=headers, json=payload)

    assert response.status_code == 201
    
def test_post_user_with_email_already_exists(client, logged_in_client):
    """Test of the post user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.post("/user/", headers=headers, json=payload)
    payload_test = payload.copy()
    payload_test["email"] = "joao@email.com"
    
    if response.status_code == 400 and response.json:
        assert response.json["error"] == "{'email': ['Email já registrado']}"

def test_post_with_invalid_token(client, logged_in_client):
    """Test of the post user route with an invalid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}123"}
    response = client.post("/user/", headers=headers, json=payload)
    
    assert response.status_code == 403
    
def test_post_with_invalid_payload(client, logged_in_client):
    """Test of the post user route with an invalid payload - without required fields"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    for key in keys_requireds:
        payload_test = payload.copy()
        payload_test.pop(key)
        response = client.post("/user/", headers=headers, json=payload_test)

        if response.status_code == 400 and response.json:
            assert response.json["error"] == f"{{'{key}': ['{key} é obrigatório.']}}"
        else:
            assert False

def test_post_success_without_not_requireds_fields(client, logged_in_client):
    """Test of the post user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    payload_test = payload.copy()
    for key in keys_not_requireds:
        payload_test.pop(key)
        payload_test["email"] = f"email{key}@email.com"
    response = client.post("/user/", headers=headers, json=payload_test)
        
    assert response.status_code == 201

def test_post_with_invalid_payload_password(client, logged_in_client):
    """Test of the post user route with an invalid payload - password"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    payload_test = payload.copy()
    payload_test["password"] = "teste123"
    response = client.post("/user/", headers=headers, json=payload_test)
    
    if response.status_code == 400 and response.json:
        assert response.json["error"] == "{'password': ['Senha fraca, utilize letras maiúsculas, minúsculas, números e caracteres especiais']}"
    else:
        assert False
        
        
def test_with_invalid_payload_telephone(client, logged_in_client):
    """Test of the post user route with an invalid payload - telephone"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    payload_test = payload.copy()
    payload_test["phone"] = "4899999999"
    response = client.post("/user/", headers=headers, json=payload_test)
    
    if response.status_code == 400 and response.json:
        assert response.json["error"] == "{'phone': ['Telefone inválido']}"
    else:
        assert False
        
def test_with_invalid_payload_email(client, logged_in_client):
    """Test of the post user route with an invalid payload - email"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    payload_test = payload.copy()
    payload_test["email"] = "joaoemail.com"
    response = client.post("/user/", headers=headers, json=payload_test)
    
    if response.status_code == 400 and response.json:
        assert response.json["error"] == "{'email': ['email inválido.']}"
    else:
        assert False
        
def test_with_invalid_payload_age(client, logged_in_client):
    """Test of the post user route with an invalid payload - age"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    payload_test = payload.copy()
    payload_test["age"] = "2000/01/01"
    response = client.post("/user/", headers=headers, json=payload_test)
    
    if response.status_code == 400 and response.json:
        assert response.json['error'] == "time data '2000/01/01' does not match format '%d/%m/%Y'"
    else:
        assert False
        
def test_with_invalid_payload_city_id(client, logged_in_client):
    """Test of the post user route with an invalid payload - city_id"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    payload_test = payload.copy()
    payload_test["city_id"] = "teste"
    response = client.post("/user/", headers=headers, json=payload_test)
    
    if response.status_code == 400 and response.json:
        assert response.json["error"] == "{'city_id': ['city_id inválido.']}"
    else:
        assert False

def test_with_invalid_payload_gender_id(client, logged_in_client):
    """Test of the post user route with an invalid payload"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    payload_test = payload.copy()
    payload_test["gender_id"] = 5
    response = client.post("/user/", headers=headers, json=payload_test)
    
    if response.status_code == 400 and response.json:
        assert response.json["error"] == "{'gender_id': ['Gênero não encontrado.']}"
    else:
        assert False
        