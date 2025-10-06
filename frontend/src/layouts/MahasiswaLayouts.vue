<!-- #MahasiswaLayouts.vue -->
<script setup lang="ts">
import MahasiswaNavbar from "@/components/partials/navbar/MahasiswaNavbar.vue";
import MahasiswaSidebar from "@/components/partials/sidebar/MahasiswaSidebar.vue";
import { ref } from "vue";

const isSidebarOpen = ref(false);

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value;
};
</script>

<template>
  <div class="flex flex-col min-h-screen bg-gray-50 overflow-x-hidden">
    <MahasiswaNavbar
      :is-sidebar-open="isSidebarOpen"
      @toggle-sidebar="toggleSidebar"
    />

    <div class="flex flex-1 pt-16">
      <MahasiswaSidebar
        :class="[
          'fixed top-16 h-[calc(100vh-4rem)] w-64 border-r transition-transform duration-300 ease-in-out z-40',
          {
            'translate-x-0': isSidebarOpen,
            '-translate-x-full': !isSidebarOpen,
          },
          'lg:translate-x-0 lg:block', // Selalu terlihat di desktop
        ]"
      />

      <div
        v-if="isSidebarOpen"
        @click="toggleSidebar"
        class="fixed inset-0 bg-black/30 z-30 lg:hidden"
      ></div>

      <main
        :class="[
          'p-4 w-full transition-all duration-300 ease-in-out',
          // Di mobile: w-full (default)
          // Di desktop: ditambahkan margin-left 64 (lebar sidebar)
          'lg:ml-64',
        ]"
      >
        <RouterView />
      </main>
    </div>
  </div>
</template>
