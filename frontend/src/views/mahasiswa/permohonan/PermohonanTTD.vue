<template>
  <div class="min-h-screen bg-gray-50 p-6">
    <div class="max-w-4xl mx-auto">
      <Card class="shadow-sm border border-gray-200 bg-white overflow-hidden">
        <!-- Card Header -->
        <div class="bg-gray-800 px-6 py-4 border-b border-gray-700">
          <div class="flex items-center gap-3">
            <div
              class="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center"
            >
              <svg
                class="w-6 h-6 text-white"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                ></path>
              </svg>
            </div>
            <div>
              <h2 class="text-xl font-bold text-white">
                Permohonan Tanda Tangan
              </h2>
              <p class="text-sm text-gray-300">
                Ajukan permohonan tanda tangan dokumen kepada dosen pembimbing
              </p>
            </div>
          </div>
        </div>

        <CardContent class="p-6">
          <form @submit.prevent="submitForm" class="space-y-6">
            <!-- Upload File Section -->
            <div class="space-y-2">
              <Label
                for="file-upload"
                class="text-sm font-bold text-gray-700 uppercase tracking-wide"
              >
                Upload Berkas <span class="text-red-600">*</span>
              </Label>

              <!-- Custom File Upload -->
              <div class="relative">
                <input
                  id="file-upload"
                  type="file"
                  @change="handleFileChange"
                  class="hidden"
                  accept=".pdf"
                />

                <div
                  @click="triggerFileInput"
                  @dragover.prevent="isDragOver = true"
                  @dragleave.prevent="isDragOver = false"
                  @drop.prevent="handleFileDrop"
                  class="relative border-2 border-dashed rounded-lg p-6 text-center cursor-pointer transition-colors"
                  :class="{
                    'border-gray-300 bg-gray-50 hover:border-gray-400 hover:bg-gray-100':
                      !isDragOver && !fieldErrors.file,
                    'border-blue-500 bg-blue-50': isDragOver,
                    'border-red-500 bg-red-50': fieldErrors.file,
                  }"
                >
                  <div v-if="!selectedFile" class="space-y-2">
                    <div
                      class="w-12 h-12 mx-auto bg-gray-200 rounded-lg flex items-center justify-center"
                    >
                      <svg
                        class="w-6 h-6 text-gray-600"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                        ></path>
                      </svg>
                    </div>
                    <div>
                      <p class="font-semibold text-gray-900 text-sm">
                        Klik untuk upload atau drag & drop
                      </p>
                      <p class="text-xs text-gray-600 mt-1">
                        PDF, DOC, DOCX, JPG, PNG (Max 10MB)
                      </p>
                    </div>
                  </div>

                  <!-- Selected File Display -->
                  <div
                    v-else
                    class="flex items-center justify-between bg-white rounded-lg p-4 border-2 border-gray-200"
                  >
                    <div class="flex items-center gap-3">
                      <div
                        class="w-10 h-10 bg-blue-50 rounded-lg flex items-center justify-center"
                      >
                        <svg
                          class="w-5 h-5 text-blue-600"
                          fill="none"
                          stroke="currentColor"
                          viewBox="0 0 24 24"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                          ></path>
                        </svg>
                      </div>
                      <div class="text-left">
                        <p class="font-semibold text-gray-900 text-sm">
                          {{ selectedFile.name }}
                        </p>
                        <p class="text-xs text-gray-600">
                          {{ formatFileSize(selectedFile.size) }}
                        </p>
                      </div>
                    </div>
                    <Button
                      @click.stop="removeFile"
                      type="button"
                      variant="outline"
                      size="sm"
                      class="text-red-600 hover:text-red-700 hover:bg-red-50 border-red-300"
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
                          d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                        ></path>
                      </svg>
                    </Button>
                  </div>
                </div>
              </div>

              <p
                v-if="fieldErrors.file"
                class="text-red-600 text-xs font-semibold flex items-center gap-1"
              >
                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                {{ fieldErrors.file }}
              </p>
            </div>

            <!-- Pilih Dosen -->
            <div class="space-y-2">
              <Label
                for="dosen"
                class="text-sm font-bold text-gray-700 uppercase tracking-wide"
              >
                Pilih Dosen <span class="text-red-600">*</span>
              </Label>

              <Select v-model="selectedDosen">
                <SelectTrigger
                  class="h-12 rounded-lg border-2 focus:border-blue-600 bg-white font-medium"
                  :class="{
                    'border-gray-300': !fieldErrors.dosen,
                    'border-red-500': fieldErrors.dosen,
                  }"
                >
                  <SelectValue placeholder="Pilih dosen pembimbing..." />
                </SelectTrigger>
                <SelectContent
                  class="rounded-lg border-2 border-gray-200 shadow-lg"
                >
                  <SelectGroup>
                    <SelectItem
                      v-for="dosen in dosenList"
                      :key="dosen.id"
                      :value="dosen.id.toString()"
                      class="focus:bg-blue-50 font-medium"
                    >
                      <div class="flex items-center gap-3">
                        <div
                          class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center"
                        >
                          <span class="text-xs font-bold text-blue-700">
                            {{ getInitials(dosen.nama) }}
                          </span>
                        </div>
                        <p class="font-semibold text-gray-900">
                          {{ dosen.nama }}
                        </p>
                      </div>
                    </SelectItem>
                  </SelectGroup>
                </SelectContent>
              </Select>

              <p
                v-if="fieldErrors.dosen"
                class="text-red-600 text-xs font-semibold flex items-center gap-1"
              >
                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                {{ fieldErrors.dosen }}
              </p>
            </div>

            <!-- Judul Permohonan -->
            <div class="space-y-2">
              <Label
                for="judul"
                class="text-sm font-bold text-gray-700 uppercase tracking-wide"
              >
                Judul Permohonan
              </Label>
              <Input
                id="judul"
                v-model="judul"
                type="text"
                placeholder="Contoh: Permohonan Tanda Tangan Skripsi"
                disabled
                class="h-12 rounded-lg border-2 border-gray-300 bg-gray-100 text-gray-600 font-medium cursor-not-allowed"
              />
              <p
                class="text-xs text-gray-600 font-medium flex items-center gap-1"
              >
                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                Judul otomatis berdasarkan jenis permohonan
              </p>
            </div>

            <!-- Deskripsi -->
            <div class="space-y-2">
              <Label
                for="deskripsi"
                class="text-sm font-bold text-gray-700 uppercase tracking-wide"
              >
                Deskripsi Permohonan
              </Label>
              <textarea
                id="deskripsi"
                v-model="deskripsi"
                rows="4"
                placeholder="Jelaskan detail permohonan Anda, tujuan penggunaan, dan informasi tambahan lainnya..."
                class="w-full rounded-lg border-2 focus:border-blue-600 focus:ring-0 bg-white font-medium p-4 resize-none placeholder:text-gray-400"
                :class="{
                  'border-gray-300': !fieldErrors.deskripsi,
                  'border-red-500': fieldErrors.deskripsi,
                }"
              />
              <div class="flex justify-between items-center">
                <p
                  v-if="fieldErrors.deskripsi"
                  class="text-red-600 text-xs font-semibold flex items-center gap-1"
                >
                  <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                    <path
                      fill-rule="evenodd"
                      d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                  {{ fieldErrors.deskripsi }}
                </p>
                <p class="text-xs text-gray-600 font-semibold ml-auto">
                  {{ deskripsi.length }}/500 karakter
                </p>
              </div>
            </div>

            <!-- Jenis Permohonan (Hidden/Auto) -->
            <input type="hidden" v-model="jenisPermohonan" />

            <!-- Action Buttons -->
            <div class="flex flex-col sm:flex-row gap-3 pt-4">
              <Button
                type="button"
                @click="cancelForm"
                variant="outline"
                class="flex-1 h-12 border-2 border-gray-300 hover:border-gray-400 hover:bg-gray-50 text-gray-700 font-bold rounded-lg uppercase text-sm tracking-wide"
              >
                <span class="flex items-center justify-center gap-2">
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
                      d="M6 18L18 6M6 6l12 12"
                    ></path>
                  </svg>
                  Batal
                </span>
              </Button>

              <Button
                type="submit"
                :disabled="isSubmitting || !isFormValid"
                class="flex-1 h-12 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-lg uppercase text-sm tracking-wide shadow-sm border-0 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span
                  v-if="!isSubmitting"
                  class="flex items-center justify-center gap-2"
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
                      d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
                    ></path>
                  </svg>
                  Ajukan Permohonan
                </span>
                <span v-else class="flex items-center justify-center gap-2">
                  <svg
                    class="animate-spin h-4 w-4 text-white"
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
                  Mengajukan...
                </span>
              </Button>
            </div>
          </form>

          <!-- Success/Error Messages -->
          <div class="space-y-3 mt-6">
            <!-- Error Alert -->
            <Alert
              v-if="error"
              variant="destructive"
              class="border-l-4 border-red-600 bg-red-50 rounded-lg"
            >
              <div class="flex items-center gap-2">
                <svg
                  class="w-5 h-5 text-red-600"
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
                <span class="font-semibold text-red-900 whitespace-pre-line">{{
                  error
                }}</span>
              </div>
            </Alert>

            <!-- Success Alert -->
            <Alert
              v-if="success"
              class="border-l-4 border-green-600 bg-green-50 rounded-lg p-4"
            >
              <div class="flex items-center gap-2">
                <!-- Icon -->
                <svg
                  class="w-5 h-5 text-green-600"
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
                <span class="font-semibold text-green-900">Berhasil!</span>
              </div>

              <!-- Pesan multi-line -->
              <div class="mt-7 text-green-900 whitespace-pre-line">
                {{ success }}
              </div>
            </Alert>
          </div>

          <!-- Information Panel -->
          <div class="mt-6 p-4 bg-blue-50 rounded-lg border-2 border-blue-200">
            <h4
              class="text-sm font-bold text-blue-900 mb-2 uppercase tracking-wide flex items-center gap-2"
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
              Informasi Penting
            </h4>
            <ul class="text-xs text-blue-800 space-y-1 font-medium">
              <li>
                • Pastikan dokumen yang diupload sudah dalam format yang benar
              </li>
              <li>• Permohonan akan diproses dalam 2-3 hari kerja</li>
              <li>
                • Anda akan mendapat notifikasi email setelah dokumen
                ditandatangani
              </li>
              <li>• Hubungi admin jika ada pertanyaan lebih lanjut</li>
            </ul>
          </div>
        </CardContent>
      </Card>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from "vue";
