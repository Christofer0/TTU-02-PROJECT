<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { apiClient } from "@/lib/axios";
import {
  Check,
  X,
  Clock,
  FileText,
  TrendingUp,
  XCircle,
  CheckCircle,
  FileCheck,
} from "lucide-vue-next";

const baseUrl = import.meta.env.VITE_API_URL;

// states
const selectedStatus = ref("ditandatangani");
const historyList = ref<any[]>([]);
const counts = ref({
  pending: 0,
  ditolak: 0,
  disetujui: 0,
  ditandatangani: 0,
});
const total = ref(0);
const loading = ref(false);
const error = ref<string | null>(null);

// visible cards (hide 'disetujui')
const visibleCounts = computed(() => {
  const { disetujui, ...rest } = counts.value;
  return { ...rest, total: total.value };
});

// Card config untuk styling
const cardConfig: Record<
  string,
  { icon: any; gradient: string; iconColor: string; bgColor: string }
> = {
  pending: {
    icon: Clock,
    gradient: "from-amber-500 to-orange-600",
    iconColor: "text-amber-600",
    bgColor: "bg-amber-50",
  },
  ditolak: {
    icon: XCircle,
    gradient: "from-red-500 to-rose-600",
    iconColor: "text-red-600",
    bgColor: "bg-red-50",
  },
  ditandatangani: {
    icon: CheckCircle,
    gradient: "from-green-500 to-emerald-600",
    iconColor: "text-green-600",
    bgColor: "bg-green-50",
  },
  total: {
    icon: TrendingUp,
    gradient: "from-blue-600 to-indigo-700",
    iconColor: "text-blue-600",
    bgColor: "bg-blue-50",
  },
};

// fetch counts per status
async function fetchCounts() {
  try {
    const res = await apiClient.get(`/history/counts`);
    counts.value = res.data.data || {};
  } catch (err: any) {
    console.error("Error fetchCounts:", err);
  }
}

// fetch total permohonan
async function fetchTotal() {
  try {
    const res = await apiClient.get(`/history/total`);
    total.value = res.data.data?.total || 0;
  } catch (err: any) {
    console.error("Error fetchTotal:", err);
  }
}

// fetch history
async function fetchHistory(status: string) {
  try {
    loading.value = true;
    error.value = null;

    let res;
    if (status === "total") {
      res = await apiClient.get(`/history/all`);
    } else {
      res = await apiClient.get(`/history/${status}`);
    }

    historyList.value = res.data.data || [];
  } catch (err: any) {
    console.error("Error fetchHistory:", err);
    if (err.response?.status === 404) {
      error.value = "Data belum tersedia";
      historyList.value = [];
    } else {
      error.value = "Gagal memuat data riwayat";
    }
  } finally {
    loading.value = false;
  }
}

// handle click card
function selectStatus(status: string) {
  selectedStatus.value = status;
  fetchHistory(status);
}

// Helper untuk Badge Status
const getStatusBadge = (status: string) => {
  switch (status) {
    case "ditandatangani":
    case "disetujui":
      return {
        text: "Ditandatangani",
        icon: Check,
        class: "bg-green-600 text-white",
      };
    case "pending":
      return {
        text: "Pending",
        icon: Clock,
        class: "bg-amber-500 text-white",
      };
    case "ditolak":
      return {
        text: "Ditolak",
        icon: X,
        class: "bg-red-600 text-white",
      };
    default:
      return {
        text: "Unknown",
        icon: FileText,
        class: "bg-gray-600 text-white",
      };
  }
};

// Helper untuk label status
const getStatusLabel = (key: string) => {
  const labels: Record<string, string> = {
    pending: "Menunggu Persetujuan",
    ditolak: "Ditolak",
    ditandatangani: "Ditandatangani",
    total: "Total Permohonan",
  };
  return labels[key] || key;
};

onMounted(async () => {
  await fetchCounts();
  await fetchTotal();
  await fetchHistory(selectedStatus.value);
});
</script>

