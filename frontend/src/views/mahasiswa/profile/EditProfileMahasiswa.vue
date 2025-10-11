<template>
  <div
    class="flex items-center justify-center min-h-screen bg-gradient-to-br from-emerald-50 via-white to-emerald-100 p-4"
  >
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-5">
      <div
        class="absolute top-20 left-20 w-72 h-72 bg-emerald-300 rounded-full mix-blend-multiply filter blur-xl animate-pulse"
      ></div>
      <div
        class="absolute bottom-20 right-20 w-72 h-72 bg-emerald-400 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-1000"
      ></div>
      <div
        class="absolute top-1/2 left-1/4 w-64 h-64 bg-emerald-200 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-500"
      ></div>
    </div>

    <Card
      class="w-[550px] max-w-full shadow-2xl shadow-emerald-100 border-0 bg-white/80 backdrop-blur-sm relative overflow-hidden"
    >
      <!-- Card decoration -->
      <div
        class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-emerald-400 via-emerald-500 to-emerald-600"
      ></div>

      <CardHeader class="text-center pb-4 pt-8">
        <!-- Profile Edit Icon -->
        <div
          class="mx-auto mb-4 w-16 h-16 bg-gradient-to-br from-emerald-400 to-emerald-500 rounded-2xl flex items-center justify-center shadow-lg shadow-emerald-200"
        >
          <svg
            class="w-8 h-8 text-white"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
            ></path>
          </svg>
        </div>

        <CardTitle class="text-2xl font-bold text-gray-800 mb-2"
          >Edit Profil Mahasiswa</CardTitle
        >
        <CardDescription class="text-gray-600">
          Perbarui informasi profil Anda untuk menjaga data tetap terkini
        </CardDescription>
      </CardHeader>

      <CardContent class="px-8 pb-8">
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <!-- Nama Lengkap -->
          <div class="space-y-2">
            <Label
              for="nama"
              class="text-sm font-semibold text-gray-700 flex items-center gap-2"
            >
              <svg
                class="w-4 h-4 text-emerald-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                ></path>
              </svg>
              Nama Lengkap <span class="text-red-500">*</span>
            </Label>
            <Input
              id="nama"
              v-model="form.nama"
              type="text"
              placeholder="Masukkan nama lengkap Anda"
              required
              disabled="true"
              class="h-12 rounded-xl border-2 border-gray-200 focus:border-emerald-400 focus:ring-emerald-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
              :class="{
                'border-red-300 focus:border-red-400 focus:ring-red-100':
                  fieldErrors.nama,
              }"
            />
            <p
              v-if="fieldErrors.nama"
              class="text-red-500 text-xs flex items-center gap-1"
            >
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              {{ fieldErrors.nama }}
            </p>
          </div>

          <!-- Email -->
          <div class="space-y-2">
            <Label
              for="email"
              class="text-sm font-semibold text-gray-700 flex items-center gap-2"
            >
              <svg
                class="w-4 h-4 text-emerald-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"
                ></path>
              </svg>
              Email <span class="text-red-500">*</span>
            </Label>
            <Input
              id="email"
              v-model="form.email"
              type="email"
              placeholder="Masukkan email aktif Anda"
              required
              disabled="true"
              class="h-12 rounded-xl border-2 border-gray-200 focus:border-emerald-400 focus:ring-emerald-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
              :class="{
                'border-red-300 focus:border-red-400 focus:ring-red-100':
                  fieldErrors.email,
              }"
            />
            <p
              v-if="fieldErrors.email"
              class="text-red-500 text-xs flex items-center gap-1"
            >
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              {{ fieldErrors.email }}
            </p>
          </div>

          <!-- Nomor HP -->
          <div class="space-y-2">
            <Label
              for="no_hp"
              class="text-sm font-semibold text-gray-700 flex items-center gap-2"
            >
              <svg
                class="w-4 h-4 text-emerald-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"
                ></path>
              </svg>
              Nomor HP
            </Label>
            <Input
              id="no_hp"
              v-model="form.no_hp"
              type="text"
              placeholder="Masukkan nomor HP (opsional)"
              class="h-12 rounded-xl border-2 border-gray-200 focus:border-emerald-400 focus:ring-emerald-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
              :class="{
                'border-red-300 focus:border-red-400 focus:ring-red-100':
                  fieldErrors.no_hp,
              }"
            />
            <p
              v-if="fieldErrors.no_hp"
              class="text-red-500 text-xs flex items-center gap-1"
            >
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              {{ fieldErrors.no_hp }}
            </p>
          </div>

          <!-- Action Buttons -->
          <div class="flex flex-col sm:flex-row gap-3 pt-4">
            <Button
              type="submit"
              :disabled="loading || !isFormValid"
              class="flex-1 h-12 bg-gradient-to-r from-emerald-400 to-emerald-500 hover:from-emerald-500 hover:to-emerald-600 text-white font-semibold rounded-xl shadow-lg shadow-emerald-200 border-0 transition-all duration-300 hover:scale-[1.02] hover:shadow-xl hover:shadow-emerald-300 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100"
            >
              <span
                v-if="!loading"
                class="flex items-center justify-center gap-2"
              >
                <svg
                  class="w-5 h-5"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M5 13l4 4L19 7"
                  ></path>
                </svg>
                Simpan Perubahan
              </span>
              <span v-else class="flex items-center justify-center gap-2">
                <svg
                  class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
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
                Menyimpan...
              </span>
            </Button>

            <Button
              type="button"
              @click="resetForm"
              variant="outline"
              class="flex-1 h-12 border-2 border-gray-200 hover:border-gray-300 text-gray-700 font-medium rounded-xl bg-white/70 backdrop-blur-sm transition-all duration-200 hover:bg-gray-50"
            >
              <span class="flex items-center justify-center gap-2">
                <svg
                  class="w-5 h-5"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
                  ></path>
                </svg>
                Reset
              </span>
            </Button>
          </div>
        </form>

        <!-- Messages -->
        <div class="space-y-4 mt-6">
          <Alert
            v-if="error"
            variant="destructive"
            class="border-red-200 bg-red-50 rounded-xl"
          >
            <svg
              class="w-4 h-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.34 16.5c-.77.833.192 2.5 1.732 2.5z"
              ></path>
            </svg>
            {{ error }}
          </Alert>

          <Alert
            v-if="success"
            class="border-emerald-200 bg-emerald-50 text-emerald-800 rounded-xl"
          >
            <svg
              class="w-4 h-4 text-emerald-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
              ></path>
            </svg>
            {{ success }}
          </Alert>
        </div>

        <!-- Profile Info Card -->
        <div
          class="mt-8 p-4 bg-emerald-50 rounded-xl border border-emerald-100"
        >
          <h4
            class="text-sm font-semibold text-emerald-800 mb-2 flex items-center gap-2"
          >
            <svg
              class="w-4 h-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              ></path>
            </svg>
            Informasi Profil
          </h4>
          <div class="text-xs text-emerald-700 space-y-1">
            <p>• Pastikan informasi yang Anda masukkan akurat dan terkini</p>
            <p>• Email akan digunakan untuk notifikasi sistem</p>
            <p>• Nomor HP dapat digunakan untuk verifikasi tambahan</p>
          </div>
        </div>

        <!-- Changed Fields Indicator -->
        <div
          v-if="hasChanges"
          class="mt-4 p-3 bg-amber-50 rounded-lg border border-amber-200"
        >
          <p class="text-sm text-amber-800 flex items-center gap-2">
            <svg
              class="w-4 h-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.34 16.5c-.77.833.192 2.5 1.732 2.5z"
              ></path>
            </svg>
            Anda memiliki perubahan yang belum disimpan
          </p>
        </div>
      </CardContent>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from "vue";
