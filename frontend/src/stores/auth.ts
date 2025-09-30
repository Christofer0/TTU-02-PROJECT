import { defineStore } from "pinia";
import { ref } from "vue";
import type { User, DosenData } from "@/types/models/user.type";

export const useAuthStore = defineStore(
  "auth",
  () => {
    // state
    const user = ref<User | null>(null); // data dasar
    const dosen = ref<DosenData | null>(null);

    const access_token = ref<string | null>(null);
    const refresh_token = ref<string | null>(null);

    // actions
    function setUser(newUser: User) {
      user.value = newUser;
    }

    function setDosen(newDosen: DosenData | null) {
      dosen.value = newDosen;
    }

    function setAccessToken(newtoken: string) {
      access_token.value = newtoken;
    }

    function setRefreshToken(newtoken: string) {
      refresh_token.value = newtoken;
    }

    function logout() {
      user.value = null;
      dosen.value = null;
      access_token.value = null;
      refresh_token.value = null;
    }

    return {
      // state
      user,
      dosen,
      access_token,
      refresh_token,

      // actions
      setUser,
      setDosen,
      setAccessToken,
      setRefreshToken,
      logout,
    };
  },
  {
    persist: true,
  }
);
