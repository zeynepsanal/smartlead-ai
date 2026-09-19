import os

from flask import Flask
from flask_cors import CORS

from config import config
from app.database import init_db
from app.routes import pages_bp, api_bp


def create_app():
    """Uygulama fabrikasi: ayarlari yukler, CORS'u acar, veritabanini
    hazirlar ve rotalari kaydeder."""
    ortam = os.environ.get('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(config[ortam])

    CORS(app, origins=app.config.get('CORS_ORIGINS', '*'))

    init_db(app)

    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/health')
    def health():
        """Sunucunun canli olup olmadigini kontrol etmek icin kullanilir."""
        return {'durum': 'aktif'}

    return app
