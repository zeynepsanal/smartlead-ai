# SmartLead AI — Gracia Akıllı Satış Asistanı

Gracia, her bedenden insanın rahat ve estetik spor kıyafetlerine ulaşmasını hedefleyen bir spor tekstil markasıdır. Bu proje, Gracia'nın internet sitesinde ziyaretçilerle yapay zekâ üzerinden sohbet eden ve iletişim bilgilerini (lead) toplayan bir asistandır.

## Ne yapar?
- Ziyaretçinin ürünler hakkındaki sorularını yapay zekâ ile yanıtlar.
- Ziyaretçinin isim ve telefon bilgisini veritabanına kaydeder.
- Kayıtlı bilgileri listeler.

## Kullanılan teknolojiler
Python, Flask, SQLite, Groq API

## Klasör yapısı
smartlead_ai/
├── run.py                  Sunucuyu başlatan giriş dosyası
├── config.py               Ayarlar ve asistanın kişiliği (BUSINESS_CONTEXT)
├── requirements.txt        Gerekli kütüphaneler
├── .env                    Gizli anahtarlar (GitHub'a yüklenmez)
├── .gitignore
└── app/
    ├── __init__.py         Uygulamanın kurulumu
    ├── database.py         Veritabanı işlemleri (SQL sadece burada)
    ├── routes.py           İstekleri karşılayan rotalar
    ├── templates/          index.html ve dashboard.html
    └── services/
        └── ai_service.py   Yapay zekâ çağrıları (sadece burada)

## API uç noktaları
- POST /api/sohbet : Yapay zekâya mesaj gönderir
- POST /api/leads  : Yeni kişi kaydeder
- GET  /api/leads  : Kayıtlı kişileri listeler

## Kurulum
1. Sanal ortam oluşturun: python -m venv venv
2. Etkinleştirin (Windows): venv\Scripts\activate
3. Kütüphaneleri yükleyin: pip install -r requirements.txt
4. Ana klasörde .env dosyası oluşturup GROQ_API_KEY değerini ekleyin.
5. Çalıştırın: python run.py

## Güvenlik
- API anahtarları .env dosyasında tutulur ve GitHub'a yüklenmez.
- SQL sorgularında ? yer tutucusu kullanılır.
- Dış servis çağrıları try-except ile korunur.
