# utils/file_utils.py
import os
import uuid
from datetime import datetime
from flask import current_app
from werkzeug.utils import secure_filename

def allowed_file(filename):
    """Check if file extension is allowed"""
    if not filename:
        return False
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def generate_unique_filename(original_filename):
    """Generate unique filename"""
    if not original_filename:
        return None
    
    # Get file extension
    ext = ''
    if '.' in original_filename:
        ext = '.' + original_filename.rsplit('.', 1)[1].lower()
    
    # Generate unique name
    unique_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"{timestamp}_{unique_id}{ext}"

def save_uploaded_file(file, subfolder=''):
    """Save uploaded file and return file path"""
    if not file or not allowed_file(file.filename):
        return None, "File type not allowed"
    
    try:
        # Generate unique filename
        filename = generate_unique_filename(file.filename)
        
        # Create full path
        upload_folder = current_app.config['UPLOAD_FOLDER']
        if subfolder:
            upload_folder = os.path.join(upload_folder, subfolder)
            os.makedirs(upload_folder, exist_ok=True)
        
        file_path = os.path.join(upload_folder, filename)
        
        # Save file
        file.save(file_path)
        
        # Return relative path
        if subfolder:
            return os.path.join(subfolder, filename), None
        else:
            return filename, None
            
    except Exception as e:
        return None, str(e)
