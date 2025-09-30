"""insert data

Revision ID: 3b24fd54516a
Revises: 5257dd84e928
Create Date: 2025-09-20 02:08:26.655743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b24fd54516a'
down_revision = '5257dd84e928'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        INSERT INTO fakultas (nama_fakultas, created_at, updated_at)
        VALUES ('Fakultas Teknologi Informasi', NOW(), NOW())
    """)

    op.execute("""
        INSERT INTO program_studi (nama_prodi, fakultas_id, created_at, updated_at)
        VALUES ('Teknik Informatika', 
        (SELECT id FROM fakultas WHERE nama_fakultas = 'Fakultas Teknologi Informasi'),
        NOW(), NOW())
    """)

    op.execute("""
        INSERT INTO jenis_permohonan 
        (id, nama_jenis_permohonan, deskripsi, is_active, created_at, updated_at) 
        VALUES
        (1, 'Surat Permohonan TTD', 'Permohonan TTD untuk perizinan mahasiswa mengambil TTU1, TTU2, KP', True, NOW(), NOW());
    """)

def downgrade():
    # Hapus Program Studi dulu (foreign key ke fakultas)
    op.execute("DELETE FROM program_studi WHERE id = 67")

    # Hapus Fakultas
    op.execute("DELETE FROM fakultas WHERE nama_fakultas = 'Fakultas Teknologi Informasi'")

    #Hapus Jenis Permohonan
    op.execute("DELETE FROM jenis_permohonan WHERE id = 1")