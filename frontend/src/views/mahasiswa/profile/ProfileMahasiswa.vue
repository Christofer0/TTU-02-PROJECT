<script setup lang="ts">
import { useAuthStore } from "@/stores/auth";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
const { user } = useAuthStore();
</script>

<!-- Profile Content - Softer Design -->
<template>
  <div class="p-8 grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-6xl mx-auto">
    <!-- Kartu Profil Mahasiswa -->
    <Card
      class="border-0 shadow-lg shadow-blue-50 bg-gradient-to-br from-white to-blue-50/30 overflow-hidden"
    >
      <CardContent class="flex flex-col items-center text-center p-8">
        <!-- Profile Image dengan efek soft -->
        <div class="relative mb-6">
          <img
            src="@/assets/default-profile.png"
            alt="Foto Profile"
            class="w-32 h-32 rounded-full object-cover shadow-lg shadow-blue-100 border-4 border-white"
          />
          <div
            class="absolute inset-0 rounded-full bg-gradient-to-t from-blue-600/10 to-transparent"
          ></div>
        </div>

        <!-- User Info -->
        <div class="space-y-2 mb-6">
          <h2 class="text-2xl font-semibold text-gray-800 tracking-tight">
            {{ user?.nama }}
          </h2>
          <p
            class="text-gray-500 font-medium text-sm bg-gray-100 px-3 py-1 rounded-full inline-block"
          >
            {{ user?.nomor_induk }}
          </p>
        </div>

        <!-- Button dengan style yang lebih soft -->
        <Button
          @click="$router.push({ name: 'EditProfileMahasiswa' })"
          class="w-full bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white shadow-lg shadow-blue-200 border-0 rounded-xl py-3 font-medium transition-all duration-300 hover:scale-[1.02] hover:shadow-xl hover:shadow-blue-300"
        >
          <span class="flex items-center justify-center space-x-2">
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
                d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
              />
            </svg>
            <span>Ubah Data Mahasiswa</span>
          </span>
        </Button>
      </CardContent>
    </Card>

    <!-- Kartu QR Code -->
    <Card
      class="border-0 shadow-lg shadow-gray-50 bg-gradient-to-br from-white to-gray-50/50 overflow-hidden"
    >
      <CardHeader class="pb-4">
        <CardTitle
          class="text-gray-800 flex items-center gap-3 text-xl font-semibold"
        >
          <div
            class="w-10 h-10 bg-gradient-to-br from-emerald-400 to-emerald-500 rounded-lg flex items-center justify-center shadow-sm"
          >
            <svg
              class="w-5 h-5 text-white"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 4v1m6 11h2m-6 0h-2v4m0-11v3m0 0h.01M12 12h4.01M16 16h4.01M12 8h4.01M16 4h4.01M4 4h4.01M4 8h4.01m0 0h.01M4 12h4.01m0 0h.01M4 16h4.01m0 0h.01"
              />
            </svg>
          </div>
          QR Mahasiswa
        </CardTitle>
        <CardDescription class="text-gray-600 leading-relaxed">
          QR Code ini berisi data mahasiswa dan total pengajuan surat Anda untuk
          kemudahan akses.
        </CardDescription>
      </CardHeader>
      <CardContent class="flex flex-col items-center justify-center pt-4">
        <!-- QR Code Container -->
        <div class="relative">
          <div
            class="w-48 h-48 bg-white rounded-2xl border-2 border-gray-100 shadow-lg flex items-center justify-center relative overflow-hidden"
          >
            <!-- QR Pattern Background -->
            <div class="absolute inset-2 opacity-10">
              <div class="grid grid-cols-8 gap-1 h-full">
                <div class="bg-gray-800 rounded-sm"></div>
                <div class="bg-gray-800 rounded-sm"></div>
                <div class="bg-gray-800 rounded-sm"></div>
                <!-- Add more pattern elements as needed -->
              </div>
            </div>
            <span class="text-gray-400 font-medium z-10">QR Code</span>
          </div>
          <!-- Subtle glow effect -->
          <div
            class="absolute inset-0 rounded-2xl bg-gradient-to-t from-blue-500/5 to-transparent -z-10 blur-xl"
          ></div>
        </div>

        <!-- Info text -->
        <p class="text-xs text-gray-500 mt-4 text-center">
          Scan untuk akses cepat informasi mahasiswa
        </p>
      </CardContent>
    </Card>
  </div>
</template>
