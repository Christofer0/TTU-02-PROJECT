<template>
  <div class="min-h-screen bg-gray-50 p-6">
    <div class="max-w-7xl mx-auto space-y-6">
      <!-- Welcome Header -->
      <Card class="border-l-4 border-blue-600 shadow-sm bg-white">
        <CardContent class="p-6">
          <div class="flex items-center justify-between">
            <div class="space-y-1">
              <div class="flex items-center gap-3">
                <div
                  class="w-12 h-12 bg-blue-600 rounded-lg flex items-center justify-center"
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
                      d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                    ></path>
                  </svg>
                </div>
                <div>
                  <h1 class="text-2xl font-bold text-gray-900">
                    {{ getGreeting() }}, {{ user?.nama }}
                  </h1>
                  <p class="text-sm text-gray-600 font-medium">
                    Sistem Informasi Akademik FTI UKSW
                  </p>
                </div>
              </div>
            </div>

            <!-- Current Time -->
            <div class="text-right">
              <p
                class="text-xs text-gray-500 uppercase tracking-wide font-semibold"
              >
                {{ currentDate }}
              </p>
              <p class="text-xl text-gray-900 font-bold">{{ currentTime }}</p>
            </div>
          </div>
        </CardContent>
      </Card>

      <!-- Quick Stats -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card class="border-2 border-gray-200 shadow-sm bg-white">
          <CardContent class="p-5">
            <div class="flex items-start justify-between">
              <div class="flex-1">
                <p
                  class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2"
                >
                  Total Permohonan
                </p>
                <p class="text-3xl font-bold text-gray-900">
                  {{ totalPermohonan }}
                </p>
              </div>
              <div class="p-3 bg-blue-50 rounded-lg">
                <svg
                  class="w-6 h-6 text-blue-600"
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
            </div>
          </CardContent>
        </Card>

        <Card class="border-2 border-gray-200 shadow-sm bg-white">
          <CardContent class="p-5">
            <div class="flex items-start justify-between">
              <div class="flex-1">
                <p
                  class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2"
                >
                  Permohonan Selesai
                </p>
                <p class="text-3xl font-bold text-gray-900">
                  {{ permohonanSelesai }}
                </p>
              </div>
              <div class="p-3 bg-green-50 rounded-lg">
                <svg
                  class="w-6 h-6 text-green-600"
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
            </div>
          </CardContent>
        </Card>

        <Card class="border-2 border-gray-200 shadow-sm bg-white">
          <CardContent class="p-5">
            <div class="flex items-start justify-between">
              <div class="flex-1">
                <p
                  class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2"
                >
                  Sedang Diproses
                </p>
                <p class="text-3xl font-bold text-gray-900">
                  {{ permohonanProses }}
                </p>
              </div>
              <div class="p-3 bg-amber-50 rounded-lg">
                <svg
                  class="w-6 h-6 text-amber-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                  ></path>
                </svg>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card class="border-2 border-gray-200 shadow-sm bg-white">
          <CardContent class="p-5">
            <div class="flex items-start justify-between">
              <div class="flex-1">
                <p
                  class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2"
                >
                  Permohonan Ditolak
                </p>
                <p class="text-3xl font-bold text-gray-900">
                  {{ permohonanDitolak }}
                </p>
              </div>
              <div class="p-3 bg-red-50 rounded-lg">
                <svg
                  class="w-6 h-6 text-red-600"
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
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <!-- Recent Activity / History Summary -->
      <Card class="shadow-sm border border-gray-200 bg-white overflow-hidden">
        <div class="bg-gray-800 text-white px-6 py-4 border-b border-gray-700">
          <div class="flex items-center justify-between">
            <h2 class="text-lg font-bold flex items-center gap-2">
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
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                ></path>
              </svg>
              Aktivitas Terbaru
            </h2>
            <Button
              @click="router.push('/mahasiswa/history')"
              variant="ghost"
              class="text-white hover:bg-gray-700 text-sm font-semibold"
            >
              Lihat Semua
              <svg
                class="w-4 h-4 ml-1"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 5l7 7-7 7"
                ></path>
              </svg>
            </Button>
          </div>
        </div>

        <CardContent class="p-6">
          <!-- Recent History Items -->
          <div class="space-y-3">
            <div
              v-for="item in recentHistory"
              :key="item.id"
              class="flex items-center gap-4 p-4 bg-gray-50 border border-gray-200 rounded-lg hover:bg-gray-100 transition-colors"
            >
              <div
                class="w-10 h-10 rounded-lg flex items-center justify-center flex-shrink-0"
                :class="getStatusColor(item.status_permohonan)"
              >
                <svg
                  class="w-5 h-5"
                  :class="getStatusIconColor(item.status_permohonan)"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    v-if="
                      item.status_permohonan === 'ditandatangani' ||
                      item.status_permohonan === 'disetujui'
                    "
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                  ></path>
                  <path
                    v-else-if="item.status_permohonan === 'pending'"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                  ></path>
                  <path
                    v-else
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M6 18L18 6M6 6l12 12"
                  ></path>
                </svg>
              </div>
              <div class="flex-1 min-w-0">
                <h4 class="text-sm font-bold text-gray-900 truncate">
                  {{ item.judul || "Permohonan" }}
                </h4>
                <p class="text-xs text-gray-600 mt-1">
                  {{ formatDate(item.created_at) }} •
                  {{ item.dosen?.user?.nama || "-" }}
                </p>
              </div>
              <span
                class="px-3 py-1 rounded-md text-xs font-bold uppercase"
                :class="getStatusBadgeClass(item.status_permohonan)"
              >
                {{ getStatusLabel(item.status_permohonan) }}
              </span>
            </div>
          </div>

          <!-- Empty State -->
          <div v-if="recentHistory.length === 0" class="text-center py-12">
            <div
              class="inline-flex items-center justify-center w-16 h-16 bg-gray-100 rounded-full mb-4"
            >
              <svg
                class="w-8 h-8 text-gray-400"
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
            <p class="text-gray-600 font-medium">Belum ada aktivitas</p>
          </div>
        </CardContent>
      </Card>

      <!-- Menu Layanan Surat -->
      <Card class="shadow-sm border border-gray-200 bg-white overflow-hidden">
        <div class="bg-gray-800 text-white px-6 py-4 border-b border-gray-700">
          <h2 class="text-lg font-bold flex items-center gap-2">
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
                d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
              ></path>
            </svg>
            Layanan Permohonan Surat
          </h2>
        </div>

        <CardContent class="p-6 space-y-6">
          <!-- Search and Filter Section -->
          <div class="bg-gray-50 rounded-lg p-6 border-2 border-gray-200">
            <Label
              class="text-sm font-bold text-gray-700 mb-4 block uppercase tracking-wide"
            >
              Pencarian Jenis Surat
            </Label>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Select Dropdown -->
              <div class="md:col-span-2">
                <Select v-model="selectedJenis">
                  <SelectTrigger
                    class="h-12 rounded-lg border-2 border-gray-300 focus:border-blue-600 bg-white font-medium"
                  >
                    <SelectValue
                      placeholder="Pilih jenis surat yang dibutuhkan..."
                    />
                  </SelectTrigger>
                  <SelectContent
                    class="rounded-lg border-2 border-gray-200 shadow-lg"
                  >
                    <SelectGroup>
                      <SelectItem
                        v-for="item in jenisPermohonanList"
                        :key="item.id"
                        :value="item.id"
                        class="focus:bg-blue-50 font-medium"
                      >
                        {{ item.nama_jenis_permohonan }}
                      </SelectItem>
                    </SelectGroup>
                  </SelectContent>
                </Select>
              </div>

              <!-- Action Buttons -->
              <div class="flex gap-2">
                <Button
                  @click="cariSurat"
                  class="flex-1 h-12 bg-blue-600 hover:bg-blue-700 text-white rounded-lg shadow-sm border-0 font-semibold uppercase text-sm tracking-wide"
                  :disabled="!selectedJenis"
                >
                  <svg
                    class="w-4 h-4 mr-2"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                    ></path>
                  </svg>
                  Cari
                </Button>

                <Button
                  @click="reloadSurat"
                  variant="outline"
                  class="h-12 border-2 border-gray-300 hover:border-gray-400 hover:bg-gray-50 rounded-lg px-4"
                >
                  <svg
                    class="w-5 h-5 text-gray-600"
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
                </Button>
              </div>
            </div>
          </div>

          <!-- Hasil Pencarian -->
          <div
            v-if="hasilSurat"
            class="bg-white rounded-lg border-2 border-gray-300 shadow-sm overflow-hidden"
          >
            <div class="bg-gray-100 px-6 py-4 border-b-2 border-gray-300">
              <h3
                class="text-base font-bold text-gray-900 uppercase tracking-wide"
              >
                Hasil Pencarian
              </h3>
            </div>

            <div class="p-6">
              <div class="flex flex-col md:flex-row items-start gap-6">
                <!-- Surat Image -->
                <div class="flex-shrink-0">
                  <div class="relative">
                    <img
                      :src="suratDefault"
                      alt="Surat Permohonan"
                      class="w-40 h-48 object-cover rounded-lg shadow-md border-2 border-gray-200"
                    />
                  </div>
                </div>

                <!-- Surat Info -->
                <div class="flex-1 space-y-4">
                  <div>
                    <h4 class="text-xl font-bold text-gray-900 mb-2">
                      {{ hasilSurat.nama_jenis_permohonan }}
                    </h4>
                    <p class="text-sm text-gray-600 leading-relaxed">
                      Surat permohonan ini dapat digunakan untuk keperluan
                      administrasi mahasiswa.
                    </p>
                  </div>

                  <!-- Detail Info -->
                  <div class="grid grid-cols-2 gap-4">
                    <div
                      class="bg-gray-50 border border-gray-200 rounded-lg p-4"
                    >
                      <div class="flex items-center gap-2 mb-2">
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
                            d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                          ></path>
                        </svg>
                        <span class="text-xs font-bold text-gray-700 uppercase"
                          >Waktu Proses</span
                        >
                      </div>
                      <p class="text-sm text-gray-900 font-semibold">
                        2-3 Hari Kerja
                      </p>
                    </div>

                    <div
                      class="bg-gray-50 border border-gray-200 rounded-lg p-4"
                    >
                      <div class="flex items-center gap-2 mb-2">
                        <svg
                          class="w-4 h-4 text-green-600"
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
                        <span class="text-xs font-bold text-gray-700 uppercase"
                          >Status</span
                        >
                      </div>
                      <p class="text-sm text-green-600 font-bold">TERSEDIA</p>
                    </div>
                  </div>

                  <!-- Action Button -->
                  <div class="pt-2">
                    <Button
                      @click="ajukanSurat"
                      class="w-full md:w-auto bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg shadow-sm border-0 font-bold uppercase text-sm tracking-wide"
                    >
                      <svg
                        class="w-4 h-4 mr-2"
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
                    </Button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Popular Services -->
          <div v-else class="space-y-4">
            <h3
              class="text-base font-bold text-gray-900 uppercase tracking-wide"
            >
              Layanan Populer
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div
                v-for="service in popularServices"
                :key="service.id"
                @click="selectPopularService(service)"
                class="bg-white border-2 border-gray-200 hover:border-blue-600 rounded-lg p-5 hover:shadow-md transition-all cursor-pointer group"
              >
                <div class="flex items-center gap-3">
                  <div
                    class="w-10 h-10 bg-blue-50 rounded-lg flex items-center justify-center flex-shrink-0"
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
                  <div class="flex-1">
                    <h4 class="font-bold text-sm text-gray-900 mb-1">
                      {{ service.nama }}
                    </h4>
                    <p class="text-xs text-gray-600">{{ service.deskripsi }}</p>
                  </div>
                  <svg
                    class="w-4 h-4 text-gray-400 group-hover:text-blue-600 transition-colors"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M9 5l7 7-7 7"
                    ></path>
                  </svg>
                </div>
              </div>
            </div>
          </div>

          <!-- Loading State -->
          <div v-if="loading" class="text-center py-12">
            <div
              class="w-12 h-12 mx-auto mb-4 border-4 border-gray-200 border-t-blue-600 rounded-full animate-spin"
            ></div>
            <p class="text-gray-600 font-medium">Memuat data...</p>
          </div>

          <!-- Error State -->
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
              <span class="font-semibold text-red-900">{{ error }}</span>
            </div>
          </Alert>
        </CardContent>
      </Card>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { apiClient } from "@/lib/axios";