import { useRouter } from "vue-router";
import { createPermohonan } from "@/services/permohonanService";
import { getAllDosen, type Dosen } from "@/services/dosenServices";
import { Card, CardContent } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Alert } from "@/components/ui/alert";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

const router = useRouter();

// Form state
const dosenList = ref<Dosen[]>([]);
const selectedDosen = ref<string>("");
const selectedFile = ref<File | null>(null);
const judul = ref("Permohonan Tanda Tangan");
const deskripsi = ref("");
const jenisPermohonan = ref<number>(1);

// UI state
const isSubmitting = ref(false);
const isDragOver = ref(false);
const error = ref("");
const success = ref("");
const fieldErrors = ref<{ [key: string]: string }>({});

// Computed properties
const isFormValid = computed(() => {
  return (
    selectedFile.value &&
    selectedDosen.value &&
    judul.value &&
    Object.keys(fieldErrors.value).length === 0
  );
});

// File handling functions
const triggerFileInput = () => {
  const fileInput = document.getElementById("file-upload") as HTMLInputElement;
  fileInput?.click();
};

const handleFileChange = (e: Event) => {
  const target = e.target as HTMLInputElement;
  if (target.files && target.files.length > 0) {
    const file = target.files[0];
    validateFile(file);
    selectedFile.value = file;
  }
};

