<template>
  <div
    class="p-6 bg-gradient-to-br from-orange-50 to-indigo-50 min-h-screen rounded-xl shadow-sm"
  >
    <h2 class="text-2xl font-bold mb-6 text-indigo-800 flex items-center gap-2">
      📜 Daftar Permohonan Tanda Tangan Digital
    </h2>

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

    <!-- Table -->
    <div
      class="overflow-x-auto bg-white shadow-md rounded-xl border border-gray-200"
    >
      <table class="w-full border-collapse">
        <thead class="bg-indigo-100 text-indigo-900 uppercase text-sm">
          <tr>
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
            class="hover:bg-orange-50 transition-all"
          >
            <td class="p-3 border text-center">{{ index + 1 }}</td>
            <td class="p-3 border">{{ permohonan.judul }}</td>
            <td class="p-3 border">{{ permohonan.mahasiswa?.user?.nama }}</td>
            <td class="p-3 border text-gray-700">{{ permohonan.deskripsi }}</td>
            <td class="p-3 border text-center">
              <span
                :class="getStatusClass(permohonan.status_permohonan)"
                class="px-2 py-1 rounded-full text-xs font-semibold tracking-wide"
              >
                {{ getStatusText(permohonan.status_permohonan) }}
              </span>
            </td>
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
            <td class="p-3 border text-center">
              <div class="flex justify-center gap-2 flex-wrap">
                <!-- Tombol Tandatangani -->
                <button
                  v-if="
                    ['pending', 'disetujui'].includes(
                      permohonan.status_permohonan
                    )
                  "
                  class="bg-teal-500 text-white px-3 py-1 rounded-lg hover:bg-teal-600 disabled:bg-gray-400 shadow-sm"
                  :disabled="signingPermohonan === permohonan.id"
                  @click="signPermohonan(permohonan.id)"
                >
                  <span v-if="signingPermohonan === permohonan.id">
                    ⏳ Menandatangani...
                  </span>
                  <span v-else>Tandatangan</span>
                </button>

                <!-- Tombol Tolak -->
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
            <td class="p-4 border text-center text-gray-500" colspan="7">
              Belum ada permohonan
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Pagination -->
    <div class="mt-6 flex justify-end items-center gap-2 text-sm text-gray-600">
      <button
        class="px-3 py-1 border rounded-lg hover:bg-indigo-50 disabled:opacity-50 disabled:hover:bg-transparent"
        :disabled="page === 1"
        @click="prevPage"
      >
        ◀ Prev
      </button>
      <span
        >Halaman <strong>{{ page }}</strong></span
      >
      <button
        class="px-3 py-1 border rounded-lg hover:bg-indigo-50 disabled:opacity-50 disabled:hover:bg-transparent"
        :disabled="permohonanList.length < perPage"
        @click="nextPage"
      >
        Next ▶
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from "vue";
import { getJenisPermohonan } from "@/services/jenisPermohonanService";
import { apiClient } from "@/lib/axios";
import Swal from "sweetalert2";

export default {
  name: "PermohonanListPermohonanTTD",
  setup() {
    const permohonanList = ref<any[]>([]);
    const jenisPermohonanList = ref<any[]>([]);
    const selectedJenis = ref<string | number>("");
    const signingPermohonan = ref<string | null>(null);

    const page = ref(1);
    const perPage = ref(10);

    const baseUrl = import.meta.env.VITE_API_URL;

    const fetchJenisPermohonan = async () => {
      try {
        jenisPermohonanList.value = await getJenisPermohonan();
      } catch (error) {
        console.error("Failed to fetch jenis permohonan:", error);
      }
    };

    const fetchPermohonan = async () => {
      try {
        const params: any = {
          page: page.value,
          per_page: perPage.value,
          // Hapus filter status agar menampilkan semua status
        };
        if (selectedJenis.value) params.jenis_id = selectedJenis.value;

        const response = await apiClient.get("/permohonan/dosen", { params });
        permohonanList.value = response.data.data;
      } catch (error) {
        console.error("Failed to fetch permohonan:", error);
      }
    };

    const viewDetail = (id: string) => {
      window.location.href = `/dosen/permohonan/${id}`;
    };

    const signPermohonan = async (id: string) => {
      const result = await Swal.fire({
        title: "Tandatangani Permohonan?",
        text: "Apakah Anda yakin ingin menandatangani permohonan ini?",
        icon: "question",
        showCancelButton: true,
        confirmButtonText: "Ya, Tandatangani",
        cancelButtonText: "Batal",
        confirmButtonColor: "#10b981", // hijau teal
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

    const rejectPermohonan = async (id: string) => {
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

    // Helper untuk styling status
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

    // Helper untuk text status yang lebih readable
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

    const nextPage = () => {
      page.value++;
      fetchPermohonan();
    };

    const prevPage = () => {
      if (page.value > 1) {
        page.value--;
        fetchPermohonan();
      }
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
      page,
      perPage,
      baseUrl,
      fetchPermohonan,
      viewDetail,
      signPermohonan,
      rejectPermohonan,
      getStatusClass,
      getStatusText,
      nextPage,
      prevPage,
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
}
</style>