import { getJenisPermohonan } from "@/services/jenisPermohonanService";
import type { JenisPermohonan } from "@/types/models/jenisPermohonan.types";
import suratDefault from "@/assets/suratPermohonan.png";

import { Card, CardContent } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
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

const baseUrl = import.meta.env.VITE_API_URL;

// Auth store and router
const { user } = useAuthStore();
const router = useRouter();

// State
const jenisPermohonanList = ref<JenisPermohonan[]>([]);
const selectedJenis = ref<number | null>(null);
const hasilSurat = ref<JenisPermohonan | null>(null);
const loading = ref(false);
const error = ref("");

// Time and date
const currentTime = ref("");
const currentDate = ref("");
const timeInterval = ref<NodeJS.Timeout | null>(null);

// Stats data from API
const totalPermohonan = ref(0);
const permohonanSelesai = ref(0);
const permohonanProses = ref(0);
const permohonanDitolak = ref(0);

// Recent history data from API
const recentHistory = ref<any[]>([]);

// Popular services
const popularServices = ref([
  {
    id: 1,
    nama: "Surat Keterangan Aktif",
    deskripsi: "Surat untuk keperluan administrasi",
  },
  {
    id: 2,
    nama: "Transkrip Nilai",
    deskripsi: "Transkrip nilai sementara",
  },
  {
    id: 3,
    nama: "Surat Pengantar PKL",
    deskripsi: "Surat untuk praktik kerja lapangan",
  },
]);

