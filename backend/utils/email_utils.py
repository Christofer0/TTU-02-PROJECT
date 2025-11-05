from flask_mail import Message
from extensions import mail
from flask import current_app
from datetime import datetime
import threading

def _send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_permohonan_email(mahasiswa_email, mahasiswa_nama, dosen_nama, status_permohonan, alasan_penolakan=None):
    try:
        # Ambil app context bener2 (wajib utk threading)
        app = current_app._get_current_object()

        now = datetime.utcnow()

        subject = f"Status Permohonan Anda {status_permohonan.capitalize()}"

        if status_permohonan.lower() == "ditandatangani":
            body = (
                f"Halo {mahasiswa_nama},\n\n"
                f"Dosen: {dosen_nama} ✅\n"
                f"Tanggal: {now.strftime('%A, %d %B %Y')}\n\n"
                f"Silakan cek aplikasi untuk melihat dokumen Anda.\n\n"
                f"Terima kasih."
            )
        else:
            alasan_text = f"Alasan Penolakan: {alasan_penolakan}\n\n" if alasan_penolakan else ""
            body = (
                f"Halo {mahasiswa_nama},\n\n"
                f"Dosen: {dosen_nama} ❌\n"
                f"{alasan_text}"
                f"Tanggal: {now.strftime('%A, %d %B %Y')}\n\n"
                f"Silakan lakukan revisi di aplikasi.\n\n"
                f"Terima kasih."
            )

        msg = Message(
            subject=subject,
            recipients=[mahasiswa_email],
            body=body,
            sender=current_app.config.get("MAIL_DEFAULT_SENDER"),
        )

        # Kirim email di background (tidak bikin API lemot)
        thread = threading.Thread(target=_send_async_email, args=(app, msg))
        thread.start()

        return True, None

    except Exception as e:
        return False, str(e)
