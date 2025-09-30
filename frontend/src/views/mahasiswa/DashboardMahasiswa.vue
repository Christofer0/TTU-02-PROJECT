<template>
  <div
    class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-blue-100 p-6 relative"
  >
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-3">
      <div
        class="absolute top-20 left-20 w-96 h-96 bg-blue-300 rounded-full mix-blend-multiply filter blur-xl animate-pulse"
      ></div>
      <div
        class="absolute bottom-20 right-20 w-96 h-96 bg-blue-400 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-1000"
      ></div>
      <div
        class="absolute top-1/2 left-1/3 w-64 h-64 bg-blue-200 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-500"
      ></div>
    </div>

    <div class="max-w-7xl mx-auto space-y-8 relative z-10">
      <!-- Welcome Header -->
      <Card
        class="border-0 shadow-lg shadow-blue-100 bg-gradient-to-r from-blue-500 to-blue-600 text-white overflow-hidden relative"
      >
        <!-- Decorative elements -->
        <div
          class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full -translate-y-16 translate-x-16"
        ></div>
        <div
          class="absolute bottom-0 left-0 w-20 h-20 bg-white/5 rounded-full translate-y-10 -translate-x-10"
        ></div>

        <CardContent class="p-8 relative">
          <div class="flex items-center justify-between">
            <div class="space-y-2">
              <div class="flex items-center gap-3">
                <div
                  class="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm"
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
                      d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
                    ></path>
                  </svg>
                </div>
                <div>
                  <h1 class="text-2xl font-bold">
                    {{ getGreeting() }}, {{ user?.nama }}!
                  </h1>
                  <p class="text-blue-100">
                    Selamat datang kembali di sistem informasi FTI UKSW
                  </p>
                </div>
              </div>
            </div>

            <!-- Current Time -->
            <div class="text-right">
              <p class="text-blue-100 text-sm">{{ currentDate }}</p>
              <p class="text-white text-lg font-semibold">{{ currentTime }}</p>
            </div>
          </div>
        </CardContent>
      </Card>

      <!-- Quick Stats -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
        <Card
          class="border-0 shadow-lg shadow-blue-50 bg-white/80 backdrop-blur-sm"
        >
          <CardContent class="p-6 text-center">
            <div
              class="w-12 h-12 mx-auto mb-3 bg-gradient-to-br from-blue-400 to-blue-500 rounded-xl flex items-center justify-center shadow-lg"
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
            <p class="text-2xl font-bold text-gray-800">
              {{ totalPermohonan }}
            </p>
            <p class="text-sm text-gray-600">Total Permohonan</p>
          </CardContent>
        </Card>

        <Card
          class="border-0 shadow-lg shadow-emerald-50 bg-white/80 backdrop-blur-sm"
        >
          <CardContent class="p-6 text-center">
            <div
              class="w-12 h-12 mx-auto mb-3 bg-gradient-to-br from-emerald-400 to-emerald-500 rounded-xl flex items-center justify-center shadow-lg"
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
                  d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                ></path>
              </svg>
            </div>
            <p class="text-2xl font-bold text-gray-800">
              {{ permohonanSelesai }}
            </p>
            <p class="text-sm text-gray-600">Permohonan Selesai</p>
          </CardContent>
        </Card>

        <Card
          class="border-0 shadow-lg shadow-amber-50 bg-white/80 backdrop-blur-sm"
        >
          <CardContent class="p-6 text-center">
            <div
              class="w-12 h-12 mx-auto mb-3 bg-gradient-to-br from-amber-400 to-amber-500 rounded-xl flex items-center justify-center shadow-lg"
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
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                ></path>
              </svg>
            </div>
            <p class="text-2xl font-bold text-gray-800">
              {{ permohonanProses }}
            </p>
            <p class="text-sm text-gray-600">Sedang Diproses</p>
          </CardContent>
        </Card>

        <Card
          class="border-0 shadow-lg shadow-red-50 bg-white/80 backdrop-blur-sm"
        >
          <CardContent class="p-6 text-center">
            <div
              class="w-12 h-12 mx-auto mb-3 bg-gradient-to-br from-red-400 to-red-500 rounded-xl flex items-center justify-center shadow-lg"
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
                  d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.34 16.5c-.77.833.192 2.5 1.732 2.5z"
                ></path>
              </svg>
            </div>
            <p class="text-2xl font-bold text-gray-800">
              {{ permohonanDitolak }}
            </p>
            <p class="text-sm text-gray-600">Permohonan Ditolak</p>
          </CardContent>
        </Card>
      </div>

      <!-- Menu Histori -->
      <Card
        class="border-0 shadow-xl shadow-blue-100 bg-white/90 backdrop-blur-sm overflow-hidden"
      >
        <div class="bg-gradient-to-r from-blue-600 to-blue-700 text-white p-6">
          <h2 class="text-xl font-bold flex items-center gap-3">
            <svg
              class="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
              ></path>
            </svg>
            Riwayat Permohonan Terbaru
          </h2>
          <p class="text-blue-100 mt-1">Lihat status permohonan surat Anda</p>
        </div>

        <CardContent class="p-6">
          <div
            v-if="recentPermohonan.length > 0"
            class="grid grid-cols-1 md:grid-cols-3 gap-6"
          >
            <div
              v-for="item in recentPermohonan"
              :key="item.id"
              class="bg-gradient-to-br from-gray-50 to-gray-100 rounded-xl p-6 border border-gray-200 hover:shadow-lg transition-all duration-300 hover:scale-[1.02] cursor-pointer"
              @click="viewDetail(item)"
            >
              <div class="flex items-start justify-between mb-4">
                <div class="flex-1">
                  <h3 class="font-semibold text-gray-800 mb-1">
                    {{ item.jenis_permohonan }}
                  </h3>
                  <p class="text-sm text-gray-600">
                    {{ formatDate(item.tanggal) }}
                  </p>
                </div>
                <div
                  class="px-3 py-1 rounded-full text-xs font-medium"
                  :class="getStatusClass(item.status)"
                >
                  {{ item.status }}
                </div>
              </div>

              <div class="flex items-center justify-between">
                <div class="flex items-center gap-2 text-sm text-gray-600">
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
                      d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                    ></path>
                  </svg>
                  ID: #{{ item.id }}
                </div>
                <svg
                  class="w-4 h-4 text-blue-500"
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

          <div v-else class="text-center py-12">
            <div
              class="w-16 h-16 mx-auto mb-4 bg-gray-100 rounded-full flex items-center justify-center"
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
                  d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
                ></path>
              </svg>
            </div>
            <p class="text-gray-500 font-medium mb-2">Belum ada permohonan</p>
            <p class="text-sm text-gray-400">
              Mulai ajukan permohonan surat Anda di bawah ini
            </p>
          </div>

          <div class="mt-6 text-center">
            <Button
              @click="router.push('/mahasiswa/riwayat')"
              variant="outline"
              class="border-2 border-blue-200 text-blue-600 hover:bg-blue-50 rounded-xl px-6 py-2"
            >
              Lihat Semua Riwayat
              <svg
                class="w-4 h-4 ml-2"
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
        </CardContent>
      </Card>

      <!-- Menu Layanan Surat -->
      <Card
        class="border-0 shadow-xl shadow-blue-100 bg-white/90 backdrop-blur-sm overflow-hidden"
      >
        <div class="bg-gradient-to-r from-blue-600 to-blue-700 text-white p-6">
          <h2 class="text-xl font-bold flex items-center gap-3">
            <svg
              class="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
              ></path>
            </svg>
            Layanan Permohonan Surat
          </h2>
          <p class="text-blue-100 mt-1">
            Pilih jenis surat yang ingin Anda ajukan
          </p>
        </div>

        <CardContent class="p-6 space-y-6">
          <!-- Search and Filter Section -->
          <div
            class="bg-gradient-to-r from-gray-50 to-gray-100 rounded-xl p-6 border border-gray-200"
          >
            <Label class="text-sm font-semibold text-gray-700 mb-4 block">
              🔍 Cari Jenis Surat
            </Label>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Select Dropdown dengan styling yang lebih baik -->
              <div class="md:col-span-2">
                <Select v-model="selectedJenis">
                  <SelectTrigger
                    class="h-12 rounded-xl border-2 border-gray-200 focus:border-blue-400 bg-white/70 backdrop-blur-sm"
                  >
                    <SelectValue
                      placeholder="Pilih jenis surat yang dibutuhkan..."
                    />
                  </SelectTrigger>
                  <SelectContent class="rounded-xl border-0 shadow-xl">
                    <SelectGroup>
                      <SelectItem
                        v-for="item in jenisPermohonanList"
                        :key="item.id"
                        :value="item.id"
                        class="focus:bg-blue-50"
                      >
                        <div class="flex items-center gap-3">
                          <div class="w-2 h-2 bg-blue-500 rounded-full"></div>
                          {{ item.nama_jenis_permohonan }}
                        </div>
                      </SelectItem>
                    </SelectGroup>
                  </SelectContent>
                </Select>
              </div>

              <!-- Action Buttons -->
              <div class="flex gap-2">
                <Button
                  @click="cariSurat"
                  class="flex-1 h-12 bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white rounded-xl shadow-lg shadow-blue-200 border-0 transition-all duration-300 hover:scale-[1.02]"
                  :disabled="!selectedJenis"
                >
                  <svg
                    class="w-5 h-5 mr-2"
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
                  class="h-12 border-2 border-gray-200 hover:border-gray-300 rounded-xl px-4"
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
            class="bg-white rounded-2xl border border-gray-200 shadow-lg overflow-hidden"
          >
            <div class="bg-gradient-to-r from-blue-50 to-blue-100 p-6 border-b">
              <h3 class="text-lg font-semibold text-gray-800 mb-2">
                Hasil Pencarian
              </h3>
              <p class="text-sm text-gray-600">
                Informasi detail surat yang Anda pilih
              </p>
            </div>

            <div class="p-8">
              <div class="flex flex-col md:flex-row items-center gap-8">
                <!-- Surat Image -->
                <div class="flex-shrink-0">
                  <div class="relative">
                    <img
                      :src="suratDefault"
                      alt="Surat Permohonan"
                      class="w-48 h-56 object-cover rounded-2xl shadow-xl border-4 border-white transition-transform duration-300 hover:scale-105"
                    />
                    <div
                      class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent rounded-2xl"
                    ></div>
                  </div>
                </div>

                <!-- Surat Info -->
                <div class="flex-1 space-y-4">
                  <div>
                    <h4 class="text-2xl font-bold text-gray-800 mb-2">
                      {{ hasilSurat.nama_jenis_permohonan }}
                    </h4>
                    <p class="text-gray-600 leading-relaxed">
                      {{
                        "Surat permohonan ini dapat digunakan untuk keperluan administrasi mahasiswa."
                      }}
                    </p>
                  </div>

                  <!-- Detail Info -->
                  <div class="grid grid-cols-2 gap-4">
                    <div class="bg-gray-50 rounded-lg p-4">
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
                        <span class="text-sm font-medium text-gray-700"
                          >Waktu Proses</span
                        >
                      </div>
                      <p class="text-sm text-gray-600">
                        {{ "2-3 Hari Kerja" }}
                      </p>
                    </div>

                    <div class="bg-gray-50 rounded-lg p-4">
                      <div class="flex items-center gap-2 mb-2">
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
                        <span class="text-sm font-medium text-gray-700"
                          >Status</span
                        >
                      </div>
                      <p class="text-sm text-emerald-600 font-medium">
                        Tersedia
                      </p>
                    </div>
                  </div>

                  <!-- Action Button -->
                  <div class="pt-4">
                    <Button
                      @click="ajukanSurat"
                      class="w-full md:w-auto bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white px-8 py-3 rounded-xl shadow-lg shadow-blue-200 border-0 transition-all duration-300 hover:scale-[1.02] font-semibold"
                    >
                      <svg
                        class="w-5 h-5 mr-2"
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
            <h3 class="text-lg font-semibold text-gray-800">Layanan Populer</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div
                v-for="service in popularServices"
                :key="service.id"
                @click="selectPopularService(service)"
                class="bg-gradient-to-br from-white to-gray-50 rounded-xl p-6 border border-gray-200 hover:shadow-lg transition-all duration-300 hover:scale-[1.02] cursor-pointer group"
              >
                <div class="flex items-center gap-4">
                  <div
                    class="w-12 h-12 bg-gradient-to-br from-blue-100 to-blue-200 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform"
                  >
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
                  <div class="flex-1">
                    <h4 class="font-semibold text-gray-800 mb-1">
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
              class="w-12 h-12 mx-auto mb-4 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin"
            ></div>
            <p class="text-gray-600">Memuat data...</p>
          </div>

          <!-- Error State -->
          <Alert
            v-if="error"
            variant="destructive"
            class="mt-4 border-red-200 bg-red-50 rounded-xl"
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
        </CardContent>
      </Card>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
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