// Helper functions for history
const getStatusColor = (status: string) => {
  const normalizedStatus = status.toLowerCase();
  switch (normalizedStatus) {
    case "ditandatangani":
    case "disetujui":
      return "bg-green-50";
    case "pending":
      return "bg-amber-50";
    case "ditolak":
      return "bg-red-50";
    default:
      return "bg-gray-50";
  }
};

const getStatusIconColor = (status: string) => {
  const normalizedStatus = status.toLowerCase();
  switch (normalizedStatus) {
    case "ditandatangani":
    case "disetujui":
      return "text-green-600";
    case "pending":
      return "text-amber-600";
    case "ditolak":
      return "text-red-600";
    default:
      return "text-gray-600";
  }
};

const getStatusBadgeClass = (status: string) => {
  const normalizedStatus = status.toLowerCase();
  switch (normalizedStatus) {
    case "ditandatangani":
    case "disetujui":
      return "bg-green-600 text-white";
    case "pending":
      return "bg-amber-500 text-white";
    case "ditolak":
      return "bg-red-600 text-white";
    default:
      return "bg-gray-600 text-white";
  }
};

const getStatusLabel = (status: string) => {
  const normalizedStatus = status.toLowerCase();
  switch (normalizedStatus) {
    case "ditandatangani":
    case "disetujui":
      return "Selesai";
    case "pending":
      return "Pending";
    case "ditolak":
      return "Ditolak";
    default:
      return "Unknown";
  }
};

