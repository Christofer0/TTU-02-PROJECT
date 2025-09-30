<template>
  <div
    class="flex items-center justify-center min-h-screen bg-gradient-to-br from-amber-50 via-white to-amber-100 p-4"
  >
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-5">
      <div
        class="absolute top-20 left-20 w-72 h-72 bg-amber-300 rounded-full mix-blend-multiply filter blur-xl animate-pulse"
      ></div>
      <div
        class="absolute bottom-20 right-20 w-72 h-72 bg-amber-400 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-1000"
      ></div>
      <div
        class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-amber-200 rounded-full mix-blend-multiply filter blur-xl animate-pulse delay-500"
      ></div>
    </div>

    <Card
      class="w-[480px] max-w-full shadow-2xl shadow-amber-100 border-0 bg-white/80 backdrop-blur-sm relative overflow-hidden"
    >
      <!-- Card decoration -->
      <div
        class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-amber-500 via-amber-600 to-amber-700"
      ></div>

      <CardHeader class="text-center pb-4 pt-8">
        <!-- Security Icon -->
        <div
          class="mx-auto mb-4 w-16 h-16 bg-gradient-to-br from-amber-500 to-amber-600 rounded-2xl flex items-center justify-center shadow-lg shadow-amber-200"
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
              d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"
            ></path>
          </svg>
        </div>

        <CardTitle class="text-2xl font-bold text-gray-800 mb-2"
          >Ganti Password</CardTitle
        >
        <CardDescription class="text-gray-600">
          Perbarui password Anda untuk menjaga keamanan akun
        </CardDescription>
      </CardHeader>

      <CardContent class="px-8 pb-8">
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <!-- Password Lama -->
          <div class="space-y-2">
            <Label
              for="old_password"
              class="text-sm font-semibold text-gray-700 flex items-center gap-2"
            >
              <svg
                class="w-4 h-4 text-amber-600"
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
              Password Lama <span class="text-red-500">*</span>
            </Label>
            <div class="relative">
              <Input
                id="old_password"
                v-model="form.old_password"
                :type="showOldPassword ? 'text' : 'password'"
                placeholder="Masukkan password lama"
                required
                class="h-12 rounded-xl border-2 border-gray-200 focus:border-amber-400 focus:ring-amber-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400 pr-12"
                :class="{
                  'border-red-300 focus:border-red-400 focus:ring-red-100':
                    fieldErrors.old_password,
                }"
              />
              <button
                type="button"
                @click="toggleOldPasswordVisibility"
                class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-amber-600 transition-colors duration-200 focus:outline-none focus:text-amber-600"
              >
                <svg
                  v-if="!showOldPassword"
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
              v-if="fieldErrors.old_password"
              class="text-red-500 text-xs flex items-center gap-1"
            >
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              {{ fieldErrors.old_password }}
            </p>
          </div>

          <!-- Password Baru -->
          <div class="space-y-2">
            <Label
              for="new_password"
              class="text-sm font-semibold text-gray-700 flex items-center gap-2"
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
                  d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
                ></path>
              </svg>
              Password Baru <span class="text-red-500">*</span>
            </Label>
            <div class="relative">
              <Input
                id="new_password"
                v-model="form.new_password"
                :type="showNewPassword ? 'text' : 'password'"
                placeholder="Masukkan password baru"
                required
                class="h-12 rounded-xl border-2 border-gray-200 focus:border-amber-400 focus:ring-amber-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400 pr-12"
                :class="{
                  'border-red-300 focus:border-red-400 focus:ring-red-100':
                    fieldErrors.new_password,
                  'border-emerald-300 focus:border-emerald-400 focus:ring-emerald-100':
                    passwordStrengthLevel > 2 && form.new_password,
                }"
              />
              <button
                type="button"
                @click="toggleNewPasswordVisibility"
                class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-amber-600 transition-colors duration-200 focus:outline-none focus:text-amber-600"
              >
                <svg
                  v-if="!showNewPassword"
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

            <!-- Password Strength Indicator -->
            <div v-if="form.new_password" class="space-y-2">
              <div class="flex items-center gap-2">
                <div
                  class="flex-1 h-2 bg-gray-200 rounded-full overflow-hidden"
                >
                  <div
                    class="h-full transition-all duration-300 rounded-full"
                    :class="{
                      'bg-red-400 w-1/4': passwordStrengthLevel === 1,
                      'bg-orange-400 w-1/2': passwordStrengthLevel === 2,
                      'bg-yellow-400 w-3/4': passwordStrengthLevel === 3,
                      'bg-green-400 w-full': passwordStrengthLevel === 4,
                    }"
                  ></div>
                </div>
                <span
                  class="text-xs font-medium"
                  :class="{
                    'text-red-600': passwordStrengthLevel === 1,
                    'text-orange-600': passwordStrengthLevel === 2,
                    'text-yellow-600': passwordStrengthLevel === 3,
                    'text-green-600': passwordStrengthLevel === 4,
                  }"
                >
                  {{ passwordStrengthText }}
                </span>
              </div>
              <div class="space-y-1">
                <div class="flex items-center gap-2 text-xs">
                  <svg
                    class="w-3 h-3"
                    :class="
                      form.new_password.length >= 8
                        ? 'text-green-600'
                        : 'text-gray-400'
                    "
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                  <span
                    :class="
                      form.new_password.length >= 8
                        ? 'text-green-600'
                        : 'text-gray-500'
                    "
                  >
                    Minimal 8 karakter
                  </span>
                </div>
                <div class="flex items-center gap-2 text-xs">
                  <svg
                    class="w-3 h-3"
                    :class="
                      /[A-Z]/.test(form.new_password)
                        ? 'text-green-600'
                        : 'text-gray-400'
                    "
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                  <span
                    :class="
                      /[A-Z]/.test(form.new_password)
                        ? 'text-green-600'
                        : 'text-gray-500'
                    "
                  >
                    Huruf besar
                  </span>
                </div>
                <div class="flex items-center gap-2 text-xs">
                  <svg
                    class="w-3 h-3"
                    :class="
                      /[0-9]/.test(form.new_password)
                        ? 'text-green-600'
                        : 'text-gray-400'
                    "
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                  <span
                    :class="
                      /[0-9]/.test(form.new_password)
                        ? 'text-green-600'
                        : 'text-gray-500'
                    "
                  >
                    Angka
                  </span>
                </div>
              </div>
            </div>

            <p
              v-if="fieldErrors.new_password"
              class="text-red-500 text-xs flex items-center gap-1"
            >
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              {{ fieldErrors.new_password }}
            </p>
          </div>

          <!-- Konfirmasi Password Baru -->
          <div class="space-y-2">
            <Label
              for="confirm_password"
              class="text-sm font-semibold text-gray-700 flex items-center gap-2"
            >
              <svg
                class="w-4 h-4 text-amber-600"
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
              Konfirmasi Password Baru <span class="text-red-500">*</span>
            </Label>
            <div class="relative">
              <Input
                id="confirm_password"
                v-model="form.confirm_password"
                :type="showConfirmPassword ? 'text' : 'password'"
                placeholder="Konfirmasi password baru"
                required
                class="h-12 rounded-xl border-2 border-gray-200 focus:border-amber-400 focus:ring-amber-100 bg-white/70 backdrop-blur-sm transition-all duration-200 placeholder:text-gray-400 pr-12"
                :class="{
                  'border-red-300 focus:border-red-400 focus:ring-red-100':
                    fieldErrors.confirm_password ||
                    (passwordMismatch && form.confirm_password),
                  'border-emerald-300 focus:border-emerald-400 focus:ring-emerald-100':
                    !passwordMismatch &&
                    form.confirm_password &&
                    form.new_password,
                }"
              />
              <button
                type="button"
                @click="toggleConfirmPasswordVisibility"
                class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 hover:text-amber-600 transition-colors duration-200 focus:outline-none focus:text-amber-600"
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
              v-if="fieldErrors.confirm_password"
              class="text-red-500 text-xs flex items-center gap-1"
            >
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              {{ fieldErrors.confirm_password }}
            </p>
            <p
              v-else-if="passwordMismatch && form.confirm_password"
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
            <p
              v-else-if="
                !passwordMismatch && form.confirm_password && form.new_password
              "
              class="text-emerald-600 text-xs flex items-center gap-1"
            >
              <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              Password sudah cocok
            </p>
          </div>

          <!-- Submit Button -->
          <Button
            type="submit"
            :disabled="loading || !isFormValid"
            class="w-full h-12 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-600 hover:to-amber-700 text-white font-semibold rounded-xl shadow-lg shadow-amber-200 border-0 transition-all duration-300 hover:scale-[1.02] hover:shadow-xl hover:shadow-amber-300 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100"
          >
            <span
              v-if="!loading"
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
                  d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"
                ></path>
              </svg>
              Ganti Password
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
              Memproses...
            </span>
          </Button>
        </form>

        <!-- Error & Success Alerts -->
        <div class="space-y-4 mt-6">
          <Alert
            v-if="error"
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
            {{ error }}
          </Alert>

          <Alert
            v-if="success"
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
            {{ success }}
          </Alert>
        </div>

        <!-- Security Tips -->
        <div class="mt-8 p-4 bg-amber-50 rounded-xl border border-amber-100">
          <h4
            class="text-sm font-semibold text-amber-800 mb-2 flex items-center gap-2"
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
              ></path>
            </svg>
            Tips Keamanan Password
          </h4>
          <ul class="text-xs text-amber-700 space-y-1">
            <li>• Gunakan kombinasi huruf besar, kecil, angka, dan simbol</li>
            <li>• Hindari menggunakan informasi pribadi yang mudah ditebak</li>
            <li>• Ganti password secara berkala untuk menjaga keamanan</li>
            <li>• Jangan gunakan password yang sama untuk akun lain</li>
          </ul>
        </div>
      </CardContent>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from "vue";
