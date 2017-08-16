import os
from flask_script import Manager, Shell, Server

from web import create_app

app = create_app('default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)

port = os.getenv('PORT', '8081')
manager.add_command("runserver", Server(host="0.0.0.0", port=int(port)))
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
