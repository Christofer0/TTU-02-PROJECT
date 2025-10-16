<template>
  <div
    class="min-h-screen flex items-center justify-center p-4 bg-gradient-to-br from-white via-stone-100 to-zinc-100"
  >
    <!-- Card -->
    <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md p-8">
      <!-- Login Step -->
      <div
        v-if="step === 'login'"
        class="flex flex-col justify-center items-center px-4"
      >
        <!-- Header -->
        <div class="text-center mb-8">
          <!-- Logo -->
          <div class="flex justify-center mb-4">
            <img
              src="@/assets/logo.png"
              alt="FTI-Service Logo"
              class="w-16 h-16"
            />
          </div>

          <h1 class="text-3xl font-bold text-gray-900 mb-2 tracking-tight">
            Selamat Datang 👋
          </h1>
          <p class="text-gray-600 text-sm">
            Masuk ke
            <span class="font-semibold text-slate-600">FTI-Service</span>
            menggunakan akun UKSW Anda
          </p>
        </div>

        <!-- Error Alert -->
        <transition name="fade">
          <div
            v-if="error"
            class="bg-red-50 border border-red-200 rounded-lg p-4 flex items-start gap-3 mb-4 w-full"
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
        </transition>

        <!-- Google Sign-In -->
        <div class="flex justify-center mb-6">
          <div
            id="googleSignInButton"
            class="transform transition-transform hover:scale-105"
          ></div>
        </div>

        <!-- Loading Spinner -->
        <transition name="fade">
          <div v-if="loading" class="flex justify-center mb-4">
            <svg
              class="w-6 h-6 animate-spin text-emerald-600"
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
        </transition>

        <!-- Email Info -->
        <div class="text-center text-sm text-gray-500 mb-2">
          <p>
            Gunakan email
            <span class="font-medium">@uksw.edu</span> atau
            <span class="font-medium">@student.uksw.edu</span>
          </p>
        </div>

        <!-- Footer -->
        <footer class="mt-8 text-gray-400 text-xs text-center">
          © {{ new Date().getFullYear() }} FTI-Service<br />
          Fakultas Teknologi Informasi UKSW
        </footer>
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

      <!-- Complete Profile Step - Dosen -->
      <div
        v-else-if="
          step === 'complete-profile' &&
          profileData &&
          profileData.role === 'dosen'
        "
        class="space-y-6 max-h-[80vh] overflow-y-auto"
      >
        <div class="text-center sticky top-0 bg-white pb-4 z-10">
          <div
            class="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4"
          >
            <img
              :src="profileData.picture"
              :alt="profileData.nama"
              class="w-20 h-20 rounded-full"
            />
          </div>
          <h2 class="text-2xl font-bold text-gray-900 mb-1">
            Lengkapi Profil Dosen
          </h2>
          <p class="text-gray-600 text-sm">{{ profileData.nama }}</p>
          <p class="text-gray-500 text-xs">{{ profileData.email }}</p>
          <span
            class="inline-block px-3 py-1 text-xs font-semibold text-green-700 bg-green-100 rounded-full mt-2"
          >
            Dosen
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

        <!-- Form Dosen -->
        <form @submit.prevent="handleCompleteProfileDosen" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              NIP/NIDN <span class="text-red-500">*</span>
            </label>
            <input
              v-model="formDataDosen.nomor_induk"
              type="text"
              placeholder="1234567890"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
              required
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Nomor HP <span class="text-red-500">*</span>
            </label>
            <input
              v-model="formDataDosen.no_hp"
              type="tel"
              placeholder="081234567890"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
              required
            />
          </div>

          <div class="grid grid-cols-2 gap-3">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                Gelar Depan
              </label>
              <input
                v-model="formDataDosen.gelar_depan"
                type="text"
                placeholder="Dr."
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                Gelar Belakang
              </label>
              <input
                v-model="formDataDosen.gelar_belakang"
                type="text"
                placeholder="M.Kom"
                class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
              />
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Jabatan
            </label>
            <input
              v-model="formDataDosen.jabatan"
              type="text"
              placeholder="Lektor"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Fakultas <span class="text-red-500">*</span>
            </label>
            <select
              v-model="formDataDosen.fakultas_id"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
              required
            >
              <option value="" disabled>Pilih Fakultas</option>
              <option :value="1">Fakultas Teknologi Informasi</option>
              <!-- Add more fakultas as needed -->
            </select>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Tanda Tangan <span class="text-gray-500 text-xs">(Optional)</span>
            </label>

            <!-- ✅ USE SignatureCreator Component -->
            <SignatureCreator
              @update:finalImage="signatureFinalBlob = $event"
            />
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full bg-green-600 hover:bg-green-700 text-white font-medium py-3 rounded-lg transition duration-200 flex items-center justify-center gap-2 disabled:bg-gray-400 disabled:cursor-not-allowed"
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
import { useAuthStore } from "@/stores/auth";
import SignatureCreator from "@/components/dosen/SignatureCreator.vue";
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
const authStore = useAuthStore();

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
const formDataDosen = ref({
  nomor_induk: "",
  no_hp: "",
  gelar_depan: "",
  gelar_belakang: "",
  jabatan: "",
  fakultas_id: 1,
});
// const signatureFile = ref<File | null>(null);
// const signaturePreview = ref<string>("");
// const signatureFileName = ref<string>("");
// const isDragging = ref(false);
// const fileInput = ref<HTMLInputElement | null>(null);

