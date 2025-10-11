import axios, { type AxiosInstance } from "axios";
import { useAuthStore } from "@/stores/auth";

export const apiClient: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:4000/api",
  timeout: 10000,

  validateStatus: function (status) {
    return (status >= 200 && status < 300) || status === 206 || status === 207;
  },
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

// ✅ OPSIONAL: Response interceptor untuk handle token refresh atau redirect
// apiClient.interceptors.response.use(
//   (response) => {
//     return response;
//   },
//   (error) => {
//     // Handle 401 Unauthorized - token expired atau invalid
//     if (error.response && error.response.status === 401) {
//       const authStore = useAuthStore();
//       authStore.clearAuth(); // Clear auth state

//       // Redirect to login (sesuaikan dengan router Anda)
//       if (window.location.pathname !== "/login") {
//         window.location.href = "/login";
//       }
//     }
//     return Promise.reject(error);
//   }
// );
