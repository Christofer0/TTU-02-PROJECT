<template>
  <div
    class="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-50 via-white to-blue-100 p-4"
  >
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-5">
      <div
        class="absolute top-32 left-32 w-96 h-96 bg-blue-300 rounded-full mix-blend-multiply filter blur-xl animate-pulse"
      ></div>
      <div
        class="absolute bottom-32 right-32 w-96 h-96 bg-blue-400 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-1000"
      ></div>
      <div
        class="absolute top-1/2 left-1/4 w-64 h-64 bg-blue-200 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-500"
      ></div>
    </div>

    <Card
      class="w-[650px] max-w-full shadow-2xl shadow-blue-100 border-0 bg-white/80 backdrop-blur-sm relative overflow-hidden"
    >
      <!-- Card decoration -->
      <div
        class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700"
      ></div>

      <CardHeader class="text-center pb-4 pt-8">
        <!-- Logo/Icon -->
        <div
          class="mx-auto mb-4 w-16 h-16 bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl flex items-center justify-center shadow-lg shadow-blue-200"
        >
          <svg
            class="w-8 h-8 text-white"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"
            ></path>
          </svg>
        </div>

        <CardTitle class="text-2xl font-bold text-gray-800 mb-2"
          >Registrasi Mahasiswa</CardTitle
        >
        <CardDescription class="text-gray-600">
          Bergabunglah dengan FTI UKSW dan mulai perjalanan akademik Anda
        </CardDescription>
      </CardHeader>

      <CardContent class="px-8 pb-8">
        <form @submit.prevent="handleRegister" class="space-y-5">
          <!-- Grid Layout untuk form yang lebih compact -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
            <!-- NIM -->
            <div class="space-y-2">
              <Label
                for="nomor_induk"
                class="text-sm font-semibold text-gray-700 flex items-center gap-2"
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
                  ></path>
                </svg>
                NIM <span class="text-red-500">*</span>
              </Label>
              <Input
                id="nomor_induk"
                v-model="form.nomor_induk"
                placeholder="Masukkan NIM"
                class="h-11 rounded-xl border-2 border-gray-200 focus:border-blue-400 focus:ring-blue-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
                :class="{
                  'border-red-300 focus:border-red-400 focus:ring-red-100':
                    fieldErrors.nomor_induk,
                }"
              />
              <p
                v-if="fieldErrors.nomor_induk"
                class="text-red-500 text-xs flex items-center gap-1"
              >
                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                {{ fieldErrors.nomor_induk[0] }}
              </p>
            </div>

            <!-- Nama Lengkap -->
            <div class="space-y-2">
              <Label
                for="nama"
                class="text-sm font-semibold text-gray-700 flex items-center gap-2"
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
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                  ></path>
                </svg>
                Nama Lengkap <span class="text-red-500">*</span>
              </Label>
              <Input
                id="nama"
                v-model="form.nama"
                placeholder="Masukkan nama lengkap"
                class="h-11 rounded-xl border-2 border-gray-200 focus:border-blue-400 focus:ring-blue-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
                :class="{
                  'border-red-300 focus:border-red-400 focus:ring-red-100':
                    fieldErrors.nama,
                }"
              />
              <p
                v-if="fieldErrors.nama"
                class="text-red-500 text-xs flex items-center gap-1"
              >
                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                {{ fieldErrors.nama[0] }}
              </p>
            </div>
          </div>

          <!-- Email (Full Width) -->
          <div class="space-y-2">
            <Label
              for="email"
              class="text-sm font-semibold text-gray-700 flex items-center gap-2"
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
                  d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"
                ></path>
              </svg>
              Email <span class="text-red-500">*</span>
            </Label>
            <Input
              id="email"
              type="email"
              v-model="form.email"
              placeholder="Masukkan email aktif Anda"
              class="h-11 rounded-xl border-2 border-gray-200 focus:border-blue-400 focus:ring-blue-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
              :class="{
                'border-red-300 focus:border-red-400 focus:ring-red-100':
                  fieldErrors.email,
              }"
            />
            <p
              v-if="fieldErrors.email"
              class="text-red-500 text-xs flex items-center gap-1"
            >
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              {{ fieldErrors.email[0] }}
            </p>
          </div>

          <!-- Password Fields Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
            <!-- Password -->
            <div class="space-y-2">
              <Label
                for="password"
                class="text-sm font-semibold text-gray-700 flex items-center gap-2"
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
                    d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"
                  ></path>
                </svg>
                Password <span class="text-red-500">*</span>
              </Label>
              <div class="relative">
                <Input
                  id="password"
                  :type="showPassword ? 'text' : 'password'"
                  v-model="form.password"
                  placeholder="Masukkan password"
                  class="h-11 rounded-xl border-2 border-gray-200 focus:border-blue-400 focus:ring-blue-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400 pr-12"
                  :class="{
                    'border-red-300 focus:border-red-400 focus:ring-red-100':
                      fieldErrors.password,
                  }"
                />
                <button
                  type="button"
                  @click="togglePasswordVisibility"
                  class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-blue-600 transition-colors duration-200 focus:outline-none focus:text-blue-600"
                >
                  <svg
                    v-if="!showPassword"
                    class="w-5 h-5"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                    ></path>
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                    ></path>
                  </svg>
                  <svg
                    v-else
                    class="w-5 h-5"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.878 9.878L3 3m6.878 6.878L21 21"
                    ></path>
                  </svg>
                </button>
              </div>
              <p
                v-if="fieldErrors.password"
                class="text-red-500 text-xs flex items-center gap-1"
              >
                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                {{ fieldErrors.password[0] }}
              </p>
            </div>

            <!-- Konfirmasi Password -->
            <div class="space-y-2">
              <Label
                for="confirmPassword"
                class="text-sm font-semibold text-gray-700 flex items-center gap-2"
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
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                  ></path>
                </svg>
                Konfirmasi Password <span class="text-red-500">*</span>
              </Label>
              <div class="relative">
                <Input
                  id="confirmPassword"
                  :type="showConfirmPassword ? 'text' : 'password'"
                  v-model="form.confirmPassword"
                  placeholder="Konfirmasi password"
                  class="h-11 rounded-xl border-2 border-gray-200 focus:border-blue-400 focus:ring-blue-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400 pr-12"
                  :class="{
                    'border-red-300 focus:border-red-400 focus:ring-red-100':
                      fieldErrors.confirmPassword || passwordMismatch,
                  }"
                />
                <button
                  type="button"
                  @click="toggleConfirmPasswordVisibility"
                  class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-blue-600 transition-colors duration-200 focus:outline-none focus:text-blue-600"
                >
                  <svg
                    v-if="!showConfirmPassword"
                    class="w-5 h-5"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                    ></path>
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                    ></path>
                  </svg>
                  <svg
                    v-else
                    class="w-5 h-5"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.878 9.878L3 3m6.878 6.878L21 21"
                    ></path>
                  </svg>
                </button>
              </div>
              <p
                v-if="fieldErrors.confirmPassword"
                class="text-red-500 text-xs flex items-center gap-1"
              >
                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                {{ fieldErrors.confirmPassword[0] }}
              </p>
              <p
                v-else-if="passwordMismatch"
                class="text-red-500 text-xs flex items-center gap-1"
              >
                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                Password tidak sama
              </p>
            </div>
          </div>

          <!-- Academic Information Grid -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
            <!-- Fakultas -->
            <div class="space-y-2">
              <Label
                for="fakultas"
                class="text-sm font-semibold text-gray-700 flex items-center gap-2"
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
                    d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"
                  ></path>
                </svg>
                Fakultas <span class="text-red-500">*</span>
              </Label>
              <select
                id="fakultas"
                v-model="form.fakultas_id"
                @change="onFakultasChange"
                class="h-11 rounded-xl border-2 border-gray-200 focus:border-blue-400 focus:ring-blue-100 bg-white/70 backdrop-blur-sm transition-all duration-200 px-3 w-full"
                :class="{
                  'border-red-300 focus:border-red-400 focus:ring-red-100':
                    fieldErrors.fakultas_id,
                }"
              >
                <option value="">Pilih Fakultas</option>
                <option
                  v-for="fak in fakultasList"
                  :key="fak.id"
                  :value="fak.id"
                >
                  {{ fak.nama_fakultas }}
                </option>
              </select>
              <p
                v-if="fieldErrors.fakultas_id"
                class="text-red-500 text-xs flex items-center gap-1"
              >
                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                {{ fieldErrors.fakultas_id[0] }}
              </p>
            </div>

            <!-- Program Studi -->
            <div class="space-y-2">
              <Label
                for="program_studi"
                class="text-sm font-semibold text-gray-700 flex items-center gap-2"
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
                    d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                  ></path>
                </svg>
                Program Studi <span class="text-red-500">*</span>
              </Label>
              <select
                id="program_studi"
                v-model="form.program_studi_id"
                :disabled="!programStudiList.length"
                class="h-11 rounded-xl border-2 border-gray-200 focus:border-blue-400 focus:ring-blue-100 bg-white/70 backdrop-blur-sm transition-all duration-200 px-3 w-full disabled:bg-gray-100 disabled:cursor-not-allowed"
                :class="{
                  'border-red-300 focus:border-red-400 focus:ring-red-100':
                    fieldErrors.program_studi_id,
                }"
              >
                <option value="">Pilih Program Studi</option>
                <option
                  v-for="prodi in programStudiList"
                  :key="prodi.id"
                  :value="prodi.id"
                >
                  {{ prodi.nama_prodi }}
                </option>
              </select>
              <p
                v-if="fieldErrors.program_studi_id"
                class="text-red-500 text-xs flex items-center gap-1"
              >
                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                {{ fieldErrors.program_studi_id[0] }}
              </p>
            </div>

            <!-- Semester -->
            <div class="space-y-2">
              <Label
                for="semester"
                class="text-sm font-semibold text-gray-700 flex items-center gap-2"
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
                    d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                  ></path>
                </svg>
                Semester <span class="text-red-500">*</span>
              </Label>
              <select
                id="semester"
                v-model="form.semester"
                class="h-11 rounded-xl border-2 border-gray-200 focus:border-blue-400 focus:ring-blue-100 bg-white/70 backdrop-blur-sm transition-all duration-200 px-3 w-full"
                :class="{
                  'border-red-300 focus:border-red-400 focus:ring-red-100':
                    fieldErrors.semester,
                }"
              >
                <option value="">Pilih Semester</option>
                <option v-for="i in 14" :key="i" :value="i">
                  Semester {{ i }}
                </option>
              </select>
              <p
                v-if="fieldErrors.semester"
                class="text-red-500 text-xs flex items-center gap-1"
              >
                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
                {{ fieldErrors.semester[0] }}
              </p>
            </div>
          </div>

          <!-- No HP (Full Width) -->
          <div class="space-y-2">
            <Label
              for="no_hp"
              class="text-sm font-semibold text-gray-700 flex items-center gap-2"
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
                  d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"
                ></path>
              </svg>
              No. HP
            </Label>
            <Input
              id="no_hp"
              v-model="form.no_hp"
              placeholder="Masukkan nomor HP (opsional)"
              class="h-11 rounded-xl border-2 border-gray-200 focus:border-blue-400 focus:ring-blue-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400"
              :class="{
                'border-red-300 focus:border-red-400 focus:ring-red-100':
                  fieldErrors.no_hp,
              }"
            />
            <p
              v-if="fieldErrors.no_hp"
              class="text-red-500 text-xs flex items-center gap-1"
            >
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              {{ fieldErrors.no_hp[0] }}
            </p>
          </div>

          <!-- Submit Button -->
          <Button
            type="submit"
            :disabled="isSubmitting || !isFormValid"
            class="w-full h-12 bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white font-semibold rounded-xl shadow-lg shadow-blue-200 border-0 transition-all duration-300 hover:scale-[1.02] hover:shadow-xl hover:shadow-blue-300 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100"
          >
            <span
              v-if="!isSubmitting"
              class="flex items-center justify-center gap-2"
            >
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
                  d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"
                ></path>
              </svg>
              Daftar Sekarang
            </span>
            <span v-else class="flex items-center justify-center gap-2">
              <svg
                class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
                fill="none"
                viewBox="0 0 24 24"
              >
                <circle
                  class="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  stroke-width="4"
                ></circle>
                <path
                  class="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                ></path>
              </svg>
              Mendaftar...
            </span>
          </Button>
        </form>

        <!-- Error & Success Alerts -->
        <div class="space-y-4 mt-6">
          <Alert
            v-if="globalError"
            variant="destructive"
            class="border-red-200 bg-red-50 rounded-xl"
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
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.34 16.5c-.77.833.192 2.5 1.732 2.5z"
              ></path>
            </svg>
            {{ globalError }}
          </Alert>

          <Alert
            v-if="successMessage"
            class="border-green-200 bg-green-50 text-green-800 rounded-xl"
          >
            <svg
              class="w-4 h-4 text-green-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
              ></path>
            </svg>
            {{ successMessage }}
          </Alert>
        </div>

        <!-- Login Link -->
        <div class="mt-8 pt-6 border-t border-gray-100">
          <p class="text-sm text-center text-gray-600">
            Sudah memiliki akun?
            <RouterLink
              to="/"
              class="text-blue-600 hover:text-blue-700 font-semibold hover:underline transition-colors duration-200 ml-1"
            >
              Masuk di sini
            </RouterLink>
          </p>
        </div>

        <!-- Footer Info -->
        <div class="mt-6 text-center">
          <p class="text-xs text-gray-500">
            Sistem Informasi Fakultas Teknologi Informasi
          </p>
          <p class="text-xs text-gray-400">Universitas Kristen Satya Wacana</p>
        </div>
      </CardContent>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed, watch } from "vue";
