from mocks_inventory import (
    configs,
    headers,
    payload_configs_and_types,
    payload_just_values_and_keys,
)


def test_post_inventory_success_status_200(client, logged_in_client):
    """Test of the user route with a valid token"""
    response = client.post(
        configs['url_base'],
        json=payload_just_values_and_keys,
        headers=headers(logged_in_client),
    )

    if response.status_code == 201 and response.json:
        assert response.json['data'] != None
    else:
        assert False


def test_post_inventory_fail_user_not_authorized_status_403(
    client, logged_in_client_with_user_read
):
    """Test of the user route with a valid token"""
    response = client.post(
        configs['url_base'],
        json=payload_just_values_and_keys,
        headers=headers(logged_in_client_with_user_read),
    )

    if response.status_code == 403 and response.json:
        assert 'Você não tem permissão' in response.json['error']
    else:
        assert False


def test_post_inventory_fail_with_invalid_token(client, logged_in_client):
    """Test of the user route with a valid token"""
    response = client.post(
        configs['url_base'],
        json=payload_just_values_and_keys,
        headers=headers(f'{logged_in_client}123'),
    )

    assert response.status_code == 403


def test_post_inventory_fail_with_invalid_payload(client, logged_in_client):
    """Test of the user route with a valid token"""
    response = client.post(
        configs['url_base'],
        json={'invalid_key': 'invalid_value'},
        headers=headers(logged_in_client),
    )

    assert response.status_code == 400


def test_post_inventory_fail_missing_fields_requireds(
    client, logged_in_client
):
    """Test of the user route with a valid token"""
    for payload_config in payload_configs_and_types:
        if payload_config['required']:
            payload = payload_just_values_and_keys.copy()
            del payload[payload_config['key']]
            response = client.post(
                configs['url_base'],
                json=payload,
                headers=headers(logged_in_client),
            )

            if response.status_code == 400 and response.json:
                assert 'é obrigatório' in response.json['error']
            else:
                assert False


def test_post_inventory_fail_with_type_wrong(client, logged_in_client):
    """Test of the user route with a valid token"""
    for payload_config in payload_configs_and_types:
        if payload_config['type'] == int or payload_config['type'] == float:
            payload = payload_just_values_and_keys.copy()
            payload[payload_config['key']] = 'invalid_value'
            response = client.post(
                configs['url_base'],
                json=payload,
                headers=headers(logged_in_client),
            )

            if response.status_code == 400 and response.json:
                assert 'inválido' in response.json['error']
            else:
                assert False


def test_post_inventory_fail_with_product_code_unique(
    client, logged_in_client
):
    """Test of the user route with a valid token"""
    for payload_config in payload_configs_and_types:
        if payload_config['unique']:
            payload = payload_just_values_and_keys.copy()
            payload[payload_config['key']] = 1
            response = client.post(
                configs['url_base'],
                json=payload,
                headers=headers(logged_in_client),
            )

            if response.status_code == 400 and response.json:
                assert 'já registrado' in response.json['error']
            else:
                assert False


def test_post_inventory_fail_with_invalid_value_null(client, logged_in_client):
    """Test of the user route with a valid token"""
    for payload_config in payload_configs_and_types:
        if payload_config['key'] == 'value':
            payload = payload_just_values_and_keys.copy()
            payload[payload_config['key']] = 0
            response = client.post(
                configs['url_base'],
                json=payload,
                headers=headers(logged_in_client),
            )

            if response.status_code == 400 and response.json:
                assert 'inválido' in response.json['error']
            else:
                assert False


def test_post_inventory_fail_with_invalid_value_negative(
    client, logged_in_client
):
    """Test of the user route with a valid token"""
    for payload_config in payload_configs_and_types:
        if payload_config['key'] == 'value':
            payload = payload_just_values_and_keys.copy()
            payload[payload_config['key']] = -1
            response = client.post(
                configs['url_base'],
                json=payload,
                headers=headers(logged_in_client),
            )

            if response.status_code == 400 and response.json:
                assert 'inválido' in response.json['error']
            else:
                assert False
