
# controllers/admin_controller.py (Additional controller for admin functions)
from flask import Blueprint,request
from utils.jwt_utils import role_required, get_current_user,jwt_required
from utils.response_utils import success_response, error_response
from app.services.history_service import HistoryService
from schemas.permohonan_schema import PermohonanSchema

admin_bp = Blueprint('admin', __name__)
service_history = HistoryService()
permohonan_schema = PermohonanSchema()
def check_role_admin():
    current_user = get_current_user()
    role = getattr(current_user, "role", None)

    if role != "admin":
        return False, None, role
    return True, current_user, role


@admin_bp.route('/users', methods=['GET'])
@role_required('admin')
def get_all_users(current_user):
    """Get all users (admin only)"""
    try:
        # Implementation for getting all users
        return success_response("Users retrieved", [])
    except Exception as e:
        return error_response("Failed to get users", str(e), 500)

@admin_bp.route('/users/<user_id>/toggle-status', methods=['POST'])
@role_required('admin')
def toggle_user_status(current_user, user_id):
    """Toggle user active status (admin only)"""
    try:
        # Implementation for toggling user status
        return success_response("User status updated")
    except Exception as e:
        return error_response("Failed to update user status", str(e), 500)
    
# @admin_bp.route('/permohonan-list', methods=['GET'])
# # @role_required('admin')
# @jwt_required()
# def get_all_permohonan():
#     """Toogle permohonan pending"""
#     is_admin, user, role = check_role_admin()
#     if not is_admin:
#         return error_response("You are not Admin", status_code=403)
#     try:
#         list_permohonan = service_history.get_all_history(user,role)

#         if not list_permohonan:
#             return error_response("No history found", status_code=404)
#         permohonan_list = permohonan_schema.dump(list_permohonan)
#         print(permohonan_list)
#         return success_response("History counts retrieved",permohonan_list)
        
#     except Exception as e:
#         print("Error Get ALL history FOR ADMIN: ", str(e))
#         return error_response("Failed to get counts", str(e), 500)



# permohonan_data = permohonan_schema.dump(permohonan)
# return success_response("Permohonan detail retrieved", permohonan_data)
    
# @admin_bp.route('/permohonan/<string:status>', methods=['GET'])
# @jwt_required()
# def get_permohonan_admin(status):
#     """
#     Ambil permohonan (semua atau berdasarkan status) — khusus admin
#     Contoh:
#     - /api/admin/permohonan → semua
#     - /api/admin/permohonan?status=pending → hanya pending
#     """
#     try:
#         current_user = get_current_user()
#         if current_user.role != "admin":
#             return error_response("You are not Admin", status_code=403)

#         # Ambil parameter status dari query string (?status=xxx)
#         print("DEBIG STATUS: ",status)
#         if status:
#             # Ambil berdasarkan status
#             permohonan_list = service_history.get_history_by_status(
#                 user_id=current_user.id,
#                 role=current_user.role,
#                 status=status
#             )
#         else:
#             return error_response("GAADA",status_code=403)
#             # Ambil semua permohonan
#             # permohonan_list = service_history.get_all_history(
#             #     user_id=current_user.id,
#             #     role=current_user.role
#             # )

#         if not permohonan_list:
#             return error_response("No permohonan found", status_code=404)

#         return success_response(
#             "Permohonan retrieved successfully",
#             permohonan_schema.dump(permohonan_list)
#         )

#     except Exception as e:
#         print("Error get_permohonan_admin:", str(e))
#         return error_response("Failed to retrieve permohonan", str(e), 500)


@admin_bp.route('/permohonan/<string:status>', methods=['GET'])
@jwt_required()
def get_all_permohonan(status):
    """
    Ambil semua data permohonan — seperti SELECT * FROM permohonan
    """
    try:
        current_user = get_current_user()
        if current_user.role != "admin":
            return error_response("You are not Admin", status_code=403)


        # Ambil semua data dari repo
        role = current_user.role
        permohonan_list = service_history.get_history_by_status(current_user,role, status)

        if not permohonan_list:
            return error_response("No data found", status_code=404)

        # Serialize pakai schema Marshmallow
        data = permohonan_schema.dump(permohonan_list, many=True)

        return success_response("All permohonan retrieved", data)

    except Exception as e:
        print("Error get_all_permohonan:", str(e))
        return error_response("Failed to retrieve data", str(e), 500)