const formatDate = (dateStr: string) => {
  const date = new Date(dateStr);
  return date.toLocaleDateString("id-ID", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
};

// Computed properties
const getGreeting = () => {
  const hour = new Date().getHours();
  if (hour < 12) return "Selamat Pagi";
  if (hour < 15) return "Selamat Siang";
  if (hour < 18) return "Selamat Sore";
  return "Selamat Malam";
};

// Update time
const updateTime = () => {
  const now = new Date();
  currentTime.value = now.toLocaleTimeString("id-ID");
  currentDate.value = now.toLocaleDateString("id-ID", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  });
};

const selectPopularService = (service: any) => {
  const foundService = jenisPermohonanList.value.find((item) =>
    item.nama_jenis_permohonan
      .toLowerCase()
      .includes(service.nama.toLowerCase())
  );

  if (foundService) {
    selectedJenis.value = foundService.id;
    hasilSurat.value = foundService;
  }
};

// Lifecycle hooks
onMounted(async () => {
  updateTime();
  timeInterval.value = setInterval(updateTime, 1000);
  await loadData();
  await loadStats();
  await loadRecentHistory();
});

onUnmounted(() => {
  if (timeInterval.value) {
    clearInterval(timeInterval.value);
  }
});

// Methods
async function loadData() {
  try {
    loading.value = true;
    error.value = "";

    jenisPermohonanList.value = await getJenisPermohonan();
    console.log("✅ Data jenis permohonan:", jenisPermohonanList.value);
  } catch (error: any) {
    console.error("⚠️ Gagal fetch jenis permohonan:", error);
    error.value = "Gagal memuat data. Silakan refresh halaman.";
  } finally {
    loading.value = false;
  }
}