import { useAuthStore } from "@/stores/auth";
import { updateProfile } from "@/services/updateProfile";
import type { User } from "@/types/models/user.type";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Alert } from "@/components/ui/alert";

const authStore = useAuthStore();

// Form type khusus mahasiswa
interface MahasiswaProfileForm {
  nama?: string;
  email?: string;
  no_hp?: string;
}

// State form
const form = ref<MahasiswaProfileForm>({
  nama: "",
  email: "",
  no_hp: undefined,
});

// Original form data untuk comparison
const originalForm = ref<MahasiswaProfileForm>({});

// Loading and message states
const loading = ref(false);
const error = ref("");
const success = ref("");
const fieldErrors = ref<{ [key: string]: string }>({});

// Computed properties
const isFormValid = computed(() => {
  const hasRequiredFields = form.value.nama && form.value.email;
  const hasNoErrors = Object.keys(fieldErrors.value).length === 0;
  return hasRequiredFields && hasNoErrors;
});

const hasChanges = computed(() => {
  return JSON.stringify(form.value) !== JSON.stringify(originalForm.value);
});

// Clear messages when form changes
watch(
  () => form.value,
  () => {
    error.value = "";
    success.value = "";
    fieldErrors.value = {};
  },
  { deep: true }
);

// Enhanced form validation
function validateForm() {
  const errors: { [key: string]: string } = {};

  if (!form.value.nama?.trim()) {
    errors.nama = "Nama lengkap wajib diisi";
  }

  if (!form.value.email?.trim()) {
    errors.email = "Email wajib diisi";
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.value.email)) {
    errors.email = "Format email tidak valid";
  }

  // Optional phone number validation
  if (form.value.no_hp && !/^[0-9+\-\s()]+$/.test(form.value.no_hp)) {
    errors.no_hp = "Format nomor HP tidak valid";
  }

  return errors;
}

