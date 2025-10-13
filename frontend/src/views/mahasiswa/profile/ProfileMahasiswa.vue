<script setup lang="ts">
import { useAuthStore } from "@/stores/auth";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
const { user } = useAuthStore();
</script>

<template>
  <div class="min-h-screen bg-gray-50 p-6">
    <div class="max-w-6xl mx-auto space-y-6">
      <!-- Page Header -->
      <div class="bg-white border-l-4 border-blue-600 shadow-sm px-6 py-4">
        <h2 class="text-2xl font-bold text-gray-900">Profil Mahasiswa</h2>
        <p class="text-sm text-gray-600 mt-1">
          Informasi dan data pribadi mahasiswa
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Kartu Profil Mahasiswa -->
        <Card class="border border-gray-200 shadow-sm bg-white">
          <div class="bg-gray-800 px-6 py-4 border-b border-gray-700">
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
              Data Mahasiswa
            </h3>
          </div>

          <CardContent class="flex flex-col items-center text-center p-8">
            <!-- Profile Image -->
            <div class="relative mb-6">
              <div
                class="w-32 h-32 rounded-full border-4 border-gray-200 overflow-hidden bg-gray-100"
              >
                <img
                  src="@/assets/default-profile.png"
                  alt="Foto Profile"
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
                class="inline-flex items-center gap-2 bg-blue-50 border border-blue-200 px-4 py-2 rounded-lg"
              >
                <svg
                  class="w-4 h-4 text-blue-600"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2"
                  />
                </svg>
                <span class="text-sm font-bold text-blue-700">
                  {{ user?.nomor_induk }}
                </span>
              </div>
            </div>

            <!-- Edit Button -->
            <Button
              @click="$router.push({ name: 'EditProfileMahasiswa' })"
              class="w-full bg-blue-600 hover:bg-blue-700 text-white border-0 rounded-lg py-3 font-bold uppercase text-sm tracking-wide shadow-sm h-12"
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
                    d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
                  />
                </svg>
                <span>Ubah Data Mahasiswa</span>
              </span>
            </Button>
          </CardContent>
        </Card>

        <!-- Kartu QR Code -->
        <!--<Card class="border border-gray-200 shadow-sm bg-white">
          <div class="bg-gray-800 px-6 py-4 border-b border-gray-700">
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
                  d="M12 4v1m6 11h2m-6 0h-2v4m0-11v3m0 0h.01M12 12h4.01M16 16h4.01M12 8h4.01M16 4h4.01M4 4h4.01M4 8h4.01m0 0h.01M4 12h4.01m0 0h.01M4 16h4.01m0 0h.01"
                />
              </svg>
              QR Code Mahasiswa
            </h3>
          </div>

           <CardContent class="p-8">
            <div
              class="bg-gray-50 border-2 border-gray-200 rounded-lg p-6 mb-4"
            >
              <p
                class="text-sm text-gray-700 font-medium text-center leading-relaxed"
              >
                QR Code ini berisi data mahasiswa dan total pengajuan surat Anda
                untuk kemudahan akses.
              </p>
            </div>


            <div class="flex flex-col items-center justify-center">
              <div class="relative">
                <div
                  class="w-48 h-48 bg-white rounded-lg border-4 border-gray-300 flex items-center justify-center"
                >

                  <div class="absolute inset-4">
                    <div
                      class="grid grid-cols-8 grid-rows-8 gap-1 h-full w-full"
                    >
                      <div class="bg-gray-800 rounded-sm"></div>
                      <div class="bg-gray-800 rounded-sm"></div>
                      <div class="bg-gray-800 rounded-sm"></div>
                      <div class="bg-white rounded-sm"></div>
                      <div class="bg-white rounded-sm"></div>
                      <div class="bg-gray-800 rounded-sm"></div>
                      <div class="bg-gray-800 rounded-sm"></div>
                      <div class="bg-gray-800 rounded-sm"></div>

                      <div class="bg-gray-800 rounded-sm"></div>
                      <div class="bg-white rounded-sm"></div>
                      <div class="bg-white rounded-sm"></div>
                      <div class="bg-white rounded-sm"></div>
                      <div class="bg-white rounded-sm"></div>
                      <div class="bg-white rounded-sm"></div>
                      <div class="bg-white rounded-sm"></div>
                      <div class="bg-gray-800 rounded-sm"></div>

                      <div class="bg-gray-800 rounded-sm"></div>
                      <div class="bg-white rounded-sm"></div>
                      <div class="bg-gray-800 rounded-sm"></div>
                      <div class="bg-gray-800 rounded-sm"></div>
                      <div class="bg-gray-800 rounded-sm"></div>
                      <div class="bg-gray-800 rounded-sm"></div>
                      <div class="bg-white rounded-sm"></div>
                      <div class="bg-gray-800 rounded-sm"></div>
                    </div>
                  </div>
                  <span
                    class="text-gray-400 font-bold text-sm z-10 bg-white px-3 py-1 rounded"
                    >QR CODE</span
                  >
                </div>
              </div>


              <div
                class="mt-6 bg-blue-50 border-l-4 border-blue-600 px-4 py-3 rounded"
              >
                <p
                  class="text-xs text-blue-800 font-semibold flex items-center gap-2"
                >
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
                      d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                  Scan untuk akses cepat informasi mahasiswa
                </p>
              </div>
            </div>
          </CardContent> 
        </Card>-->
      </div>
    </div>
  </div>
</template>
