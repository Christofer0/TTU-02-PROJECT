// service/jenisPermohonanService.ts
import { apiClient } from "@/lib/axios";
import type { JenisPermohonan } from "@/types/models/jenisPermohonan.types";

export async function getJenisPermohonan(): Promise<JenisPermohonan[]> {
  const response = await apiClient.get("/jenis-permohonan/");
  return response.data.data;
}
