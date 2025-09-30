import { apiClient } from "@/lib/axios";

export const createPermohonan = async (data: {
  id_dosen: string;
  id_jenis_permohonan: number;
  judul: string;
  deskripsi?: string;
  file?: File;
}) => {
  const formData = new FormData();
  formData.append("id_dosen", data.id_dosen);
  formData.append("id_jenis_permohonan", String(data.id_jenis_permohonan));
  formData.append("judul", data.judul);
  if (data.deskripsi) formData.append("deskripsi", data.deskripsi);
  if (data.file) formData.append("file", data.file);

  const res = await apiClient.post("/permohonan/", formData);

  return res.data;
};
