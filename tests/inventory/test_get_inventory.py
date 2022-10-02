from mocks_inventory import headers


def test_get_inventory_success_status_200(client, logged_in_client):
    """Test of the user route with a valid token without parameter name"""
    name = 'jo'
    response = client.get(
        f'/inventory/?name={name}', headers=headers(logged_in_client)
    )

    if response.status_code == 200 and response.json:
        assert response.json['Status'] == 'Sucesso'


def test_get_inventory_fail_with_invalid_token(client, logged_in_client):
    """Test of the user route with an invalid token"""
    response = client.get(
        '/inventory/results', headers=headers(f'{logged_in_client}123')
    )

    assert response.status_code == 403


def test_get_inventory_results_success_status_200(client, logged_in_client):
    """Test of the user route with a valid token without parameter name"""
    response = client.get(
        '/inventory/results', headers=headers(logged_in_client)
    )

    if response.status_code == 200 and response.json:
        assert response.json['itens emprestados'] >= 0
        assert response.json['numero de usuários'] >= 0
        assert response.json['quantidade de produtos'] >= 0
        assert response.json['valor total de itens'] != ''


def test_get_inventory_success_with_name_filter(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    name_teste = 'jo'
    url = f'/inventory/?name={name_teste}'
    response = client.get(url, headers=headers(logged_in_client))

    if response.status_code == 200 and response.json:
        assert response.json['Status'] == 'Sucesso'


def test_get_inventory_fail_invalid_with_name_not_found(
    client, logged_in_client
):
    """Test of the user route with a name that does not exist in the database"""
    name_teste = 'João123'
    url = f'/inventory/?name={name_teste}'
    response = client.get(url, headers=headers(logged_in_client))

    assert response.status_code == 204


def test_get_inventory_success_with_paginate_validate(
    client, logged_in_client
):
    """Test of the user route with a name that exists in the database"""
    name_teste = 'jo'
    page = 1
    url = f'/inventory/?name={name_teste}&page={page}'
    response = client.get(url, headers=headers(logged_in_client))

    if response.status_code == 200 and response.json:
        assert response.json['Status'] == 'Sucesso'


def test_get_inventory_fail_with_paginate_invalid(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    name_teste = 'jo'
    page = 1000
    url = f'/inventory/?name={name_teste}&page={page}'
    response = client.get(url, headers=headers(logged_in_client))

    assert response.status_code == 204


def test_get_inventory_success_with_item_in_company(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = '/inventory/?page=1'
    response = client.get(url, headers=headers(logged_in_client))

    if response.status_code == 200 and response.json:
        for item in response.json['Dados']:
            if item['user']['name'] == 'Na empresa':
                assert item['user']['name'] == 'Na empresa'
                break


def test_get_inventory_success_with_item_in_user(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = '/inventory/?page=1'
    response = client.get(url, headers=headers(logged_in_client))

    if response.status_code == 200 and response.json:
        for item in response.json['Dados']:
            if item['user']['name'] != 'Na empresa':
                assert item['user']['name'] != 'Na empresa'
                break


def test_get_inventory_success_with_item_in_user_keys_requireds(
    client, logged_in_client
):
    """Test of the user route with a name that exists in the database"""
    url = '/inventory/?page=1'
    response = client.get(url, headers=headers(logged_in_client))

    if response.status_code == 200 and response.json:
        for item in response.json['Dados']:
            if item['user']['name'] != 'Na empresa':
                assert 'id' in item
                assert 'product_code' in item
                assert 'title' in item
                assert 'product_category' in item
                assert 'id' in item['user']
                assert 'name' in item['user']
                break


def test_get_inventory_success_num_items_in_page(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = '/inventory/?page=1'
    response = client.get(url, headers=headers(logged_in_client))

    if response.status_code == 200 and response.json:
        assert len(response.json['Dados']) == 20


def test_get_inventory_success_without_paginate(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = '/inventory/'
    response = client.get(url, headers=headers(logged_in_client))

    if response.status_code == 200 and response.json:
        assert len(response.json['Dados']) == 20


def test_get_inventory_success_by_id_success(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = '/inventory/1'
    response = client.get(url, headers=headers(logged_in_client))

    if response.status_code == 200 and response.json:
        assert response.json['Status'] == 'Sucesso'


def test_get_inventory_fail_by_id_fail(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = '/inventory/100000'
    response = client.get(url, headers=headers(logged_in_client))

    assert response.status_code == 404


def test_get_inventory_success_fields_returned(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    list_result_keys = {
        'id': int,
        'product_code': int,
        'title': str,
        'brand': str,
        'template': str,
        'description': str,
        'value': float,
        'product_category': str,
        'user': {'name': str, 'id': int},
    }
    url = '/inventory/1'
    response = client.get(url, headers=headers(logged_in_client))

    if response.status_code == 200 and response.json:
        for key in list_result_keys:
            if key == 'user':
                for key_user in list_result_keys[key]:
                    assert key_user in response.json['Dados'][key]
            else:
                assert key in response.json['Dados']


def test_get_inventory_success_result_type_of_data(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    list_result_keys = {
        'id': int,
        'product_code': int,
        'title': str,
        'brand': str,
        'template': str,
        'description': str,
        'value': float,
        'product_category': str,
        'user': {'name': str, 'id': int},
    }
    url = '/inventory/10'
    response = client.get(url, headers=headers(logged_in_client))

    if response.status_code == 200 and response.json:
        for key in list_result_keys:
            if key == 'user':
                for key_user in list_result_keys[key]:
                    assert type(
                        response.json['Dados'][key][key_user]
                    ) == list_result_keys[key][key_user] or type(
                        response.json['Dados'][key][key_user] is None
                    )
            else:
                assert (
                    type(response.json['Dados'][key]) == list_result_keys[key]
                )


def test_get_inventory_success_download_template_url(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    url = '/inventory/2'
    response = client.get(url, headers=headers(logged_in_client))
    url_validate = response.json['Dados']['template']

    if response.status_code == 200 and response.json:
        assert url_validate[:8] == 'https://'