import { useRouter, RouterLink } from "vue-router";
import { registerMahasiswa } from "@/services/register";
import { apiClient } from "@/lib/axios";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Alert } from "@/components/ui/alert";

const router = useRouter();

// State form
const form = ref({
  nomor_induk: "",
  nama: "",
  email: "",
  password: "",
  confirmPassword: "",
  fakultas_id: "",
  program_studi_id: "",
  semester: "",
  no_hp: "",
});

// Password visibility states
const showPassword = ref(false);
const showConfirmPassword = ref(false);

// Data lists
const fakultasList = ref<any[]>([]);
const programStudiList = ref<any[]>([]);

// Messages and loading states
const fieldErrors = ref<{ [key: string]: string[] }>({});
const globalError = ref("");
const successMessage = ref("");
const isSubmitting = ref(false);

// Password visibility toggles
function togglePasswordVisibility() {
  showPassword.value = !showPassword.value;
}

function toggleConfirmPasswordVisibility() {
  showConfirmPassword.value = !showConfirmPassword.value;
}

// Computed properties for enhanced validation
const passwordMismatch = computed(() => {
  return (
    form.value.password &&
    form.value.confirmPassword &&
    form.value.password !== form.value.confirmPassword
  );
});

const isFormValid = computed(() => {
  const requiredFields = [
    "nomor_induk",
    "nama",
    "email",
    "password",
    "confirmPassword",
    "fakultas_id",
    "program_studi_id",
    "semester",
  ];

  const hasRequiredFields = requiredFields.every(
    (field) => form.value[field as keyof typeof form.value]
  );

  const hasNoErrors = Object.keys(fieldErrors.value).length === 0;
  const passwordsMatch = !passwordMismatch.value;

  return hasRequiredFields && hasNoErrors && passwordsMatch;
});

