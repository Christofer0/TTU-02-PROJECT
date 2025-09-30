# config.py
import os
from datetime import timedelta
from decouple import config

class Config:
    # Basic Flask config
    SECRET_KEY = config('SECRET_KEY', default='dev-secret-key')
    
    # Database config
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default='sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }
    
    # JWT config
    JWT_SECRET_KEY = config('JWT_SECRET_KEY', default='jwt-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=int(config('JWT_ACCESS_TOKEN_EXPIRES', default=3600)))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(seconds=int(config('JWT_REFRESH_TOKEN_EXPIRES', default=2592000)))
    JWT_ALGORITHM = 'HS256'
    
    # File upload config
    UPLOAD_FOLDER = config('UPLOAD_FOLDER', default='uploads')
    QR_CODE_FOLDER = config('QR_CODE_FOLDER', default='uploads/qr_codes')
    UPLOAD_SIGNED = config('UPLOAD_SIGNED', default='storage/signed')
    DOCUMENT_PERMOHONAN_TTD_PATH = config('DOCUMENT_PERMOHONAN_TTD_PATH', default='storage/signed/permohonan_ttd')
    MAX_CONTENT_LENGTH = int(config('MAX_CONTENT_LENGTH', default=16777216))  # 16MB
    ALLOWED_EXTENSIONS = set(config('ALLOWED_EXTENSIONS', default='pdf,doc,docx,jpg,jpeg,png').split(','))

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    # 'testing': TestingConfig
}