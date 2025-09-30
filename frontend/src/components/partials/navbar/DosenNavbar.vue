<!-- Header Dosen - Simple Navbar -->
<template>
  <header
    class="fixed top-0 left-0 w-full h-16 bg-white/95 backdrop-blur-sm shadow-sm flex items-center justify-between px-8 border-b border-gray-100 z-50"
  >
    <!-- Kiri: Logo + Nama FTI -->
    <div class="flex items-center space-x-3">
      <div
        class="w-9 h-9 rounded-lg bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center shadow-sm"
      >
        <img
          src="@/assets/logo.png"
          alt="Logo FTI"
          class="w-6 h-6 object-contain"
        />
      </div>
      <span class="font-semibold text-gray-800 text-lg tracking-tight">
        FTI UKSW
      </span>
    </div>

    <!-- Kanan: Nama dosen -->
    <div v-if="dosen" class="flex items-center space-x-2">
      <CircleUser class="w-5 h-5 text-gray-600" />
      <span class="text-gray-700 font-medium text-sm">{{ dosen.nama }}</span>
    </div>
  </header>
</template>

<script setup lang="ts">
import { CircleUser } from "lucide-vue-next";
import { useAuthStore } from "@/stores/auth";

const { user: dosen } = useAuthStore(); // asumsinya role dosen
</script>