// Clear field errors when user starts typing
watch(
  () => form.value,
  (newForm, oldForm) => {
    Object.keys(newForm).forEach((key) => {
      if (
        newForm[key as keyof typeof newForm] !==
        oldForm?.[key as keyof typeof oldForm]
      ) {
        if (fieldErrors.value[key]) {
          delete fieldErrors.value[key];
        }
      }
    });
  },
  { deep: true }
);

// Clear global messages when form changes
watch(
  () => form.value,
  () => {
    globalError.value = "";
    successMessage.value = "";
  },
  { deep: true }
);

// Load fakultas on mount
onMounted(async () => {
  try {
    const res = await apiClient.get("/fakultas/");
    fakultasList.value = res.data.data || [];
  } catch (error: any) {
    console.error("Error loading fakultas:", error);
    globalError.value = "Gagal memuat data fakultas. Silakan refresh halaman.";
  }
});

// Update program studi based on fakultas selection
function onFakultasChange() {
  try {
    const selected = fakultasList.value.find(
      (f: any) => f.id === Number(form.value.fakultas_id)
    );

    programStudiList.value = selected?.program_studi || [];
    form.value.program_studi_id = ""; // Reset program studi selection

    // Clear related errors
    if (fieldErrors.value.fakultas_id) {
      delete fieldErrors.value.fakultas_id;
    }
    if (fieldErrors.value.program_studi_id) {
      delete fieldErrors.value.program_studi_id;
    }
  } catch (error) {
    console.error("Error updating program studi:", error);
    programStudiList.value = [];
  }
}

