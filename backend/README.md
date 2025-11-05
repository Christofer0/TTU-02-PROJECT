## ⚙️ Setup & Installation

### 1. Clone Repository From GITHUB

### 2. HAPUS FOLDER backend/migrations

### 3. MASUK cmd backend =>

    # 1. Initialize the database (run once)
        # flask db init

        # 2. Create initial migration
        # flask db migrate -m "Initial migration"

        # 3. Apply migration to database
        # flask db upgrade

### 4. Insert First Data

        # 1. First insert database the database (run once)
        # flask db revision -m "Insert First Data"
        # setelah muncul file di migrations masukkan
                def upgrade():
                    op.execute("""
                        INSERT INTO fakultas (nama_fakultas, created_at, updated_at)
                        VALUES ('Fakultas Teknologi Informasi', NOW(), NOW())
                    """)

                    op.execute("""
                        INSERT INTO program_studi (id,nama_prodi, fakultas_id, created_at, updated_at)
                        VALUES (67,'Teknik Informatika',
                        (SELECT id FROM fakultas WHERE nama_fakultas = 'Fakultas Teknologi Informasi'),
                        NOW(), NOW())
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
                    # Hapus Program Studi dulu (foreign key ke fakultas)
                    op.execute("DELETE FROM program_studi WHERE id = 67")

                    # Hapus Fakultas
                    op.execute("DELETE FROM fakultas WHERE nama_fakultas = 'Fakultas Teknologi Informasi'")

                    #Hapus Jenis Permohonan
                    op.execute("DELETE FROM jenis_permohonan WHERE id = 1")
        # flask db upgrade

### 5.

        1. pendaftar pertama akan menjadi role = admin (namun belom benar2 berjalan untuk dashboardnya)
        2. pendaftar ke 2 bisa dosen / mahasiswa. tergantung. jika menggunakan email student maka role = mahasiswa jika email biasa menjadi dosen()
        3. bisa dicoba aplikasinya.

### 6. Create View

        # 1. create view to database (run once)
        # flask db revision -m "create triggers view for users"
        # setelah muncul file di migrations baru, masukkan:

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

            """
            )

        def downgrade():
            op.execute("DROP VIEW IF EXISTS v_mahasiswa CASCADE;")
            op.execute("DROP VIEW IF EXISTS v_dosen CASCADE;")
            op.execute("DROP VIEW IF EXISTS v_admin CASCADE;")

        kembali ke cmd lalu masukkan flask db upgrade
