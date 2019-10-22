from app import create_app, db
from flask_script import Manager, Shell, Server
from app.models import User
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
# app = create_app('development')
# app = create_app('test')
app =creat_app('production')


manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)
