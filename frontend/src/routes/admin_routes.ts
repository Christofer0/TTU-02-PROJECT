const routes = [
  {
    path: "dashboard",
    component: () => import("@/views/admin/DashboardAdmin.vue"),
  },
  {
    path: "profile",
    component: () => import("@/views/admin/profile/ProfileAdmin.vue"),
  },
  {
    path: "update-profile",
    name: "EditProfileAdmin",
    component: () => import("@/views/admin/profile/EditProfileAdmin.vue"),
  },
  {
    path: "list-permohonan",
    component: () => import("@/views/admin/ListPermohonanAdmin.vue"),
  },
  {
    path: "history",
    component: () => import("@/views/admin/HistoryAdmin.vue"),
  },
  {
    path: "users",
    component: () => import("@/views/admin/ListUsersAdmin.vue"),
  },
];

export const admin_routes = routes;
