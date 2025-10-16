"""create views_mhs dosen dll

Revision ID: f7c634c9381d
Revises: f9f6fc677798
Create Date: 2025-10-15 14:59:45.730519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7c634c9381d'
down_revision = 'f9f6fc677798'
branch_labels = None
depends_on = None


def upgrade():
    op.execute (
    """
        -- =========================
        -- TRIGGERS untuk updated_at
        -- =========================
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = CURRENT_TIMESTAMP;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;

        CREATE TRIGGER update_fakultas_updated_at BEFORE UPDATE ON fakultas
            FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

        CREATE TRIGGER update_program_studi_updated_at BEFORE UPDATE ON program_studi
            FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

        CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
            FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

        CREATE TRIGGER update_permohonan_updated_at BEFORE UPDATE ON permohonan
            FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

        -- =========================
        -- VIEWS
        -- =========================

        -- VIEW Mahasiswa
        CREATE VIEW v_mahasiswa AS
        SELECT 
            u.id as user_id,
            u.nomor_induk,
            u.nama,
            u.email,
            u.no_hp,
            u.is_active,
            m.semester,
            f.id as fakultas_id,
            f.nama_fakultas,
            ps.id as program_studi_id,
            ps.nama_prodi,
            u.created_at,
            u.last_login
        FROM users u
        JOIN mahasiswa m ON u.id = m.user_id
        JOIN fakultas f ON m.fakultas_id = f.id
        JOIN program_studi ps ON m.program_studi_id = ps.id
        WHERE u.role = 'mahasiswa';

        -- VIEW Dosen
        CREATE VIEW v_dosen AS
        SELECT 
            u.id as user_id,
            u.nomor_induk,
            u.nama,
            u.email,
            u.no_hp,
            u.is_active,
            d.gelar_depan,
            d.gelar_belakang,
            CASE 
                WHEN d.gelar_depan IS NOT NULL AND d.gelar_belakang IS NOT NULL THEN
                    CONCAT(d.gelar_depan, ' ', u.nama, ' ', d.gelar_belakang)
                WHEN d.gelar_depan IS NOT NULL THEN
                    CONCAT(d.gelar_depan, ' ', u.nama)
                WHEN d.gelar_belakang IS NOT NULL THEN
                    CONCAT(u.nama, ' ', d.gelar_belakang)
                ELSE u.nama
            END as nama_lengkap,
            d.jabatan,
            f.id as fakultas_id,
            f.nama_fakultas,
            d.ttd_path,
            d.signature_upload_at,
            u.created_at,
            u.last_login
        FROM users u
        JOIN dosen d ON u.id = d.user_id
        LEFT JOIN fakultas f ON d.fakultas_id = f.id
        WHERE u.role = 'dosen';

        -- VIEW Admin
        CREATE VIEW v_admin AS
        SELECT 
            u.id as user_id,
            u.nomor_induk,
            u.nama,
            u.email,
            u.no_hp,
            u.is_active,
            u.created_at,
            u.last_login
        FROM users u
        WHERE u.role = 'admin';
    """
    )

def downgrade():
    op.execute("DROP VIEW IF EXISTS v_mahasiswa CASCADE;")
    op.execute("DROP VIEW IF EXISTS v_dosen CASCADE;")
    op.execute("DROP VIEW IF EXISTS v_admin CASCADE;")