<template>
  <div class="min-h-screen bg-gray-50 p-6">
    <div class="max-w-7xl mx-auto space-y-6">
      <!-- Header Section -->
      <div class="bg-white border-l-4 border-blue-600 shadow-sm px-6 py-4">
        <h2 class="text-2xl font-bold text-gray-900">
          Riwayat Permohonan Tanda Tangan
        </h2>
        <p class="text-sm text-gray-600 mt-1">
          Dashboard monitoring status permohonan tanda tangan digital
        </p>
      </div>

      <!-- Stats Cards -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <div
          v-for="(value, key) in visibleCounts"
          :key="key"
          @click="selectStatus(key)"
          class="cursor-pointer bg-white border-2 shadow-sm hover:shadow-md rounded-lg p-5 transition-all duration-200"
          :class="{
            'border-blue-600 shadow-md': selectedStatus === key,
            'border-gray-200 hover:border-gray-300': selectedStatus !== key,
          }"
        >
          <div class="flex items-start justify-between">
            <div class="flex-1">
              <p
                class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2"
              >
                {{ getStatusLabel(key) }}
              </p>
              <p
                class="text-3xl font-bold"
                :class="
                  selectedStatus === key ? 'text-blue-600' : 'text-gray-900'
                "
              >
                {{ value }}
              </p>
            </div>
            <div class="p-3 rounded-lg" :class="cardConfig[key]?.bgColor">
              <component
                :is="cardConfig[key]?.icon"
                class="w-6 h-6"
                :class="cardConfig[key]?.iconColor"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- Table Section -->
      <div
        class="bg-white shadow-sm rounded-lg border border-gray-200 overflow-hidden"
      >
        <!-- Table Header -->
        <div class="bg-gray-800 px-6 py-4 border-b border-gray-700">
          <h3 class="text-lg font-semibold text-white flex items-center gap-2">
            <FileCheck class="w-5 h-5" />
            {{ getStatusLabel(selectedStatus) }}
          </h3>
        </div>

        <div class="p-6">
          <div v-if="selectedStatus === 'total'" class="text-center py-12">
            <div
              class="inline-flex items-center justify-center w-16 h-16 bg-slate-100 rounded-full mb-4"
            >
              <FileText class="w-8 h-8 text-slate-400" />
            </div>
            <p class="text-slate-600 font-medium">
              Tidak ada tabel untuk status Total Permohonan
            </p>
          </div>
          <!-- Loading State -->
          <div v-else-if="loading" class="text-center py-12">
            <div
              class="inline-block animate-spin rounded-full h-12 w-12 border-4 border-gray-200 border-t-blue-600"
            ></div>
            <p class="text-gray-600 mt-4 font-medium">Memuat data...</p>
          </div>

          <!-- Error State -->
          <div v-else-if="error" class="text-center py-12">
            <div
              class="inline-flex items-center justify-center w-16 h-16 bg-red-100 rounded-full mb-4"
            >
              <XCircle class="w-8 h-8 text-red-600" />
            </div>
            <p class="text-gray-700 font-medium">{{ error }}</p>
          </div>

          <!-- Empty State -->
          <div v-else-if="historyList.length === 0" class="text-center py-12">
            <div
              class="inline-flex items-center justify-center w-16 h-16 bg-gray-100 rounded-full mb-4"
            >
              <FileText class="w-8 h-8 text-gray-400" />
            </div>
            <p class="text-gray-600 font-medium">
              Tidak ada data untuk status ini
            </p>
          </div>

          <!-- Table Content -->
          <div v-else class="overflow-x-auto w-full">
            <table class="w-full">
              <thead>
                <tr class="bg-gray-50 border-y border-gray-200">
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-gray-700 uppercase tracking-wider"
                  >
                    No
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-gray-700 uppercase tracking-wider"
                  >
                    Tanggal
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-gray-700 uppercase tracking-wider"
                  >
                    Jenis Permohonan
                  </th>
                  <th
                    class="px-4 py-3 text-center text-xs font-bold text-gray-700 uppercase tracking-wider"
                  >
                    Status
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-gray-700 uppercase tracking-wider"
                  >
                    Dosen
                  </th>
                  <th
                    class="px-4 py-3 text-center text-xs font-bold text-gray-700 uppercase tracking-wider"
                  >
                    File
                  </th>
                  <th
                    class="px-4 py-3 text-center text-xs font-bold text-gray-700 uppercase tracking-wider"
                  >
                    Keterangan
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200">
                <tr
                  v-for="(item, index) in historyList"
                  :key="item.id"
                  class="hover:bg-gray-50 transition-colors"
                >
                  <td class="px-4 py-4">
                    <span class="text-sm font-semibold text-gray-900">
                      {{ index + 1 }}
                    </span>
                  </td>
                  <td class="px-4 py-4 whitespace-nowrap">
                    <span class="text-sm text-gray-700 font-medium">
                      {{
                        new Date(item.created_at).toLocaleDateString("id-ID", {
                          day: "2-digit",
                          month: "short",
                          year: "numeric",
                        })
                      }}
                    </span>
                  </td>
                  <td class="px-4 py-4">
                    <span class="text-sm text-gray-900 font-medium">
                      {{ item.judul || "-" }}
                    </span>
                  </td>
                  <td class="px-4 py-4">
                    <div class="flex justify-center">
                      <span
                        :class="[
                          'inline-flex items-center rounded-md px-3 py-1.5 text-xs font-bold uppercase tracking-wide',
                          getStatusBadge(item.status_permohonan).class,
                        ]"
                      >
                        <component
                          :is="getStatusBadge(item.status_permohonan).icon"
                          class="w-3.5 h-3.5 mr-1.5"
                        />
                        {{ getStatusBadge(item.status_permohonan).text }}
                      </span>
                    </div>
                  </td>
                  <td class="px-4 py-4 whitespace-nowrap">
                    <span class="text-sm text-gray-700 font-medium">
                      {{ item.dosen?.user?.nama || "-" }}
                    </span>
                  </td>
                  <td class="px-4 py-4">
                    <div class="flex justify-center">
                      <div v-if="item?.file_signed_path">
                        <a
                          :href="`${baseUrl}/files/signed/${item.file_signed_path}`"
                          target="_blank"
                          rel="noopener noreferrer"
                          title="Buka PDF"
                          class="inline-flex items-center gap-2 px-3 py-2 bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold rounded-md transition-colors"
                        >
                          <FileText class="w-4 h-4" />
                          Lihat PDF
                        </a>
                      </div>
                      <div v-else-if="item?.status_permohonan == 'ditolak'">
                        <span
                          class="inline-flex items-center gap-2 px-3 py-2 bg-red-100 text-red-700 text-xs font-semibold rounded-md"
                        >
                          <X class="w-4 h-4" />
                          Tidak Ada
                        </span>
                      </div>
                      <div v-else-if="item?.status_permohonan == 'pending'">
                        <span
                          class="inline-flex items-center gap-2 px-3 py-2 bg-amber-100 text-amber-700 text-xs font-semibold rounded-md"
                        >
                          <Clock class="w-4 h-4" />
                          Proses
                        </span>
                      </div>
                    </div>
                  </td>
                  <td class="px-4 py-4">
                    <div class="flex justify-center">
                      <div
                        v-if="item?.qr_code_path"
                        class="w-16 h-16 border-2 border-gray-200 rounded-md p-1 bg-white"
                      >
                        <img
                          :src="`${baseUrl}/files/uploads/qr_codes/${item.qr_code_path}`"
                          alt="QR Code"
                          class="w-full h-full object-contain"
                        />
                      </div>
                      <div
                        v-else-if="item?.komentar_penolakan"
                        class="max-w-xs"
                      >
                        <div
                          class="bg-red-50 border-l-4 border-red-500 px-3 py-2 text-xs text-red-700 font-medium"
                        >
                          {{ item.komentar_penolakan }}
                        </div>
                      </div>
                      <div
                        v-else
                        class="line-clamp-1 text-sm text-gray-400 font-medium"
                      >
                        {{ item.deskripsi }}
                      </div>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Minimalist & Professional Animations */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>
