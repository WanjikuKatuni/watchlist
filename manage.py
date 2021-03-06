#from app import app #import app instance
from app import create_app, db #import create app function from app folder, import db  from app.intit file as well to create  python shelll using flaskscript
from flask_script import Manager, Server #manager innitialise extension and server launches server
from app.models import User, Role #import user class from the models.py
from flask_migrate import Migrate, MigrateCommand #used to track and keep changes on db

#CREATE APP INSTANCE
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

#initialise migrate class and pass app instance
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

@manager.command #create a new command

def test():
    '''
    run unnit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()    

@manager.shell #used to create the shell context
def make_shell_context(): #allows to pass properties into the shell
    return dict(app = app,db = db,User = User, Role = Role) #pass app instance, db instancfe and user class


if __name__=='__main__':
    manager.run()