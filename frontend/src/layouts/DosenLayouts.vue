<template>
  <div class="flex flex-col min-h-screen">
    <DosenNavbar />

    <!-- Main layout: Sidebar + Content -->
    <div class="flex flex-1">
      <!-- Sidebar -->
      <DosenSidebar class="w-64 border-r" />

      <!-- Main Content -->
      <main class="ml-64 mt-16 p-4 w-full">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import DosenNavbar from "@/components/partials/navbar/DosenNavbar.vue";
import DosenSidebar from "@/components/partials/sidebar/DosenSidebar.vue";
</script>
