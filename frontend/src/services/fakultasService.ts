import { apiClient } from "@/lib/axios";

export interface Fakultas {
  id: number;
  nama_fakultas: string;
}

export interface ProgramStudi {
  id: number;
  nama_prodi: string;
  fakultas_id: number;
}

// Ambil semua fakultas
export async function getFakultas(): Promise<Fakultas[]> {
  const res = await apiClient.get("/fakultas/");
  return res.data.data || [];
}

// Ambil program studi berdasarkan fakultas
export async function getProdiByFakultas(
  fakultasId: number
): Promise<ProgramStudi[]> {
  const res = await apiClient.get(`/fakultas/${fakultasId}/prodi`);
  return res.data.data || [];
}
