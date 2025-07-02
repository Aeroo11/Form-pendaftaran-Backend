from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from config.database import get_db_connection, close_connection
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'maba_form_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            # Mengambil data dari form
            nama = request.form['nama']
            tanggal_lahir = request.form['tanggal_lahir']
            email = request.form['email']
            telepon = request.form['telepon']
            alamat = request.form['alamat']
            jenis_kelamin = request.form['jenis_kelamin']
            jurusan = request.form['jurusan']
            asal_sekolah = request.form['asal_sekolah']
            nilai = request.form['nilai']
            motivasi = request.form['motivasi']
            
            # Validasi sederhana
            if not nama or not email or not telepon:
                flash('Semua bidang yang wajib harus diisi!')
                return redirect(url_for('index'))
            
            # Menyimpan data ke MySQL
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                
                # Siapkan query SQL
                query = """INSERT INTO pendaftar 
                        (waktu_daftar, nama_lengkap, tanggal_lahir, email, no_telepon, alamat, 
                        jenis_kelamin, jurusan_pilihan, asal_sekolah, nilai_rata_rata, motivasi)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                
                # Data untuk dimasukkan
                data_tuple = (
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    nama, tanggal_lahir, email, telepon, alamat,
                    jenis_kelamin, jurusan, asal_sekolah, nilai, motivasi
                )
                
                # Eksekusi query
                cursor.execute(query, data_tuple)
                conn.commit()
                
                # Tutup koneksi
                close_connection(conn, cursor)
                
                # Redirect ke halaman sukses
                return render_template('success.html', nama=nama)
            else:
                flash('Tidak dapat terhubung ke database!')
                return redirect(url_for('index'))
        
        except Error as e:
            flash(f'Error database: {str(e)}')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Terjadi kesalahan: {str(e)}')
            return redirect(url_for('index'))

# Endpoint untuk melihat semua pendaftar (opsional)
@app.route('/admin/pendaftar')
def lihat_pendaftar():
    try:
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            
            # Query untuk mengambil semua data pendaftar
            query = "SELECT * FROM pendaftar ORDER BY waktu_daftar DESC"
            cursor.execute(query)
            
            # Ambil semua data
            pendaftar_list = cursor.fetchall()
            
            # Tutup koneksi
            close_connection(conn, cursor)
            
            # Render template dengan data
            return render_template('admin/pendaftar.html', pendaftar_list=pendaftar_list)
        else:
            flash('Tidak dapat terhubung ke database!')
            return redirect(url_for('index'))
    
    except Error as e:
        flash(f'Error database: {str(e)}')
        return redirect(url_for('index'))
    except Exception as e:
        flash(f'Terjadi kesalahan: {str(e)}')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
