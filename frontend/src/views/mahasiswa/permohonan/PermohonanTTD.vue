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
      class="w-[650px] max-w-full shadow-2xl shadow-purple-100 border-0 bg-white/80 backdrop-blur-sm relative overflow-hidden"
    >
      <!-- Card decoration -->
      <div
        class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-purple-400 via-purple-500 to-purple-600"
      ></div>

      <CardHeader class="text-center pb-4 pt-8">
        <!-- Document Sign Icon -->
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
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
            ></path>
          </svg>
        </div>

        <CardTitle class="text-2xl font-bold text-gray-800 mb-2"
          >Permohonan Tanda Tangan</CardTitle
        >
        <CardDescription class="text-gray-600">
          Ajukan permohonan tanda tangan dokumen kepada dosen pembimbing
        </CardDescription>
      </CardHeader>

      <CardContent class="px-8 pb-8">
        <form @submit.prevent="submitForm" class="space-y-6">
          <!-- Upload File Section -->
          <div class="space-y-3">
            <Label
              for="file-upload"
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
                  d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                ></path>
              </svg>
              Upload Berkas <span class="text-red-500">*</span>
            </Label>

            <!-- Custom File Upload -->
            <div class="relative">
              <input
                id="file-upload"
                type="file"
                @change="handleFileChange"
                class="hidden"
                accept=".pdf,.doc,.docx,.jpg,.jpeg,.png"
                :class="{ 'border-red-300': fieldErrors.file }"
              />

              <div
                @click="triggerFileInput"
                @dragover.prevent="isDragOver = true"
                @dragleave.prevent="isDragOver = false"
                @drop.prevent="handleFileDrop"
                class="relative border-2 border-dashed rounded-xl p-8 text-center cursor-pointer transition-all duration-300 hover:scale-[1.02]"
                :class="{
                  'border-purple-300 bg-purple-50 hover:border-purple-400':
                    !isDragOver && !fieldErrors.file,
                  'border-purple-400 bg-purple-100': isDragOver,
                  'border-red-300 bg-red-50': fieldErrors.file,
                }"
              >
                <div v-if="!selectedFile" class="space-y-3">
                  <div
                    class="w-12 h-12 mx-auto bg-purple-100 rounded-lg flex items-center justify-center"
                  >
                    <svg
                      class="w-6 h-6 text-purple-600"
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
                    <p class="font-medium text-gray-700">
                      Klik untuk upload atau drag & drop
                    </p>
                    <p class="text-sm text-gray-500">
                      PDF, DOC, DOCX, JPG, PNG (Max 10MB)
                    </p>
                  </div>
                </div>

                <!-- Selected File Display -->
                <div
                  v-else
                  class="flex items-center justify-between bg-white rounded-lg p-4 shadow-sm border border-gray-200"
                >
                  <div class="flex items-center gap-3">
                    <div
                      class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center"
                    >
                      <svg
                        class="w-5 h-5 text-purple-600"
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
                      <p class="font-medium text-gray-800 text-sm">
                        {{ selectedFile.name }}
                      </p>
                      <p class="text-xs text-gray-500">
                        {{ formatFileSize(selectedFile.size) }}
                      </p>
                    </div>
                  </div>
                  <Button
                    @click.stop="removeFile"
                    variant="outline"
                    size="sm"
                    class="text-red-600 hover:text-red-700 hover:bg-red-50 border-red-200"
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
              class="text-red-500 text-xs flex items-center gap-1"
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
                ></path>
              </svg>
              Pilih Dosen <span class="text-red-500">*</span>
            </Label>

            <Select v-model="selectedDosen">
              <SelectTrigger
                class="h-12 rounded-xl border-2 border-gray-200 focus:border-purple-400 bg-white/70 backdrop-blur-sm"
                :class="{
                  'border-red-300 focus:border-red-400': fieldErrors.dosen,
                }"
              >
                <SelectValue placeholder="Pilih dosen pembimbing..." />
              </SelectTrigger>
              <SelectContent class="rounded-xl border-0 shadow-xl">
                <SelectGroup>
                  <SelectItem
                    v-for="dosen in dosenList"
                    :key="dosen.id"
                    :value="dosen.id.toString()"
                    class="focus:bg-purple-50"
                  >
                    <div class="flex items-center gap-3">
                      <div
                        class="w-8 h-8 bg-purple-100 rounded-full flex items-center justify-center"
                      >
                        <span class="text-xs font-medium text-purple-600">
                          {{ getInitials(dosen.nama) }}
                        </span>
                      </div>
                      <div class="text-left">
                        <p class="font-medium">{{ dosen.nama }}</p>
                        <p class="text-xs text-gray-500">
                          {{ dosen.nip || "NIP: -" }}
                        </p>
                      </div>
                    </div>
                  </SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>

            <p
              v-if="fieldErrors.dosen"
              class="text-red-500 text-xs flex items-center gap-1"
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
                  d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a1.994 1.994 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"
                ></path>
              </svg>
              Judul Permohonan
            </Label>
            <Input
              id="judul"
              v-model="judul"
              type="text"
              placeholder="Contoh: Permohonan Tanda Tangan Skripsi"
              disabled
              class="h-12 rounded-xl border-2 border-gray-200 bg-gray-50 text-gray-500 cursor-not-allowed"
            />
            <p class="text-xs text-gray-500 flex items-center gap-1">
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
                  d="M4 6h16M4 12h16M4 18h7"
                ></path>
              </svg>
              Deskripsi Permohonan
            </Label>
            <textarea
              id="deskripsi"
              v-model="deskripsi"
              rows="4"
              placeholder="Jelaskan detail permohonan Anda, tujuan penggunaan, dan informasi tambahan lainnya..."
              class="w-full rounded-xl border-2 border-gray-200 focus:border-purple-400 focus:ring-purple-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400 p-4 resize-none"
              :class="{
                'border-red-300 focus:border-red-400': fieldErrors.deskripsi,
              }"
            />
            <div class="flex justify-between items-center">
              <p
                v-if="fieldErrors.deskripsi"
                class="text-red-500 text-xs flex items-center gap-1"
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
              <p class="text-xs text-gray-500">
                {{ deskripsi.length }}/500 karakter
              </p>
            </div>
          </div>

          <!-- Jenis Permohonan (Hidden/Auto) -->
          <input type="hidden" v-model="jenisPermohonan" />

          <!-- Action Buttons -->
          <div class="flex flex-col sm:flex-row gap-4 pt-6">
            <Button
              type="button"
              @click="cancelForm"
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
                    d="M6 18L18 6M6 6l12 12"
                  ></path>
                </svg>
                Batal
              </span>
            </Button>

            <Button
              type="submit"
              :disabled="isSubmitting || !isFormValid"
              class="flex-1 h-12 bg-gradient-to-r from-purple-400 to-purple-500 hover:from-purple-500 hover:to-purple-600 text-white font-semibold rounded-xl shadow-lg shadow-purple-200 border-0 transition-all duration-300 hover:scale-[1.02] hover:shadow-xl hover:shadow-purple-300 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100"
            >
              <span
                v-if="!isSubmitting"
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
                    d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
                  ></path>
                </svg>
                Ajukan Permohonan
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
                Mengajukan...
              </span>
            </Button>
          </div>
        </form>

        <!-- Success/Error Messages -->
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
            class="border-purple-200 bg-purple-50 text-purple-800 rounded-xl"
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
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
              ></path>
            </svg>
            {{ success }}
          </Alert>
        </div>

        <!-- Information Panel -->
        <div class="mt-8 p-4 bg-purple-50 rounded-xl border border-purple-100">
          <h4
            class="text-sm font-semibold text-purple-800 mb-2 flex items-center gap-2"
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
          <ul class="text-xs text-purple-700 space-y-1">
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
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from "vue";
import { useRouter } from "vue-router";
import { createPermohonan } from "@/services/permohonanService";
import { getAllDosen, type Dosen } from "@/services/dosenServices";
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
  } catch (error) {
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
  // Reset states
  fieldErrors.value = {};
  error.value = "";
  success.value = "";

  // Validate form
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
    success.value =
      "Permohonan berhasil diajukan! Anda akan mendapat notifikasi melalui email.";

    // Reset form after success
    setTimeout(() => {
      router.push("/mahasiswa/dashboard");
    }, 3000);
  } catch (err: any) {
    console.error("❌ Gagal ajukan:", err);

    // Handle different types of errors
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

// Clear messages when form changes
watch(
  () => [selectedFile.value, selectedDosen.value, deskripsi.value],
  () => {
    error.value = "";
    success.value = "";
  },
  { deep: true }
);

// Lifecycle
onMounted(fetchDosen);
</script>
