// Base user
export interface User {
  id: string;
  nomor_induk: string;
  nama: string;
  email: string;
  no_hp: string | null;
  role: "admin" | "dosen" | "mahasiswa"; // fix tiga role
  is_active: boolean;
  is_admin: boolean;
  is_dosen: boolean;
  is_mahasiswa: boolean;
  created_at: string; // ISO string
  updated_at: string; // ISO string
  last_login: string | null;
  signature_upload_at: string | null;
  ttd_path: string | null;
}

// Mahasiswa-specific
export interface MahasiswaData {
  fakultas_id: number;
  program_studi_id: number;
  semester: number;
}

// Dosen-specific
export interface DosenData {
  fakultas_id: number;
  gelar_depan: string | null;
  gelar_belakang: string | null;
  jabatan: string | null;
  ttd_path: string | null;
  signature_upload_at: string | null;
}

// Profile (user + role data)
export interface Profile extends User {
  mahasiswa?: MahasiswaData;
  dosen?: DosenData;
}
