import { apiClient } from "../lib/axios";
import type { LoginResponse } from "../types/respons/loginRespons.type";

export async function login(nomor_induk: string, password: string) {
  const { data } = await apiClient.post("/auth/login", {
    nomor_induk,
    password,
  });

  return data.data as LoginResponse;
}
