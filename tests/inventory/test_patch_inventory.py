from mocks import delete_keys_by_atribute, payload_just_values_and_keys

configs = {
    "url_base": "/inventory/",
    "url_product_code": "/inventory/1",
    "product_code": 1,
}


def headers(logged_in_client):
    return {"Authorization": f"Bearer {logged_in_client}"}


def test_patch_inventory_success_status_204(client, logged_in_client):
    """Test of the user route with a valid token"""
    payload = delete_keys_by_atribute(payload_just_values_and_keys, "patch", False)
    response = client.patch(
        configs["url_product_code"], json=payload, headers=headers(logged_in_client)
    )

    assert response.status_code == 204


def test_patch_inventory_fail_invalid_token(client, logged_in_client):
    """Test of the user route with a valid token"""
    response = client.patch(
        configs["url_base"],
        json=payload_just_values_and_keys,
        headers=headers(logged_in_client),
    )

    response.status_code == 403


def test_patch_inventory_fail_without_permission(
    client, logged_in_client_with_user_read
):
    """Test of the user route with a valid token"""
    response = client.patch(
        configs["url_base"],
        json=payload_just_values_and_keys,
        headers=headers(logged_in_client_with_user_read),
    )
    print(response.json)
    assert response.status_code == 405


def test_patch_inventory_fail_without_payload(client, logged_in_client):
    """Test of the user route with a valid token"""
    response = client.post(
        configs["url_base"], json={}, headers=headers(logged_in_client)
    )

    if response.status_code == 400 and response.json:
        assert "é obrigatório" in response.json["error"]


def test_patch_inventory_success_with_parcial_fields(client, logged_in_client):
    """Test of the user route with a valid token"""
    payload_patch = delete_keys_by_atribute(
        payload_just_values_and_keys, "patch", False
    )

    for key in payload_patch:
        payload_copy = payload_patch.copy()
        del payload_copy[key]
        response = client.patch(
            configs["url_product_code"],
            json=payload_copy,
            headers=headers(logged_in_client),
        )

        assert response.status_code == 204


def test_patch_inventory_fail_with_invalid_fields(client, logged_in_client):
    """Test of the user route with a valid token"""
    payload_patch = delete_keys_by_atribute(payload_just_values_and_keys, "patch", True)

    for key in payload_patch:
        payload_copy = payload_patch.copy()
        del payload_copy[key]
        response = client.patch(
            configs["url_product_code"],
            json=payload_copy,
            headers=headers(logged_in_client),
        )

        if response.status_code == 400 and response.json:
            assert "não permite alteração" in response.json["error"]


def test_patch_inventory_fail_with_invalid_payload_values(client, logged_in_client):
    """Test of the user route with a valid token"""
    payload_patch = delete_keys_by_atribute(payload_just_values_and_keys, "type", int)
    payload_just_field_value = delete_keys_by_atribute(payload_patch, "type", str)

    for key in payload_just_field_value:
        payload_copy = payload_just_field_value.copy()
        payload_copy[key] = "invalid_value"
        response = client.patch(
            configs["url_product_code"],
            json=payload_copy,
            headers=headers(logged_in_client),
        )

        if response.status_code == 400 and response.json:
            assert f"{key} inválido" in response.json["error"]

def test_patch_inventory_fail_with_invalid_payload_value_null(client, logged_in_client):
    """Test of the user route with a valid token"""
    payload_patch = delete_keys_by_atribute(payload_just_values_and_keys, "type", int)
    payload_just_field_value = delete_keys_by_atribute(payload_patch, "type", str)

    for key in payload_just_field_value:
        payload_copy = payload_just_field_value.copy()
        payload_copy[key] = 0
        response = client.patch(
            configs["url_product_code"],
            json=payload_copy,
            headers=headers(logged_in_client),
        )

        if response.status_code == 400 and response.json:
            assert "Valor inválido" in response.json["error"]
            
def test_patch_inventory_fail_with_invalid_payload_value_negative(client, logged_in_client):
    """Test of the user route with a valid token"""
    payload_patch = delete_keys_by_atribute(payload_just_values_and_keys, "type", int)
    payload_just_field_value = delete_keys_by_atribute(payload_patch, "type", str)

    for key in payload_just_field_value:
        payload_copy = payload_just_field_value.copy()
        payload_copy[key] = -1
        response = client.patch(
            configs["url_product_code"],
            json=payload_copy,
            headers=headers(logged_in_client),
        )

        if response.status_code == 400 and response.json:
            assert "Valor inválido" in response.json["error"]