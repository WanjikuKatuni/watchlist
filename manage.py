#from app import app #import app instance
from app import create_app #import create app function from app folder
from flask_script import Manager, Server #manager innitialise extension and server launches server


#CREATE APP INSTANCE
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()    