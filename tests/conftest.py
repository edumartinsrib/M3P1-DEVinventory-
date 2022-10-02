import pytest
from flask import json
from sqlalchemy import event

from src.app import DB, create_app
from src.app.models.user import User
from src.app.routes import routes

mimetype = 'application/json'
headers = {'Content-Type': mimetype, 'Accept': mimetype}


@pytest.fixture(scope='session')
def app():
    app_on = create_app('testing')
    routes(app_on)
    return app_on


@pytest.fixture
def logged_in_client(client):
    data = {'email': 'joao@email.com', 'password': 'senha'}

    response = client.post(
        'user/login', data=json.dumps(data), headers=headers
    )
    return response.json['token']


@pytest.fixture
def logged_in_client_with_user_read(client):
    data = {'email': 'ana@email.com', 'password': 'Xyzw#123'}

    response = client.post(
        'user/login', data=json.dumps(data), headers=headers
    )
    return response.json['token']


@pytest.fixture
def logged_in_client_with_user_write(client):
    data = {'email': 'pablo@email.com', 'password': 'Dev&0001'}

    response = client.post(
        'user/login', data=json.dumps(data), headers=headers
    )
    return response.json['token']


@pytest.fixture
def logged_in_client_with_user_patch(client):
    data = {'email': 'juca@email.com', 'password': 'Toor&456'}

    response = client.post(
        'user/login', data=json.dumps(data), headers=headers
    )
    return response.json['token']


@pytest.fixture(scope='function', autouse=True)
def session(app):
    with app.app_context():
        connection = DB.engine.connect()
        transaction = connection.begin()
        options = dict(bind=connection, binds={})
        sess = DB.create_scoped_session(options=options)
        sess.begin_nested()

        @event.listens_for(sess(), 'after_transaction_end')
        def restart_savepoint(sess2, trans):
            if trans.nested and not trans._parent.nested:
                sess2.expire_all()
                sess2.begin_nested()

        DB.session = sess
        yield sess
        sess.remove()
        transaction.rollback()
        connection.close()
