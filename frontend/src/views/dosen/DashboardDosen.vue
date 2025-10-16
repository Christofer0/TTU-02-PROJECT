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
        <!-- Kelola User -->
        <Card
          class="cursor-pointer transition hover:shadow-md border border-gray-200 bg-white"
          @click="router.push('/dosen/history')"
        >
          <CardContent class="p-6 flex items-center justify-between">
            <div>
              <h2 class="text-xl font-bold text-gray-900">Lihat History</h2>
              <p class="text-sm text-gray-600 mt-1">
                Apa saja yang sudah pernah saya lakukan 🤔
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
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import { apiClient } from "@/lib/axios";
import { Card, CardContent } from "@/components/ui/card";

const router = useRouter();
const { user } = useAuthStore();

const currentTime = ref("");
const currentDate = ref("");
const interval = ref<number | null>(null);

const totalPending = ref(0);
const totalDitandatangani = ref(0);
const totalDitolak = ref(0);

const permohonanList = ref<any[]>([]);

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
</script>