// Enhanced form validation
function validateForm() {
  const errors: { [key: string]: string[] } = {};

  // Required field validation
  if (!form.value.nomor_induk.trim()) {
    errors.nomor_induk = ["NIM wajib diisi"];
  }

  if (!form.value.nama.trim()) {
    errors.nama = ["Nama lengkap wajib diisi"];
  }

  if (!form.value.email.trim()) {
    errors.email = ["Email wajib diisi"];
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.value.email)) {
    errors.email = ["Format email tidak valid"];
  }

  if (!form.value.password) {
    errors.password = ["Password wajib diisi"];
  } else if (form.value.password.length < 6) {
    errors.password = ["Password minimal 6 karakter"];
  }

  if (!form.value.confirmPassword) {
    errors.confirmPassword = ["Konfirmasi password wajib diisi"];
  } else if (form.value.password !== form.value.confirmPassword) {
    errors.confirmPassword = ["Password tidak sama"];
  }

  if (!form.value.fakultas_id) {
    errors.fakultas_id = ["Fakultas wajib dipilih"];
  }

  if (!form.value.program_studi_id) {
    errors.program_studi_id = ["Program studi wajib dipilih"];
  }

  if (!form.value.semester) {
    errors.semester = ["Semester wajib dipilih"];
  }

  // Optional field validation
  if (form.value.no_hp && !/^[0-9+\-\s()]+$/.test(form.value.no_hp)) {
    errors.no_hp = ["Format nomor HP tidak valid"];
  }

  return errors;
}

