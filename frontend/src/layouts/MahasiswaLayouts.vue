<template>
  <div class="flex flex-col min-h-screen">
    <MahasiswaNavbar />

    <!-- Main layout: Sidebar + Content -->
    <div class="flex flex-1">
      <!-- Sidebar -->
      <MahasiswaSidebar class="w-64 border-r" />

      <!-- Main Content -->
      <main class="ml-64 mt-16 p-4 w-full">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import MahasiswaNavbar from "@/components/partials/navbar/MahasiswaNavbar.vue";
import MahasiswaSidebar from "@/components/partials/sidebar/MahasiswaSidebar.vue";
</script>
