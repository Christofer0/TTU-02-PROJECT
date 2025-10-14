<template>
  <div class="p-6 bg-gradient-to-b from-yellow-50 to-orange-50 min-h-screen">
    <h1
      class="text-3xl font-bold mb-6 text-gray-900 border-b-4 border-orange-500 pb-2 flex items-center gap-2"
    >
      📋 Daftar Permohonan Tanda Tangan
      <span class="text-sm font-normal text-gray-600">(Read-Only)</span>
    </h1>

    <div v-if="loading" class="flex justify-center items-center py-10">
      <div
        class="animate-spin rounded-full h-10 w-10 border-t-4 border-orange-500 border-gray-200"
      ></div>
      <p class="ml-3 text-gray-700 font-medium">Memuat data...</p>
    </div>

    <div
      v-else-if="error"
      class="text-center text-red-600 bg-red-50 border border-red-200 p-4 rounded-lg shadow-sm"
    >
      ⚠️ {{ error }}
    </div>

    <div
      v-else-if="permohonanList.length > 0"
      class="overflow-x-auto shadow-lg rounded-xl border border-orange-200 bg-white"
    >
      <table class="min-w-full text-sm text-center text-gray-800">
        <thead
          class="bg-gradient-to-r from-yellow-400 to-orange-500 text-white uppercase text-xs tracking-wider"
        >
          <tr>
            <th class="px-5 py-3">Judul</th>
            <th class="px-5 py-3">Jenis</th>
            <th class="px-5 py-3">Mahasiswa</th>
            <th class="px-5 py-3">Dosen</th>
            <th class="px-5 py-3">Status</th>
            <th class="px-5 py-3">Tanggal</th>
            <th class="px-5 py-3">File</th>
          </tr>
        </thead>

        <tbody class="divide-y divide-orange-100 bg-white">
          <tr
            v-for="item in permohonanList"
            :key="item.id"
            class="hover:bg-orange-50 transition"
          >
            <td class="px-5 py-3 font-medium text-gray-900">
              {{ item.judul }}
            </td>

            <td class="px-5 py-3">
              {{ item.jenis_permohonan?.nama_jenis_permohonan || "-" }}
            </td>

            <td class="px-5 py-3">
              <div class="font-semibold text-gray-900">
                {{ item.mahasiswa?.user?.nama }}
              </div>
              <div class="text-xs text-gray-500 leading-snug">
                {{ item.mahasiswa?.user?.nomor_induk }}
              </div>
            </td>

            <td class="px-5 py-3">
              <div class="font-semibold text-gray-900">
                {{ item.dosen?.nama_lengkap }}
              </div>
            </td>

            <td class="px-5 py-3">
              <span
                :class="[
                  'px-3 py-1 rounded-full text-xs font-bold border',
                  getStatusClass(item.status_permohonan),
                ]"
              >
                {{ formatStatusText(item.status_permohonan) }}
              </span>
            </td>

            <td class="px-5 py-3">
              {{ formatDate(item.created_at) }}
            </td>

            <td class="px-5 py-3">
              <a
                v-if="item.file_path"
                :href="`${baseUrl}/files/uploads/${item.file_path}`"
                target="_blank"
                class="text-orange-600 hover:text-orange-700 hover:underline font-semibold"
              >
                {{ item.file_name || "Lihat File" }}
              </a>
              <span v-else class="text-gray-400 italic">-</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div
      v-else
      class="text-center mt-8 text-gray-700 bg-white py-10 border border-orange-200 rounded-lg shadow-sm"
    >
      Tidak ada data permohonan ditemukan.
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from "vue";
import { apiClient } from "@/lib/axios";

interface Permohonan {
  id: number;
  judul: string;
  status_permohonan: string;
  created_at: string;
  file_path?: string;
  file_name?: string;
  // komentar?: string;
  komentar_penolakan?: string;
  jenis_permohonan?: { nama_jenis_permohonan: string };
  mahasiswa?: {
    user?: { nama: string; nomor_induk: string };
    program_studi?: { nama_prodi: string };
    fakultas_mahasiswa?: { nama_fakultas: string };
  };
  dosen?: {
    nama_lengkap: string;
    jabatan?: string;
    fakultas_dosen?: { nama_fakultas: string };
  };
}

const baseUrl = import.meta.env.VITE_API_URL;
const permohonanList = ref<Permohonan[]>([]);
const loading = ref(false);
const error = ref<string | null>(null);

const fetchPermohonan = async () => {
  loading.value = true;
  error.value = null;

  try {
    const { data } = await apiClient.get("/admin/permohonan/pending");
    permohonanList.value = data.data || [];
  } catch (err: any) {
    error.value =
      err?.response?.data?.message || "Gagal memuat data permohonan.";
  } finally {
    loading.value = false;
  }
};

const formatDate = (dateStr?: string) => {
  if (!dateStr) return "-";
  return new Date(dateStr).toLocaleString("id-ID", {
    dateStyle: "medium",
    timeStyle: "short",
  });
};

const getStatusClass = (status: string) => {
  switch (status) {
    case "approved":
      return "bg-green-100 text-green-700 border-green-300";
    case "pending":
      return "bg-yellow-100 text-yellow-700 border-yellow-300";
    case "rejected":
      return "bg-red-100 text-red-700 border-red-300";
    case "completed":
      return "bg-blue-100 text-blue-700 border-blue-300";
    default:
      return "bg-gray-100 text-gray-700 border-gray-300";
  }
};

const formatStatusText = (status: string) => {
  const map: Record<string, string> = {
    pending: "Menunggu",
    approved: "Disetujui",
    rejected: "Ditolak",
    completed: "Selesai",
  };
  return map[status] || "Tidak Diketahui";
};

onMounted(fetchPermohonan);
</script>

<style scoped>
table {
  border-collapse: separate;
  border-spacing: 0;
}
th:first-child {
  border-top-left-radius: 0.5rem;
}
th:last-child {
  border-top-right-radius: 0.5rem;
}
</style>
