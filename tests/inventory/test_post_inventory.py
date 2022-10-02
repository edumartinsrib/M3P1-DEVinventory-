from mocks import payload_configs_and_types, payload_just_values_and_keys


def test_post_inventory_success_status_200(client, logged_in_client):
    """Test of the user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.post(
        f"/inventory/", json=payload_just_values_and_keys, headers=headers
    )

    if response.status_code == 201 and response.json:
        assert response.json["data"] != None


def test_post_inventory_fail_user_not_authorized_status_403(
    client, logged_in_client_with_user_read
):
    """Test of the user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client_with_user_read}"}
    response = client.post(
        f"/inventory/", json=payload_just_values_and_keys, headers=headers
    )

    if response.status_code == 403 and response.json:
        assert "Você não tem permissão" in response.json["error"]


def test_post_inventory_fail_with_invalid_token(client, logged_in_client):
    """Test of the user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}123"}
    response = client.post(
        f"/inventory/", json=payload_just_values_and_keys, headers=headers
    )

    assert response.status_code == 403


def test_post_inventory_fail_with_invalid_payload(client, logged_in_client):
    """Test of the user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    response = client.post(
        f"/inventory/", json={"invalid_key": "invalid_value"}, headers=headers
    )

    assert response.status_code == 400


def test_post_inventory_fail_missing_fields_requireds(client, logged_in_client):
    """Test of the user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    for payload_config in payload_configs_and_types:
        if payload_config["required"]:
            payload = payload_just_values_and_keys.copy()
            del payload[payload_config["key"]]
            response = client.post(f"/inventory/", json=payload, headers=headers)

            if response.status_code == 400 and response.json:
                assert "é obrigatório" in response.json["error"]
            else:
                assert False


def test_post_inventory_fail_with_type_wrong(client, logged_in_client):
    """Test of the user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    for payload_config in payload_configs_and_types:
        if payload_config["type"] == int or payload_config["type"] == float:
            payload = payload_just_values_and_keys.copy()
            payload[payload_config["key"]] = "invalid_value"
            response = client.post(f"/inventory/", json=payload, headers=headers)

            if response.status_code == 400 and response.json:
                assert "inválido" in response.json["error"]
            else:
                assert False


def test_post_inventory_fail_with_product_code_unique(client, logged_in_client):
    """Test of the user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    for payload_config in payload_configs_and_types:
        if payload_config["unique"]:
            payload = payload_just_values_and_keys.copy()
            payload[payload_config["key"]] = 1
            response = client.post(f"/inventory/", json=payload, headers=headers)

            if response.status_code == 400 and response.json:
                assert "já registrado" in response.json["error"]
            else:
                assert False


def test_post_inventory_fail_with_invalid_value_null(client, logged_in_client):
    """Test of the user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    for payload_config in payload_configs_and_types:
        if payload_config["key"] == "value":
            payload = payload_just_values_and_keys.copy()
            payload[payload_config["key"]] = 0
            response = client.post(f"/inventory/", json=payload, headers=headers)

            if response.status_code == 400 and response.json:
                assert "inválido" in response.json["error"]
            else:
                assert False


def test_post_inventory_fail_with_invalid_value_negative(client, logged_in_client):
    """Test of the user route with a valid token"""
    headers = {"Authorization": f"Bearer {logged_in_client}"}
    for payload_config in payload_configs_and_types:
        if payload_config["key"] == "value":
            payload = payload_just_values_and_keys.copy()
            payload[payload_config["key"]] = -1
            response = client.post(f"/inventory/", json=payload, headers=headers)

            if response.status_code == 400 and response.json:
                assert "inválido" in response.json["error"]
            else:
                assert False
