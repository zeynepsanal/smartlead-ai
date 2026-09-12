import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Tüm ayarları ve gizli anahtarları .env dosyasından okuyan yapılandırma sınıfı."""

    SECRET_KEY = os.environ.get('SECRET_KEY', 'gracia-gizli-anahtar-degistir')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'leads.db')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'groq')
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')

    # Yapay zekanin kisiligini tanimlayan metin.
    BUSINESS_CONTEXT = """Sen Gracia'nin asistanisin. Gracia, her bedenden
    insanin rahatca konforlu ve estetik spor kiyafetlerine erisimini
    saglayan bir spor tekstil markasidir. Standart bedenlerin yaninda
    farkli beden gereksinimlerine uygun, anatomik kesim ve esneme
    paylariyla tasarlanmis kaliteli ve estetik bir koleksiyon sunar.
    Musterilere kibar, sicak ve kapsayici bir dille yaklasip urunler
    hakkinda bilgi ver. Musteriyi iletisim bilgisi birakmaya yonlendir.
    Turkce konus."""


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
