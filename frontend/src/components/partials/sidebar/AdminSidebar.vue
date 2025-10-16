<template>
  <div
    class="bg-white/95 backdrop-blur-sm border-r border-gray-100 flex flex-col h-full"
  >
    <!-- Bagian atas: menu -->
    <div
      class="px-6 py-6 border-t border-gray-100 sticky bottom-0 bg-white/95 backdrop-blur-sm"
    >
      <!-- Dashboard -->
      <RouterLink
        to="/admin/dashboard"
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
        <span class="font-medium text-gray-700 group-hover:text-gray-900">
          Dashboard
        </span>
      </RouterLink>

      <!-- Profile -->
      <RouterLink
        to="/admin/profile"
        class="group flex items-center space-x-3 px-4 py-3 rounded-xl hover:bg-gray-50 transition-all duration-200 hover:scale-[1.02]"
        active-class="bg-gradient-to-r from-green-50 to-green-100 text-green-700 shadow-sm border-l-4 border-green-500"
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
        <span class="font-medium text-gray-700 group-hover:text-gray-900">
          Profile
        </span>
      </RouterLink>

      <!-- Profile -->
      <RouterLink
        to="/admin/users"
        class="group flex items-center space-x-3 px-4 py-3 rounded-xl hover:bg-gray-50 transition-all duration-200 hover:scale-[1.02]"
        active-class="bg-gradient-to-r from-slate-50 to-slate-100 text-slate-700 shadow-sm border-l-4 border-slate-500"
      >
        <div
          class="w-8 h-8 bg-gradient-to-br from-slate-400 to-slate-500 rounded-lg flex items-center justify-center shadow-sm group-hover:shadow-md transition-shadow"
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
        <span class="font-medium text-gray-700 group-hover:text-gray-900">
          Users
        </span>
      </RouterLink>

      <!-- Permohonan (kuning-oranye) -->
      <RouterLink
        to="/admin/list-permohonan"
        class="group flex items-center space-x-3 px-4 py-3 rounded-xl hover:bg-gray-50 transition-all duration-200 hover:scale-[1.02]"
        active-class="bg-gradient-to-r from-yellow-50 to-orange-100 text-orange-700 shadow-sm border-l-4 border-orange-500"
      >
        <div
          class="w-8 h-8 bg-gradient-to-br from-yellow-400 to-orange-500 rounded-lg flex items-center justify-center shadow-sm group-hover:shadow-md transition-shadow"
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
        <span class="font-medium text-gray-700 group-hover:text-gray-900">
          Permohonan
        </span>
      </RouterLink>

      <!-- History (biru-keunguan) -->
      <RouterLink
        to="/admin/history"
        class="group flex items-center space-x-3 px-4 py-3 rounded-xl hover:bg-gray-50 transition-all duration-200 hover:scale-[1.02]"
        active-class="bg-gradient-to-r from-indigo-50 to-purple-100 text-indigo-700 shadow-sm border-l-4 border-indigo-500"
      >
        <div
          class="w-8 h-8 bg-gradient-to-br from-indigo-400 to-purple-500 rounded-lg flex items-center justify-center shadow-sm group-hover:shadow-md transition-shadow"
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
        <span class="font-medium text-gray-700 group-hover:text-gray-900">
          History
        </span>
      </RouterLink>
    </div>

    <!-- Bagian bawah: Logout -->
    <div class="px-6 py-6 border-t border-gray-100">
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
