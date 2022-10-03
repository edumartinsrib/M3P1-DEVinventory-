from mocks_users import headers


def test_get_users_success_status_200(client, logged_in_client):
    """Test of the user route with a valid token without parameter name"""
    response = client.get('/user/', headers=headers(logged_in_client))

    assert response.status_code == 200


def test_get_user_fail_without_permission(client, logged_in_client_with_user_write):
    """Test of the user route fail without permission"""
    response = client.get('/user/', headers=headers(logged_in_client_with_user_write))
    
    assert response.status_code == 403


def test_get_users_fail_with_invalid_token(client, logged_in_client):
    """Test of the user route with an invalid token"""
    assert (
        client.get(
            '/user/', headers=headers(f'{logged_in_client}123')
        ).status_code
        == 403
    )


def test_get_user_success_with_name(client, logged_in_client):
    """Test of the user route with a name that exists in the database"""
    name_teste = 'Pa'
    url = f'/user/?name={name_teste}'
    response = client.get(url, headers=headers(logged_in_client))

    assert response.status_code == 200
    assert response.json['Status'] == 'Sucesso'


def test_get_user_fail_with_name_not_found(client, logged_in_client):
    """Test of the user route with a name that does not exist in the database"""
    name_teste = 'João123'
    url = f'/user/?name={name_teste}'
    response = client.get(url, headers=headers(logged_in_client))

    assert response.status_code == 204


def test_get_user_success_with_paginate_only(client, logged_in_client):
    """Test of the user route with pagination"""
    page = 1
    url = f'/user/?page={page}'
    response = client.get(url, headers=headers(logged_in_client))

    assert response.status_code == 200
    assert response.json['Status'] == 'Sucesso'


def test_get_user_success_with_name_and_paginate_validate(client, logged_in_client):
    """Test of the user route with pagination"""
    name_teste = 'Pa'
    page = 1
    url = f'/user/?name={name_teste}&page={page}'
    response = client.get(url, headers=headers(logged_in_client))

    assert response.status_code == 200
    assert response.json['Status'] == 'Sucesso'

def test_get_user_fail_with_paginate_invalid(client, logged_in_client):
    """Test of the user route with invalid pagination"""
    page = 1000
    url = f'/user/?page={page}'
    response = client.get(url, headers=headers(logged_in_client))

    assert response.status_code == 204
