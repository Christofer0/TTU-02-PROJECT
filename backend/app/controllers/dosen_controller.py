#app/controller/dosen_controller.py
from flask import Blueprint, jsonify, request
from app.services.dosen_service import DosenService
from flask_jwt_extended import jwt_required,get_jwt_identity
from utils.response_utils import success_response, error_response
from utils.file_utils import save_uploaded_file
from PIL import Image

dosen_bp = Blueprint("dosen", __name__)
dosen_service = DosenService()


@dosen_bp.route("/", methods=["GET"])
def get_all_dosen():
    result = dosen_service.get_all_dosen()
    return jsonify(result), 200




@dosen_bp.route('/upload-signature', methods=['POST'])
@jwt_required()
def upload_signature():
    """Upload dosen signature"""
    try:
        # Ambil user ID dari JWT
        user_id = get_jwt_identity()

        if 'signature' not in request.files:
            return error_response("No signature file provided", status_code=400)
        
        file = request.files['signature']
        if file.filename == '':
            return error_response("No file selected", status_code=400)
        
        # img = Image.open(file)
        # if img.width != 900 or img.height != 900:
        #     return error_response(f"Ukuran TTD harus 724X344 px", status_code=400)
        
        # Save file
        file_path, error = save_uploaded_file(file, 'signatures')
        if error:
            return error_response(f"Failed to save signature: {error}", status_code=400)
        
        # Update dosen record
        dosen, error = dosen_service.upload_signature(user_id, file_path)
        if error:
            return error_response(error, status_code=500)
        
        from schemas.dosen_schema import DosenSchema
        dosen_schema = DosenSchema()
        dosen_data = dosen_schema.dump(dosen)
        return success_response("Signature uploaded successfully", dosen_data)
        
    except Exception as e:
        return error_response("Failed to upload signature", str(e), 500)

