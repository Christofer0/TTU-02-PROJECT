export interface RegisterPayload {
  nomor_induk: string;
  nama: string;
  email: string;
  password: string;
  fakultas_id: number;
  program_studi_id: number;
  semester: number;
  no_hp?: string | null;
  // Hanya untuk validasi frontend, tidak dikirim ke backend
  confirmPassword?: string;
}
