"""first insert

Revision ID: f9f6fc677798
Revises: 2edbc929fb9a
Create Date: 2025-10-07 22:32:16.462677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9f6fc677798'
down_revision = '2edbc929fb9a'
branch_labels = None
depends_on = None


def upgrade():
    # Tambahkan fakultas baru
    op.execute("""
        INSERT INTO fakultas (nama_fakultas, created_at, updated_at)
        VALUES ('Fakultas Teknologi Informasi', NOW(), NOW());
    """)

    # Tambahkan program studi dengan ID 67
    op.execute("""
        INSERT INTO program_studi (id, nama_prodi, fakultas_id, created_at, updated_at)
        VALUES (
            67,
            'Teknik Informatika',
            (SELECT id FROM fakultas WHERE nama_fakultas = 'Fakultas Teknologi Informasi'),
            NOW(),
            NOW()
        );
    """)

    # Tambahkan jenis permohonan dengan route_path
    op.execute("""
        INSERT INTO jenis_permohonan 
        (id, nama_jenis_permohonan, deskripsi, route_path, is_active, created_at, updated_at) 
        VALUES
        (
            1,
            'Surat Permohonan TTD',
            'Permohonan TTD untuk perizinan mahasiswa mengambil TTU1, TTU2, KP',
            '/PermohonanTTD',
            True,
            NOW(),
            NOW()
        );
    """)


def downgrade():
    # Hapus Program Studi
    op.execute("DELETE FROM program_studi WHERE id = 67;")

    # Hapus Fakultas
    op.execute("DELETE FROM fakultas WHERE nama_fakultas = 'Fakultas Teknologi Informasi';")

    # Hapus Jenis Permohonan
    op.execute("DELETE FROM jenis_permohonan WHERE id = 1;")