from flask import Flask

from config import config
from app.database import init_db
from app.routes import bp

app = Flask(__name__)
app.config.from_object(config['development'])

init_db(app)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
    