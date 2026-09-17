from flask import Blueprint, request, jsonify

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError

bp = Blueprint('routes', __name__)


@bp.route('/api/sohbet', methods=['POST'])
def sohbet():
    """Ziyaretcinin mesajini alir, yapay zekadan yanit doner."""
    data = request.get_json(silent=True) or {}
    mesaj = (data.get('mesaj') or '').strip()
    gecmis = data.get('gecmis', [])

    if not mesaj:
        return jsonify({'hata': 'Mesaj bos olamaz.'}), 400

    try:
        yanit = ai_service.yanit_uret(mesaj, gecmis)
    except AIServiceError as e:
        return jsonify({'hata': str(e)}), 500

    return jsonify({'yanit': yanit})


@bp.route('/api/leads', methods=['POST'])
def lead_kaydet():
    """Ziyaretcinin isim/telefon bilgisini veritabanina kaydeder."""
    data = request.get_json(silent=True) or {}
    isim = (data.get('isim') or '').strip()
    telefon = (data.get('telefon') or '').strip()
    mesaj = data.get('mesaj')

    if not isim or not telefon:
        return jsonify({'hata': 'Isim ve telefon zorunlu.'}), 400

    lead_ekle(isim, telefon, mesaj)
    return jsonify({'durum': 'basarili'}), 201


@bp.route('/api/leads', methods=['GET'])
def lead_listele():
    """Kayitli tum leadleri (musteri kayitlarini) listeler."""
    return jsonify(tum_leadler())
