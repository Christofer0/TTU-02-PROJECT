const routes = [
  {
    path: "form/:jenisId",
    name: "PermohonanForm",
    component: () => import("@/views/mahasiswa/permohonan/PermohonanTTD.vue"),
  },
];
export const permohonan_routes = routes;