// Fungsi load profile & data dropdown
const loadProfile = async () => {
  const profile = authStore.user;
  if (profile) {
    const profileData = {
      nama: profile.nama,
      email: profile.email,
      no_hp: profile.no_hp ?? "",
    };
    form.value = { ...profileData };
    originalForm.value = { ...profileData };
  }
};

// Reset form to original values
const resetForm = () => {
  form.value = { ...originalForm.value };
  fieldErrors.value = {};
  error.value = "";
  success.value = "";
};

// Mounted
onMounted(loadProfile);

// Enhanced submit handler
const handleSubmit = async () => {
  // Reset states
  loading.value = true;
  error.value = "";
  success.value = "";
  fieldErrors.value = {};

  try {
    // Frontend validation
    const validationErrors = validateForm();
    if (Object.keys(validationErrors).length > 0) {
      fieldErrors.value = validationErrors;
      error.value = "Mohon periksa kembali form Anda.";
      return;
    }

    // Check if there are actually changes
    if (!hasChanges.value) {
      error.value = "Tidak ada perubahan untuk disimpan.";
      return;
    }

    // Prepare clean form data
    const cleanForm = {
      nama: form.value.nama?.trim(),
      email: form.value.email?.trim().toLowerCase(),
      no_hp: form.value.no_hp?.trim() || null,
    };

    const res = await updateProfile(cleanForm);

    if (res.success) {
      success.value = "Profil berhasil diperbarui!";
      console.log("Profile updated:", res.data);

      // Update auth store with new data
      authStore.setUser(res.data as User);

      // Update original form data
      originalForm.value = { ...form.value };

      // Auto-hide success message after 5 seconds
      setTimeout(() => {
        success.value = "";
      }, 5000);
    } else {
      error.value = res.msg || "Gagal memperbarui profil";
    }
  } catch (err: any) {
    console.error("Update profile error:", err);

    // Handle different types of errors
    if (err.response?.status === 422) {
      // Validation errors from server
      const data = err.response.data;
      if (data?.errors) {
        fieldErrors.value = data.errors;
        error.value = "Terdapat kesalahan pada form.";
      } else {
        error.value = data?.message || "Data yang Anda masukkan tidak valid.";
      }
    } else if (err.response?.status === 401) {
      // Unauthorized
      error.value = "Sesi Anda telah berakhir. Silakan login ulang.";
    } else if (err.response?.status === 409) {
      // Conflict (duplicate data)
      error.value = "Email sudah digunakan oleh akun lain.";
    } else if (err.response?.status === 500) {
      // Server error
      error.value = "Terjadi kesalahan pada server. Silakan coba lagi nanti.";
    } else if (err.code === "NETWORK_ERROR" || !err.response) {
      // Network error
      error.value =
        "Tidak dapat terhubung ke server. Periksa koneksi internet Anda.";
    } else {
      // Generic error
      error.value =
        err?.message ||
        err.response?.data?.message ||
        "Terjadi kesalahan saat memperbarui profil.";
    }
  } finally {
    loading.value = false;
  }
};
</script>
