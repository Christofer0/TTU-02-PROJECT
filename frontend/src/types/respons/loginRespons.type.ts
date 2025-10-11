import type { User, DosenData, MahasiswaData } from "../models/user.type";

export interface LoginSuccessResponse {
  access_token: string;
  refresh_token: string;
  expires_in: number;
  user: User;
  dosen?: DosenData;
  mahasiswa?: MahasiswaData;
}

export interface CompleteProfileRequest {
  token: string;
  semester: number;
  no_hp: string;
}

export interface CompleteProfileAdminRequest {
  token: string;
  nomor_induk: string;
  no_hp: string;
}

export interface ApiError {
  success: false;
  message: string;
  errors?: Record<string, string[]>;
}

export interface GoogleLoginResponse {
  success: boolean;
  message: string;
  data: {
    needs_profile: boolean;
    role?: string;
    nomor_induk?: string;
    prodi_id?: number;
    email?: string;
    nama?: string;
    picture?: string;
    access_token?: string;
    refresh_token?: string;
    user?: User;
    mahasiswa?: MahasiswaData;
  };
}
