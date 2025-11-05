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
    """Job: kirim email ke dosen setiap Senin jam 09:00 WIB"""
    print(f"[{datetime.now()}] Menjalankan job weekly pending notification...")

    # Ambil jumlah permohonan pending per dosen
    pending_counts = (
        db.session.query(Permohonan.id_dosen, db.func.count(Permohonan.id))
        .filter(Permohonan.status_permohonan == 'pending')
        .group_by(Permohonan.id_dosen)
        .all()
    )

    for id_dosen, jumlah_pending in pending_counts:
        # Ambil user dari tabel User berdasarkan id_dosen
        dosen_user = User.query.filter_by(id=id_dosen).first()
        if not dosen_user or not dosen_user.email:
            print(f"[WARNING] Dosen dengan ID {id_dosen} tidak punya email, dilewati.")
            continue

        recipient_email = dosen_user.email
        subject = "Pengingat Permohonan Berstatus Pending"
        body = (
            f"Halo {dosen_user.nama},\n\n"
            f"Anda memiliki {jumlah_pending} permohonan yang masih berstatus pending.\n"
            "Mohon segera ditinjau di sistem pengajuan.\n\n"
            "Salam,\nFTI-Service"
        )

        try:
            msg = Message(subject=subject, recipients=[recipient_email], body=body)
            mail.send(msg)
            print(f"[INFO] Email dikirim ke {recipient_email}")
        except Exception as e:
            print(f"[ERROR] Gagal kirim email ke {recipient_email}: {e}")

    


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
        day_of_week='mon',  # Senin
        hour=9,             # Jam 09:00 WIB
        minute=00,
        timezone=pytz.timezone("Asia/Jakarta")
    )

    scheduler.start()
    
