<!-- PermohonanListPermohonanTTD.vue - FIXED VERSION -->
<template>
  <div class="p-4">
    <h2 class="text-xl font-bold mb-4">Daftar Permohonan TTD</h2>

    <!-- Filter -->
    <div class="flex items-center gap-4 mb-4">
      <label for="jenis">Filter Jenis Permohonan:</label>
      <select
        id="jenis"
        v-model="selectedJenis"
        @change="fetchPermohonan"
        class="border px-2 py-1 rounded"
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
    <table class="w-full border border-gray-200">
      <thead class="bg-gray-100">
        <tr>
          <th class="p-2 border">No</th>
          <th class="p-2 border">Judul</th>
          <th class="p-2 border">Mahasiswa</th>
          <th class="p-2 border">Jenis</th>
          <th class="p-2 border">Status</th>
          <th class="p-2 border">File</th>
          <th class="p-2 border">Aksi</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(permohonan, index) in permohonanList" :key="permohonan.id">
          <td class="p-2 border">{{ index + 1 }}</td>
          <td class="p-2 border">{{ permohonan.judul }}</td>
          <td class="p-2 border">{{ permohonan.mahasiswa?.user?.nama }}</td>
          <td class="p-2 border">
            {{ permohonan.jenis_permohonan?.nama_jenis_permohonan }}
          </td>
          <td class="p-2 border">
            <span
              :class="getStatusClass(permohonan.status_permohonan)"
              class="px-2 py-1 rounded text-xs font-semibold"
            >
              {{ getStatusText(permohonan.status_permohonan) }}
            </span>
          </td>
          <td class="p-2 border">
            <!-- Tampilkan file yang sudah ditandatangani jika ada -->
            <div v-if="permohonan.file_signed_path" class="space-y-1">
              <a
                :href="`${baseUrl}/files/signed/${permohonan.file_signed_path}`"
                target="_blank"
                class="text-green-600 underline block"
              >
                📄 File Tertandatangani
              </a>
              <a
                v-if="permohonan.file_path"
                :href="`${baseUrl}/files/uploads/${permohonan.file_path}`"
                target="_blank"
                class="text-blue-500 underline text-xs block"
              >
                📎 File Asli
              </a>
            </div>
            <!-- Jika belum ditandatangani, tampilkan file asli -->
            <a
              v-else-if="permohonan.file_path"
              :href="`${baseUrl}/files/uploads/${permohonan.file_path}`"
              target="_blank"
              class="text-blue-500 underline"
            >
              📄 Lihat / Download
            </a>
            <span v-else>-</span>
          </td>
          <td class="p-2 border">
            <div class="flex gap-2 flex-wrap">
              <!-- Tombol Tandatangani untuk status pending atau disetujui -->
              <button
                v-if="
                  ['pending', 'disetujui'].includes(
                    permohonan.status_permohonan
                  )
                "
                class="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600 disabled:bg-gray-400"
                :disabled="signingPermohonan === permohonan.id"
                @click="signPermohonan(permohonan.id)"
              >
                <span v-if="signingPermohonan === permohonan.id">
                  ⏳ Menandatangani...
                </span>
                <span v-else> ✍️ Tandatangani </span>
              </button>

              <!-- Tombol Tolak hanya untuk pending -->
              <button
                v-if="permohonan.status_permohonan === 'pending'"
                class="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
                @click="rejectPermohonan(permohonan.id)"
              >
                ❌ Tolak
              </button>

              <!-- Tombol Detail
              <button
                class="bg-gray-500 text-white px-3 py-1 rounded hover:bg-gray-600"
                @click="viewDetail(permohonan.id)"
              >
                👁️ Detail
              </button> -->
            </div>
          </td>
        </tr>
        <tr v-if="permohonanList.length === 0">
          <td class="p-2 border text-center" colspan="7">
            Belum ada permohonan
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Pagination -->
    <div class="mt-4 flex justify-end gap-2">
      <button
        class="px-3 py-1 border rounded disabled:opacity-50"
        :disabled="page === 1"
        @click="prevPage"
      >
        Prev
      </button>
      <span>Halaman {{ page }}</span>
      <button
        class="px-3 py-1 border rounded disabled:opacity-50"
        :disabled="permohonanList.length < perPage"
        @click="nextPage"
      >
        Next
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from "vue";
import { getJenisPermohonan } from "@/services/jenisPermohonanService";
import { apiClient } from "@/lib/axios";

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

    // FUNGSI BARU: Tandatangani permohonan
    const signPermohonan = async (id: string) => {
      if (!confirm("Apakah Anda yakin ingin menandatangani permohonan ini?"))
        return;

      signingPermohonan.value = id;

      try {
        const response = await apiClient.post(`/permohonan/${id}/sign`);

        if (response.data.success) {
          alert("✅ Permohonan berhasil ditandatangani!");
          await fetchPermohonan(); // Refresh data
        }
      } catch (error: any) {
        console.error("Gagal menandatangani permohonan:", error);
        const errorMsg =
          error.response?.data?.message || "Gagal menandatangani permohonan";
        alert(`❌ ${errorMsg}`);
      } finally {
        signingPermohonan.value = null;
      }
    };

    const rejectPermohonan = async (id: string) => {
      const komentar = prompt("Masukkan komentar penolakan:");
      if (!komentar) return;
      try {
        await apiClient.post(`/permohonan/${id}/reject`, {
          komentar_penolakan: komentar,
        });
        alert("✅ Permohonan berhasil ditolak");
        fetchPermohonan();
      } catch (error) {
        console.error("Gagal menolak permohonan:", error);
        alert("❌ Gagal menolak permohonan");
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
/* Optional: smooth transitions */
button {
  transition: all 0.2s ease;
}

button:disabled {
  cursor: not-allowed;
}
</style>
