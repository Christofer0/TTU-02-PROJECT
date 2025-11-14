from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz
from flask_mail import Message
from extensions import db, mail
from app.models.permohonan_model import Permohonan
from app.models.dosen_model import Dosen
from app.models.user_model import User

# Inisialisasi scheduler dengan timezone Jakarta
scheduler = BackgroundScheduler(timezone=pytz.timezone("Asia/Jakarta"))


def send_weekly_pending_notifications():

    # Ambil semua dosen
    dosen_list = User.query.filter_by(role="dosen").all()

    for dosen in dosen_list:
        if not dosen.email:
            continue
        
        # Hitung pending milik dosen
        jumlah_pending = (
            Permohonan.query
            .filter_by(id_dosen=dosen.id, status_permohonan="pending")
            .count()
        )

        if jumlah_pending == 0:
            continue  

        subject = f"Pengingat Permohonan Pending - {datetime.now().strftime('%d %b %Y')}"
        body = (
            f"Halo {dosen.nama},\n\n"
            f"Ada {jumlah_pending} permohonan pending.\n"
            "Mohon ditinjau.\n\nSalam,\nFTI-Service"
        )

        try:
            msg = Message(subject, recipients=[dosen.email], body=body)
            mail.send(msg)
        except Exception as e:
            print(f"[ERROR] gagal kirim email {dosen.email}: {e}")
    


def start_scheduler(app):
    """Inisialisasi APScheduler"""
    # Bungkus fungsi job agar memiliki app_context dari Flask
    def job_wrapper():
        with app.app_context():
            send_weekly_pending_notifications()

    # Jadwalkan job
    scheduler.add_job(
        func=job_wrapper,
        trigger='cron',
        day_of_week='*',  
        hour=9,             # Jam 09:00 WIB
        minute=00,
        timezone=pytz.timezone("Asia/Jakarta")
    )

    scheduler.start()
    
