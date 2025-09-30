import axios, { type AxiosInstance } from "axios";
import { useAuthStore } from "@/stores/auth";

export const apiClient: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:4000/api",
  timeout: 10000,
});

// Tambahkan interceptor untuk inject token
apiClient.interceptors.request.use(
  (config) => {
    const authStore = useAuthStore();
    if (authStore.access_token) {
      config.headers.Authorization = `Bearer ${authStore.access_token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