const signatureFinalBlob = ref<Blob | null>(null);

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
    console.log(res.status, "status code");

    // === CASE 1: Need to complete profile (206 or 207) ===
    if (res.status === 206 || res.status === 207) {
      profileData.value = {
        ...data.data,
        token: response.credential,
      };
      step.value = "complete-profile";
    }
    // === CASE 2: Login success ===
    else if (res.status === 200 && data.success) {
      // Simpan token dan user
      localStorage.setItem("access_token", data.data.access_token);
      localStorage.setItem("refresh_token", data.data.refresh_token);
      localStorage.setItem("user", JSON.stringify(data.data.user));

      // Simpan ke Pinia store
      authStore.setAccessToken(data.data.access_token);
      authStore.setRefreshToken(data.data.refresh_token);
      authStore.setUser(data.data.user);

      // jika dosen
      if (data.data.user.role === "dosen" && data.data.dosen) {
        authStore.setDosen(data.data.dosen);
      }
      // else if(data.data.user.role === "mahasiswa" && data.data.mahasiswa){
      //   authStore.setMahasiswa(data.data.mahasiswa);
      // }
      step.value = "success";

      // Redirect berdasarkan role
      const role = data.data.user.role;
      const routes: Record<string, string> = {
        admin: "/admin/dashboard",
        dosen: "/dosen/dashboard",
        mahasiswa: "/mahasiswa/dashboard",
      };

      setTimeout(() => {
        router.push(routes[role] || "/dashboard");
      }, 1500);
    }
    // === CASE 3: Error ===
    else {
      error.value = data.message || "Login gagal";
    }
  } catch (err: any) {
    // Handle axios error for status 206/207
    if (
      err.response &&
      (err.response.status === 206 || err.response.status === 207)
    ) {
      const data = err.response.data;
      profileData.value = {
        ...data.data,
        token: response.credential,
      };
      step.value = "complete-profile";
    } else {
      error.value =
        err.response?.data?.message || "Terjadi kesalahan. Silakan coba lagi.";
    }
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
      localStorage.setItem("access_token", data.data.access_token);
      localStorage.setItem("refresh_token", data.data.refresh_token);
      localStorage.setItem("user", JSON.stringify(data.data.user));

      authStore.setAccessToken(data.data.access_token);
      authStore.setRefreshToken(data.data.refresh_token);
      authStore.setUser(data.data.user);
      step.value = "success";

      setTimeout(() => {
        router.push("/mahasiswa/dashboard");
      }, 1500);
    } else {
      error.value = data.message || "Gagal menyimpan profil.";
    }
  } catch (err: any) {
    error.value =
      err.response?.data?.message || "Terjadi kesalahan saat menyimpan profil.";
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
      localStorage.setItem("access_token", data.data.access_token);
      localStorage.setItem("refresh_token", data.data.refresh_token);
      localStorage.setItem("user", JSON.stringify(data.data.user));

      authStore.setAccessToken(data.data.access_token);
      authStore.setRefreshToken(data.data.refresh_token);
      authStore.setUser(data.data.user);

      step.value = "success";
      setTimeout(() => {
        router.push("/admin/dashboard");
      }, 1500);
    } else {
      error.value = data.message || "Gagal menyimpan profil admin.";
    }
  } catch (err: any) {
    error.value =
      err.response?.data?.message ||
      "Terjadi kesalahan saat menyimpan profil admin.";
    console.error(err);
  } finally {
    loading.value = false;
  }
};

const handleCompleteProfileDosen = async () => {
  loading.value = true;
  error.value = "";

  try {
    const formDataToSend = new FormData();
    formDataToSend.append("token", profileData.value?.token || "");
    formDataToSend.append("nomor_induk", formDataDosen.value.nomor_induk);
    formDataToSend.append("no_hp", formDataDosen.value.no_hp);
    formDataToSend.append("gelar_depan", formDataDosen.value.gelar_depan || "");
    formDataToSend.append(
      "gelar_belakang",
      formDataDosen.value.gelar_belakang || ""
    );
    formDataToSend.append("jabatan", formDataDosen.value.jabatan || "");
    formDataToSend.append(
      "fakultas_id",
      formDataDosen.value.fakultas_id.toString()
    );

    // ✅ UPDATED: Kirim final blob dari editor
    if (signatureFinalBlob.value) {
      // Convert Blob to File
      const signatureFileToSend = new File(
        [signatureFinalBlob.value],
        `signature_${Date.now()}.png`,
        { type: "image/png" }
      );
      formDataToSend.append("signature", signatureFileToSend);
    }

    const res = await apiClient.post(
      `/auth/google/complete-profile/dosen`,
      formDataToSend,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );

    const data = res.data;

    if (data.success) {
      localStorage.setItem("access_token", data.data.access_token);
      localStorage.setItem("refresh_token", data.data.refresh_token);
      localStorage.setItem("user", JSON.stringify(data.data.user));

      authStore.setAccessToken(data.data.access_token);
      authStore.setRefreshToken(data.data.refresh_token);
      authStore.setUser(data.data.user);
      authStore.setDosen(data.data.dosen);

      step.value = "success";
      setTimeout(() => {
        router.push("/dosen/dashboard");
      }, 1500);
    } else {
      error.value = data.message || "Gagal menyimpan profil dosen.";
    }
  } catch (err: any) {
    error.value =
      err.response?.data?.message ||
      "Terjadi kesalahan saat menyimpan profil dosen.";
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>

<style>
.element {
  background: linear-gradient(to right, #cffafe, #d8b4fe, #0ea5e9);
}
</style>
