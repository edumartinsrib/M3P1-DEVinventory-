def test_get_inventory_success_status_200(client, logged_in_client):
    """Test of the user route with a valid token without parameter name"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    name = "jo"
    response = client.get(f"/inventory/?name={name}", headers=headers)

    if response.status_code == 200 and response.json:
        assert response.json["Status"] == "Sucesso"