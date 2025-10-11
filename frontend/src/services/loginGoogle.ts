import { ref } from "vue";
import type {
  GoogleLoginResponse,
  CompleteProfileRequest,
  LoginSuccessResponse,
} from "@/types/respons";
import { apiClient } from "@/lib/axios";

export function useGoogleAuth() {
  const loading = ref(false);
  const error = ref("");

  const API_BASE_URL =
    import.meta.env.VITE_API_BASE_URL || "http://localhost:5000";

  /**
   * Login with Google token
   */
  const loginWithGoogle = async (
    googleToken: string
  ): Promise<GoogleLoginResponse | null> => {
    loading.value = true;
    error.value = "";

    try {
      const response = await apiClient.post(
        `${API_BASE_URL}/api/auth/google/login`,
        {
          token: googleToken,
        }
      );

      const data: GoogleLoginResponse = await response.data.json();

      if (!response.data.ok) {
        error.value = data.message || "Login gagal";
        return null;
      }

      return data;
    } catch (err) {
      error.value = "Terjadi kesalahan koneksi. Silakan coba lagi.";
      console.error("Google login error:", err);
      return null;
    } finally {
      loading.value = false;
    }
  };

  /**
   * Complete profile for mahasiswa
   */
  const completeProfileMahasiswa = async (
    payload: CompleteProfileRequest
  ): Promise<LoginSuccessResponse | null> => {
    loading.value = true;
    error.value = "";

    try {
      const response = await fetch(
        `${API_BASE_URL}/api/auth/google/complete-profile/mahasiswa`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        }
      );

      const data: LoginSuccessResponse = await response.json();

      if (!response.ok) {
        error.value = "Registrasi gagal";
        return null;
      }

      return data;
    } catch (err) {
      error.value = "Terjadi kesalahan koneksi. Silakan coba lagi.";
      console.error("Complete profile error:", err);
      return null;
    } finally {
      loading.value = false;
    }
  };

  /**
   * Save auth data to localStorage
   */
  const saveAuthData = (
    accessToken: string,
    refreshToken: string,
    user: any
  ) => {
    localStorage.setItem("access_token", accessToken);
    localStorage.setItem("refresh_token", refreshToken);
    localStorage.setItem("user", JSON.stringify(user));
  };

  /**
   * Clear auth data from localStorage
   */
  const clearAuthData = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("user");
  };

  /**
   * Get current user from localStorage
   */
  const getCurrentUser = () => {
    const userStr = localStorage.getItem("user");
    return userStr ? JSON.parse(userStr) : null;
  };

  /**
   * Check if user is authenticated
   */
  const isAuthenticated = () => {
    return !!localStorage.getItem("access_token");
  };

  return {
    loading,
    error,
    loginWithGoogle,
    completeProfileMahasiswa,
    saveAuthData,
    clearAuthData,
    getCurrentUser,
    isAuthenticated,
  };
}
