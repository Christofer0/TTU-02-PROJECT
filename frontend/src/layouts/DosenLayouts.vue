<template>
  <div class="flex flex-col min-h-screen">
    <DosenNavbar
      :is-sidebar-open="isSidebarOpen"
      @toggle-sidebar="toggleSidebar"
    />

    <!-- Main layout: Sidebar + Content -->
    <div class="flex flex-1 pt-16">
      <DosenSidebar
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

<script setup lang="ts">
import DosenNavbar from "@/components/partials/navbar/DosenNavbar.vue";
import DosenSidebar from "@/components/partials/sidebar/DosenSidebar.vue";
import { ref } from "vue";

const isSidebarOpen = ref(false);

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value;
};
</script>
