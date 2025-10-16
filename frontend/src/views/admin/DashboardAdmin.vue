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
                  class="w-12 h-12 bg-gradient-to-br from-blue-600 to-blue-700 rounded-lg flex items-center justify-center"
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
                    Admin Panel - Sistem Informasi Akademik FTI UKSW
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
        <!-- Total Permohonan -->
        <Card
          class="border-2 border-blue-100 shadow-sm bg-white hover:shadow-md transition-shadow"
        >
          <CardContent class="p-5">
            <div class="flex items-start justify-between">
              <div class="flex-1">
                <p
                  class="text-xs font-semibold text-blue-600 uppercase tracking-wide mb-2"
                >
                  Total Permohonan
                </p>
                <p class="text-3xl font-bold text-gray-900">
                  {{ totalPermohonan }}
                </p>
                <p class="text-xs text-gray-500 mt-1">Semua waktu</p>
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

        <!-- Permohonan Pending -->
        <Card
          class="border-2 border-amber-100 shadow-sm bg-white hover:shadow-md transition-shadow"
        >
          <CardContent class="p-5">
            <div class="flex items-start justify-between">
              <div class="flex-1">
                <p
                  class="text-xs font-semibold text-amber-600 uppercase tracking-wide mb-2"
                >
                  Menunggu Verifikasi
                </p>
                <p class="text-3xl font-bold text-gray-900">
                  {{ permohonanPending }}
                </p>
                <p class="text-xs text-gray-500 mt-1">Perlu tindakan</p>
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

        <!-- Total Mahasiswa -->
        <Card
          class="border-2 border-green-100 shadow-sm bg-white hover:shadow-md transition-shadow"
        >
          <CardContent class="p-5">
            <div class="flex items-start justify-between">
              <div class="flex-1">
                <p
                  class="text-xs font-semibold text-green-600 uppercase tracking-wide mb-2"
                >
                  Total Mahasiswa
                </p>
                <p class="text-3xl font-bold text-gray-900">
                  {{ totalMahasiswa }}
                </p>
                <p class="text-xs text-gray-500 mt-1">Aktif</p>
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
                    d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
                  ></path>
                </svg>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Total Dosen -->
        <Card
          class="border-2 border-purple-100 shadow-sm bg-white hover:shadow-md transition-shadow"
        >
          <CardContent class="p-5">
            <div class="flex items-start justify-between">
              <div class="flex-1">
                <p
                  class="text-xs font-semibold text-purple-600 uppercase tracking-wide mb-2"
                >
                  Total Dosen
                </p>
                <p class="text-3xl font-bold text-gray-900">
                  {{ totalDosen }}
                </p>
                <p class="text-xs text-gray-500 mt-1">Aktif</p>
              </div>
              <div class="p-3 bg-purple-50 rounded-lg">
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
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                  ></path>
                </svg>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <!-- Recent Activity / Permohonan Terbaru -->
      <!-- <Card class="shadow-sm border border-gray-200 bg-white overflow-hidden">
        <div
          class="bg-gradient-to-r from-blue-600 to-blue-700 text-white px-6 py-4"
        >
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
              Permohonan Terbaru
            </h2>
            <a
              href="/admin/list-permohonan"
              class="text-white hover:bg-blue-500 px-3 py-2 rounded-md text-sm font-semibold transition-colors flex items-center gap-1"
            >
              Lihat Semua
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
                  d="M9 5l7 7-7 7"
                ></path>
              </svg>
            </a>
          </div>
        </div>

        <CardContent class="p-6">

          <div class="space-y-3">
            <div
              v-for="item in recentPermohonan"
              :key="item.id"
              class="flex items-center gap-4 p-4 bg-gray-50 border border-gray-200 rounded-lg hover:bg-white hover:border-blue-200 hover:shadow-sm transition-all group"
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
                <h4
                  class="text-sm font-bold text-gray-900 truncate group-hover:text-blue-600 transition-colors"
                >
                  {{ item.judul || "Permohonan" }}
                </h4>
                <p class="text-xs text-gray-600 mt-1">
                  {{ formatDate(item.created_at) }} •
                  {{ item.mahasiswa?.user?.nama || "-" }} •
                  {{ item.jenis_permohonan?.nama_jenis_permohonan || "-" }}
                </p>
              </div>
              <span
                class="px-3 py-1 rounded-full text-xs font-bold uppercase border"
                :class="getStatusBadgeClass(item.status_permohonan)"
              >
                {{ getStatusLabel(item.status_permohonan) }}
              </span>
            </div>
          </div>


          <div v-if="recentPermohonan.length === 0" class="text-center py-12">
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
            <p class="text-gray-600 font-medium">Belum ada permohonan</p>
            <p class="text-sm text-gray-500 mt-1">
              Permohonan baru akan muncul di sini
            </p>
          </div>
        </CardContent>
      </Card> -->

      <!-- Quick Access Menu -->
      <Card class="shadow-sm border border-gray-200 bg-white overflow-hidden">
        <div
          class="bg-gradient-to-r from-gray-800 to-gray-900 text-white px-6 py-4"
        >
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
                d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
              ></path>
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
              ></path>
            </svg>
            Quick Access
          </h2>
        </div>

        <CardContent class="p-6">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <!-- Kelola Permohonan -->
            <a
              href="/admin/list-permohonan"
              class="group p-6 bg-white border-2 border-yellow-100 rounded-lg hover:border-yellow-300 hover:shadow-md transition-all cursor-pointer"
            >
              <div class="flex items-center gap-4">
                <div
                  class="w-12 h-12 bg-yellow-50 rounded-lg flex items-center justify-center flex-shrink-0 group-hover:bg-yellow-100 transition-colors"
                >
                  <svg
                    class="w-6 h-6 text-yellow-600"
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
                  <h4
                    class="font-bold text-gray-900 mb-1 group-hover:text-yellow-600 transition-colors"
                  >
                    Detail Permohonan
                  </h4>
                  <p class="text-sm text-gray-600">
                    Lihat dan kelola semua permohonan surat
                  </p>
                </div>
                <svg
                  class="w-5 h-5 text-yellow-400 group-hover:text-yellow-600 transition-colors"
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
            </a>

            <!-- Kelola User -->
            <a
              href="/admin/users"
              class="group p-6 bg-white border-2 border-slate-300 rounded-lg hover:border-slate-400 hover:shadow-md transition-all cursor-pointer"
            >
              <div class="flex items-center gap-4">
                <div
                  class="w-12 h-12 bg-slate-50 rounded-lg flex items-center justify-center flex-shrink-0 group-hover:bg-slate-100 transition-colors"
                >
                  <svg
                    class="w-6 h-6 text-slate-600"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
                    ></path>
                  </svg>
                </div>
                <div class="flex-1">
                  <h4
                    class="font-bold text-gray-900 mb-1 group-hover:text-slate-600 transition-colors"
                  >
                    Kelola User
                  </h4>
                  <p class="text-sm text-gray-600">
                    Manajemen data mahasiswa dan dosen
                  </p>
                </div>
                <svg
                  class="w-5 h-5 text-gray-400 group-hover:text-slate-600 transition-colors"
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
            </a>

            <!-- Laporan -->
            <a
              href="/admin/history"
              class="group p-6 bg-white border-2 border-purple-100 rounded-lg hover:border-purple-300 hover:shadow-md transition-all cursor-pointer"
            >
              <div class="flex items-center gap-4">
                <div
                  class="w-12 h-12 bg-purple-50 rounded-lg flex items-center justify-center flex-shrink-0 group-hover:bg-purple-100 transition-colors"
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
                      d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                    ></path>
                  </svg>
                </div>
                <div class="flex-1">
                  <h4
                    class="font-bold text-gray-900 mb-1 group-hover:text-purple-600 transition-colors"
                  >
                    Laporan
                  </h4>
                  <p class="text-sm text-gray-600">
                    Generate laporan dan analytics
                  </p>
                </div>
                <svg
                  class="w-5 h-5 text-gray-400 group-hover:text-purple-600 transition-colors"
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
            </a>
          </div>
        </CardContent>
      </Card>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import { useAuthStore } from "@/stores/auth";