const handleFileDrop = (e: DragEvent) => {
  isDragOver.value = false;

  if (e.dataTransfer && e.dataTransfer.files.length > 0) {
    const file = e.dataTransfer.files[0];
    validateFile(file);
    selectedFile.value = file;
  }
};

const validateFile = (file: File) => {
  const maxSize = 10 * 1024 * 1024; // 10MB
  const allowedTypes = [
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "image/jpeg",
    "image/jpg",
    "image/png",
  ];

  if (file.size > maxSize) {
    fieldErrors.value.file = "Ukuran file tidak boleh lebih dari 10MB";
    selectedFile.value = null;
    return false;
  }

  if (!allowedTypes.includes(file.type)) {
    fieldErrors.value.file =
      "Format file tidak didukung. Gunakan PDF, DOC, DOCX, JPG, atau PNG";
    selectedFile.value = null;
    return false;
  }

  delete fieldErrors.value.file;
  return true;
};

const removeFile = () => {
  selectedFile.value = null;
  delete fieldErrors.value.file;
  const fileInput = document.getElementById("file-upload") as HTMLInputElement;
  if (fileInput) fileInput.value = "";
};

const formatFileSize = (bytes: number) => {
  if (bytes === 0) return "0 Bytes";
  const k = 1024;
  const sizes = ["Bytes", "KB", "MB", "GB"];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i];
};

