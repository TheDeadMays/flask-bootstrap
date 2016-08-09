#! /usr/bin/env python

import os

from app import db, create_app

from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('APP_CONFIG', 'default'))
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager.run()
