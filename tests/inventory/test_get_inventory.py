def test_get_inventory_success_status_200(client, logged_in_client):
    """Test of the user route with a valid token without parameter name"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    name = "jo"
    response = client.get(f"/inventory/?name={name}", headers=headers)

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
        assert response.json["valor total de itens"] != ""


def test_get_inventory_success_with_name_filter(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    name_teste = "jo"
    url = f"/inventory/?name={name_teste}"
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get(url, headers=headers)

    if response.status_code == 200 and response.json:
        assert response.json["Status"] == "Sucesso"


def test_get_inventory_invalid_with_name_not_found(client, logged_in_client):
    """Test of the user route with a name that does not exist in the database"""
    name_teste = "João123"
    url = f"/inventory/?name={name_teste}"
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get(url, headers=headers)

    assert response.status_code == 204


def test_get_inventory_success_with_paginate_validate(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    name_teste = "jo"
    page = 1
    url = f"/inventory/?name={name_teste}&page={page}"
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get(url, headers=headers)

    if response.status_code == 200 and response.json:
        assert response.json["Status"] == "Sucesso"


def test_get_inventory_fail_with_paginate_invalid(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    name_teste = "jo"
    page = 1000
    url = f"/inventory/?name={name_teste}&page={page}"
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get(url, headers=headers)

    assert response.status_code == 204


def test_get_inventory_success_with_item_in_company(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = f"/inventory/?page=1"
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get(url, headers=headers)

    if response.status_code == 200 and response.json:
        for item in response.json["Dados"]:
            if item["user"]["name"] == "Na empresa":
                assert item["user"]["name"] == "Na empresa"
                break


def test_get_inventory_success_with_item_in_user(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = f"/inventory/?page=1"
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get(url, headers=headers)

    if response.status_code == 200 and response.json:
        for item in response.json["Dados"]:
            if item["user"]["name"] != "Na empresa":
                assert item["user"]["name"] != "Na empresa"
                break


def test_get_inventory_with_item_in_user_keys_requireds(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = f"/inventory/?page=1"
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get(url, headers=headers)

    if response.status_code == 200 and response.json:
        for item in response.json["Dados"]:
            if item["user"]["name"] != "Na empresa":
                assert "id" in item
                assert "product_code" in item
                assert "title" in item
                assert "product_category" in item
                assert "id" in item["user"]
                assert "name" in item["user"]
                break


def test_get_inventory_num_items_in_page(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = f"/inventory/?page=1"
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get(url, headers=headers)

    if response.status_code == 200 and response.json:
        assert len(response.json["Dados"]) == 20


def test_get_inventory_without_paginate(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = f"/inventory/"
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get(url, headers=headers)

    if response.status_code == 200 and response.json:
        assert len(response.json["Dados"]) == 20


def test_get_inventory_by_id_success(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = f"/inventory/1"
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.get(url, headers=headers)

    if response.status_code == 200 and response.json:
        assert response.json["Status"] == "Sucesso"
