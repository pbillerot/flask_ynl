from flask import Flask
from ask_sdk_core.skill_builder import SkillBuilder
from flask_ask_sdk.skill_adapter import SkillAdapter

app = Flask(__name__)
skill_builder = SkillBuilder()
# Register your intent handlers to the skill_builder object
skill_adapter = SkillAdapter(
    skill=skill_builder.create(), skill_id=<SKILL_ID>, app=app)


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ask_sdk_core.skill_builder import SkillBuilder
from flask_ask_sdk.skill_adapter import SkillAdapter

db = SQLAlchemy()

def create_app():

    from .skill import sb
    from .settings import SQLALCHEMY_DATABASE_URI

    app = Flask(__name__)
    # Register your intent handlers to the skill_builder object
    skill_adapter = SkillAdapter(
        skill=sb.create(), 
        skill_id=<SKILL_ID>,
        app=app)

    # app.register_blueprint(main)

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route("/"):
    def invoke_skill:
        # return skill_adapter.dispatch_request()
        return 'Skin en marche!!!'


    return app

