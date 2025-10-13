<template>
  <div
    class="min-h-screen bg-gradient-to-br from-green-50 to-blue-50 flex items-center justify-center p-4"
  >
    <div class="max-w-2xl w-full">
      <!-- Loading State -->
      <div v-if="loading" class="bg-white rounded-lg shadow-xl p-8 text-center">
        <div
          class="animate-spin rounded-full h-16 w-16 border-b-2 border-green-500 mx-auto mb-4"
        ></div>
        <p class="text-gray-600">Memverifikasi dokumen...</p>
      </div>

      <!-- Valid Document -->
      <div
        v-else-if="isValid && documentData"
        class="bg-white rounded-lg shadow-xl overflow-hidden"
      >
        <!-- Header -->
        <div
          class="bg-gradient-to-r from-green-500 to-green-600 p-6 text-white"
        >
          <div class="flex items-center justify-center mb-4">
            <svg
              class="w-16 h-16"
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
          </div>
          <h1 class="text-3xl font-bold text-center">Dokumen Valid</h1>
          <p class="text-center text-green-100 mt-2">
            Dokumen ini telah diverifikasi dan ditandatangani secara resmi
          </p>
        </div>

        <!-- Content -->
        <div class="p-6 space-y-6">
          <!-- Document Info -->
          <div class="border-b pb-4">
            <h2 class="text-lg font-semibold text-gray-800 mb-3">
              Informasi Dokumen
            </h2>
            <div class="grid grid-cols-1 gap-3">
              <div>
                <label class="text-sm text-gray-500">ID Permohonan</label>
                <p class="font-medium text-gray-800">
                  {{ documentData.permohonan_id }}
                </p>
              </div>
              <div>
                <label class="text-sm text-gray-500">Jenis Permohonan</label>
                <p class="font-medium text-gray-800">
                  {{ documentData.jenis_permohonan?.nama || "-" }}
                </p>
              </div>
              <div>
                <label class="text-sm text-gray-500">Judul</label>
                <p class="font-medium text-gray-800">
                  {{ documentData.judul }}
                </p>
              </div>
              <div v-if="documentData.deskripsi">
                <label class="text-sm text-gray-500">Deskripsi</label>
                <p class="font-medium text-gray-800">
                  {{ documentData.deskripsi }}
                </p>
              </div>
            </div>
          </div>

          <!-- Student Info -->
          <div class="border-b pb-4">
            <h2 class="text-lg font-semibold text-gray-800 mb-3">
              Informasi Mahasiswa
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div>
                <label class="text-sm text-gray-500">Nama Lengkap</label>
                <p class="font-medium text-gray-800">
                  {{ documentData.mahasiswa.nama }}
                </p>
              </div>
              <div>
                <label class="text-sm text-gray-500">NIM</label>
                <p class="font-medium text-gray-800">
                  {{ documentData.mahasiswa.nomor_induk }}
                </p>
              </div>
              <div>
                <label class="text-sm text-gray-500">Program Studi</label>
                <p class="font-medium text-gray-800">
                  {{ documentData.mahasiswa.program_studi }}
                </p>
              </div>
              <div>
                <label class="text-sm text-gray-500">Fakultas</label>
                <p class="font-medium text-gray-800">
                  {{ documentData.mahasiswa.fakultas }}
                </p>
              </div>
            </div>
          </div>

          <!-- Lecturer Info -->
          <div class="border-b pb-4">
            <h2 class="text-lg font-semibold text-gray-800 mb-3">
              Ditandatangani Oleh
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div>
                <label class="text-sm text-gray-500">Nama Dosen</label>
                <p class="font-medium text-gray-800">
                  {{ documentData.dosen.nama }}
                </p>
              </div>
              <div>
                <label class="text-sm text-gray-500">Waktu Tanda Tangan</label>
                <p class="font-medium text-gray-800">
                  {{ formatDate(documentData.signed_at) }}
                </p>
              </div>
            </div>
          </div>

          <!-- Timestamp -->
          <div class="bg-gray-50 rounded-lg p-4">
            <div class="flex items-center justify-between text-sm">
              <span class="text-gray-500">Tanggal Dibuat</span>
              <span class="font-medium text-gray-800">{{
                formatDate(documentData.created_at)
              }}</span>
            </div>
          </div>
        </div>

        <!-- Footer -->
        <div class="bg-gray-50 px-6 py-4 text-center text-sm text-gray-500">
          <p>Dokumen ini terverifikasi melalui sistem TTU</p>
          <p class="mt-1">Jika ada pertanyaan, silakan hubungi pihak terkait</p>
        </div>
      </div>

      <!-- Error State -->
      <div v-else class="bg-white rounded-lg shadow-xl p-8 text-center">
        <svg
          class="w-16 h-16 text-red-500 mx-auto mb-4"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          ></path>
        </svg>
        <h2 class="text-2xl font-bold text-gray-800 mb-2">Verifikasi Gagal</h2>
        <p class="text-gray-600">{{ errorMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { apiClient } from "@/lib/axios";

const route = useRoute();
const loading = ref(true);
const isValid = ref(false);
const documentData = ref<any>(null);
const errorMessage = ref("");

const verifyDocument = async () => {
  try {
    const permohonanId = route.params.id;
    const response = await apiClient.get(`/verify/${permohonanId}`);

    if (response.data.success && response.data.data.status === "valid") {
      isValid.value = true;
      documentData.value = response.data.data;
    } else {
      isValid.value = false;
      errorMessage.value = response.data.message || "Dokumen tidak valid";
    }
  } catch (error: any) {
    isValid.value = false;
    errorMessage.value =
      error.response?.data?.message ||
      "Dokumen tidak valid atau tidak ditemukan";
    console.error("Verification error:", error);
  } finally {
    loading.value = false;
  }
};

// const formatDate = (dateString: string) => {
//   if (!dateString) return "-";
//   const date = new Date(dateString);
//   return date.toLocaleString("id-ID", {
//     year: "numeric",
//     month: "long",
//     day: "numeric",
//     hour: "2-digit",
//     minute: "2-digit",
//   });
// };

const formatDate = (dateString: string) => {
  if (!dateString) return "-";

  // 1. Tambahkan akhiran 'Z' pada string untuk secara eksplisit
  //    memberi tahu browser bahwa ini adalah waktu UTC.
  //    Contoh: "2025-10-12T06:09:18.628644" menjadi "2025-10-12T06:09:18.628644Z"
  const utcDateString = dateString.endsWith("Z")
    ? dateString
    : dateString + "Z";

  const date = new Date(utcDateString);

  // 2. Gunakan toLocaleString dengan timeZone 'Asia/Jakarta' (WIB)
  return date.toLocaleString("id-ID", {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    // KUNCI: Konversi dari UTC ke WIB saat menampilkan
    timeZone: "Asia/Jakarta",
  });
};

onMounted(() => {
  verifyDocument();
});
</script>
