import { components } from "reka-ui/constant";

const routes = [
  {
    path: "dashboard",
    component: () => import("@/views/dosen/DashboardDosen.vue"),
  },
  {
    path: "profile",
    component: () => import("@/views/dosen/profile/ProfileDosen.vue"),
  },
  {
    path: "update-profile",
    name: "EditProfileDosen",
    component: () => import("@/views/dosen/profile/EditProfileDosen.vue"),
  },
  {
    path: "change-password",
    name: "DosenChangePassword",
    component: () => import("@/views/auth/ChangePassword.vue"),
  },
  {
    path: "list-permohonan-TTD",
    component: () => import("@/views/dosen/permohonan/ListPermohonanTTD.vue"),
  },
  {
    path: "testDosen",
    component: () => import("@/components/dosen/SignatureCreator.vue"),
  },
];

export const dosen_routes = routes;
