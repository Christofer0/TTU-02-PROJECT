<!-- GoogleLoginFlow.vue -->
<template>
  <div
    class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4"
  >
    <div class="bg-white rounded-2xl shadow-xl w-full max-w-md p-8">
      <!-- Login Step -->
      <div v-if="step === 'login'" class="space-y-6">
        <div class="text-center">
          <h1 class="text-3xl font-bold text-gray-900 mb-2">Selamat Datang</h1>
          <p class="text-gray-600">Masuk dengan akun UKSW Anda</p>
        </div>

        <!-- Error Alert -->
        <div
          v-if="error"
          class="bg-red-50 border border-red-200 rounded-lg p-4 flex items-start gap-3"
        >
          <svg
            class="w-5 h-5 text-red-600 flex-shrink-0 mt-0.5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <p class="text-sm text-red-800">{{ error }}</p>
        </div>

        <!-- Google Sign-In Button -->
        <div class="flex justify-center">
          <div id="googleSignInButton"></div>
        </div>

        <!-- Loading -->
        <div v-if="loading" class="flex justify-center">
          <svg
            class="w-6 h-6 animate-spin text-blue-600"
            fill="none"
            viewBox="0 0 24 24"
          >
            <circle
              class="opacity-25"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              stroke-width="4"
            ></circle>
            <path
              class="opacity-75"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            ></path>
          </svg>
        </div>

        <div class="text-center text-sm text-gray-500">
          <p>Gunakan email @uksw.edu atau @student.uksw.edu</p>
        </div>
      </div>

      <!-- Complete Profile Step - Mahasiswa -->
      <div
        v-else-if="
          step === 'complete-profile' &&
          profileData &&
          profileData.role === 'mahasiswa'
        "
        class="space-y-6"
      >
        <div class="text-center">
          <div
            class="w-20 h-20 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4"
          >
            <img
              :src="profileData.picture"
              :alt="profileData.nama"
              class="w-20 h-20 rounded-full"
            />
          </div>
          <h2 class="text-2xl font-bold text-gray-900 mb-1">
            Lengkapi Profil Anda
          </h2>
          <p class="text-gray-600 text-sm">{{ profileData.nama }}</p>
          <p class="text-gray-500 text-xs">{{ profileData.email }}</p>
        </div>

        <!-- Error Alert -->
        <div
          v-if="error"
          class="bg-red-50 border border-red-200 rounded-lg p-4 flex items-start gap-3"
        >
          <svg
            class="w-5 h-5 text-red-600 flex-shrink-0 mt-0.5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <p class="text-sm text-red-800">{{ error }}</p>
        </div>

        <!-- Form Mahasiswa -->
        <form
          @submit.prevent="handleCompleteProfileMahasiswa"
          class="space-y-4"
        >
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              NIM
            </label>
            <input
              type="text"
              :value="profileData.nomor_induk"
              disabled
              class="w-full px-4 py-2 border border-gray-300 rounded-lg bg-gray-50 text-gray-600"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Semester <span class="text-red-500">*</span>
            </label>
            <select
              v-model="formData.semester"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              required
            >
              <option v-for="sem in 14" :key="sem" :value="sem">
                Semester {{ sem }}
              </option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Nomor HP <span class="text-red-500">*</span>
            </label>
            <input
              v-model="formData.no_hp"
              type="tel"
              placeholder="081234567890"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              required
            />
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 rounded-lg transition duration-200 flex items-center justify-center gap-2 disabled:bg-gray-400 disabled:cursor-not-allowed"
          >
            <svg
              v-if="loading"
              class="w-5 h-5 animate-spin"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                class="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                stroke-width="4"
              ></circle>
              <path
                class="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              ></path>
            </svg>
            <span v-if="loading">Memproses...</span>
            <span v-else>Simpan & Masuk</span>
          </button>
        </form>
      </div>

      <!-- Complete Profile Step - Admin -->
      <div
        v-else-if="
          step === 'complete-profile' &&
          profileData &&
          profileData.role === 'admin'
        "
        class="space-y-6"
      >
        <div class="text-center">
          <div
            class="w-20 h-20 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4"
          >
            <img
              :src="profileData.picture"
              :alt="profileData.nama"
              class="w-20 h-20 rounded-full"
            />
          </div>
          <h2 class="text-2xl font-bold text-gray-900 mb-1">
            Lengkapi Profil Admin
          </h2>
          <p class="text-gray-600 text-sm">{{ profileData.nama }}</p>
          <p class="text-gray-500 text-xs">{{ profileData.email }}</p>
          <span
            class="inline-block px-3 py-1 text-xs font-semibold text-purple-700 bg-purple-100 rounded-full mt-2"
          >
            Administrator
          </span>
        </div>

        <!-- Error Alert -->
        <div
          v-if="error"
          class="bg-red-50 border border-red-200 rounded-lg p-4 flex items-start gap-3"
        >
          <svg
            class="w-5 h-5 text-red-600 flex-shrink-0 mt-0.5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <p class="text-sm text-red-800">{{ error }}</p>
        </div>

        <!-- Form Admin -->
        <form @submit.prevent="handleCompleteProfileAdmin" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Nomor Induk <span class="text-red-500">*</span>
            </label>
            <input
              v-model="formDataAdmin.nomor_induk"
              type="text"
              placeholder="A001"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              required
            />
            <p class="mt-1 text-xs text-gray-500">Contoh: A001, ADM001, dll</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Nomor HP <span class="text-red-500">*</span>
            </label>
            <input
              v-model="formDataAdmin.no_hp"
              type="tel"
              placeholder="081234567890"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              required
            />
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full bg-purple-600 hover:bg-purple-700 text-white font-medium py-3 rounded-lg transition duration-200 flex items-center justify-center gap-2 disabled:bg-gray-400 disabled:cursor-not-allowed"
          >
            <svg
              v-if="loading"
              class="w-5 h-5 animate-spin"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                class="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                stroke-width="4"
              ></circle>
              <path
                class="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              ></path>
            </svg>
            <span v-if="loading">Memproses...</span>
            <span v-else>Simpan & Masuk</span>
          </button>
        </form>
      </div>

      <!-- Success Step -->
      <div v-else-if="step === 'success'" class="text-center space-y-4 py-8">
        <div
          class="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto"
        >
          <svg
            class="w-12 h-12 text-green-600"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M5 13l4 4L19 7"
            />
          </svg>
        </div>
        <h2 class="text-2xl font-bold text-gray-900">Berhasil!</h2>
        <p class="text-gray-600">Anda akan dialihkan ke dashboard...</p>
        <svg
          class="w-6 h-6 animate-spin text-blue-600 mx-auto"
          fill="none"
          viewBox="0 0 24 24"
        >
          <circle
            class="opacity-25"
            cx="12"
            cy="12"
            r="10"
            stroke="currentColor"
            stroke-width="4"
          ></circle>
          <path
            class="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
          ></path>
        </svg>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { apiClient } from "@/lib/axios";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth"; // <--- tambahkan ini

