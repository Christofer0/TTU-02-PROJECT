<!-- Header Component - Softer Design -->
<template>
  <header
    class="fixed top-0 left-0 w-full h-16 bg-white/95 backdrop-blur-sm shadow-sm flex items-center justify-between px-8 border-b border-gray-100 z-50"
  >
    <!-- Kiri: Logo + Nama FTI dengan spacing yang lebih baik -->
    <div class="flex items-center space-x-3">
      <div
        class="w-9 h-9 rounded-lg bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center shadow-sm"
      >
        <img
          src="@/assets/logo.png"
          alt="Logo"
          class="w-6 h-6 object-contain"
        />
      </div>
      <span class="font-semibold text-gray-800 text-lg tracking-tight"
        >FTI UKSW</span
      >
    </div>

    <!-- Kanan: Nama user dengan ikon yang lebih soft -->
    <div
      v-if="user"
      class="flex items-center space-x-3 bg-gray-50 rounded-full px-4 py-2"
    >
      <div
        class="w-8 h-8 bg-gradient-to-br from-gray-400 to-gray-500 rounded-full flex items-center justify-center"
      >
        <CircleUser class="w-5 h-5 text-white" />
      </div>
      <span class="text-gray-700 font-medium text-sm">{{ user.nama }}</span>
    </div>
  </header>
</template>

<script setup lang="ts">
import { CircleUser } from "lucide-vue-next";
import { useAuthStore } from "@/stores/auth";
const { user } = useAuthStore();
</script>
