<template>
  <div
    class="p-6 bg-gradient-to-br from-orange-50 to-indigo-50 min-h-screen rounded-xl shadow-sm"
  >
    <h2 class="text-2xl font-bold mb-6 text-indigo-800 flex items-center gap-2">
      📜 Daftar Permohonan Tanda Tangan Digital
    </h2>

    <!-- Batch Actions Bar -->
    <div
      v-if="selectedIds.size > 0"
      class="bg-indigo-600 text-white p-4 rounded-lg mb-4 flex items-center justify-between shadow-lg animate-pulse"
    >
      <div class="flex items-center gap-3">
        <input type="checkbox" checked disabled class="w-5 h-5" />
        <span class="font-semibold"
          >{{ selectedIds.size }} permohonan dipilih</span
        >
      </div>
      <div class="flex gap-2">
        <button
          @click="clearSelection"
          class="bg-white text-indigo-600 px-4 py-2 rounded-lg hover:bg-indigo-50 transition-all font-medium"
        >
          Batal Pilih
        </button>
        <button
          @click="handleBatchSign"
          :disabled="isBatchProcessing"
          class="bg-green-500 text-white px-6 py-2 rounded-lg hover:bg-green-600 disabled:bg-gray-400 disabled:cursor-not-allowed transition-all font-medium flex items-center gap-2"
        >
          <span v-if="isBatchProcessing">⏳ Memproses...</span>
          <span v-else>✍️ Tandatangani Semua</span>
        </button>
      </div>
    </div>

    <!-- Progress Bar -->
    <div
      v-if="isBatchProcessing"
      class="bg-white p-4 rounded-lg mb-4 shadow-md"
    >
      <div class="flex justify-between mb-2">
        <span class="text-sm font-medium text-gray-700">
          Menandatangani permohonan secara batch...
        </span>
        <span class="text-sm font-medium text-indigo-600">
          Memproses {{ selectedIds.size }} permohonan
        </span>
      </div>
      <div class="w-full bg-gray-200 rounded-full h-3">
        <div
          class="bg-indigo-600 h-3 rounded-full transition-all duration-500 animate-pulse"
          style="width: 100%"
        />
      </div>
      <p class="text-xs text-gray-500 mt-2">
        Mohon tunggu, proses sedang berjalan...
      </p>
    </div>

    <!-- Filter -->
    <div class="flex items-center gap-3 mb-6 bg-white p-3 rounded-lg shadow-sm">
      <label for="jenis" class="text-gray-700 font-medium"
        >Filter Jenis Permohonan:</label
      >
      <select
        id="jenis"
        v-model="selectedJenis"
        @change="fetchPermohonan"
        class="border border-indigo-200 focus:ring-2 focus:ring-indigo-400 px-3 py-2 rounded-lg outline-none"
      >
        <option value="">Semua</option>
        <option
          v-for="jenis in jenisPermohonanList"
          :key="jenis.id"
          :value="jenis.id"
        >
          {{ jenis.nama_jenis_permohonan }}
        </option>
      </select>
    </div>

    <!-- Info Box -->
    <div class="mt-4 mb-5 bg-blue-50 border border-blue-200 rounded-lg p-4">
      <p class="text-sm text-blue-800">
        <strong>💡 Tips:</strong> Centang permohonan yang ingin ditandatangani,
        lalu klik tombol
        <span class="font-semibold">"Tandatangani Semua"</span> untuk proses
        batch. Hanya permohonan dengan status
        <span class="font-semibold">Menunggu</span> atau
        <span class="font-semibold">Disetujui</span> yang dapat ditandatangani.
      </p>
    </div>

    <!-- Table -->
    <div
      class="overflow-x-auto bg-white shadow-md rounded-xl border border-gray-200"
    >
      <table class="w-full border-collapse">
        <thead class="bg-indigo-100 text-indigo-900 uppercase text-sm">
          <tr>
            <th class="p-3 border">
              <input
                type="checkbox"
                :checked="isAllSignableSelected"
                @change="toggleSelectAll"
                :disabled="signablePermohonan.length === 0"
                class="w-5 h-5 cursor-pointer"
                title="Pilih semua yang dapat ditandatangani"
              />
            </th>
            <th class="p-3 border">No</th>
            <th class="p-3 border text-left">Judul</th>
            <th class="p-3 border text-left">Mahasiswa</th>
            <th class="p-3 border text-left">Deskripsi</th>
            <th class="p-3 border text-center">Status</th>
            <th class="p-3 border text-center">File</th>
            <th class="p-3 border text-center">Aksi</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(permohonan, index) in permohonanList"
            :key="permohonan.id"
            :class="[
              'hover:bg-orange-50 transition-all',
              selectedIds.has(permohonan.id)
                ? 'bg-indigo-50 border-l-4 border-l-indigo-500'
                : '',
            ]"
          >
            <!-- Checkbox -->
            <td class="p-3 border text-center">
              <input
                v-if="canSign(permohonan.status_permohonan)"
                type="checkbox"
                :checked="selectedIds.has(permohonan.id)"
                @change="toggleSelect(permohonan.id)"
                class="w-5 h-5 cursor-pointer"
              />
            </td>

            <td class="p-3 border text-center">{{ index + 1 }}</td>

            <!-- Judul -->
            <td class="p-3 border">
              <div class="line-clamp-2 font-medium">{{ permohonan.judul }}</div>
            </td>

            <!-- Nama Mahasiswa -->
            <td class="p-3 border">{{ permohonan.mahasiswa?.user?.nama }}</td>

            <!-- Deskripsi -->
            <td class="p-3 border text-gray-700">
              <div class="line-clamp-1">{{ permohonan.deskripsi }}</div>
            </td>

            <!-- Status -->
            <td class="p-3 border text-center">
              <span
                :class="getStatusClass(permohonan.status_permohonan)"
                class="px-2 py-1 rounded-full text-xs font-semibold tracking-wide"
              >
                {{ getStatusText(permohonan.status_permohonan) }}
              </span>
            </td>

            <!-- File -->
            <td class="p-3 border text-center">
              <div v-if="permohonan.file_signed_path" class="space-y-1">
                <a
                  :href="`${baseUrl}/files/signed/${permohonan.file_signed_path}`"
                  target="_blank"
                  class="text-teal-600 hover:text-teal-800 underline block"
                >
                  📄 File Tertandatangani
                </a>
                <a
                  v-if="permohonan.file_path"
                  :href="`${baseUrl}/files/uploads/${permohonan.file_path}`"
                  target="_blank"
                  class="text-indigo-500 hover:text-indigo-700 underline text-xs block"
                >
                  📎 File Asli
                </a>
              </div>
              <a
                v-else-if="permohonan.file_path"
                :href="`${baseUrl}/files/uploads/${permohonan.file_path}`"
                target="_blank"
                class="text-indigo-600 hover:text-indigo-800 underline"
              >
                📄 Lihat / Download
              </a>
              <span v-else class="text-gray-400 italic">-</span>
            </td>

            <!-- Aksi -->
            <td class="p-3 border text-center">
              <div class="flex justify-center gap-2 flex-wrap">
                <button
                  v-if="canSign(permohonan.status_permohonan)"
                  class="bg-teal-500 text-white px-3 py-1 rounded-lg hover:bg-teal-600 disabled:bg-gray-400 shadow-sm"
                  :disabled="signingPermohonan === permohonan.id"
                  @click="signPermohonan(permohonan.id)"
                >
                  <span v-if="signingPermohonan === permohonan.id"
                    >⏳ Menandatangani...</span
                  >
                  <span v-else>Tandatangan</span>
                </button>

                <button
                  v-if="permohonan.status_permohonan === 'pending'"
                  class="bg-red-500 text-white px-3 py-1 rounded-lg hover:bg-red-600 shadow-sm"
                  @click="rejectPermohonan(permohonan.id)"
                >
                  Tolak
                </button>
              </div>
            </td>
          </tr>

          <tr v-if="permohonanList.length === 0">
            <td class="p-4 border text-center text-gray-500" colspan="8">
              Belum ada permohonan
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted, computed } from "vue";
import { getJenisPermohonan } from "@/services/jenisPermohonanService";
import { apiClient } from "@/lib/axios";
import Swal from "sweetalert2";