// Mock data untuk statistik (dalam implementasi nyata, ambil dari API)
const totalPermohonan = ref(12);
const permohonanSelesai = ref(8);
const permohonanProses = ref(3);
const permohonanDitolak = ref(1);

// Mock data untuk riwayat terbaru
const recentPermohonan = ref([
  {
    id: 1,
    jenis_permohonan: "Surat Keterangan Aktif Kuliah",
    status: "Selesai",
    tanggal: "2024-01-15",
  },
  {
    id: 2,
    jenis_permohonan: "Transkrip Nilai Sementara",
    status: "Diproses",
    tanggal: "2024-01-18",
  },
  {
    id: 3,
    jenis_permohonan: "Surat Pengantar PKL",
    status: "Ditolak",
    tanggal: "2024-01-20",
  },
]);

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

// Utility functions
const formatDate = (dateString: string) => {
  const date = new Date(dateString);
  return date.toLocaleDateString("id-ID", {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
};

const getStatusClass = (status: string) => {
  switch (status.toLowerCase()) {
    case "selesai":
      return "bg-emerald-100 text-emerald-800";
    case "diproses":
      return "bg-amber-100 text-amber-800";
    case "ditolak":
      return "bg-red-100 text-red-800";
    default:
      return "bg-gray-100 text-gray-800";
  }
};

const viewDetail = (item: any) => {
  // Navigate to detail page or show modal
  router.push(`/mahasiswa/permohonan/${item.id}`);
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

    // Load additional data (statistics, recent requests, etc.)
    // In a real implementation, these would be separate API calls
  } catch (error: any) {
    console.error("⚠️ Gagal fetch jenis permohonan:", error);
    error.value = "Gagal memuat data. Silakan refresh halaman.";
  } finally {
    loading.value = false;
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

  // Check if route is registered in Vue Router
  const isRegistered = router.getRoutes().some((r) => r.path === targetPath);

  if (isRegistered) {
    router.push(targetPath);
  } else {
    // Fallback route jika route spesifik belum ada
    router.push({
      name: "PermohonanForm",
      params: { jenisId: hasilSurat.value.id },
    });
  }
}
</script>
