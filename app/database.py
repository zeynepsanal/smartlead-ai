import sqlite3
from flask import g
from config import Config


def get_db():
    """Veritabanina baglanir; satirlara sutun adiyla erisim saglar."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(Config.DATABASE_URL)
        db.row_factory = sqlite3.Row
    return db


def init_db(app):
    """'leads' tablosunu olusturur (yoksa)."""
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                tarih TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()


def lead_ekle(isim, telefon, mesaj=None):
    """Yeni bir lead kaydi ekler."""
    db = get_db()
    db.execute(
        'INSERT INTO leads (isim, telefon, mesaj) VALUES (?, ?, ?)',
        (isim, telefon, mesaj)
    )
    db.commit()


def tum_leadler():
    """Tum kayitlari en yeniden eskiye getirir."""
    db = get_db()
    cursor = db.execute('SELECT * FROM leads ORDER BY tarih DESC')
    return [dict(row) for row in cursor.fetchall()]