async function loadStats() {
  try {
    // Fetch counts
    const countsRes = await apiClient.get(`/history/counts`);
    const counts = countsRes.data.data || {};

    permohonanProses.value = counts.pending || 0;
    permohonanDitolak.value = counts.ditolak || 0;
    permohonanSelesai.value = counts.ditandatangani || 0;

    // Fetch total
    const totalRes = await apiClient.get(`/history/total`);
    totalPermohonan.value = totalRes.data.data?.total || 0;
  } catch (error: any) {
    console.error("⚠️ Gagal fetch stats:", error);
  }
}

async function loadRecentHistory() {
  try {
    // Fetch all history and take only the latest 3
    const res = await apiClient.get(`/history/all`);
    const allHistory = res.data.data || [];

    // Sort by created_at desc and take first 3
    recentHistory.value = allHistory
      .sort(
        (a: any, b: any) =>
          new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
      )
      .slice(0, 3);
  } catch (error: any) {
    console.error("⚠️ Gagal fetch recent history:", error);
  }
}

function cariSurat() {
  if (!selectedJenis.value) {
    error.value = "Silakan pilih jenis surat terlebih dahulu!";
    return;
  }

  const surat = jenisPermohonanList.value.find(
    (item) => item.id === selectedJenis.value
  );

  if (surat) {
    hasilSurat.value = surat;
    error.value = "";
  } else {
    error.value = "Surat tidak ditemukan!";
  }
}

function reloadSurat() {
  selectedJenis.value = null;
  hasilSurat.value = null;
  error.value = "";
  loadData();
}

function ajukanSurat() {
  if (!hasilSurat.value) {
    error.value = "Pilih surat yang akan diajukan terlebih dahulu!";
    return;
  }

  const targetPath = hasilSurat.value.route_path;
  if (!targetPath) {
    error.value = "⚠️ Halaman permohonan untuk surat ini belum tersedia!";
    return;
  }

  console.log("📩 Ajukan surat untuk route:", targetPath);

  const isRegistered = router.getRoutes().some((r) => r.path === targetPath);

  if (isRegistered) {
    router.push(targetPath);
  } else {
    router.push({
      name: "PermohonanForm",
      params: { jenisId: hasilSurat.value.id },
    });
  }
}
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
