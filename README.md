# Aplikasi Pendaftaran Mahasiswa Baru - Tech Edition

Aplikasi web untuk pendaftaran mahasiswa baru dengan tampilan modern teknologis. Aplikasi ini menggunakan **Python Flask** sebagai backend dan **MySQL** sebagai database.

## 📸 Screenshot Aplikasi

<!-- TAMBAHKAN SCREENSHOT APLIKASI DI SINI -->
![Form Pendaftaran](/static/images/docs/form-pendaftaran.png)
![Halaman Sukses](/static/images/docs/success-page.png)
![Panel Admin](/static/images/docs/admin-panel.png)

## 🚀 Teknologi yang Digunakan

- **Backend:** Python 3 dengan framework Flask
- **Database:** MySQL
- **Frontend:** HTML5, CSS3
- **Font:** Google Fonts (Outfit, Rajdhani)
- **Efek Visual:** CSS Animations, Gradients, Glassmorphism

## 📋 Prasyarat

Sebelum menjalankan aplikasi, pastikan Anda memiliki:

1. Python 3.7+ terinstall
2. MySQL Server (bisa melalui XAMPP, WAMP, atau instalasi langsung)
3. Pip (Python package manager)

## 💻 Instalasi

### 1. Clone atau Download Repository

```bash
git clone [url-repository] 
# atau download ZIP dan ekstrak
```

### 2. Setup Database

1. Jalankan MySQL Server
2. Buka phpMyAdmin atau MySQL CLI
3. Import file SQL dari folder database:

```bash
mysql -u root -p < database/setup.sql
```

Atau melalui phpMyAdmin:
- Buka http://localhost/phpmyadmin
- Buat database baru bernama `db_pendaftaran_maba`
- Import file `database/setup.sql`

### 3. Setup Virtual Environment

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Untuk Windows
venv\Scripts\activate
# Untuk MacOS/Linux
source venv/bin/activate

# Install dependensi
pip install -r requirements.txt
```

### 4. Konfigurasi Database

Edit file `config/database.py` sesuai dengan konfigurasi MySQL Anda:

```python
DB_CONFIG = {
    'host': 'localhost',
    'database': 'db_pendaftaran_maba',
    'user': 'root',  # Sesuaikan dengan username MySQL Anda
    'password': ''   # Sesuaikan dengan password MySQL Anda
}
```

## 🔧 Menjalankan Aplikasi

1. Pastikan virtual environment aktif
2. Pastikan MySQL server berjalan
3. Jalankan aplikasi:

```bash
python run.py
```

4. Buka browser dan akses:
   - Form Pendaftaran: http://localhost:5000/
   - Panel Admin: http://localhost:5000/admin/pendaftar

## 📁 Struktur Proyek

```
/project-root
│
├── /app                # Folder utama aplikasi
│   ├── __init__.py     # File inisialisasi aplikasi
│   ├── config.py       # Konfigurasi aplikasi
│   ├── models.py       # Definisi model database
│   ├── routes.py       # Definisi route/endpoint
│   └── templates/      # Folder untuk file HTML
│
├── /static             # Folder untuk file statis
│   ├── /css             # File CSS
│   ├── /js              # File JavaScript
│   └── /images          # Gambar
│
├── /database            # Folder untuk file database
│   └── setup.sql       # Script untuk setup database
│
├── requirements.txt     # Daftar dependensi Python
└── run.py              # File untuk menjalankan aplikasi
```

## 📤 File untuk Push ke GitHub

Berikut daftar file yang harus disertakan saat mendorong proyek ke GitHub:

- Semua file dan folder di atas kecuali:
  - `venv/`         # Folder virtual environment
  - `*.pyc`         # File bytecode Python
  - `__pycache__/`  # Folder cache Python
  - `.env`          # File konfigurasi lingkungan (jika ada)
  - `database/`     # Folder yang berisi file SQL setup database


