
payload = {
        "city_id": 1566,
        "gender_id": 1,
        "role_id": 1,
        "name": "João Victor",
        "age": "01/01/2000",
        "email": "joao2@email.com",
        "phone": "48999999999",
        "password": "teste123*A",
        "cep": '80130780',
        "street": "Almeida street",
        "district": "Capoeiras",
        "number_street": 210
}

keys_allow_patch = ["cep", "street", "district", "number_street", 'phone', "city_id", "gender_id", "role_id", "name", "email", "password", ]
keys_not_allow_patch = ['id']

def test_patch_user_success(client, logged_in_client):
    """Test of the patch user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    user = 2
        
    response = client.patch(f"/user/{user}", headers=headers, json=payload)
    
    assert response.status_code == 204

def test_patch_user_with_invalid_token(client, logged_in_client):
    """Test of the patch user route with a invalid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}123"}
    user = 2
    payload_test = payload.copy()
    payload_test["email"] = "emailTeste@gmail.com"
    response = client.patch(f"/user/{user}", headers=headers, json=payload_test)
    assert response.status_code == 403

def test_patch_user_invalid_field(client, logged_in_client):
    """Test of the patch user route with a invalid filed """
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    user = 2
    payload_test = payload.copy()
    payload_test["id"] = "invalid_field"
    response = client.patch(f"/user/{user}", headers=headers, json=payload_test)
    
    assert response.status_code == 400
    
def test_patch_user_not_found(client, logged_in_client):
    """Test of the patch user not found """
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    user = 999
    payload_teste = {"cep": '99999'}
    
    response = client.patch(f"/user/{user}", headers=headers, json=payload_teste)
    
    assert response.status_code == 404
    
def test_patch_user_with_not_required_fields(client, logged_in_client):
    """Test of the patch user not found """
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    user = 2
    for key in keys_allow_patch:
        payload_test = payload.copy()
        payload_test["email"] = f"email{key}@email.com"            
        payload_test.pop(key)
        response = client.patch(f"/user/{user}", headers=headers, json=payload_test)
        assert response.status_code == 204

def test_patch_user_with_email_registered(client, logged_in_client):
    """Test of the patch user with email registered """
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    payload_test = payload.copy()
    payload_test["email"] = "joao@email.com"
    response = client.patch(f"/user/{1}", headers=headers, json=payload_test)
    
    if response.status_code == 400 and response.json:
        assert response.json["error"] == "{'email': ['Email já registrado']}"