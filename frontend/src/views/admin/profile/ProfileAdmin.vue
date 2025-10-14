<script setup lang="ts">
import { useAuthStore } from "@/stores/auth";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const { user } = useAuthStore();
</script>
<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 to-emerald-50 p-6">
    <div class="max-w-6xl mx-auto space-y-6">
      <!-- Page Header -->
      <div class="bg-white border-l-4 border-emerald-600 shadow-sm px-6 py-4">
        <h2 class="text-2xl font-bold text-gray-900">Profil Admin</h2>
        <p class="text-sm text-gray-600 mt-1">
          Informasi dan data personal administrator sistem
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Kartu Profil Admin -->
        <Card class="border border-gray-200 shadow-sm bg-white">
          <div class="bg-emerald-700 px-6 py-4 border-b border-emerald-600">
            <h3 class="text-lg font-bold text-white flex items-center gap-2">
              <svg
                class="w-5 h-5"
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
              Data Admin
            </h3>
          </div>

          <CardContent class="flex flex-col items-center text-center p-8">
            <!-- Profile Image -->
            <div class="relative mb-6">
              <div
                class="w-32 h-32 rounded-full border-4 border-emerald-100 overflow-hidden bg-gray-100"
              >
                <img
                  src="@/assets/default-profile.png"
                  alt="Foto Admin"
                  class="w-full h-full object-cover"
                />
              </div>
            </div>

            <!-- User Info -->
            <div class="space-y-3 mb-6 w-full">
              <h2 class="text-2xl font-bold text-gray-900">
                {{ user?.nama }}
              </h2>
              <div
                class="inline-flex items-center gap-2 bg-emerald-50 border border-emerald-200 px-4 py-2 rounded-lg"
              >
                <svg
                  class="w-4 h-4 text-emerald-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 
                    0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0
                    c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2"
                  />
                </svg>
                <span class="text-sm font-bold text-emerald-700">
                  {{ user?.nomor_induk }}
                </span>
              </div>
            </div>

            <!-- Edit Button -->
            <Button
              @click="$router.push({ name: 'EditProfileAdmin' })"
              class="w-full bg-emerald-600 hover:bg-emerald-700 text-white border-0 rounded-lg py-3 font-bold uppercase text-sm tracking-wide shadow-sm h-12"
            >
              <span class="flex items-center justify-center gap-2">
                <svg
                  class="w-4 h-4"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M11 5H6a2 2 0 00-2 2v11a2 2 
                    0 002 2h11a2 2 0 002-2v-5m-1.414-9.414
                    a2 2 0 112.828 2.828L11.828 15H9v-2.828
                    l8.586-8.586z"
                  />
                </svg>
                <span>Ubah Data Admin</span>
              </span>
            </Button>
          </CardContent>
        </Card>
      </div>
    </div>
  </div>
</template>
