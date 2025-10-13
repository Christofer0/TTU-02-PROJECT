<template>
  <div
    class="bg-white/95 backdrop-blur-sm border-r border-gray-100 flex flex-col justify-between"
    style="/* Kelas posisi sudah diatur di MahasiswaLayouts.vue */"
  >
    <div class="mt-6 px-6 space-y-2 **overflow-y-auto**">
      <RouterLink
        to="/mahasiswa/dashboard"
        class="group flex items-center space-x-3 px-4 py-3 rounded-xl hover:bg-gray-50 transition-all duration-200 hover:scale-[1.02]"
        active-class="bg-gradient-to-r from-blue-50 to-blue-100 text-blue-700 shadow-sm border-l-4 border-blue-500"
      >
        <div
          class="w-8 h-8 bg-gradient-to-br from-blue-400 to-blue-500 rounded-lg flex items-center justify-center shadow-sm group-hover:shadow-md transition-shadow"
        >
          <svg
            class="w-4 h-4 text-white"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
            />
          </svg>
        </div>
        <span class="font-medium text-gray-700 group-hover:text-gray-900"
          >Dashboard</span
        >
      </RouterLink>

      <RouterLink
        to="/mahasiswa/profile"
        class="group flex items-center space-x-3 px-4 py-3 rounded-xl hover:bg-gray-50 transition-all duration-200 hover:scale-[1.02]"
        active-class="bg-gradient-to-r from-blue-50 to-blue-100 text-blue-700 shadow-sm border-l-4 border-blue-500"
      >
        <div
          class="w-8 h-8 bg-gradient-to-br from-emerald-400 to-emerald-500 rounded-lg flex items-center justify-center shadow-sm group-hover:shadow-md transition-shadow"
        >
          <svg
            class="w-4 h-4 text-white"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
            />
          </svg>
        </div>
        <span class="font-medium text-gray-700 group-hover:text-gray-900"
          >Profile</span
        >
      </RouterLink>

      <!-- <RouterLink
        to="/mahasiswa/change-password"
        class="group flex items-center space-x-3 px-4 py-3 rounded-xl hover:bg-gray-50 transition-all duration-200 hover:scale-[1.02]"
        active-class="bg-gradient-to-r from-blue-50 to-blue-100 text-blue-700 shadow-sm border-l-4 border-blue-500"
      >
        <div
          class="w-8 h-8 bg-gradient-to-br from-amber-400 to-amber-500 rounded-lg flex items-center justify-center shadow-sm group-hover:shadow-md transition-shadow"
        >
          <svg
            class="w-4 h-4 text-white"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"
            />
          </svg>
        </div>
        <span class="font-medium text-gray-700 group-hover:text-gray-900"
          >Ganti Password</span
        >
      </RouterLink> -->

      <RouterLink
        to="/mahasiswa/history"
        class="group flex items-center space-x-3 px-4 py-3 rounded-xl hover:bg-gray-50 transition-all duration-200 hover:scale-[1.02]"
        active-class="bg-gradient-to-r from-blue-50 to-blue-100 text-blue-700 shadow-sm border-l-4 border-blue-500"
      >
        <div
          class="w-8 h-8 bg-gradient-to-br from-amber-400 to-amber-500 rounded-lg flex items-center justify-center shadow-sm group-hover:shadow-md transition-shadow"
        >
          <svg
            class="w-4 h-4 text-white"
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
        <span class="font-medium text-gray-700 group-hover:text-gray-900"
          >History</span
        >
      </RouterLink>

      <div class="h-4"></div>
    </div>

    <div class="px-6 py-6 border-t border-gray-100 mt-95">
      <button
        @click="handleLogout"
        class="group w-full flex items-center space-x-3 px-4 py-3 rounded-xl bg-gradient-to-r from-red-50 to-red-100 hover:from-red-100 hover:to-red-200 text-red-600 hover:text-red-700 transition-all duration-200 hover:scale-[1.02] shadow-sm hover:shadow-md"
      >
        <div
          class="w-8 h-8 bg-gradient-to-br from-red-400 to-red-500 rounded-lg flex items-center justify-center shadow-sm group-hover:shadow-md transition-shadow"
        >
          <svg
            class="w-4 h-4 text-white"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
            />
          </svg>
        </div>
        <span class="font-medium">Logout</span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";

const auth = useAuthStore();
const router = useRouter();

function handleLogout() {
  auth.logout();
  router.push({ name: "Login" });
}
</script>
