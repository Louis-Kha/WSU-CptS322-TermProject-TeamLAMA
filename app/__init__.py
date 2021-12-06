from flask import Flask, app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
# TODO: (milestone 3) import LoginManager and Moment extensions here
from flask_login import LoginManager

db = SQLAlchemy()
# TODO: (milestone 3) create LoginManager object and configure the login view as 'auth.login', i.e, `login` route in `auth` Blueprint. 
login = LoginManager()
login.login_view = 'auth.login'
# TODO: (milestone 3) create Moment object
moment = Moment()

def create_app(config_class=Config):
    # print("test test test")
    # ijk = False

    # def change_global():
    #     global ijk
    #     ijk = True

    # choice = ""
    # if ijk == False:
    #     print("Test1")
    #     print("1: Student Regisration Automation")
    #     print("2: Faculty Registration Automation")
    #     print("3: Student Login")
    #     print("4: Faculty Login")
    #     choice = input("Please input the choice of the automation you would like to run: ")
    #     change_global()
    # else:
    #     pass
    # print("----------------------------------Outside")
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER 
    app.template_folder = config_class.TEMPLATE_FOLDER
   # print("test test test")

    db.init_app(app)
    # TODO: (milestone 3) Configure the app object for login using `init_app` function.
    login.init_app(app)
    moment.init_app(app) 
    # TODO: (milestone 3) Configure the app object for moment using `init_app` function.
    # 
    # print("test test test")

    # blueprint registration
    from app.Controller.errors import bp_errors as errors
    app.register_blueprint(errors)
    from app.Controller.auth_routes import bp_auth as auth
    app.register_blueprint(auth)
    from app.Controller.routes import bp_routes as routes
    app.register_blueprint(routes)

    if not app.debug and not app.testing:
        pass
        # ... no changes to logging setup

    return app