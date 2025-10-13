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

// Card config khusus DOSEN (warna biru & ungu sebagai tema akademik)
const cardConfig: Record<
  string,
  { icon: any; gradient: string; iconColor: string; bgColor: string }
> = {
  pending: {
    icon: Clock,
    gradient: "from-sky-400 to-blue-500",
    iconColor: "text-sky-600",
    bgColor: "bg-sky-50",
  },
  ditolak: {
    icon: XCircle,
    gradient: "from-rose-500 to-red-600",
    iconColor: "text-rose-600",
    bgColor: "bg-rose-50",
  },
  ditandatangani: {
    icon: CheckCircle,
    gradient: "from-indigo-500 to-purple-600",
    iconColor: "text-indigo-600",
    bgColor: "bg-indigo-50",
  },
  total: {
    icon: TrendingUp,
    gradient: "from-violet-600 to-purple-700",
    iconColor: "text-violet-600",
    bgColor: "bg-violet-50",
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

// Helper untuk Badge Status (warna disesuaikan dosen)
const getStatusBadge = (status: string) => {
  switch (status) {
    case "ditandatangani":
    case "disetujui":
      return {
        text: "Ditandatangani",
        icon: Check,
        class: "bg-indigo-600 text-white",
      };
    case "pending":
      return {
        text: "Pending",
        icon: Clock,
        class: "bg-sky-500 text-white",
      };
    case "ditolak":
      return {
        text: "Ditolak",
        icon: X,
        class: "bg-rose-600 text-white",
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
    ditandatangani: "Sudah Ditandatangani",
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
      <div class="bg-white border-l-4 border-indigo-600 shadow-sm px-6 py-4">
        <h2 class="text-2xl font-bold text-gray-900">
          Riwayat Permohonan Tanda Tangan
        </h2>
        <p class="text-sm text-gray-600 mt-1">
          Monitoring status permohonan tanda tangan dari mahasiswa
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
            'border-indigo-600 shadow-md': selectedStatus === key,
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
                  selectedStatus === key ? 'text-indigo-600' : 'text-gray-900'
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
        <div class="bg-indigo-700 px-6 py-4 border-b border-indigo-600">
          <h3 class="text-lg font-semibold text-white flex items-center gap-2">
            <FileCheck class="w-5 h-5" />
            {{ getStatusLabel(selectedStatus) }}
          </h3>
        </div>

        <div class="p-6">
          <!-- Loading -->
          <div v-if="loading" class="text-center py-12">
            <div
              class="inline-block animate-spin rounded-full h-12 w-12 border-4 border-gray-200 border-t-indigo-600"
            ></div>
            <p class="text-gray-600 mt-4 font-medium">Memuat data...</p>
          </div>

          <!-- Error -->
          <div v-else-if="error" class="text-center py-12">
            <div
              class="inline-flex items-center justify-center w-16 h-16 bg-rose-100 rounded-full mb-4"
            >
              <XCircle class="w-8 h-8 text-rose-600" />
            </div>
            <p class="text-gray-700 font-medium">{{ error }}</p>
          </div>

          <!-- Empty -->
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

          <!-- Table -->
          <div v-else class="overflow-x-auto">
            <table class="w-full">
              <thead>
                <tr class="bg-gray-50 border-y border-gray-200">
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-gray-700 uppercase"
                  >
                    No
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-gray-700 uppercase"
                  >
                    Tanggal
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-gray-700 uppercase"
                  >
                    Mahasiswa
                  </th>
                  <th
                    class="px-4 py-3 text-center text-xs font-bold text-gray-700 uppercase"
                  >
                    Status
                  </th>
                  <th
                    class="px-4 py-3 text-center text-xs font-bold text-gray-700 uppercase"
                  >
                    File
                  </th>
                  <th
                    class="px-4 py-3 text-center text-xs font-bold text-gray-700 uppercase"
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
                  <td class="px-4 py-4 font-semibold">{{ index + 1 }}</td>
                  <td class="px-4 py-4">
                    {{
                      new Date(item.created_at).toLocaleDateString("id-ID", {
                        day: "2-digit",
                        month: "short",
                        year: "numeric",
                      })
                    }}
                  </td>
                  <td class="px-4 py-4">
                    {{ item.mahasiswa?.user?.nama || "-" }}
                  </td>
                  <td class="px-4 py-4 text-center">
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
                  </td>
                  <td class="px-4 py-4 text-center">
                    <a
                      v-if="item?.file_signed_path"
                      :href="`${baseUrl}/files/signed/${item.file_signed_path}`"
                      target="_blank"
                      class="inline-flex items-center gap-2 px-3 py-2 bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-semibold rounded-md transition-colors"
                    >
                      <FileText class="w-4 h-4" />
                      Lihat PDF
                    </a>
                    <span v-else class="text-xs text-gray-500 font-medium">
                      Tidak Ada
                    </span>
                  </td>
                  <td class="px-4 py-4 text-center">
                    <div
                      v-if="item?.status_permohonan == 'ditolak'"
                      class="text-red-600 text-xs bg-red-100 px-4 py-2 rounded-lg shadow-sm"
                    >
                      {{ item.komentar_penolakan }}
                    </div>
                    <div
                      v-else-if="item?.status_permohonan == 'ditandatangani'"
                      class="text-green-600 font-semibold text-xs bg-green-100 px-4 py-2 rounded-lg shadow-sm"
                    >
                      Approved
                    </div>
                    <div
                      v-else-if="item?.status_permohonan == 'pending'"
                      class="text-yellow-400 text-xs bg-yellow-100 px-4 py-2 rounded-lg shadow-sm"
                    >
                      Waiting
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
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
.animate-spin {
  animation: spin 1s linear infinite;
}
</style>