const getInitials = (name: string) => {
  return name
    .split(" ")
    .map((n) => n[0])
    .join("")
    .substring(0, 2)
    .toUpperCase();
};

// Form functions
const fetchDosen = async () => {
  try {
    dosenList.value = await getAllDosen();
  } catch (error: Error | any) {
    console.error("Gagal fetch data dosen:", error);
    error.value = "Gagal memuat data dosen. Silakan refresh halaman.";
  }
};

const validateForm = () => {
  const errors: { [key: string]: string } = {};

  if (!selectedFile.value) {
    errors.file = "File dokumen wajib diupload";
  }

  if (!selectedDosen.value) {
    errors.dosen = "Pilih dosen pembimbing";
  }

  if (!judul.value.trim()) {
    errors.judul = "Judul permohonan wajib diisi";
  }

  if (deskripsi.value.length > 500) {
    errors.deskripsi = "Deskripsi tidak boleh lebih dari 500 karakter";
  }

  return errors;
};

const submitForm = async () => {
  fieldErrors.value = {};
  error.value = "";
  success.value = "";

  const validationErrors = validateForm();
  if (Object.keys(validationErrors).length > 0) {
    fieldErrors.value = validationErrors;
    error.value = "Mohon periksa kembali form Anda.";
    return;
  }

  try {
    isSubmitting.value = true;

    const res = await createPermohonan({
      id_dosen: selectedDosen.value,
      id_jenis_permohonan: jenisPermohonan.value,
      judul: judul.value.trim(),
      deskripsi: deskripsi.value.trim(),
      file: selectedFile.value || undefined,
    });

    console.log("✅ Permohonan berhasil:", res);
    success.value = "Permohonan berhasil diajukan!";

    setTimeout(() => {
      router.push("/mahasiswa/dashboard");
    }, 3000);
  } catch (err: any) {
    console.error("❌ Gagal ajukan:", err);

    if (err.response?.status === 422) {
      const data = err.response.data;
      if (data?.errors) {
        fieldErrors.value = data.errors;
        error.value = "Terdapat kesalahan pada form.";
      } else {
        error.value = data?.message || "Data yang Anda masukkan tidak valid.";
      }
    } else if (err.response?.status === 401) {
      error.value = "Sesi Anda telah berakhir. Silakan login ulang.";
    } else if (err.response?.status === 500) {
      error.value = "Terjadi kesalahan pada server. Silakan coba lagi nanti.";
    } else {
      error.value =
        err.response?.data?.message ||
        "Terjadi kesalahan saat mengajukan permohonan.";
    }
  } finally {
    isSubmitting.value = false;
  }
};

const cancelForm = () => {
  router.back();
};

watch(
  () => [selectedFile.value, selectedDosen.value, deskripsi.value],
  () => {
    error.value = "";
    success.value = "";
  },
  { deep: true }
);

onMounted(fetchDosen);
</script>

<style scoped>
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>
