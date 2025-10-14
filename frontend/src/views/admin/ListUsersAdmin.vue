<script setup lang="ts">
import { ref, onMounted } from "vue";
import { apiClient } from "@/lib/axios";
import { Users, UserCog, XCircle, Loader2 } from "lucide-vue-next";

const baseUrl = import.meta.env.VITE_API_URL;

// ==================
// STATE
// ==================
const users = ref<any[]>([]);
const selectedRole = ref("semua");
const roles = ref(["semua", "admin", "dosen", "mahasiswa"]);
const loading = ref(false);
const error = ref<string | null>(null);

// ==================
// FETCH DATA
// ==================
async function fetchUsers(role: string) {
  try {
    loading.value = true;
    error.value = null;
    let res;
    if (role === "semua") {
      res = await apiClient.get(`/users`);
    } else {
      res = await apiClient.get(`/users/role/${role}`);
    }
    users.value = res.data.data || [];
  } catch (err: any) {
    console.error("Error fetchUsers:", err);
    error.value = "Gagal memuat data pengguna";
  } finally {
    loading.value = false;
  }
}

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
        class="bg-white shadow-sm rounded-lg border border-slate-200 overflow-hidden"
      >
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
          <div v-else class="overflow-x-auto">
            <table class="w-full">
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
                        'bg-green-100 text-green-700':
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
                        'bg-green-100 text-green-700': user.active,
                        'bg-rose-100 text-rose-600': !user.active,
                      }"
                    >
                      {{ user.active ? "Aktif" : "Nonaktif" }}
                    </span>
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
