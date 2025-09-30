import { apiClient } from "../lib/axios";
import type { RegisterPayload } from "@/types/payload/registerPayload.type";

export async function registerMahasiswa(payload: RegisterPayload) {
  const { confirmPassword, ...dataToSend } = payload; // buang confirmPassword
  const { data } = await apiClient.post("/auth/register", dataToSend);
  return data;
}
