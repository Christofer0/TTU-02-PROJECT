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
          <td class="p-2 border">{{ permohonan.status_permohonan }}</td>
          <td class="p-2 border">
            <a
              v-if="permohonan.file_path"
              :href="`${baseUrl}/files/uploads/${permohonan.file_path}`"
              target="_blank"
              class="text-blue-500 underline"
            >
              Lihat / Download
            </a>
            <span v-else>-</span>
          </td>
          <td class="p-2 border flex gap-2">
            <button
              v-if="permohonan.status_permohonan === 'pending'"
              class="bg-green-500 text-white px-2 py-1 rounded"
              @click="approvePermohonan(permohonan.id)"
            >
              Setuju
            </button>
            <button
              v-if="permohonan.status_permohonan === 'pending'"
              class="bg-red-500 text-white px-2 py-1 rounded"
              @click="rejectPermohonan(permohonan.id)"
            >
              Tolak
            </button>
            <button
              class="bg-blue-500 text-white px-2 py-1 rounded"
              @click="viewDetail(permohonan.id)"
            >
              Detail
            </button>
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
        class="px-3 py-1 border rounded"
        :disabled="page === 1"
        @click="prevPage"
      >
        Prev
      </button>
      <span>Halaman {{ page }}</span>
      <button
        class="px-3 py-1 border rounded"
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

    const page = ref(1);
    const perPage = ref(10);

    // Ambil dari env VITE_API_BASE_URL, misal http://127.0.0.1:4000
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
          status: "pending",
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

    const approvePermohonan = async (id: string) => {
      if (!confirm("Apakah Anda yakin ingin menyetujui permohonan ini?"))
        return;
      try {
        await apiClient.post(`/permohonan/${id}/sign`);
        fetchPermohonan();
      } catch (error) {
        console.error("Gagal menyetujui permohonan:", error);
        alert("Gagal menyetujui permohonan");
      }
    };

    const rejectPermohonan = async (id: string) => {
      const komentar = prompt("Masukkan komentar penolakan:");
      if (!komentar) return;
      try {
        await apiClient.post(`/permohonan/${id}/reject`, {
          komentar_penolakan: komentar,
        });
        fetchPermohonan();
      } catch (error) {
        console.error("Gagal menolak permohonan:", error);
        alert("Gagal menolak permohonan");
      }
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
      page,
      perPage,
      baseUrl,
      fetchPermohonan,
      viewDetail,
      approvePermohonan,
      rejectPermohonan,
      nextPage,
      prevPage,
    };
  },
};
</script>

<style scoped>
/* opsional styling */
</style>