interface Permohonan {
  id: number;
  judul: string;
  deskripsi: string;
  status_permohonan: string;
  file_path?: string;
  file_signed_path?: string;
  mahasiswa?: {
    user?: {
      nama: string;
    };
  };
  jenis_permohonan?: {
    nama_jenis_permohonan: string;
  };
}

interface BatchSignResult {
  success: Array<{ id: number; judul: string }>;
  failed: Array<{ id: number; reason: string }>;
  total: number;
}

export default {
  name: "BatchSignPermohonanTTD",
  setup() {
    const permohonanList = ref<Permohonan[]>([]);
    const jenisPermohonanList = ref<any[]>([]);
    const selectedJenis = ref<string | number>("");
    const signingPermohonan = ref<number | null>(null);

    // Batch signing states
    const selectedIds = ref<Set<number>>(new Set());
    const isBatchProcessing = ref(false);

    const baseUrl = import.meta.env.VITE_API_URL;

    // Computed
    const signablePermohonan = computed(() =>
      permohonanList.value.filter((p) =>
        ["pending", "disetujui"].includes(p.status_permohonan)
      )
    );

    const isAllSignableSelected = computed(() => {
      const signableIds = signablePermohonan.value.map((p) => p.id);
      return (
        signableIds.length > 0 &&
        signableIds.every((id) => selectedIds.value.has(id))
      );
    });

    // Methods
    const fetchJenisPermohonan = async () => {
      try {
        jenisPermohonanList.value = await getJenisPermohonan();
      } catch (error) {
        console.error("Failed to fetch jenis permohonan:", error);
      }
    };

    const fetchPermohonan = async () => {
      try {
        const params: any = {};
        if (selectedJenis.value) params.jenis_id = selectedJenis.value;

        const response = await apiClient.get("/permohonan/dosen", { params });
        permohonanList.value = response.data.data;
      } catch (error) {
        console.error("Failed to fetch permohonan:", error);
      }
    };

    const toggleSelect = (id: number) => {
      const newSelected = new Set(selectedIds.value);
      if (newSelected.has(id)) {
        newSelected.delete(id);
      } else {
        newSelected.add(id);
      }
      selectedIds.value = newSelected;
    };

    const toggleSelectAll = () => {
      const signableIds = signablePermohonan.value.map((p) => p.id);
      if (isAllSignableSelected.value) {
        selectedIds.value = new Set();
      } else {
        selectedIds.value = new Set(signableIds);
      }
    };

    const clearSelection = () => {
      selectedIds.value = new Set();
    };

    const canSign = (status: string) =>
      ["pending", "disetujui"].includes(status);

    const handleBatchSign = async () => {
      if (selectedIds.value.size === 0) {
        Swal.fire({
          title: "Peringatan",
          text: "Pilih minimal 1 permohonan untuk ditandatangani",
          icon: "warning",
          confirmButtonColor: "#3b82f6",
        });
        return;
      }

      const result = await Swal.fire({
        title: "Tandatangani Batch?",
        html: `Anda akan menandatangani <strong>${selectedIds.value.size} permohonan</strong> sekaligus.<br><br>Proses ini mungkin memakan waktu beberapa saat. Lanjutkan?`,
        icon: "question",
        showCancelButton: true,
        confirmButtonText: "Ya, Tandatangani Semua",
        cancelButtonText: "Batal",
        confirmButtonColor: "#10b981",
        cancelButtonColor: "#d33",
      });

      if (!result.isConfirmed) return;

      isBatchProcessing.value = true;

      try {
        const response = await apiClient.post("/permohonan/batch-sign", {
          permohonan_ids: Array.from(selectedIds.value),
        });

        if (response.data.success) {
          const data = response.data.data as BatchSignResult;
          const { success, failed } = data;
          let resultHtml = `
  <div style="text-align: center;">
    <p><strong style="color:#10b981;">✅ Berhasil:</strong> ${success.length} permohonan</p>
`;

          if (failed.length > 0) {
            resultHtml += `
    <p><strong style="color:#ef4444;">❌ Gagal:</strong> ${failed.length} permohonan</p>
    <ul style="margin-top:10px;font-size:0.9em;color:#666;text-align:left;max-height:200px;overflow-y:auto;">
  `;

            failed.forEach((item: any) => {
              resultHtml += `<li style="margin-bottom: 8px;"><strong>ID ${item.id}:</strong> ${item.reason}</li>`;
            });

            resultHtml += `</ul>`;
          }

          resultHtml += `</div>`;

          await Swal.fire({
            title: "Batch Signing Selesai!",
            html: resultHtml,
            icon: success.length > 0 ? "success" : "error",
            confirmButtonColor: "#3b82f6",
            width: "600px",
          });

          // Clear selection and refresh
          selectedIds.value = new Set();
          await fetchPermohonan();
        }
      } catch (error: any) {
        console.error("Batch sign error:", error);
        const errorMsg =
          error.response?.data?.message ||
          "Terjadi kesalahan saat batch signing.";
        Swal.fire({
          title: "Gagal",
          text: errorMsg,
          icon: "error",
          confirmButtonColor: "#ef4444",
        });
      } finally {
        isBatchProcessing.value = false;
      }
    };

    const signPermohonan = async (id: number) => {
      const result = await Swal.fire({
        title: "Tandatangani Permohonan?",
        text: "Apakah Anda yakin ingin menandatangani permohonan ini?",
        icon: "question",
        showCancelButton: true,
        confirmButtonText: "Ya, Tandatangani",
        cancelButtonText: "Batal",
        confirmButtonColor: "#10b981",
        cancelButtonColor: "#d33",
      });

      if (!result.isConfirmed) return;

      signingPermohonan.value = id;

      try {
        const response = await apiClient.post(`/permohonan/${id}/sign`);

        if (response.data.success) {
          await Swal.fire({
            title: "Berhasil!",
            text: "Permohonan berhasil ditandatangani ✅",
            icon: "success",
            confirmButtonColor: "#3b82f6",
          });
          await fetchPermohonan();
        }
      } catch (error: any) {
        console.error("Gagal menandatangani permohonan:", error);
        const errorMsg =
          error.response?.data?.message ||
          "Terjadi kesalahan saat menandatangani.";
        Swal.fire({
          title: "Gagal",
          text: errorMsg,
          icon: "error",
          confirmButtonColor: "#ef4444",
        });
      } finally {
        signingPermohonan.value = null;
      }
    };

    const rejectPermohonan = async (id: number) => {
      const { value: komentar, isConfirmed } = await Swal.fire({
        title: "Tolak Permohonan",
        input: "textarea",
        inputLabel: "Masukkan alasan penolakan:",
        inputPlaceholder: "Tuliskan alasan di sini...",
        showCancelButton: true,
        confirmButtonText: "Tolak Permohonan",
        cancelButtonText: "Batal",
        confirmButtonColor: "#ef4444",
        inputValidator: (value) => {
          if (!value) {
            return "Komentar penolakan wajib diisi!";
          }
        },
      });

      if (!isConfirmed || !komentar) return;

      try {
        await apiClient.post(`/permohonan/${id}/reject`, {
          komentar_penolakan: komentar,
        });
        await Swal.fire({
          title: "Ditolak",
          text: "Permohonan berhasil ditolak ❌",
          icon: "success",
          confirmButtonColor: "#3b82f6",
        });
        fetchPermohonan();
      } catch (error) {
        console.error("Gagal menolak permohonan:", error);
        Swal.fire({
          title: "Gagal",
          text: "Terjadi kesalahan saat menolak permohonan.",
          icon: "error",
          confirmButtonColor: "#ef4444",
        });
      }
    };

    const getStatusClass = (status: string) => {
      const classes: Record<string, string> = {
        pending: "bg-yellow-100 text-yellow-800",
        disetujui: "bg-green-100 text-green-800",
        ditolak: "bg-red-100 text-red-800",
        ditandatangani: "bg-blue-100 text-blue-800",
        selesai: "bg-purple-100 text-purple-800",
      };
      return classes[status] || "bg-gray-100 text-gray-800";
    };

    const getStatusText = (status: string) => {
      const texts: Record<string, string> = {
        pending: "Menunggu",
        disetujui: "Disetujui",
        ditolak: "Ditolak",
        ditandatangani: "Ditandatangani",
        selesai: "Selesai",
      };
      return texts[status] || status;
    };

    onMounted(async () => {
      await fetchJenisPermohonan();
      await fetchPermohonan();
    });

    return {
      permohonanList,
      jenisPermohonanList,
      selectedJenis,
      signingPermohonan,
      selectedIds,
      isBatchProcessing,
      baseUrl,
      signablePermohonan,
      isAllSignableSelected,
      fetchPermohonan,
      toggleSelect,
      toggleSelectAll,
      clearSelection,
      canSign,
      handleBatchSign,
      signPermohonan,
      rejectPermohonan,
      getStatusClass,
      getStatusText,
    };
  },
};
</script>

<style scoped>
button {
  transition: all 0.25s ease;
}
button:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

@keyframes pulse {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.9;
  }
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

.line-clamp-1 {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
}

.line-clamp-2 {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}
</style>
