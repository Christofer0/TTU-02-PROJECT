import { createRouter, createWebHistory } from "vue-router";
import { mahasiswa_routes } from "./mahasiswa_routes";
import { permohonan_routes } from "./permohonan_routes";
import { dosen_routes } from "./dosen_routes";
import { admin_routes } from "./admin_routes";
import { useAuthStore } from "@/stores/auth";
import VerifyValid from "@/views/verify/VerifyValid.vue";
import GoogleLoginFlow from "@/views/auth/LoginView.vue";
const routes = [
  {
    path: "/",
    name: "Login",
    component: GoogleLoginFlow,
  },
  {
    path: "/register",
    component: () => import("@/views/auth/RegisterView.vue"),
  },
  {
    path: "/verify-document/:id",
    name: "verifyDocument",
    component: VerifyValid,
    meta: { requiresAuth: false, layout: "none" },
  },
  {
    path: "/admin",
    component: () => import("@/layouts/AdminLayouts.vue"),
    children: admin_routes,
    meta: { requiresAuth: true, role: "admin" },
  },
  {
    path: "/mahasiswa",
    component: () => import("@/layouts/MahasiswaLayouts.vue"),
    children: mahasiswa_routes,
    meta: { requiresAuth: true, role: "mahasiswa" },
  },
  {
    path: "/dosen",
    component: () => import("@/layouts/DosenLayouts.vue"),
    children: dosen_routes,
    meta: { requiresAuth: true, role: "dosen" },
  },
  {
    path: "/permohonan",
    component: () => import("@/layouts/MahasiswaLayouts.vue"),
    children: permohonan_routes,
  },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, _from, next) => {
  const authStore = useAuthStore();
  const user = authStore.user;

  if (to.meta.requiresAuth && !user) {
    return next("/"); // belum login -> redirect login
  }

  if (to.meta.role && user?.role !== to.meta.role) {
    //kalau roe tidak sesuai page -> redirect role yang benar
    if (user?.role === "dosen") return next("/dosen/dashboard");
    if (user?.role === "mahasiswa") return next("/mahasiswa/dashboard");
    return next("/");
  }

  next();
});