import { apiClient } from "@/lib/axios";
import { Card, CardContent } from "@/components/ui/card";

// Auth store
const { user } = useAuthStore();

// State
const currentTime = ref("");
const currentDate = ref("");
const timeInterval = ref<number | null>(null);

// Stats data from API
const totalPermohonan = ref(0);
const permohonanPending = ref(0);
const totalMahasiswa = ref(0);
const totalDosen = ref(0);

// Recent permohonan data from API
// const recentPermohonan = ref<any[]>([]);

// // Helper functions for status
// const getStatusColor = (status: string) => {
//   const normalizedStatus = status.toLowerCase();
//   switch (normalizedStatus) {
//     case "ditandatangani":
//     case "disetujui":
//       return "bg-green-50";
//     case "pending":
//       return "bg-amber-50";
//     case "ditolak":
//       return "bg-red-50";
//     default:
//       return "bg-gray-50";
//   }
// };

// const getStatusIconColor = (status: string) => {
//   const normalizedStatus = status.toLowerCase();
//   switch (normalizedStatus) {
//     case "ditandatangani":
//     case "disetujui":
//       return "text-green-600";
//     case "pending":
//       return "text-amber-600";
//     case "ditolak":
//       return "text-red-600";
//     default:
//       return "text-gray-600";
//   }
// };