// =========================
// Types
// =========================
interface ProfileData {
  needs_profile: boolean;
  role: string;
  nomor_induk: string;
  program_studi_id: number;
  email: string;
  nama: string;
  picture?: string;
  token?: string;
}

interface FormData {
  semester: number;
  no_hp: string;
}

interface GoogleCallbackResponse {
  credential?: string;
}

// =========================
// Router & Store
// =========================
const router = useRouter();
const authStore = useAuthStore(); // <--- gunakan store Pinia

// =========================
// State
// =========================
const step = ref<"login" | "complete-profile" | "success">("login");
const loading = ref(false);
const error = ref("");
const profileData = ref<ProfileData | null>(null);
const formData = ref<FormData>({
  semester: 1,
  no_hp: "",
});
const formDataAdmin = ref({
  nomor_induk: "",
  no_hp: "",
});

// =========================
// Config
// =========================
const GOOGLE_CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID;

// =========================
// Initialize Google Sign-In
// =========================
onMounted(() => {
  const script = document.createElement("script");
  script.src = "https://accounts.google.com/gsi/client";
  script.async = true;
  script.defer = true;
  document.body.appendChild(script);

  script.onload = () => {
    if (window.google) {
      window.google.accounts.id.initialize({
        client_id: GOOGLE_CLIENT_ID,
        callback: handleGoogleCallback,
      });

      window.google.accounts.id.renderButton(
        document.getElementById("googleSignInButton")!,
        {
          theme: "outline",
          size: "large",
          text: "signin_with",
          width: "350",
        }
      );
    }
  };
});

