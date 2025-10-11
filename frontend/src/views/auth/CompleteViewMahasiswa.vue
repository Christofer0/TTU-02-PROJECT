<template>
  <div
    class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8"
  >
    <div class="max-w-2xl w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Lengkapi Profil Anda
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600">
          Silakan lengkapi data profil mahasiswa
        </p>
      </div>

      <div class="mt-8 bg-white shadow sm:rounded-lg">
        <div class="px-4 py-5 sm:p-6">
          <form @submit.prevent="handleSubmit" class="space-y-6">
            <!-- Data Otomatis dari Google (Read-only) -->
            <div class="border-b border-gray-200 pb-6">
              <h3 class="text-lg font-medium text-gray-900 mb-4">
                Data dari Akun Google
              </h3>

              <!-- Nama -->
              <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700"
                  >Nama Lengkap</label
                >
                <input
                  type="text"
                  :value="profileData.nama"
                  disabled
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md bg-gray-100 text-gray-600 cursor-not-allowed"
                />
              </div>

              <!-- Email -->
              <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700"
                  >Email Institusi</label
                >
                <input
                  type="email"
                  :value="profileData.email"
                  disabled
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md bg-gray-100 text-gray-600 cursor-not-allowed"
                />
              </div>

              <!-- NIM (Nomor Induk Mahasiswa) -->
              <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700"
                  >NIM</label
                >
                <input
                  type="text"
                  :value="profileData.nomor_induk"
                  disabled
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md bg-gray-100 text-gray-600 cursor-not-allowed"
                />
              </div>

              <!-- Fakultas (Auto-detect dari NIM) -->
              <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700"
                  >Fakultas</label
                >
                <input
                  type="text"
                  :value="detectedFakultas"
                  disabled
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md bg-gray-100 text-gray-600 cursor-not-allowed"
                />
                <p class="mt-1 text-xs text-gray-500">
                  Terdeteksi otomatis dari NIM
                </p>
              </div>

              <!-- Program Studi (Auto-detect dari NIM) -->
              <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700"
                  >Program Studi</label
                >
                <input
                  type="text"
                  :value="detectedProdi"
                  disabled
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md bg-gray-100 text-gray-600 cursor-not-allowed"
                />
                <p class="mt-1 text-xs text-gray-500">
                  Terdeteksi otomatis dari NIM
                </p>
              </div>
            </div>

            <!-- Input Manual -->
            <div class="pt-6">
              <h3 class="text-lg font-medium text-gray-900 mb-4">
                Data yang Perlu Dilengkapi
              </h3>

              <!-- Semester -->
              <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">
                  Semester Saat Ini <span class="text-red-500">*</span>
                </label>
                <select
                  v-model="formData.semester"
                  required
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                  :class="{ 'border-red-500': errors.semester }"
                >
                  <option value="">Pilih Semester</option>
                  <option v-for="sem in 14" :key="sem" :value="sem">
                    Semester {{ sem }}
                  </option>
                </select>
                <p v-if="errors.semester" class="mt-1 text-sm text-red-600">
                  {{ errors.semester }}
                </p>
              </div>

              <!-- No HP -->
              <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">
                  Nomor HP <span class="text-red-500">*</span>
                </label>
                <input
                  v-model="formData.no_hp"
                  type="tel"
                  placeholder="08xxxxxxxxxx"
                  required
                  maxlength="15"
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                  :class="{ 'border-red-500': errors.no_hp }"
                  @input="validateNoHp"
                />
                <p v-if="errors.no_hp" class="mt-1 text-sm text-red-600">
                  {{ errors.no_hp }}
                </p>
                <p v-else class="mt-1 text-xs text-gray-500">
                  Contoh: 081234567890
                </p>
              </div>
            </div>

            <!-- Error Message -->
            <div v-if="errorMessage" class="rounded-md bg-red-50 p-4">
              <div class="flex">
                <div class="flex-shrink-0">
                  <svg
                    class="h-5 w-5 text-red-400"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                      clip-rule="evenodd"
                    />
                  </svg>
                </div>
                <div class="ml-3">
                  <p class="text-sm font-medium text-red-800">
                    {{ errorMessage }}
                  </p>
                </div>
              </div>
            </div>

            <!-- Submit Button -->
            <div class="flex items-center justify-end space-x-3">
              <button
                type="button"
                @click="handleCancel"
                class="px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              >
                Batal
              </button>
              <button
                type="submit"
                :disabled="isLoading"
                class="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span v-if="isLoading">Menyimpan...</span>
                <span v-else>Simpan dan Lanjutkan</span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const router = useRouter();

interface ProfileData {
  role: string;
  email: string;
  nama: string;
  nomor_induk: string;
}

interface FormData {
  semester: number | string;
  no_hp: string;
}

interface Errors {
  semester?: string;
  no_hp?: string;
}

const profileData = ref<ProfileData>({
  role: "",
  email: "",
  nama: "",
  nomor_induk: "",
});

const formData = ref<FormData>({
  semester: "",
  no_hp: "",
});