// const getStatusBadgeClass = (status: string) => {
//   const normalizedStatus = status.toLowerCase();
//   switch (normalizedStatus) {
//     case "ditandatangani":
//     case "disetujui":
//       return "bg-green-600 text-white";
//     case "pending":
//       return "bg-amber-500 text-white";
//     case "ditolak":
//       return "bg-red-600 text-white";
//     default:
//       return "bg-gray-600 text-white";
//   }
// };

// const getStatusLabel = (status: string) => {
//   const normalizedStatus = status.toLowerCase();
//   switch (normalizedStatus) {
//     case "ditandatangani":
//     case "disetujui":
//       return "Selesai";
//     case "pending":
//       return "Pending";
//     case "ditolak":
//       return "Ditolak";
//     default:
//       return "Unknown";
//   }
// };

// const formatDate = (dateStr: string) => {
//   const date = new Date(dateStr);
//   return date.toLocaleDateString("id-ID", {
//     day: "2-digit",
//     month: "short",
//     year: "numeric",
//   });
// };

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

// Lifecycle hooks
onMounted(async () => {
  updateTime();
  timeInterval.value = setInterval(updateTime, 1000);
  await loadStats();
  // await loadRecentPermohonan();
});

onUnmounted(() => {
  if (timeInterval.value) {
    clearInterval(timeInterval.value);
  }
});

// Methods
async function loadStats() {
  try {
    // Fetch admin stats
    const statsRes = await apiClient.get(`/admin/stats`);
    const stats = statsRes.data.data || {};

    totalPermohonan.value = stats.total || 0;
    permohonanPending.value = stats.pending || 0;
    totalMahasiswa.value = stats.total_mahasiswa || 0;
    totalDosen.value = stats.total_dosen || 0;
  } catch (error: any) {
    console.error("⚠️ Gagal fetch admin stats:", error);
    // Fallback dummy data untuk development
    // totalPermohonan.value = 125;
    // permohonanPending.value = 8;
    // totalMahasiswa.value = 850;
    // totalDosen.value = 45;
  }
}

// async function loadRecentPermohonan() {
//   try {
//     // Fetch recent permohonan for admin (all users)
//     const res = await apiClient.get(`/admin/permohonan/recent`);
//     const allPermohonan = res.data.data || [];

//     // Sort by created_at desc and take first 5
//     recentPermohonan.value = allPermohonan
//       .sort(
//         (a: any, b: any) =>
//           new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
//       )
//       .slice(0, 5);
//   } catch (error: any) {
//     console.error("⚠️ Gagal fetch recent permohonan:", error);
//     // Fallback empty array
//     recentPermohonan.value = [];
//   }
// }
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