import { useAuthStore } from "@/stores/auth";
import { changePassword } from "@/services/changePassword";
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

const auth = useAuthStore();

const form = ref({
  old_password: "",
  new_password: "",
  confirm_password: "",
});

// Password visibility states
const showOldPassword = ref(false);
const showNewPassword = ref(false);
const showConfirmPassword = ref(false);

// Loading and message states
const loading = ref(false);
const error = ref("");
const success = ref("");
const fieldErrors = ref<{ [key: string]: string }>({});

// Password visibility toggle functions
function toggleOldPasswordVisibility() {
  showOldPassword.value = !showOldPassword.value;
}

function toggleNewPasswordVisibility() {
  showNewPassword.value = !showNewPassword.value;
}

function toggleConfirmPasswordVisibility() {
  showConfirmPassword.value = !showConfirmPassword.value;
}

// Password validation
const passwordMismatch = computed(() => {
  return (
    form.value.new_password &&
    form.value.confirm_password &&
    form.value.new_password !== form.value.confirm_password
  );
});

// Password strength calculation
const passwordStrengthLevel = computed(() => {
  const password = form.value.new_password;
  if (!password) return 0;

  let score = 0;
  if (password.length >= 8) score++;
  if (/[A-Z]/.test(password)) score++;
  if (/[a-z]/.test(password)) score++;
  if (/[0-9]/.test(password)) score++;
  if (/[^A-Za-z0-9]/.test(password)) score++;

  if (score <= 2) return 1; // Weak
  if (score === 3) return 2; // Fair
  if (score === 4) return 3; // Good
  return 4; // Strong
});

