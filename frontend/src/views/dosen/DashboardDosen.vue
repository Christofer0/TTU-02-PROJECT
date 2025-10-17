<template>
  <div class="min-h-screen bg-gray-50 p-6">
    <div class="max-w-7xl mx-auto space-y-6">
      <!-- Header -->
      <Card class="border-l-4 border-green-600 shadow-sm bg-white">
        <CardContent class="p-6 flex justify-between items-center">
          <div>
            <h1 class="text-2xl font-bold text-gray-900">
              {{ getGreeting() }}, {{ user?.nama }}
            </h1>
            <p class="text-sm text-gray-600 font-medium">
              Dashboard Dosen • Sistem Informasi Akademik FTI UKSW
            </p>
          </div>
          <div class="text-right">
            <p class="text-xs text-gray-500 uppercase font-semibold">
              {{ currentDate }}
            </p>
            <p class="text-xl font-bold text-gray-900">{{ currentTime }}</p>
          </div>
        </CardContent>
      </Card>

      <!-- 🧭 Menu Navigasi Cepat -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Kelola Permohonan -->
        <Card
          class="cursor-pointer transition hover:shadow-md border border-gray-200 bg-white"
          @click="router.push('/dosen/list-permohonan-TTD')"
        >
          <CardContent class="p-6 flex items-center justify-between">
            <div>
              <h2 class="text-xl font-bold text-gray-900">Kelola Permohonan</h2>
              <p class="text-sm text-gray-600 mt-1">
                Tinjau, setujui, atau tolak permohonan surat mahasiswa.
              </p>
            </div>
            <div class="p-4 bg-blue-50 rounded-lg">
              <svg
                class="w-10 h-10 text-blue-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414A1 1 0 0119 9V19a2 2 0 01-2 2z"
                />
              </svg>
            </div>
          </CardContent>
        </Card>

        <!-- Lihat History -->
        <Card
          class="cursor-pointer transition hover:shadow-md border border-gray-200 bg-white"
          @click="router.push('/dosen/history')"
        >
          <CardContent class="p-6 flex items-center justify-between">
            <div>
              <h2 class="text-xl font-bold text-gray-900">Lihat History</h2>
              <p class="text-sm text-gray-600 mt-1">
                Aktivitas apa saja yang sudah saya lakukan 🤔
              </p>
            </div>
            <div class="p-4 bg-slate-50 rounded-lg">
              <svg
                class="w-10 h-10 text-slate-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
            </div>
          </CardContent>
        </Card>
      </div>

      <!-- 🕒 Aktivitas Terbaru -->
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
              @click="router.push('/dosen/history')"
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
          <div v-if="recentHistory.length" class="space-y-3">
            <div
              v-for="item in recentHistory.slice(0, 5)"
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
                  {{ item.mahasiswa?.user?.nama || "-" }}
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
          <div v-else class="text-center text-gray-500 text-sm py-4">
            Tidak ada aktivitas terbaru.
          </div>
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
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const router = useRouter();
const { user } = useAuthStore();

const currentTime = ref("");
const currentDate = ref("");
const interval = ref<number | null>(null);

const totalPending = ref(0);
const totalDitandatangani = ref(0);
const totalDitolak = ref(0);
const permohonanList = ref<any[]>([]);
const recentHistory = ref<any[]>([]);

const getGreeting = () => {
  const h = new Date().getHours();
  if (h < 12) return "Selamat Pagi";
  if (h < 15) return "Selamat Siang";
  if (h < 18) return "Selamat Sore";
  return "Selamat Malam";
};

const updateTime = () => {
  const now = new Date();
  currentTime.value = now.toLocaleTimeString("id-ID");
  currentDate.value = now.toLocaleDateString("id-ID", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
  });
};

onMounted(async () => {
  updateTime();
  interval.value = setInterval(updateTime, 1000);
  await loadStats();
  await loadPermohonan();
  await loadRecentHistory();
});

onUnmounted(() => {
  if (interval.value) clearInterval(interval.value);
});

async function loadStats() {
  try {
    const res = await apiClient.get("/dosen/stats");
    const data = res.data.data || {};
    totalPending.value = data.pending || 0;
    totalDitandatangani.value = data.ditandatangani || 0;
    totalDitolak.value = data.ditolak || 0;
  } catch (err) {
    console.error("Gagal memuat statistik:", err);
  }
}

async function loadPermohonan() {
  try {
    const res = await apiClient.get("/dosen/pending");
    permohonanList.value = res.data.data || [];
  } catch (err) {
    console.error("Gagal memuat permohonan:", err);
  }
}

async function loadRecentHistory() {
  try {
    const res = await apiClient.get("/dosen/recent-history");
    recentHistory.value = res.data.data || [];
  } catch (err) {
    console.error("Gagal memuat aktivitas terbaru:", err);
  }
}

function formatDate(dateStr: string) {
  return new Date(dateStr).toLocaleString("id-ID", {
    day: "numeric",
    month: "long",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function getStatusColor(status: string) {
  if (status === "disetujui" || status === "ditandatangani")
    return "bg-green-100";
  if (status === "pending") return "bg-yellow-100";
  return "bg-red-100";
}

function getStatusIconColor(status: string) {
  if (status === "disetujui" || status === "ditandatangani")
    return "text-green-600";
  if (status === "pending") return "text-yellow-600";
  return "text-red-600";
}

function getStatusBadgeClass(status: string) {
  if (status === "disetujui" || status === "ditandatangani")
    return "bg-green-100 text-green-700";
  if (status === "pending") return "bg-yellow-100 text-yellow-700";
  return "bg-red-100 text-red-700";
}

function getStatusLabel(status: string) {
  const labels: Record<string, string> = {
    pending: "Menunggu",
    disetujui: "Disetujui",
    ditandatangani: "Ditandatangani",
    ditolak: "Ditolak",
  };
  return labels[status] || "Tidak Diketahui";
}
</script>
