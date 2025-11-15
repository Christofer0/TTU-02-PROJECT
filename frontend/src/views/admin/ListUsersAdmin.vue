<script setup lang="ts">
import { ref, onMounted } from "vue";
import { apiClient } from "@/lib/axios";
import { Users, UserCog, XCircle, Loader2, CheckCircle } from "lucide-vue-next";
import type { User } from "@/types/models/user.type";

const baseUrl = import.meta.env.VITE_API_URL;

// ==================
// STATE
// ==================
const users = ref<any[]>([]);
const selectedRole = ref("semua");
const roles = ref(["semua", "dosen", "mahasiswa"]);
const loading = ref(false);
const error = ref<string | null>(null);
import Swal from "sweetalert2";

const formatDate = (dateString: string) => {
  if (!dateString) return "-";

  // Coba parse langsung
  let date = new Date(dateString);

  // Jika gagal, coba tambahkan Z (buat ISO tanpa Z)
  if (isNaN(date.getTime())) {
    date = new Date(dateString + "Z");
  }

  // Jika tetap invalid
  if (isNaN(date.getTime())) return "-";

  return date.toLocaleString("id-ID", {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    timeZone: "Asia/Jakarta", // ubah sesuai zona kamu
  });
};

// ==================
// FETCH DATA
// ==================
async function fetchUsers(role: string) {
  try {
    loading.value = true;
    error.value = null;
    let res;
    if (role === "semua") {
      res = await apiClient.get(`/admin/users`);
    } else if (role === "dosen") {
      res = await apiClient.get(`admin/users/role/${role}`);
      users.value = (res.data.data || []).map((u: any, index: number) => ({
        no: index + 1,
        nama_lengkap: u.nama_lengkap,
        nomor_induk: u.nomor_induk,
        jabatan: u.jabatan,
        fakultas: u.fakultas,
        email: u.email,
        status: u.status,
        terakhir_login: u.terakhir_login,
      }));
    } else if (role === "mahasiswa") {
      res = await apiClient.get(`admin/users/role/${role}`);
      users.value = (res.data.data || []).map((u: any) => ({
        nama: u.nama,
        nomor_induk: u.nomor_induk,
        email: u.email,
        no_hp: u.no_hp,
        nama_prodi: u.nama_prodi,
        semester: u.semester,
        is_active: u.is_active,
        last_login: u.last_login,
      }));
    } else {
      res = await apiClient.get(`admin/users/role/${role}`);
    }
    users.value = res.data.data || [];
  } catch (err: any) {
    console.error("Error fetchUsers:", err);
    error.value = "Gagal memuat data pengguna";
  } finally {
    loading.value = false;
  }
}

const toggleStatus = async (user: User, action: "activate" | "deactivate") => {
  if (loading.value) return;
  loading.value = true;

  try {
    // buat pesan konfirmasi dinamis
    const message =
      action === "activate"
        ? `Yakin ingin activate ${user.role} dengan NIM ${user.nomor_induk}?`
        : `Yakin ingin deactivate ${user.role} dengan NIM ${user.nomor_induk}?`;

    // tampilkan konfirmasi dan hentikan jika dibatalkan
    const result = await Swal.fire({
      title: "Konfirmasi",
      html: message,
      icon: "question",
      showCancelButton: true,
      confirmButtonText: "Ya, lanjutkan",
      cancelButtonText: "Batal",
    });

    if (!result.isConfirmed) {
      loading.value = false;
      return; // <-- langsung berhenti di sini kalau user cancel
    }

    // lanjutkan request ke server hanya jika user menekan OK
    const response = await apiClient.post(`admin/users/${user.id}/${action}`);
    console.log("Response:", response.data);

    // update status di UI
    user.is_active = action === "activate";

    Swal.fire({
      title: "Berhasil",
      text: "Status user berhasil diperbaharui",
      icon: "success",
    });
  } catch (error) {
    console.error("Error:", error);
    Swal.fire({
      title: "Gagal",
      text: "Gagal memperbaharui status user",
      icon: "error",
    });
  } finally {
    loading.value = false;
  }
};

// ==================
// UI LOGIC
// ==================
function selectRole(role: string) {
  selectedRole.value = role;
  fetchUsers(role);
}

onMounted(() => {
  fetchUsers(selectedRole.value);
});
</script>