const passwordStrengthText = computed(() => {
  switch (passwordStrengthLevel.value) {
    case 1:
      return "Lemah";
    case 2:
      return "Sedang";
    case 3:
      return "Baik";
    case 4:
      return "Kuat";
    default:
      return "";
  }
});

// Form validation
const isFormValid = computed(() => {
  return (
    form.value.old_password &&
    form.value.new_password &&
    form.value.confirm_password &&
    !passwordMismatch.value &&
    passwordStrengthLevel.value >= 2 &&
    Object.keys(fieldErrors.value).length === 0
  );
});

// Clear messages when form changes
watch(
  () => form.value,
  () => {
    error.value = "";
    success.value = "";
    fieldErrors.value = {};
  },
  { deep: true }
);

// Enhanced form validation
function validateForm() {
  const errors: { [key: string]: string } = {};

  if (!form.value.old_password) {
    errors.old_password = "Password lama wajib diisi";
  }

  if (!form.value.new_password) {
    errors.new_password = "Password baru wajib diisi";
  } else if (form.value.new_password.length < 8) {
    errors.new_password = "Password minimal 8 karakter";
  } else if (passwordStrengthLevel.value < 2) {
    errors.new_password = "Password terlalu lemah";
  }

  if (!form.value.confirm_password) {
    errors.confirm_password = "Konfirmasi password wajib diisi";
  } else if (form.value.new_password !== form.value.confirm_password) {
    errors.confirm_password = "Password tidak sama";
  }

  // Check if new password is same as old password
  if (
    form.value.old_password &&
    form.value.new_password &&
    form.value.old_password === form.value.new_password
  ) {
    errors.new_password = "Password baru harus berbeda dari password lama";
  }

  return errors;
}

