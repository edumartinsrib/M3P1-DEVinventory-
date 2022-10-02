from mocks_users import headers, keys_allow_patch, payload


def test_patch_user_success(client, logged_in_client):
    """Test of the patch user route with a valid token"""
    user = 2
    response = client.patch(f"/user/{user}", headers=headers(logged_in_client), json=payload)
    
    assert response.status_code == 204

def test_patch_user_fail_with_invalid_token(client, logged_in_client):
    """Test of the patch user route with a invalid token"""
    user = 2
    payload_test = payload.copy()
    payload_test["email"] = "emailTeste@gmail.com"
    response = client.patch(f"/user/{user}", headers=headers(f"{logged_in_client}123"), json=payload_test)
    assert response.status_code == 403

def test_patch_user_fail_invalid_field(client, logged_in_client):
    """Test of the patch user route with a invalid filed """
    user = 2
    payload_test = payload.copy()
    payload_test["id"] = "invalid_field"
    response = client.patch(f"/user/{user}", headers=headers(logged_in_client), json=payload_test)
    
    assert response.status_code == 400
    
def test_patch_user_fail_not_found(client, logged_in_client):
    """Test of the patch user not found """
    user = 999
    payload_teste = {"cep": '99999'}
    
    response = client.patch(f"/user/{user}", headers=headers(logged_in_client), json=payload_teste)
    
    assert response.status_code == 404
    
def test_patch_user_success_with_not_required_fields(client, logged_in_client):
    """Test of the patch user not found """
    user = 2
    for key in keys_allow_patch:
        payload_test = payload.copy()
        payload_test["email"] = f"email{key}@email.com"            
        payload_test.pop(key)
        response = client.patch(f"/user/{user}", headers=headers(logged_in_client), json=payload_test)
        assert response.status_code == 204

def test_patch_user_fail_with_email_registered(client, logged_in_client):
    """Test of the patch user with email registered """
    payload_test = payload.copy()
    payload_test["email"] = "joao@email.com"
    response = client.patch(f"/user/{1}", headers=headers(logged_in_client), json=payload_test)
    
    if response.status_code == 400 and response.json:
        assert response.json["error"] == "{'email': ['Email já registrado']}"
        
def test_patch_user_fail_without_permission(client, logged_in_client_with_user_read):
    """Test of the post user route with a valid token"""
    payload_test = payload.copy()
    payload_test["email"] = "joao@email.com"
    response = client.patch(f"/user/{1}", headers=headers(logged_in_client_with_user_read), json=payload_test)
    
    if response.status_code == 403 and response.json:
        assert "Você não tem permissão" in response.json["error"]
    else:
        assert False
        