<template>
  <div class="min-h-screen bg-slate-50 p-6">
    <div class="max-w-7xl mx-auto space-y-6">
      <!-- Header -->
      <div class="bg-white border-l-4 border-slate-500 shadow-sm px-6 py-4">
        <h2 class="text-2xl font-bold text-slate-900 flex items-center gap-2">
          <Users class="w-6 h-6 text-slate-500" />
          Daftar Pengguna (Admin)
        </h2>
        <p class="text-sm text-slate-600 mt-1">
          Lihat dan kelola pengguna berdasarkan peran (role)
        </p>
      </div>

      <!-- Filter Roles -->
      <div class="flex flex-wrap gap-3">
        <button
          v-for="role in roles"
          :key="role"
          @click="selectRole(role)"
          class="px-4 py-2 rounded-lg border font-semibold text-sm transition-all"
          :class="{
            'bg-slate-600 text-white shadow-sm': selectedRole === role,
            'bg-white text-slate-700 border-slate-300 hover:bg-slate-100':
              selectedRole !== role,
          }"
        >
          {{ role.charAt(0).toUpperCase() + role.slice(1) }}
        </button>
      </div>

      <!-- Table -->
      <div
        class="bg-white shadow-sm rounded-lg border border-slate-200 overflow-hidden lg:w-[calc(100dvw-310px)]"
      >
        <!-- w-[calc(dvw-300px)] -->
        <div class="bg-slate-600 px-6 py-4 border-b border-slate-500">
          <h3 class="text-lg font-semibold text-white flex items-center gap-2">
            <UserCog class="w-5 h-5" />
            {{
              selectedRole === "semua"
                ? "Semua Pengguna"
                : "Role: " + selectedRole
            }}
          </h3>
        </div>

        <div class="p-6">
          <!-- Loading -->
          <div v-if="loading" class="text-center py-12">
            <Loader2 class="w-12 h-12 text-slate-500 animate-spin mx-auto" />
            <p class="text-slate-600 mt-4 font-medium">Memuat data...</p>
          </div>

          <!-- Error -->
          <div v-else-if="error" class="text-center py-12">
            <div
              class="inline-flex items-center justify-center w-16 h-16 bg-rose-100 rounded-full mb-4"
            >
              <XCircle class="w-8 h-8 text-rose-600" />
            </div>
            <p class="text-slate-700 font-medium">{{ error }}</p>
          </div>

          <!-- Empty -->
          <div v-else-if="users.length === 0" class="text-center py-12">
            <div
              class="inline-flex items-center justify-center w-16 h-16 bg-slate-100 rounded-full mb-4"
            >
              <Users class="w-8 h-8 text-slate-400" />
            </div>
            <p class="text-slate-600 font-medium">
              Tidak ada pengguna dengan role ini
            </p>
          </div>

          <!-- Table -->
          <div v-else class="w-full overflow-x-auto">
            <table v-if="selectedRole === 'dosen'" class="min-w-max w-full">
              <thead>
                <tr class="bg-slate-50 border-y border-slate-200">
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    No
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Nama Lengkap
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Nomor Induk
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Jabatan
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Fakultas
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Email
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    No HP
                  </th>
                  <th
                    class="px-4 py-3 text-center text-xs font-bold text-slate-700 uppercase"
                  >
                    Status Aktif
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Terakhir Login
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-200">
                <tr
                  v-for="(user, index) in users"
                  :key="user.nomor_induk"
                  class="hover:bg-slate-50 transition-colors"
                >
                  <td class="px-4 py-4 font-semibold text-slate-900">
                    {{ index + 1 }}
                  </td>
                  <td class="px-4 py-4 text-slate-800">
                    {{ user.nama_lengkap }}
                  </td>
                  <td class="px-4 py-4 text-slate-700">
                    {{ user.nomor_induk }}
                  </td>
                  <td class="px-4 py-4 text-slate-700">{{ user.jabatan }}</td>
                  <td class="px-4 py-4 text-slate-700">
                    {{ user.nama_fakultas }}
                  </td>
                  <td class="px-4 py-4 text-slate-700">{{ user.email }}</td>
                  <td class="px-4 py-4 text-slate-700">{{ user.no_hp }}</td>
                  <td class="px-4 py-4 text-center">
                    <span
                      class="text-xs font-semibold px-3 py-1.5 rounded-md"
                      :class="{
                        'bg-green-100 text-green-700': user.is_active,
                        'bg-rose-100 text-rose-600': !user.is_active,
                      }"
                    >
                      {{ user.is_active ? "Aktif" : "Nonaktif" }}
                    </span>
                  </td>
                  <td class="px-4 py-4 text-slate-600 text-sm">
                    {{ formatDate(user.last_login) }}
                  </td>
                </tr>
              </tbody>
            </table>
            <table
              v-else-if="selectedRole === 'mahasiswa'"
              class="min-w-max w-full"
            >
              <thead>
                <tr class="bg-slate-50 border-y border-slate-200">
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    No
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Nama Lengkap
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Nomor Induk
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Email
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    No HP
                  </th>
                  <th
                    class="px-4 py-3 text-center text-xs font-bold text-slate-700 uppercase"
                  >
                    Nama Program Studi
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Semester
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Status Aktif
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Terakhir Login
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-200">
                <tr
                  v-for="(user, index) in users"
                  :key="user.nomor_induk"
                  class="hover:bg-slate-50 transition-colors"
                >
                  <td class="px-4 py-4 font-semibold text-slate-900">
                    {{ index + 1 }}
                  </td>
                  <td class="px-4 py-4 text-slate-800">
                    {{ user.nama }}
                  </td>
                  <td class="px-4 py-4 text-slate-700">
                    {{ user.nomor_induk }}
                  </td>
                  <td class="px-4 py-4 text-slate-700">{{ user.email }}</td>
                  <td class="px-4 py-4 text-slate-700">
                    {{ user.no_hp }}
                  </td>
                  <td class="px-4 py-4 text-slate-700">
                    {{ user.nama_prodi }}
                  </td>
                  <td class="px-4 py-4 text-slate-700">{{ user.semester }}</td>
                  <td class="px-4 py-4 text-center">
                    <span
                      class="text-xs font-semibold px-3 py-1.5 rounded-md"
                      :class="{
                        'bg-green-100 text-green-700': user.is_active,
                        'bg-rose-100 text-rose-600': !user.is_active,
                      }"
                    >
                      {{ user.is_active ? "Aktif" : "Nonaktif" }}
                    </span>
                  </td>
                  <td class="px-4 py-4 text-slate-600 text-sm">
                    {{ formatDate(user.last_login) }}
                  </td>
                </tr>
              </tbody>
            </table>

            <table v-else class="w-full">
              <!-- TABLE ADMIN -->

              <thead>
                <tr class="bg-slate-50 border-y border-slate-200">
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    No
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Nama
                  </th>
                  <th
                    class="px-4 py-3 text-left text-xs font-bold text-slate-700 uppercase"
                  >
                    Email
                  </th>
                  <th
                    class="px-4 py-3 text-center text-xs font-bold text-slate-700 uppercase"
                  >
                    Role
                  </th>
                  <th
                    class="px-4 py-3 text-center text-xs font-bold text-slate-700 uppercase"
                  >
                    Status
                  </th>
                  <th
                    class="px-4 py-3 text-center text-xs font-bold text-slate-700 uppercase"
                  >
                    Action
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-200">
                <tr
                  v-for="(user, index) in users"
                  :key="user.id"
                  class="hover:bg-slate-50 transition-colors"
                >
                  <td class="px-4 py-4 font-semibold">{{ index + 1 }}</td>
                  <td class="px-4 py-4 text-slate-800">{{ user.nama }}</td>
                  <td class="px-4 py-4 text-slate-700">{{ user.email }}</td>
                  <td class="px-4 py-4 text-center">
                    <span
                      class="inline-block px-3 py-1.5 text-xs font-bold rounded-md"
                      :class="{
                        'bg-slate-200 text-slate-700': user.role === 'admin',
                        'bg-blue-100 text-blue-700': user.role === 'dosen',
                        'bg-violet-100 text-violet-700':
                          user.role === 'mahasiswa',
                      }"
                    >
                      {{ user.role }}
                    </span>
                  </td>
                  <td class="px-4 py-4 text-center">
                    <span
                      class="text-xs font-semibold px-3 py-1.5 rounded-md"
                      :class="{
                        'bg-green-100 text-green-700': user.is_active,
                        'bg-rose-100 text-rose-600': !user.is_active,
                      }"
                    >
                      {{ user.is_active ? "Aktif" : "Nonaktif" }}
                    </span>
                  </td>

                  <td v-if="user.role !== 'admin'" class="text-center">
                    <button
                      v-if="user.is_active"
                      @click="toggleStatus(user, 'deactivate')"
                      class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm font-semibold text-red-600 bg-red-50 border border-red-200 hover:bg-red-100 transition-all duration-200 shadow-sm"
                    >
                      <XCircle class="w-4 h-4" /> Nonaktifkan
                    </button>
                    <button
                      v-else
                      @click="toggleStatus(user, 'activate')"
                      class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm font-semibold text-green-600 bg-green-50 border border-green-200 hover:bg-green-100 transition-all duration-200 shadow-sm"
                    >
                      <CheckCircle class="w-4 h-4" /> Aktifkan
                    </button>
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
