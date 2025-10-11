<template>
  <div
    class="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-50 via-white to-blue-100 p-4"
  >
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-5">
      <div
        class="absolute top-20 left-20 w-72 h-72 bg-blue-300 rounded-full mix-blend-multiply filter blur-xl animate-pulse"
      ></div>
      <div
        class="absolute bottom-20 right-20 w-72 h-72 bg-blue-400 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-1000"
      ></div>
    </div>

    <Card
      class="w-[420px] shadow-2xl shadow-blue-100 border-0 bg-white/80 backdrop-blur-sm relative overflow-hidden"
    >
      <!-- Card decoration -->
      <div
        class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700"
      ></div>

      <CardHeader class="text-center pb-2 pt-8">
        <!-- Logo/Icon -->
        <div
          class="mx-auto mb-4 w-16 h-16 bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl flex items-center justify-center shadow-lg shadow-blue-200"
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
              d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"
            ></path>
          </svg>
        </div>

        <CardTitle class="text-2xl font-bold text-gray-800 mb-2"
          >Selamat Datang</CardTitle
        >
        <CardDescription class="text-gray-600">
          Masuk ke akun FTI UKSW Anda untuk melanjutkan
        </CardDescription>
      </CardHeader>

      <CardContent class="px-8 pb-8">
        <form @submit.prevent="handleLogin" class="space-y-6">
          <!-- Nomor Induk Field -->
          <div class="space-y-2">
            <Label
              for="nomorInduk"
              class="text-sm font-semibold text-gray-700 flex items-center gap-2"
            >
              <svg
                class="w-4 h-4 text-blue-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2"
                ></path>
              </svg>
              Nomor Induk
            </Label>
            <Input
              id="nomorInduk"
              v-model="nomorInduk"
              placeholder="Masukkan nomor induk Anda"
              class="h-12 rounded-xl border-2 border-gray-200 focus:border-blue-400 focus:ring-blue-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
            />
          </div>

          <!-- Password Field -->
          <div class="space-y-2">
            <Label
              for="password"
              class="text-sm font-semibold text-gray-700 flex items-center gap-2"
            >
              <svg
                class="w-4 h-4 text-blue-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"
                ></path>
              </svg>
              Password
            </Label>
            <div class="relative">
              <Input
                id="password"
                :type="showPassword ? 'text' : 'password'"
                v-model="password"
                placeholder="Masukkan password Anda"
                class="h-12 rounded-xl border-2 border-gray-200 focus:border-blue-400 focus:ring-blue-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400 pr-12"
              />
              <!-- Eye Icon Button -->
              <button
                type="button"
                @click="togglePasswordVisibility"
                class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-blue-600 transition-colors duration-200 focus:outline-none focus:text-blue-600"
              >
                <svg
                  v-if="!showPassword"
                  class="w-5 h-5"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                  ></path>
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                  ></path>
                </svg>
                <svg
                  v-else
                  class="w-5 h-5"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.878 9.878L3 3m6.878 6.878L21 21"
                  ></path>
                </svg>
              </button>
            </div>
          </div>

          <!-- Login Button -->
          <Button
            type="submit"
            class="w-full h-12 bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white font-semibold rounded-xl shadow-lg shadow-blue-200 border-0 transition-all duration-300 hover:scale-[1.02] hover:shadow-xl hover:shadow-blue-300"
            :disabled="!nomorInduk || !password"
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
                  d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
                ></path>
              </svg>
              Masuk ke Akun
            </span>
          </Button>
        </form>

        <!-- Error Alert -->
        <Alert
          v-if="errorMessage"
          variant="destructive"
          class="mt-6 border-red-200 bg-red-50 rounded-xl"
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
          {{ errorMessage }}
        </Alert>

        <!-- Register Link -->
        <div class="mt-8 pt-6 border-t border-gray-100">
          <p class="text-sm text-center text-gray-600">
            Belum memiliki akun?
            <RouterLink
              to="/register"
              class="text-blue-600 hover:text-blue-700 font-semibold hover:underline transition-colors duration-200 ml-1"
            >
              Daftar sekarang
            </RouterLink>
          </p>
        </div>

        <!-- Footer Info -->
        <div class="mt-6 text-center">
          <p class="text-xs text-gray-500">
            Sistem Informasi Fakultas Teknologi Informasi
          </p>
          <p class="text-xs text-gray-400">Universitas Kristen Satya Wacana</p>
        </div>
      </CardContent>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { RouterLink, useRouter } from "vue-router";
import { login } from "@/services/login";
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
import { useAuthStore } from "@/stores/auth";

const auth = useAuthStore();
const router = useRouter();
const nomorInduk = ref("");
const password = ref("");
const errorMessage = ref("");
const showPassword = ref(false);

// Toggle password visibility
function togglePasswordVisibility() {
  showPassword.value = !showPassword.value;
}

async function handleLogin() {
  try {
    const result = await login(nomorInduk.value, password.value);

    auth.setUser(result.user);
    auth.setAccessToken(result.access_token);
    auth.setRefreshToken(result.refresh_token);

    // Set dosen-specific data jika ada
    if (result.dosen) {
      auth.setDosen(result.dosen);
    }

    // Gunakan auth.user.value untuk pengecekan role
    if (auth?.user?.role === "mahasiswa") {
      router.push("/mahasiswa/dashboard");
      return;
    } else if (auth?.user?.role === "dosen") {
      router.push("/dosen/dashboard");
      return;
    } else if (auth?.user?.role === "admin") {
      router.push("/admin/dashboard");
      return;
    }
  } catch (error: any) {
    errorMessage.value =
      error.response?.data?.message || "Login gagal, silakan coba lagi.";
  }
}
</script>