// Handle form submission with enhanced error handling
const handleSubmit = async () => {
  // Reset states
  error.value = "";
  success.value = "";
  fieldErrors.value = {};

  // Check authentication
  if (!auth.access_token) {
    error.value = "Sesi Anda telah berakhir. Silakan login ulang.";
    return;
  }

  // Frontend validation
  const validationErrors = validateForm();
  if (Object.keys(validationErrors).length > 0) {
    fieldErrors.value = validationErrors;
    error.value = "Mohon periksa kembali form Anda.";
    return;
  }

  try {
    loading.value = true;

    const result = await changePassword(
      form.value.old_password,
      form.value.new_password,
      auth.access_token
    );

    // Success handling
    success.value = result.message || "Password berhasil diubah!";

    // Reset form after success
    form.value.old_password = "";
    form.value.new_password = "";
    form.value.confirm_password = "";

    // Optional: Auto redirect after success
    setTimeout(() => {
      success.value = "";
    }, 5000);
  } catch (err: any) {
    console.error("Change password error:", err);

    // Handle different types of errors
    if (err.response?.status === 400) {
      // Bad request - usually validation errors
      const data = err.response.data;
      if (data?.errors) {
        fieldErrors.value = data.errors;
        error.value = "Terdapat kesalahan pada form.";
      } else {
        error.value = data?.message || "Password lama tidak benar.";
      }
    } else if (err.response?.status === 401) {
      // Unauthorized
      error.value = "Sesi Anda telah berakhir. Silakan login ulang.";
      // Optional: redirect to login
      // auth.logout();
      // router.push('/login');
    } else if (err.response?.status === 422) {
      // Validation errors
      const data = err.response.data;
      if (data?.errors) {
        fieldErrors.value = data.errors;
      }
      error.value = data?.message || "Data yang Anda masukkan tidak valid.";
    } else if (err.response?.status === 429) {
      // Too many requests
      error.value = "Terlalu banyak percobaan. Silakan coba lagi nanti.";
    } else if (err.response?.status === 500) {
      // Server error
      error.value = "Terjadi kesalahan pada server. Silakan coba lagi nanti.";
    } else if (err.code === "NETWORK_ERROR" || !err.response) {
      // Network error
      error.value =
        "Tidak dapat terhubung ke server. Periksa koneksi internet Anda.";
    } else {
      // Generic error
      error.value =
        err.response?.data?.message ||
        "Terjadi kesalahan saat mengubah password.";
    }
  } finally {
    loading.value = false;
  }
};
</script>
