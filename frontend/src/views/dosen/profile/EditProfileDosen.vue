<template>
  <div
    class="flex items-center justify-center min-h-screen bg-gradient-to-br from-purple-50 via-white to-purple-100 p-4"
  >
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-5">
      <div
        class="absolute top-20 left-20 w-72 h-72 bg-purple-300 rounded-full mix-blend-multiply filter blur-xl animate-pulse"
      ></div>
      <div
        class="absolute bottom-20 right-20 w-72 h-72 bg-purple-400 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-1000"
      ></div>
      <div
        class="absolute top-1/2 left-1/4 w-64 h-64 bg-purple-200 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-500"
      ></div>
    </div>

    <Card
      class="w-[550px] max-w-full shadow-2xl shadow-purple-100 border-0 bg-white/80 backdrop-blur-sm relative overflow-hidden"
    >
      <!-- Card decoration -->
      <div
        class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-purple-400 via-purple-500 to-purple-600"
      ></div>

      <CardHeader class="text-center pb-4 pt-8">
        <!-- Profile Edit Icon -->
        <div
          class="mx-auto mb-4 w-16 h-16 bg-gradient-to-br from-purple-400 to-purple-500 rounded-2xl flex items-center justify-center shadow-lg shadow-purple-200"
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
            />
          </svg>
        </div>

        <CardTitle class="text-2xl font-bold text-gray-800 mb-2">
          Edit Profil Dosen
        </CardTitle>
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
                class="w-4 h-4 text-purple-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                />
              </svg>
              Nama Lengkap <span class="text-red-500">*</span>
            </Label>
            <Input
              id="nama"
              v-model="form.nama"
              type="text"
              placeholder="Masukkan nama lengkap"
              required
              class="h-12 rounded-xl border-2 border-gray-200 focus:border-purple-400 focus:ring-purple-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
              :class="{
                'border-red-300 focus:border-red-400 focus:ring-red-100':
                  fieldErrors.nama,
              }"
            />
            <p
              v-if="fieldErrors.nama"
              class="text-red-500 text-xs flex items-center gap-1"
            >
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
                class="w-4 h-4 text-purple-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M16 12a4 4 0 10-8 0 4 4 0 008 0zM16 12v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9"
                />
              </svg>
              Email <span class="text-red-500">*</span>
            </Label>
            <Input
              id="email"
              v-model="form.email"
              type="email"
              placeholder="Masukkan email aktif"
              required
              class="h-12 rounded-xl border-2 border-gray-200 focus:border-purple-400 focus:ring-purple-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
              :class="{
                'border-red-300 focus:border-red-400 focus:ring-red-100':
                  fieldErrors.email,
              }"
            />
            <p
              v-if="fieldErrors.email"
              class="text-red-500 text-xs flex items-center gap-1"
            >
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
                class="w-4 h-4 text-purple-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M3 5a2 2 0 012-2h3.28l1.498 4.493-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257 4.493 1.498V19a2 2 0 01-2 2h-1C9.7 21 3 14.3 3 6V5z"
                />
              </svg>
              Nomor HP
            </Label>
            <Input
              id="no_hp"
              v-model="form.no_hp"
              type="text"
              placeholder="Masukkan nomor HP (opsional)"
              class="h-12 rounded-xl border-2 border-gray-200 focus:border-purple-400 focus:ring-purple-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
            />
          </div>

          <!-- Alert success / error -->
          <div class="pt-2 space-y-1">
            <p
              v-if="success"
              class="text-green-600 text-sm flex items-center gap-1"
            >
              ✅ {{ success }}
            </p>
            <p
              v-if="error"
              class="text-red-600 text-sm flex items-center gap-1"
            >
              ⚠️ {{ error }}
            </p>
          </div>

          <!-- Buttons -->
          <div class="flex flex-col sm:flex-row gap-3 pt-4">
            <Button
              type="submit"
              :disabled="loading || !isFormValid"
              class="flex-1 h-12 bg-gradient-to-r from-purple-400 to-purple-500 hover:from-purple-500 hover:to-purple-600 text-white font-semibold rounded-xl shadow-lg shadow-purple-200 border-0 transition-all duration-300"
            >
              Simpan Perubahan
            </Button>
            <Button
              type="button"
              @click="resetForm"
              variant="outline"
              class="flex-1 h-12 border-2 border-gray-200 text-gray-700 rounded-xl bg-white/70 hover:bg-gray-50"
            >
              Reset
            </Button>
          </div>
        </form>
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

const authStore = useAuthStore();

interface DosenProfileForm {
  nama?: string;
  email?: string;
  no_hp?: string;
}

const form = ref<DosenProfileForm>({
  nama: "",
  email: "",
  no_hp: "",
});
const originalForm = ref<DosenProfileForm>({});
const loading = ref(false);
const error = ref("");
const success = ref("");
const fieldErrors = ref<{ [key: string]: string }>({});

const isFormValid = computed(() => {
  return (
    !!form.value.nama &&
    !!form.value.email &&
    Object.keys(fieldErrors.value).length === 0
  );
});

const hasChanges = computed(
  () => JSON.stringify(form.value) !== JSON.stringify(originalForm.value)
);

watch(
  () => form.value,
  () => {
    error.value = "";
    success.value = "";
    fieldErrors.value = {};
  },
  { deep: true }
);

function validateForm() {
  const errors: { [key: string]: string } = {};
  if (!form.value.nama?.trim()) errors.nama = "Nama wajib diisi";
  if (!form.value.email?.trim()) {
    errors.email = "Email wajib diisi";
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.value.email)) {
    errors.email = "Format email tidak valid";
  }
  if (form.value.no_hp && !/^[0-9+\-\s()]+$/.test(form.value.no_hp)) {
    errors.no_hp = "Format nomor HP tidak valid";
  }
  return errors;
}

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

const resetForm = () => {
  form.value = { ...originalForm.value };
};

onMounted(loadProfile);

const handleSubmit = async () => {
  loading.value = true;
  error.value = "";
  success.value = "";
  fieldErrors.value = {};

  try {
    const validationErrors = validateForm();
    if (Object.keys(validationErrors).length > 0) {
      fieldErrors.value = validationErrors;
      error.value = "Mohon periksa kembali form Anda.";
      return;
    }
    if (!hasChanges.value) {
      error.value = "Tidak ada perubahan untuk disimpan.";
      return;
    }

    const cleanForm = {
      nama: form.value.nama?.trim(),
      email: form.value.email?.trim().toLowerCase(),
      no_hp: form.value.no_hp?.trim() || null,
    };

    const res = await updateProfile(cleanForm);
    if (res.success) {
      success.value = "Profil dosen berhasil diperbarui!";
      authStore.setUser(res.data as User);
      originalForm.value = { ...form.value };
    } else {
      error.value = res.msg || "Gagal memperbarui profil dosen";
    }
  } catch (err: any) {
    error.value =
      err?.message || "Terjadi kesalahan saat memperbarui profil dosen.";
  } finally {
    loading.value = false;
  }
};
</script>
