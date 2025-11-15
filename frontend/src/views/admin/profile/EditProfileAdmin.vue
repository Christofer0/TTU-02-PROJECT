<template>
  <div
    class="relative flex items-center justify-center min-h-screen bg-gradient-to-br from-slate-50 via-white to-slate-100 p-4 overflow-hidden"
  >
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-10 pointer-events-none">
      <div
        class="absolute top-20 left-20 w-72 h-72 bg-blue-400 rounded-full mix-blend-multiply filter blur-xl animate-pulse"
      ></div>
      <div
        class="absolute bottom-20 right-20 w-72 h-72 bg-indigo-500 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-1000"
      ></div>
      <div
        class="absolute top-1/2 left-1/4 w-64 h-64 bg-cyan-300 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-500"
      ></div>
    </div>

    <Card
      class="w-[550px] max-w-full shadow-2xl shadow-slate-200 border-0 bg-white/85 backdrop-blur-md relative overflow-hidden z-10"
    >
      <!-- Card Decoration -->
      <div
        class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-blue-500 via-indigo-600 to-cyan-500"
      ></div>

      <CardHeader class="text-center pb-4 pt-8">
        <div
          class="mx-auto mb-4 w-16 h-16 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center shadow-lg shadow-blue-200"
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
              d="M11 5H6a2 2 0 00-2 2v11a2 2 
              0 002 2h11a2 2 0 002-2v-5m-1.414-9.414
              a2 2 0 112.828 2.828L11.828 15H9v-2.828
              l8.586-8.586z"
            />
          </svg>
        </div>

        <CardTitle class="text-2xl font-bold text-gray-800 mb-2">
          Edit Profil Admin
        </CardTitle>
        <CardDescription class="text-gray-600">
          Perbarui informasi akun admin Anda untuk memastikan sistem tetap aman
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
                class="w-4 h-4 text-blue-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14
                  a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                />
              </svg>
              Nama Lengkap <span class="text-red-500">*</span>
            </Label>
            <Input
              id="nama"
              v-model="form.nama"
              type="text"
              placeholder="Masukkan nama lengkap admin"
              required
              class="h-12 rounded-xl border-2 border-gray-200 focus:border-blue-500 focus:ring-blue-100 bg-white/80 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
            />
          </div>

          <!-- Email -->
          <div class="space-y-2">
            <Label
              for="email"
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
                  d="M16 12a4 4 0 10-8 0 4 4 0 
                  008 0zm0 0v1.5a2.5 2.5 0 005 
                  0V12a9 9 0 10-9 9m4.5-1.206
                  a8.959 8.959 0 01-4.5 1.207"
                />
              </svg>
              Email <span class="text-red-500">*</span>
            </Label>
            <Input
              id="email"
              v-model="form.email"
              type="email"
              placeholder="Masukkan email admin"
              required
              disabled
              class="h-12 rounded-xl border-2 border-gray-200 focus:border-blue-500 focus:ring-blue-100 bg-white/80 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
            />
          </div>

          <!-- Nomor HP -->
          <div class="space-y-2">
            <Label
              for="no_hp"
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
                  d="M3 5a2 2 0 012-2h3.28a1 1 
                  0 01.948.684l1.498 4.493a1 1 
                  0 01-.502 1.21l-2.257 1.13
                  a11.042 11.042 0 005.516 5.516
                  l1.13-2.257a1 1 0 011.21-.502
                  l4.493 1.498a1 1 0 01.684.949V19
                  a2 2 0 01-2 2h-1C9.716 21 
                  3 14.284 3 6V5z"
                />
              </svg>
              Nomor HP
            </Label>
            <Input
              id="no_hp"
              v-model="form.no_hp"
              type="text"
              placeholder="Masukkan nomor HP admin"
              class="h-12 rounded-xl border-2 border-gray-200 focus:border-blue-500 focus:ring-blue-100 bg-white/80 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
            />
          </div>

          <!-- Tombol -->
          <div class="flex flex-col sm:flex-row gap-3 pt-4">
            <Button
              type="submit"
              class="flex-1 h-12 bg-gradient-to-r from-blue-500 to-indigo-600 hover:from-indigo-600 hover:to-cyan-600 text-white font-semibold rounded-xl shadow-lg shadow-blue-200 border-0 transition-all duration-300 hover:scale-[1.02] hover:shadow-xl hover:shadow-blue-300"
            >
              Simpan Perubahan
            </Button>

            <Button
              type="button"
              @click="resetForm"
              variant="outline"
              class="flex-1 h-12 border-2 border-gray-200 hover:border-gray-300 text-gray-700 font-medium rounded-xl bg-white/70 backdrop-blur-sm transition-all duration-200 hover:bg-gray-50"
            >
              Reset
            </Button>
          </div>
        </form>

        <!-- Informasi -->
        <div
          class="mt-8 p-4 bg-blue-50 rounded-xl border border-blue-100 text-blue-800"
        >
          <h4 class="text-sm font-semibold mb-2 flex items-center gap-2">
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
                d="M13 16h-1v-4h-1m1-4h.01
                M21 12a9 9 0 11-18 0 9 9 
                0 0118 0z"
              />
            </svg>
            Panduan Profil Admin
          </h4>
          <div class="text-xs space-y-1">
            <p>• Pastikan data sesuai dengan identitas resmi</p>
            <p>• Email digunakan untuk akses sistem dan notifikasi</p>
            <p>• Nomor HP akan digunakan untuk verifikasi keamanan</p>
          </div>
        </div>
      </CardContent>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
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
import Swal from "sweetalert2";

const authStore = useAuthStore();

interface AdminProfileForm {
  nama: string;
  email: string;
  no_hp: string;
}

const form = ref<AdminProfileForm>({
  nama: "",
  email: "",
  no_hp: "",
});

const originalForm = ref<AdminProfileForm>({
  nama: "",
  email: "",
  no_hp: "",
});

const loading = ref(false);

onMounted(() => {
  const profile = authStore.user as User | null;
  if (profile) {
    const profileData: AdminProfileForm = {
      nama: profile.nama,
      email: profile.email,
      no_hp: profile.no_hp ?? "",
    };
    form.value = { ...profileData };
    originalForm.value = { ...profileData };
  }
});

const resetForm = () => {
  form.value = { ...originalForm.value };
};

const handleSubmit = async () => {
  try {
    loading.value = true;

    // kirim ke backend
    const response = await updateProfile(form.value);

    if (response.success) {
      // ✅ perbarui data di auth store (tanpa ubah definisi store)
      const updatedUser = {
        ...authStore.user,
        ...response.data,
      };
      authStore.setUser(updatedUser);

      // perbarui form original agar "reset" pakai data terbaru
      form.value = {
        nama: response.data.nama,
        email: response.data.email,
        no_hp: response.data.no_hp ?? "",
      };
      originalForm.value = { ...form.value };
      await Swal.fire({
        title: "Berhasil",
        text: "Profil berhasil diperbaharui",
        icon: "success",
      });
    } else {
      await Swal.fire({
        title: "Gagal",
        text: "Gagal memperbaharui profil",
        icon: "error",
      });
    }
  } catch (error) {
    console.error(error);
    await Swal.fire({
      title: "Gagal",
      text: "Terjadi kesalahan saat memperbarui profil",
      icon: "error",
    });
  } finally {
    loading.value = false;
  }
};
</script>
