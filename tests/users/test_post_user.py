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

keys_requireds = ["city_id", "gender_id", "role_id", "name", "email", "password"]

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