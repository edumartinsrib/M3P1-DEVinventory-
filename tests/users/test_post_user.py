from mocks_users import headers, keys_not_requireds, keys_requireds, payload


def test_post_user_success(client, logged_in_client):
    """Test of the post user route with a valid token"""
    response = client.post(
        '/user/', headers=headers(logged_in_client), json=payload
    )

    assert response.status_code == 201


def test_post_user_fail_invalid_token(client, logged_in_client):
    """Test of the post user route with an invalid token"""
    response = client.post(
        '/user/', headers=headers(f'{logged_in_client}123'), json=payload
    )

    assert response.status_code == 403


def test_post_user_success_without_not_requireds_fields(
    client, logged_in_client
):
    """Test of the post user route with a valid token"""
    payload_test = payload.copy()
    for key in keys_not_requireds:
        payload_test.pop(key)
        payload_test['email'] = f'email{key}@email.com'
    response = client.post(
        '/user/', headers=headers(logged_in_client), json=payload_test
    )

    assert response.status_code == 201


def test_post_user_fail_with_email_already_exists(client, logged_in_client):
    """Test of the post user route with a valid token"""
    payload_test = payload.copy()
    payload_test['email'] = 'joao@email.com'
    response = client.post(
        '/user/', headers=headers(logged_in_client), json=payload_test
    )

    if response.status_code == 400 and response.json:
        assert 'Email já registrado' in response.json['error']


def test_post_user_fail_invalid_permission_user(
    client, logged_in_client_with_user_read
):
    """Test of the post user route with a valid token"""
    response = client.post(
        '/user/',
        headers=headers(logged_in_client_with_user_read),
        json=payload,
    )

    if response.status_code == 403 and response.json:
        assert 'Você não tem permissão' in response.json['error']


def test_post_user_fail_invalid_payload(client, logged_in_client):
    """Test of the post user route with an invalid payload - without required fields"""
    for key in keys_requireds:
        payload_test = payload.copy()
        payload_test.pop(key)
        response = client.post(
            '/user/', headers=headers(logged_in_client), json=payload_test
        )

        if response.status_code == 400 and response.json:
            assert (
                response.json['error']
                == f"{{'{key}': ['{key} é obrigatório.']}}"
            )
        else:
            assert False


def test_post_user_fail_invalid_payload_password(client, logged_in_client):
    """Test of the post user route with an invalid payload - password"""
    payload_test = payload.copy()
    payload_test['password'] = 'teste123'
    response = client.post(
        '/user/', headers=headers(logged_in_client), json=payload_test
    )

    if response.status_code == 400 and response.json:
        assert (
            response.json['error']
            == "{'password': ['Senha fraca, utilize letras maiúsculas, minúsculas, números e caracteres especiais']}"
        )
    else:
        assert False


def test_post_user_fail_with_invalid_payload_telephone(
    client, logged_in_client
):
    """Test of the post user route with an invalid payload - telephone"""
    payload_test = payload.copy()
    payload_test['phone'] = '4899999999'
    response = client.post(
        '/user/', headers=headers(logged_in_client), json=payload_test
    )

    if response.status_code == 400 and response.json:
        assert response.json['error'] == "{'phone': ['Telefone inválido']}"


def test_post_user_fail_with_invalid_payload_email(client, logged_in_client):
    """Test of the post user route with an invalid payload - email"""
    payload_test = payload.copy()
    payload_test['email'] = 'joaoemail.com'
    response = client.post(
        '/user/', headers=headers(logged_in_client), json=payload_test
    )

    if response.status_code == 400 and response.json:
        assert 'email inválido.' in response.json['error']


def test_post_user_fail_with_invalid_payload_age(client, logged_in_client):
    """Test of the post user route with an invalid payload - age"""
    payload_test = payload.copy()
    payload_test['age'] = '2000/01/01'
    response = client.post(
        '/user/', headers=headers(logged_in_client), json=payload_test
    )

    if response.status_code == 400 and response.json:
        assert (
            response.json['error']
            == f"time data '{payload_test['age']}' does not match format '%d/%m/%Y'"
        )


def test_post_user_fail_with_invalid_payload_city_id(client, logged_in_client):
    """Test of the post user route with an invalid payload - city_id"""
    payload_test = payload.copy()
    payload_test['city_id'] = 'teste'
    response = client.post(
        '/user/', headers=headers(logged_in_client), json=payload_test
    )

    if response.status_code == 400 and response.json:
        assert 'city_id inválido.' in response.json['error']
    else:
        assert False


def test_post_user_fail_with_invalid_payload_gender_id(
    client, logged_in_client
):
    """Test of the post user route with an invalid payload"""
    payload_test = payload.copy()
    payload_test['gender_id'] = 5
    response = client.post(
        '/user/', headers=headers(logged_in_client), json=payload_test
    )

    if response.status_code == 400 and response.json:
        assert (
            response.json['error']
            == "{'gender_id': ['Gênero não encontrado.']}"
        )
    else:
        assert False


def test_post_user_fail_role_with_success_create_role(
    client, logged_in_client
):
    """Test of the post user route with a valid token"""
    payload_test = {
        'name': 'teste',
        'description': 'teste02',
        'permissions': [1, 2, 3],
    }
    response = client.post(
        '/user/role', headers=headers(logged_in_client), json=payload_test
    )

    assert response.status_code == 201
    assert response.json['status'] == 'sucesso'


def test_post_user_fail_role_with_invalid_payload_create_role(
    client, logged_in_client
):
    """Test of the post user route with a valid token"""
    fields_requireds = ['name', 'description', 'permissions']
    payload = {
        'name': 'teste',
        'description': 'teste02',
        'permissions': [1, 2, 3],
    }
    for key in fields_requireds:
        payload_test = payload.copy()
        payload_test.pop(key)
        response = client.post(
            '/user/role', headers=headers(logged_in_client), json=payload_test
        )

        if response.status_code == 400 and response.json:
            assert (
                response.json['error']
                == f"{{'{key}': ['{key} é obrigatório.']}}"
            )
        else:
            assert False


def test_post_user_fail_role_with_invalid_payload_create_role_permissions(
    client, logged_in_client
):
    """Test of the post user route with a valid token"""
    payload_test = {
        'name': 'teste',
        'description': 'teste02',
        'permissions': [1, 2, 3, 5, 6],
    }
    response = client.post(
        '/user/role', headers=headers(logged_in_client), json=payload_test
    )

    if response.status_code == 400 and response.json:
        assert 'Permissão não encontrada' in response.json['error']
    else:
        assert False


def test_post_user_fail_role_with_invalid_create_role_with_existing_name_and_description(
    client, logged_in_client
):
    """Test of the post user route with a valid token"""
    payload_test = {
        'name': 'Administrador do Sistema',
        'description': 'SYSTEM_ADMIN',
        'permissions': [1, 2, 3, 4],
    }
    response = client.post(
        '/user/role', headers=headers(logged_in_client), json=payload_test
    )

    if response.status_code == 400 and response.json:
        assert 'Função já registrada' in response.json['error']
        assert 'Descrição já registrada' in response.json['error']
    else:
        assert False


def test_post_user_fail_role_with_invalid_permission_user(
    client, logged_in_client_with_user_read
):
    """Test of the post user route with a valid token"""
    payload_test = {
        'name': 'test',
        'description': 'test',
        'permissions': [1, 2, 3],
    }
    response = client.post(
        '/user/role',
        headers=headers(logged_in_client_with_user_read),
        json=payload_test,
    )

    if response.status_code == 403 and response.json:
        assert 'Você não tem permissão' in response.json['error']
    else:
        assert False
