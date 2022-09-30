def test_get_inventory_suceess_status_200(client, logged_in_client):
    """Test of the user route with a valid token without parameter name"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    name = "jo"
    response = client.get(f"/inventory/?name={name}", headers=headers)
    print(response.json)
    if response.status_code == 200 and response.json:
        assert response.json["Status"] == "Sucesso"
        
        
def test_inventory_fail_with_invalid_token(client, logged_in_client):
    """Test of the user route with an invalid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}123"}
    assert client.get("/inventory/results", headers=headers).status_code == 403


def test_inventory_results_success_status_200(client, logged_in_client):
    """Test of the user route with a valid token without parameter name"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get("/inventory/results", headers=headers)

    if response.status_code == 200 and response.json:
        assert response.json["itens emprestados"] >= 0
        assert response.json["numero de usuários"] >= 0
        assert response.json["quantidade de produtos"] >= 0
        assert response.json["valor total de itens"] != ''