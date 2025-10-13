<template>
  <div
    class="min-h-screen bg-gradient-to-br from-emerald-50 via-white to-emerald-50 flex items-center justify-center p-4"
  >
    <div class="max-w-3xl w-full">
      <!-- Loading State -->
      <div
        v-if="loading"
        class="bg-white rounded-xl shadow-2xl p-8 text-center border-2 border-emerald-200"
      >
        <div class="relative w-20 h-20 mx-auto mb-6">
          <div
            class="absolute inset-0 border-4 border-emerald-100 rounded-full"
          ></div>
          <div
            class="absolute inset-0 border-4 border-t-emerald-500 rounded-full animate-spin"
          ></div>
        </div>
        <h3 class="text-xl font-bold text-emerald-800 mb-2">
          Verifying Document
        </h3>
        <p class="text-emerald-600">
          Please wait while we authenticate the document...
        </p>
      </div>

      <!-- Valid Document -->
      <div
        v-else-if="isValid && documentData"
        class="bg-white rounded-xl shadow-2xl overflow-hidden border-2 border-emerald-200"
      >
        <!-- Header -->
        <div
          class="bg-gradient-to-r from-emerald-600 to-emerald-700 p-8 relative overflow-hidden"
        >
          <div
            class="absolute top-0 right-0 w-64 h-64 bg-emerald-400 opacity-20 rounded-full -mr-32 -mt-32"
          ></div>
          <div
            class="absolute bottom-0 left-0 w-48 h-48 bg-emerald-500 opacity-20 rounded-full -ml-24 -mb-24"
          ></div>
          <div class="relative z-10">
            <div class="flex items-center justify-center mb-6">
              <div
                class="w-20 h-20 bg-white rounded-full flex items-center justify-center shadow-lg"
              >
                <svg
                  class="w-12 h-12 text-emerald-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2.5"
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                  ></path>
                </svg>
              </div>
            </div>
            <h1 class="text-3xl font-bold text-center text-white mb-2">
              Document Verified
            </h1>
            <p class="text-center text-emerald-100 font-medium">
              This document has been officially verified and digitally signed
            </p>
            <div class="mt-4 flex justify-center">
              <span
                class="inline-flex items-center px-4 py-2 bg-white bg-opacity-20 backdrop-blur-sm border border-white rounded-full text-sm text-emerald-600 font-semibold"
              >
                <span
                  class="w-2 h-2 bg-emerald-600 rounded-full mr-2 animate-pulse"
                ></span>
                Authenticated
              </span>
            </div>
          </div>
        </div>

        <!-- Content -->
        <div class="p-8 space-y-8">
          <!-- Document Info -->
          <div class="border-b-2 border-emerald-100 pb-6">
            <h2
              class="text-xl font-bold text-emerald-800 mb-4 flex items-center"
            >
              <svg
                class="w-5 h-5 mr-2 text-emerald-600"
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
              Document Information
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div
                class="bg-emerald-50 rounded-lg p-4 border border-emerald-100"
              >
                <label
                  class="text-xs font-bold text-emerald-600 uppercase tracking-wider"
                  >Application ID</label
                >
                <p class="mt-1 font-bold text-emerald-900 text-lg">
                  {{ documentData.permohonan_id }}
                </p>
              </div>
              <div
                class="bg-emerald-50 rounded-lg p-4 border border-emerald-100"
              >
                <label
                  class="text-xs font-bold text-emerald-600 uppercase tracking-wider"
                  >Application Type</label
                >
                <p class="mt-1 font-bold text-emerald-900 text-lg">
                  {{ documentData.jenis_permohonan?.nama || "-" }}
                </p>
              </div>
              <div
                class="bg-emerald-50 rounded-lg p-4 md:col-span-2 border border-emerald-100"
              >
                <label
                  class="text-xs font-bold text-emerald-600 uppercase tracking-wider"
                  >Title</label
                >
                <p class="mt-1 font-bold text-emerald-900 text-lg">
                  {{ documentData.judul }}
                </p>
              </div>
              <div
                v-if="documentData.deskripsi"
                class="bg-emerald-50 rounded-lg p-4 md:col-span-2 border border-emerald-100"
              >
                <label
                  class="text-xs font-bold text-emerald-600 uppercase tracking-wider"
                  >Description</label
                >
                <p class="mt-1 text-emerald-700">
                  {{ documentData.deskripsi }}
                </p>
              </div>
            </div>
          </div>

          <!-- Student Info -->
          <div class="border-b-2 border-emerald-100 pb-6">
            <h2
              class="text-xl font-bold text-emerald-800 mb-4 flex items-center"
            >
              <svg
                class="w-5 h-5 mr-2 text-emerald-600"
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
              Student Information
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div
                class="bg-emerald-50 rounded-lg p-4 border border-emerald-100"
              >
                <label
                  class="text-xs font-bold text-emerald-600 uppercase tracking-wider"
                  >Full Name</label
                >
                <p class="mt-1 font-bold text-emerald-900">
                  {{ documentData.mahasiswa.nama }}
                </p>
              </div>
              <div
                class="bg-emerald-50 rounded-lg p-4 border border-emerald-100"
              >
                <label
                  class="text-xs font-bold text-emerald-600 uppercase tracking-wider"
                  >Student ID</label
                >
                <p class="mt-1 font-bold text-emerald-900">
                  {{ documentData.mahasiswa.nomor_induk }}
                </p>
              </div>
              <div
                class="bg-emerald-50 rounded-lg p-4 border border-emerald-100"
              >
                <label
                  class="text-xs font-bold text-emerald-600 uppercase tracking-wider"
                  >Study Program</label
                >
                <p class="mt-1 font-bold text-emerald-900">
                  {{ documentData.mahasiswa.program_studi }}
                </p>
              </div>
              <div
                class="bg-emerald-50 rounded-lg p-4 border border-emerald-100"
              >
                <label
                  class="text-xs font-bold text-emerald-600 uppercase tracking-wider"
                  >Faculty</label
                >
                <p class="mt-1 font-bold text-emerald-900">
                  {{ documentData.mahasiswa.fakultas }}
                </p>
              </div>
            </div>
          </div>

          <!-- Signature Info -->
          <div class="border-b-2 border-emerald-100 pb-6">
            <h2
              class="text-xl font-bold text-emerald-800 mb-4 flex items-center"
            >
              <svg
                class="w-5 h-5 mr-2 text-emerald-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
                ></path>
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                ></path>
              </svg>
              Digital Signature
            </h2>
            <div
              class="bg-gradient-to-r from-emerald-50 to-green-50 rounded-lg p-6 border-2 border-emerald-200"
            >
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label
                    class="text-xs font-bold text-emerald-600 uppercase tracking-wider"
                    >Signed By</label
                  >
                  <p class="mt-1 font-bold text-emerald-900 text-lg">
                    {{ documentData.dosen.nama }}
                  </p>
                </div>
                <div>
                  <label
                    class="text-xs font-bold text-emerald-600 uppercase tracking-wider"
                    >Signature Time</label
                  >
                  <p class="mt-1 font-bold text-emerald-900 text-lg">
                    {{ formatDate(documentData.signed_at) }}
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Verification Badge -->
          <div
            class="bg-gradient-to-r from-emerald-600 to-green-600 rounded-lg p-6 text-center relative overflow-hidden"
          >
            <div
              class="absolute top-0 right-0 w-32 h-32 bg-white opacity-10 rounded-full -mr-16 -mt-16"
            ></div>
            <div
              class="absolute bottom-0 left-0 w-24 h-24 bg-white opacity-10 rounded-full -ml-12 -mb-12"
            ></div>
            <div class="relative z-10">
              <div class="flex items-center justify-center mb-3">
                <svg
                  class="w-8 h-8 text-yellow-300 mr-3"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                  ></path>
                </svg>
                <span class="text-yellow-300 font-bold text-lg"
                  >Official Verification</span
                >
              </div>
              <p class="text-white text-sm font-medium">
                This document has been verified through the official digital
                signature system
              </p>
              <p class="text-emerald-100 text-xs mt-2">
                Verification ID: {{ documentData.permohonan_id }}
              </p>
            </div>
          </div>
        </div>

        <!-- Footer -->
        <div
          class="bg-emerald-50 px-8 py-4 text-center border-t-2 border-emerald-200"
        >
          <p class="text-emerald-700 font-medium text-sm">
            For inquiries, please contact the relevant department
          </p>
          <p class="text-emerald-600 text-xs mt-1">
            © {{ new Date().getFullYear() }} Document Verification System
          </p>
        </div>
      </div>

      <!-- Error State -->
      <div
        v-else
        class="bg-white rounded-xl shadow-2xl p-8 text-center border-2 border-red-200"
      >
        <div
          class="w-20 h-20 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-6"
        >
          <svg
            class="w-12 h-12 text-red-600"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            ></path>
          </svg>
        </div>
        <h2 class="text-2xl font-bold text-red-800 mb-2">
          Verification Failed
        </h2>
        <p class="text-red-600 font-medium">{{ errorMessage }}</p>
        <button
          @click="verifyDocument"
          class="mt-6 px-6 py-3 bg-emerald-600 text-white font-bold rounded-lg hover:bg-emerald-700 transition-colors shadow-lg"
        >
          Try Again
        </button>
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
  loading.value = true;
  try {
    const permohonanId = route.params.id;
    const response = await apiClient.get(`/verify/${permohonanId}`);

    if (response.data.success && response.data.data.status === "valid") {
      isValid.value = true;
      documentData.value = response.data.data;
    } else {
      isValid.value = false;
      errorMessage.value = response.data.message || "Document is not valid";
    }
  } catch (error: any) {
    isValid.value = false;
    errorMessage.value =
      error.response?.data?.message || "Document not found or invalid";
    console.error("Verification error:", error);
  } finally {
    loading.value = false;
  }
};

const formatDate = (dateString: string) => {
  if (!dateString) return "-";

  const utcDateString = dateString.endsWith("Z")
    ? dateString
    : dateString + "Z";
  const date = new Date(utcDateString);

  return date.toLocaleString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    timeZone: "UTC",
  });
};

onMounted(() => {
  verifyDocument();
});
</script>