// Handle form submission
async function handleRegister() {
  // Reset states
  fieldErrors.value = {};
  globalError.value = "";
  successMessage.value = "";
  isSubmitting.value = true;

  try {
    // Frontend validation
    const validationErrors = validateForm();
    if (Object.keys(validationErrors).length > 0) {
      fieldErrors.value = validationErrors;
      globalError.value = "Mohon periksa kembali form Anda.";
      return;
    }

    // Prepare payload
    const payload = {
      nomor_induk: form.value.nomor_induk.trim(),
      nama: form.value.nama.trim(),
      email: form.value.email.trim().toLowerCase(),
      password: form.value.password,
      confirmPassword: form.value.confirmPassword,
      fakultas_id: Number(form.value.fakultas_id),
      program_studi_id: Number(form.value.program_studi_id),
      semester: Number(form.value.semester),
      no_hp: form.value.no_hp.trim() || null,
      role: "mahasiswa",
    };

    // Submit registration
    await registerMahasiswa(payload);

    // Success handling
    successMessage.value =
      "Registrasi berhasil! Anda akan diarahkan ke halaman login dalam beberapa detik.";

    // Reset form
    form.value = {
      nomor_induk: "",
      nama: "",
      email: "",
      password: "",
      confirmPassword: "",
      fakultas_id: "",
      program_studi_id: "",
      semester: "",
      no_hp: "",
    };
    programStudiList.value = [];

    // Redirect to login after 3 seconds
    setTimeout(() => {
      router.push({ name: "Login" });
    }, 3000);
  } catch (err: any) {
    console.error("Registration error:", err);

    // Handle different types of errors
    if (err.response?.status === 422) {
      // Validation errors from server
      const data = err.response.data;
      if (data?.errors) {
        fieldErrors.value = data.errors;
        globalError.value =
          "Terdapat kesalahan pada form. Silakan periksa kembali.";
      } else {
        globalError.value =
          data?.message || "Data yang Anda masukkan tidak valid.";
      }
    } else if (err.response?.status === 409) {
      // Conflict (duplicate data)
      globalError.value =
        "NIM atau email sudah terdaftar. Silakan gunakan data yang berbeda.";
    } else if (err.response?.status === 500) {
      // Server error
      globalError.value =
        "Terjadi kesalahan pada server. Silakan coba lagi nanti.";
    } else if (err.code === "NETWORK_ERROR" || !err.response) {
      // Network error
      globalError.value =
        "Tidak dapat terhubung ke server. Periksa koneksi internet Anda.";
    } else {
      // Generic error
      globalError.value =
        err.response?.data?.message || "Registrasi gagal. Silakan coba lagi.";
    }
  } finally {
    isSubmitting.value = false;
  }
}
</script>
