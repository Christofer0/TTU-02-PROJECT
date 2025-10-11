import { apiClient } from "@/lib/axios";
import type { LoginResponse } from "../types/respons/loginRespons.type";

// export async function login(nomor_induk: string, password: string) {
//   const { data } = await apiClient.post("/auth/login", {
//     nomor_induk,
//     password,
//   });

//   return data.data as LoginResponse;
// }

const API_URL = apiClient;

// Traditional login
export async function login(
  nomor_induk: string,
  password: string
): Promise<LoginResponse> {
  try {
    const response = await apiClient.post(`${API_URL}/auth/login`, {
      nomor_induk,
      password,
    });

    if (response.data.success) {
      return response.data.data;
    }

    throw new Error(response.data.message || "Login gagal");
  } catch (error: any) {
    if (error.response?.data?.message) {
      throw new Error(error.response.data.message);
    }
    throw error;
  }
}

// Google OAuth login
export async function loginWithGoogle(
  googleToken: string
): Promise<LoginResponse> {
  try {
    const response = await apiClient.post(`${API_URL}/auth/google`, {
      token: googleToken,
    });

    if (response.data.success) {
      return response.data.data;
    }

    throw new Error(response.data.message || "Google login gagal");
  } catch (error: any) {
    if (error.response?.data?.message) {
      throw new Error(error.response.data.message);
    }
    throw error;
  }
}

// Logout
export async function logout(): Promise<void> {
  // Clear local storage
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
  localStorage.removeItem("user");
}
