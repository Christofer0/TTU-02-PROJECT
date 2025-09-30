// src/services/dosenService.ts
import { apiClient } from "@/lib/axios";

export interface Dosen {
  id: string; // atau user_id kalau backend pakai itu
  nama: string;
  fakultas_id?: number;
  gelar_depan?: string;
  gelar_belakang?: string;
  jabatan?: string;
}

export const getAllDosen = async (): Promise<Dosen[]> => {
  const res = await apiClient.get("/dosen/");
  return res.data;
};
