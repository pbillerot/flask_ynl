from flask import Flask, Blueprint
from ask_sdk_core.skill_builder import SkillBuilder
from flask_ask_sdk.skill_adapter import SkillAdapter
from skill import sb

app = Flask(__name__)
skill_adapter = SkillAdapter(
  skill=sb.create(), skill_id="amzn1.ask.skill.bd7515ac-93e7-48c6-b2b5-58dcd0fb0951", app=app)

skill_adapter.register(app=app, route="/alexa")

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
