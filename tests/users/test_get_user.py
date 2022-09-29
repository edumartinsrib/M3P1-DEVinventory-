def test_users_success_status_200(client, logged_in_client):
    """Test of the user route with a valid token without parameter name"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    assert client.get("/user/", headers=headers).status_code == 200


def test_users_fail_with_invalid_token(client, logged_in_client):
    """Test of the user route with an invalid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}123"}
    assert client.get("/user/", headers=headers).status_code == 403


def test_user_success_with_name(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    name_teste = "João"
    url = f"/user/?name={name_teste}"
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get(url, headers=headers)

    if response.status_code == 200 and response.json:
        assert response.json["Dados"][0]["name"] == "João Victor"
        assert response.json["Status"] == "Sucesso"
    else:
        assert False


def test_user_fail_with_name_not_found(client, logged_in_client):
    """Test of the user route with a name that does not exist in the database"""
    name_teste = "João123"
    url = f"/user/?name={name_teste}"
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get(url, headers=headers)

    assert response.status_code == 204