// =========================
// Handle Google callback
// =========================
const handleGoogleCallback = async (response: GoogleCallbackResponse) => {
  loading.value = true;
  error.value = "";

  try {
    const res = await apiClient.post(`/auth/google/login`, {
      token: response.credential,
    });

    const data = res.data;
    console.log(data, "resData");

    // === CASE 1: Need to complete profile ===
    if (res.status === 206) {
      profileData.value = {
        ...data.data,
        token: response.credential,
      };
      step.value = "complete-profile";
    }

    // === CASE 2: Login success ===
    else if (data.success) {
      // Simpan token dan user ke localStorage
      localStorage.setItem("access_token", data.data.access_token);
      localStorage.setItem("refresh_token", data.data.refresh_token);
      localStorage.setItem("user", JSON.stringify(data.data.user));

      // Simpan ke Pinia store juga
      authStore.setAccessToken(data.data.access_token);
      authStore.setRefreshToken(data.data.refresh_token);
      authStore.setUser(data.data.user);

      step.value = "success";

      // Redirect berdasarkan role
      const role = data.data.user.role;
      console.log(role, "ini role");
      const routes: Record<string, string> = {
        admin: "/admin/dashboard",
        dosen: "/dosen/dashboard",
        mahasiswa: "/mahasiswa/dashboard",
      };

      router.push(routes[role] || "/dashboard");
    }

    // === CASE 3: Error dari backend ===
    else {
      error.value = data.message || "Login gagal";
    }
  } catch (err) {
    error.value = "Terjadi kesalahan. Silakan coba lagi.";
    console.error(err);
  } finally {
    loading.value = false;
  }
};

// =========================
// Handle complete profile (Mahasiswa)
// =========================
const handleCompleteProfileMahasiswa = async () => {
  loading.value = true;
  error.value = "";

  try {
    const res = await apiClient.post(
      `/auth/google/complete-profile/mahasiswa`,
      {
        token: profileData.value?.token,
        semester: parseInt(formData.value.semester.toString()),
        no_hp: formData.value.no_hp,
      }
    );

    const data = res.data;

    if (data.success) {
      // Simpan ke localStorage
      localStorage.setItem("access_token", data.data.access_token);
      localStorage.setItem("refresh_token", data.data.refresh_token);
      localStorage.setItem("user", JSON.stringify(data.data.user));

      // Simpan juga ke store
      authStore.setAccessToken(data.data.access_token);
      authStore.setRefreshToken(data.data.refresh_token);
      authStore.setUser(data.data.user);

      step.value = "success";

      router.push("/mahasiswa/dashboard");
    } else {
      error.value = data.message || "Registrasi gagal";
    }
  } catch (err) {
    error.value = "Terjadi kesalahan. Silakan coba lagi.";
    console.error(err);
  } finally {
    loading.value = false;
  }
};

// =========================
// Handle complete profile (Admin)
// =========================
const handleCompleteProfileAdmin = async () => {
  loading.value = true;
  error.value = "";

  try {
    const res = await apiClient.post(`/auth/google/complete-profile/admin`, {
      token: profileData.value?.token,
      nomor_induk: formDataAdmin.value.nomor_induk,
      no_hp: formDataAdmin.value.no_hp,
    });

    const data = res.data;

    if (data.success) {
      // Simpan ke localStorage
      localStorage.setItem("access_token", data.data.access_token);
      localStorage.setItem("refresh_token", data.data.refresh_token);
      localStorage.setItem("user", JSON.stringify(data.data.user));

      // Simpan juga ke store
      authStore.setAccessToken(data.data.access_token);
      authStore.setRefreshToken(data.data.refresh_token);
      authStore.setUser(data.data.user);

      step.value = "success";

      router.push("/admin/dashboard");
    } else {
      error.value = data.message || "Registrasi gagal";
    }
  } catch (err) {
    error.value = "Terjadi kesalahan. Silakan coba lagi.";
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>