const errors = ref<Errors>({});
const errorMessage = ref("");
const isLoading = ref(false);

const fakultasList = ref<any[]>([]);
const prodiList = ref<any[]>([]);

// Computed: Deteksi Fakultas dari NIM
const detectedFakultas = computed(() => {
  // Logika deteksi fakultas (sesuaikan dengan aturan NIM institusi Anda)
  // Contoh: 2 digit pertama NIM = kode fakultas
  if (!profileData.value.nomor_induk) return "Belum terdeteksi";

  // Cari fakultas berdasarkan kode
  const fakultasKode = profileData.value.nomor_induk.substring(0, 2);
  const fakultas = fakultasList.value.find((f) => f.kode === fakultasKode);

  return fakultas ? fakultas.nama : "Fakultas tidak ditemukan";
});

// Computed: Deteksi Program Studi dari NIM
const detectedProdi = computed(() => {
  // Logika deteksi prodi (sesuaikan dengan aturan NIM institusi Anda)
  // Contoh: 2-4 digit pertama NIM = kode prodi
  if (!profileData.value.nomor_induk) return "Belum terdeteksi";

  // Cari prodi berdasarkan kode
  const prodiKode = profileData.value.nomor_induk.substring(0, 4);
  const prodi = prodiList.value.find((p) => p.kode === prodiKode);

  return prodi ? prodi.nama : "Program Studi tidak ditemukan";
});

// Load data dari sessionStorage
onMounted(async () => {
  const tempProfile = sessionStorage.getItem("temp_profile");

  if (!tempProfile) {
    // Jika tidak ada data, redirect ke login
    router.push("/login");
    return;
  }

  const data = JSON.parse(tempProfile);
  profileData.value = {
    role: data.role,
    email: data.email,
    nama: data.nama,
    nomor_induk: data.email.split("@")[0], // Extract NIM dari email
  };

  // Load fakultas dan prodi dari backend
  await loadFakultasProdi();
});

// Load data fakultas dan program studi
const loadFakultasProdi = async () => {
  try {
    // Fetch fakultas
    const fakultasResponse = await axios.get("/api/fakultas");
    fakultasList.value = fakultasResponse.data.data;

    // Fetch program studi
    const prodiResponse = await axios.get("/api/program-studi");
    prodiList.value = prodiResponse.data.data;
  } catch (error) {
    console.error("Error loading fakultas/prodi:", error);
  }
};

// Validasi No HP
const validateNoHp = () => {
  const noHp = formData.value.no_hp;

  if (!noHp) {
    errors.value.no_hp = "Nomor HP wajib diisi";
  } else if (!/^08[0-9]{8,13}$/.test(noHp)) {
    errors.value.no_hp =
      "Format nomor HP tidak valid (harus dimulai dengan 08)";
  } else {
    errors.value.no_hp = "";
  }
};

// Validasi form
const validateForm = (): boolean => {
  errors.value = {};

  if (!formData.value.semester) {
    errors.value.semester = "Semester wajib dipilih";
  }

  validateNoHp();

  return Object.keys(errors.value).length === 0;
};

// Handle Submit
const handleSubmit = async () => {
  if (!validateForm()) {
    return;
  }

  isLoading.value = true;
  errorMessage.value = "";

  try {
    // Cari fakultas_id dan program_studi_id berdasarkan NIM
    const fakultasKode = profileData.value.nomor_induk.substring(0, 2);
    const prodiKode = profileData.value.nomor_induk.substring(0, 4);

    const fakultas = fakultasList.value.find((f) => f.kode === fakultasKode);
    const prodi = prodiList.value.find((p) => p.kode === prodiKode);

    if (!fakultas || !prodi) {
      errorMessage.value =
        "Fakultas atau Program Studi tidak ditemukan dari NIM Anda";
      isLoading.value = false;
      return;
    }

    // Kirim data ke backend
    const payload = {
      nama: profileData.value.nama,
      email: profileData.value.email,
      nomor_induk: profileData.value.nomor_induk,
      role: profileData.value.role,
      no_hp: formData.value.no_hp,
      fakultas_id: fakultas.id,
      program_studi_id: prodi.id,
      semester: Number(formData.value.semester),
    };

    const response = await axios.post("/api/auth/complete-profile", payload);
    console.log("Response:", response.data);
    const data = response.data.data;

    // Simpan tokens
    localStorage.setItem("access_token", data.access_token);
    localStorage.setItem("refresh_token", data.refresh_token);
    localStorage.setItem("user", JSON.stringify(data.user));

    // Hapus temp data
    sessionStorage.removeItem("temp_profile");

    // Redirect ke dashboard mahasiswa
    router.push("/mahasiswa/dashboard");
  } catch (error: any) {
    isLoading.value = false;
    errorMessage.value =
      error.response?.data?.message ||
      "Gagal menyimpan profil. Silakan coba lagi.";
  }
};

// Handle Cancel
const handleCancel = () => {
  sessionStorage.removeItem("temp_profile");
  router.push("/login");
};
</script>

<style scoped>
/* Tambahan styling jika diperlukan */
</style>
