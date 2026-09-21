import os

class Config:
    # Güvenlik Ayarı (Formlar ve kullanıcı oturumları için şifreleme anahtarı)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nuit-and-co-sessiz-luks-2026'
    
    # Nuit & Co. Şirket Kimliği
    COMPANY_NAME = "Nuit & Co."
    BRAND_IDENTITY = "Sessiz Lüks (Quiet Luxury)"
    ECOSYSTEM_FOCUS = "Uyku Ekosistemi ve Yenilenme"
    
    # İlerisi için Veritabanı Altyapısı (Müşteri ve sipariş verileri için)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///nuit_co.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    