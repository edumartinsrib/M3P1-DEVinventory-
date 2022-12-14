from mocks_users import headers, keys_allow_patch, payload


def test_patch_user_success(client, logged_in_client):
    """Test of the patch user route with a valid token"""
    user = 2
    response = client.patch(
        f'/user/{user}', headers=headers(logged_in_client), json=payload
    )

    assert response.status_code == 204


def test_patch_user_fail_with_invalid_token(client, logged_in_client):
    """Test of the patch user route with a invalid token"""
    user = 2
    payload_test = payload.copy()
    payload_test['email'] = 'emailTeste@gmail.com'
    response = client.patch(
        f'/user/{user}',
        headers=headers(f'{logged_in_client}123'),
        json=payload_test,
    )
    assert response.status_code == 403


def test_patch_user_fail_invalid_field(client, logged_in_client):
    """Test of the patch user route with a invalid filed"""
    user = 2
    payload_test = payload.copy()
    payload_test['id'] = 'invalid_field'
    response = client.patch(
        f'/user/{user}', headers=headers(logged_in_client), json=payload_test
    )

    assert response.status_code == 400


def test_patch_user_fail_not_found(client, logged_in_client):
    """Test of the patch user not found"""
    user = 999
    payload_teste = {'cep': '99999'}

    response = client.patch(
        f'/user/{user}', headers=headers(logged_in_client), json=payload_teste
    )

    assert response.status_code == 404


def test_patch_user_success_with_not_required_fields(client, logged_in_client):
    """Test of the patch user not found"""
    user = 2
    for key in keys_allow_patch:
        payload_test = payload.copy()
        payload_test['email'] = f'email{key}@email.com'
        payload_test.pop(key)
        response = client.patch(
            f'/user/{user}',
            headers=headers(logged_in_client),
            json=payload_test,
        )
        assert response.status_code == 204


def test_patch_user_fail_with_email_registered(client, logged_in_client):
    """Test of the patch user with email registered"""
    payload_test = payload.copy()
    payload_test['email'] = 'joao@email.com'
    response = client.patch(
        f'/user/{1}', headers=headers(logged_in_client), json=payload_test
    )

    if response.status_code == 400 and response.json:
        assert 'Email j?? registrado' in response.json['error']


def test_patch_user_fail_without_permission(
    client, logged_in_client_with_user_read
):
    """Test of the post user route without permission"""
    payload_test = payload.copy()
    payload_test['email'] = 'joao@email.com'
    response = client.patch(
        f'/user/{1}',
        headers=headers(logged_in_client_with_user_read),
        json=payload_test,
    )

    if response.status_code == 403 and response.json:
        assert 'Voc?? n??o tem permiss??o' in response.json['error']

def test_patch_user_with_invalid_types_payload_email(client, logged_in_client):
    """Test of the patch user route with a invalid payload email"""
    user = 1
    payload_test = {
        "email": "invalid",
    }
    response = client.patch(
        f'/user/{user}', headers=headers(logged_in_client), json=payload_test
    )

    assert response.status_code == 400
    
def test_patch_user_with_invalid_types_payload_password(client, logged_in_client):
    """Test of the patch user route with a invalid password"""
    user = 2
    payload_test = {
        "password": 123,
    }

    response = client.patch(
        f'/user/{user}', headers=headers(logged_in_client), json=payload_test
    )
    assert response.status_code == 400


def test_patch_user_with_invalid_types_payload_numbers(client, logged_in_client):
    """Test of the patch user route with a invalid payload fields numbers"""
    user = 2
    payload_test = []
    for keys, values in payload.items():
        if isinstance(values, int) and keys != 'id':
            payload_test.append({keys: 'invalid'})
 
    response = client.patch(f'/user/{user}', headers=headers(logged_in_client), json=payload_test)    
    assert response.status_code == 400


def test_patch_user_fail_with_invalid_payload_phone(client, logged_in_client):
    """Test of the patch user route with a invalid payload phone"""
    user = 2
    payload_test = {
        "phone": "invalid",
    }

    response = client.patch(
        f'/user/{user}', headers=headers(logged_in_client), json=payload_test
    )
    assert response.status_code == 400
