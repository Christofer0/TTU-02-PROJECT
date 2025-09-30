# utils/qr_utils.py
import qrcode
import hashlib
import json
import os
from datetime import datetime
from flask import current_app
from PIL import Image

def generate_qr_code(data, permohonan_id):
    """Generate QR code for document verification"""
    try:
        # Create QR code data
        qr_data = {
            'permohonan_id': permohonan_id,
            'timestamp': datetime.utcnow().isoformat(),
            'data': data
        }
        
        # Generate hash for verification
        qr_string = json.dumps(qr_data, sort_keys=True)
        verification_hash = hashlib.sha256(qr_string.encode()).hexdigest()
        
        # Add hash to QR data
        qr_data['hash'] = verification_hash
        
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(json.dumps(qr_data))
        qr.make(fit=True)
        
        # Create QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save QR code
        qr_folder = current_app.config['QR_CODE_FOLDER']
        os.makedirs(qr_folder, exist_ok=True)
        
        filename = f"qr_{permohonan_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        file_path = os.path.join(qr_folder, filename)
        
        img.save(file_path)
        
        return filename, json.dumps(qr_data), None
        
    except Exception as e:
        return None, None, str(e)

def verify_qr_code(qr_data_string):
    """Verify QR code data integrity"""
    try:
        qr_data = json.loads(qr_data_string)
        
        if 'hash' not in qr_data:
            return False, "Invalid QR code format"
        
        # Extract hash and remove it from data
        provided_hash = qr_data.pop('hash')
        
        # Recalculate hash
        qr_string = json.dumps(qr_data, sort_keys=True)
        calculated_hash = hashlib.sha256(qr_string.encode()).hexdigest()
        
        # Verify hash
        if provided_hash != calculated_hash:
            return False, "QR code has been tampered with"
        
        return True, "QR code is valid"
        
    except Exception as e:
        return False, f"Error verifying QR code: {str(e)}"