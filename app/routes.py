from flask import Blueprint, request, jsonify, render_template

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError

# Sayfalari gosteren blueprint (HTML doner)
pages_bp = Blueprint('pages', __name__)

# API isteklerini karsilayan blueprint (JSON doner)
api_bp = Blueprint('api', __name__)


@pages_bp.route('/')
def anasayfa():
    """Karsilama sayfasini gosterir."""
    return render_template('index.html')


@pages_bp.route('/dashboard')
def dashboard():
    """Yonetim panelini gosterir."""
    return render_template('dashboard.html')


@api_bp.route('/sohbet', methods=['POST'])
def sohbet():
    """Ziyaretcinin mesajini alir, yapay zekadan yanit doner."""
    data = request.get_json(silent=True) or {}
    mesaj = (data.get('mesaj') or '').strip()
    gecmis = data.get('gecmis', [])

    if not mesaj:
        return jsonify({'basari': False, 'hata': 'Mesaj bos olamaz.'}), 400

    try:
        yanit = ai_service.yanit_uret(mesaj, gecmis)
    except AIServiceError as e:
        return jsonify({'basari': False, 'hata': str(e)}), 503

    return jsonify({'basari': True, 'yanit': yanit})


@api_bp.route('/leads', methods=['POST'])
def lead_kaydet():
    """Ziyaretcinin isim/telefon bilgisini veritabanina kaydeder."""
    data = request.get_json(silent=True) or {}
    isim = (data.get('isim') or '').strip()
    telefon = (data.get('telefon') or '').strip()
    mesaj = data.get('mesaj')

    if not isim or not telefon:
        return jsonify({'basari': False, 'hata': 'Isim ve telefon zorunlu.'}), 400

    try:
        lead_ekle(isim, telefon, mesaj)
    except Exception as e:
        return jsonify({'basari': False, 'hata': 'Kayit sirasinda bir sorun olustu.'}), 503

    return jsonify({'basari': True, 'durum': 'basarili'}), 201


@api_bp.route('/leads', methods=['GET'])
def lead_listele():
    """Kayitli tum leadleri (musteri kayitlarini) listeler."""
    try:
        leadler = tum_leadler()
    except Exception as e:
        return jsonify({'basari': False, 'hata': 'Kayitlar okunamadi.'}), 503

    return jsonify({'basari': True, 'leadler': leadler})