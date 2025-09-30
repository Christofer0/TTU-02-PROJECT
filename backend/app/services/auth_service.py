# services/auth_service.py
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token, create_refresh_token
from app.repositories.user_repository import UserRepository
from app.repositories.mahasiswa_repository import MahasiswaRepository
from app.repositories.dosen_repository import DosenRepository
from utils.password_utils import hash_password, check_password
from app.models.user_model import User
from app.models.mahasiswa_model import Mahasiswa
from app.models.dosen_model import Dosen
from extensions import db

class AuthService:
    """Service for authentication operations"""
    
    def __init__(self):
        self.user_repo = UserRepository()
        self.mahasiswa_repo = MahasiswaRepository()
        self.dosen_repo = DosenRepository()
    
    def login(self, nomor_induk: str, password: str) -> tuple:
        """Authenticate user login"""
        # Get user by nomor induk
        user = self.user_repo.get_by_nomor_induk(nomor_induk)
        
        if not user:
            return None, "User not found"
        
        if not user.is_active:
            return None, "Account is deactivated"
        
        # Check password
        if not check_password(password, user.password):
            return None, "Invalid password"
        
        # Update last login
        self.user_repo.update_last_login(user.id)
        
        # Create tokens
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': user
        }, None
    
    def register(self, user_data: dict) -> tuple:
        """Register new user with auto role assignment"""
        try:
            # Check if nomor_induk already exists
            existing_user = self.user_repo.get_by_nomor_induk(user_data['nomor_induk'])
            if existing_user:
                return None, "Nomor induk already exists"
            
            # Check if email already exists
            existing_email = self.user_repo.get_by_email(user_data['email'])
            if existing_email:
                return None, "Email already exists"
            
            # Auto assign role based on user count
            user_count = self.user_repo.get_user_count()
            if user_count == 0:
                # First user becomes admin
                assigned_role = 'admin'
            else:
                # Use provided role or default to mahasiswa
                assigned_role = user_data.get('role', 'mahasiswa')
            
            # Hash password
            user_data['password'] = hash_password(user_data['password'])
            
            # Create user with assigned role
            user = User(
                nomor_induk=user_data['nomor_induk'],
                password=user_data['password'],
                nama=user_data['nama'],
                email=user_data['email'],
                role=assigned_role,  # Use assigned role
                no_hp=user_data.get('no_hp'),
                is_active=user_data.get('is_active', True)
            )
            
            db.session.add(user)
            db.session.flush()  # Get user.id
            
            # Create role-specific record only for non-admin users
            if user.role == 'mahasiswa':
                # Untuk mahasiswa, fakultas_id dan program_studi_id bisa optional saat registrasi
                # Bisa di-set nanti melalui update profile
                mahasiswa = Mahasiswa(
                    user_id=user.id,
                    fakultas_id=user_data.get('fakultas_id'),
                    program_studi_id=user_data.get('program_studi_id'),
                    semester=user_data.get('semester', 1)
                )
                db.session.add(mahasiswa)
            
            elif user.role == 'dosen':
                dosen = Dosen(
                    user_id=user.id,
                    fakultas_id=user_data.get('fakultas_id'),
                    gelar_depan=user_data.get('gelar_depan'),
                    gelar_belakang=user_data.get('gelar_belakang'),
                    jabatan=user_data.get('jabatan'),
                    ttd_path=user_data.get('ttd_path'),
                    signature_upload_at=user_data.get('signature_upload_at')
                )
                db.session.add(dosen)
            
            # Admin tidak perlu tabel tambahan
            
            db.session.commit()
            return user, None
            
        except Exception as e:
            db.session.rollback()
            return None, str(e)
    
    def refresh_token(self, user_id: str) -> tuple:
        """Create new access token"""
        user = self.user_repo.get_by_id(user_id)
        if not user or not user.is_active:
            return None, "Invalid user"
        
        access_token = create_access_token(identity=user_id)
        return {'access_token': access_token}, None