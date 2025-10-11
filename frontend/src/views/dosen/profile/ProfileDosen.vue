<template>
  <div class="p-8 grid grid-cols-1 lg:grid-cols-3 gap-8 max-w-7xl mx-auto">
    <!-- Kartu Profil Dosen -->
    <Card
      class="border-0 shadow-lg shadow-purple-50 bg-gradient-to-br from-white to-purple-50/30 overflow-hidden"
    >
      <CardContent class="flex flex-col items-center text-center p-8">
        <!-- Profile Image -->
        <div class="relative mb-6">
          <img
            src="@/assets/default-profile.png"
            alt="Foto Profile"
            class="w-32 h-32 rounded-full object-cover shadow-lg shadow-purple-100 border-4 border-white"
          />
          <div
            class="absolute inset-0 rounded-full bg-gradient-to-t from-purple-600/10 to-transparent"
          ></div>
        </div>

        <!-- User Info -->
        <div class="space-y-2 mb-6">
          <h2 class="text-2xl font-semibold text-gray-800 tracking-tight">
            {{ user?.nama }}
          </h2>
          <p
            class="text-gray-500 font-medium text-sm bg-gray-100 px-3 py-1 rounded-full inline-block"
          >
            {{ user?.nomor_induk }}
          </p>
        </div>

        <!-- Button Edit Profile -->
        <Button
          @click="$router.push({ name: 'EditProfileDosen' })"
          class="w-full bg-gradient-to-r from-purple-400 to-purple-500 hover:from-purple-500 hover:to-purple-600 text-white shadow-lg shadow-purple-200 border-0 rounded-xl py-3 font-medium transition-all duration-300 hover:scale-[1.02] hover:shadow-xl hover:shadow-purple-300"
        >
          <span class="flex items-center justify-center space-x-2">
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
                d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
              />
            </svg>
            <span>Ubah Data Dosen</span>
          </span>
        </Button>
      </CardContent>
    </Card>

    <!-- Kartu Upload TTD -->
    <Card
      class="border-0 shadow-lg shadow-purple-50 bg-gradient-to-br from-white to-purple-50/30 overflow-hidden flex flex-col justify-center"
    >
      <CardContent class="flex flex-col items-center text-center p-8">
        <!-- Preview TTD -->

        <div v-if="dosen?.ttd_path">
          <img
            :src="`${baseUrl}/files/uploads/${dosen.ttd_path}`"
            alt="TTD"
            class="h-32 mx-auto mb-4"
          />
        </div>
        <div v-else>
          <img
            src="@/assets/no-ttd.png"
            alt="TTD Default"
            class="h-32 mx-auto mb-4"
          />
        </div>

        <p class="text-lg font-semibold text-purple-800">TTD</p>

        <!-- Upload Input -->
        <input
          type="file"
          accept="image/png"
          @change="handleTTDUpload"
          class="mt-4 file:bg-purple-50 file:text-purple-700 file:border-0 file:rounded file:px-4 file:py-2 file:mr-4 hover:file:bg-purple-100"
        />

        <!-- Link Panduan -->
        <a
          href="#"
          class="text-purple-600 font-bold text-sm mt-2 inline-block hover:text-purple-800 hover:underline"
        >
          Panduan Upload File TTD
        </a>

        <!-- Submit Button -->
        <Button
          @click="submitTTD"
          class="w-full bg-gradient-to-r from-purple-500 to-purple-600 hover:from-purple-600 hover:to-purple-700 text-white shadow-lg shadow-purple-200 border-0 rounded-xl py-3 font-medium mt-4 transition-all duration-300 hover:scale-[1.02] hover:shadow-xl hover:shadow-purple-300"
        >
          📝 Ubah TTD
        </Button>
      </CardContent>
    </Card>

    <!-- Kartu QR Code -->
    <Card
      class="border-0 shadow-lg shadow-gray-50 bg-gradient-to-br from-white to-gray-50/50 overflow-hidden"
    >
      <CardHeader class="pb-4">
        <CardTitle
          class="text-gray-800 flex items-center gap-3 text-xl font-semibold"
        >
          <div
            class="w-10 h-10 bg-gradient-to-br from-purple-400 to-purple-500 rounded-lg flex items-center justify-center shadow-sm"
          >
            <svg
              class="w-5 h-5 text-white"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 4v1m6 11h2m-6 0h-2v4m0-11v3m0 0h.01M12 12h4.01M16 16h4.01M12 8h4.01M16 4h4.01M4 4h4.01M4 8h4.01m0 0h.01M4 12h4.01m0 0h.01M4 16h4.01m0 0h.01"
              />
            </svg>
          </div>
          QR Dosen
        </CardTitle>
        <CardDescription class="text-gray-600 leading-relaxed">
          QR Code ini berisi data dosen dan informasi terkait aktivitas Anda
          untuk kemudahan akses.
        </CardDescription>
      </CardHeader>
      <CardContent class="flex flex-col items-center justify-center pt-4">
        <div class="relative">
          <div
            class="w-48 h-48 bg-white rounded-2xl border-2 border-gray-100 shadow-lg flex items-center justify-center relative overflow-hidden"
          >
            <span class="text-gray-400 font-medium z-10">QR Code</span>
          </div>
          <div
            class="absolute inset-0 rounded-2xl bg-gradient-to-t from-purple-500/5 to-transparent -z-10 blur-xl"
          ></div>
        </div>
        <p class="text-xs text-gray-500 mt-4 text-center">
          Scan untuk akses cepat informasi dosen
        </p>
      </CardContent>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import { useAuthStore } from "@/stores/auth";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { apiClient } from "@/lib/axios";

const auth = useAuthStore();
const user = computed(() => auth.user);
const dosen = computed(() => auth.dosen); // langsung dari store
const selectedFile = ref<File | null>(null);

const baseUrl = import.meta.env.VITE_API_URL;

// Handle pilih file
const handleTTDUpload = (e: Event) => {
  const target = e.target as HTMLInputElement;
  if (target.files && target.files[0]) {
    selectedFile.value = target.files[0];
  }
};

// Submit upload signature
const submitTTD = async () => {
  if (!selectedFile.value) {
    alert("Silakan pilih file TTD terlebih dahulu!");
    return;
  }

  try {
    const formData = new FormData();
    formData.append("signature", selectedFile.value);

    const res = await apiClient.post("/dosen/upload-signature", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    // Update store langsung
    auth.setDosen(res.data.data);
    selectedFile.value = null;

    alert("TTD berhasil diperbarui!");
  } catch (err) {
    console.error(err);
    alert("Terjadi kesalahan saat upload TTD");
  }
};
</script>
