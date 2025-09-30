<template>
  <div class="flex flex-col min-h-screen">
    <AdminNavbar />

    <!-- Main layout: Sidebar + Content -->
    <div class="flex flex-1">
      <!-- Sidebar -->
      <AdminSidebar class="w-64 border-r" />

      <!-- Main Content -->
      <main class="ml-64 mt-16 p-4 w-full">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import AdminNavbar from "@/components/partials/navbar/AdminNavbar.vue";
import AdminSidebar from "@/components/partials/sidebar/AdminSidebar.vue";
</script>
