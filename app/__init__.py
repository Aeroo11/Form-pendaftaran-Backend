from flask import Flask
import os

def create_app():
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    
    # Konfigurasi aplikasi
    app.secret_key = os.environ.get('SECRET_KEY', 'maba_form_secret_key')
    
    # Daftarkan routes
    from app.routes import register_routes
    register_routes(app)
    
    # Daftarkan error handlers
    from app.routes import register_error_handlers
    register_error_handlers(app)
    
    return app
