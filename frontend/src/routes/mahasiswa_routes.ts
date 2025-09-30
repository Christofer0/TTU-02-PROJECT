const routes = [
  {
    path: "dashboard",
    component: () => import("@/views/mahasiswa/DashboardMahasiswa.vue"),
  },
  {
    path: "profile",
    component: () => import("@/views/mahasiswa/profile/ProfileMahasiswa.vue"),
  },
  {
    path: "update-profile",
    name: "EditProfileMahasiswa",
    component: () =>
      import("@/views/mahasiswa/profile/EditProfileMahasiswa.vue"),
  },
  {
    path: "change-password",
    name: "MahasiswaChangePassword",
    component: () => import("@/views/auth/ChangePassword.vue"),
  },
];

export const mahasiswa_routes = routes;
