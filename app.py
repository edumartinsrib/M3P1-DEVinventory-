import os

import click
from flask.cli import with_appcontext

from src.app import DB, create_app
from src.app.db import populate_db
from src.app.routes import routes

app = create_app(os.getenv('FLASK_ENV'))
routes(app)


@click.command(name='populate_db')
@with_appcontext
def call_command():
    populate_db()


@click.command(name='delete_tables')
@with_appcontext
def delete_tables():
    DB.drop_all()


app.cli.add_command(call_command)
app.cli.add_command(delete_tables)

if __name__ == '__main__':
    app.run()
