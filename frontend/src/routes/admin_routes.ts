const routes = [
  {
    path: "dashboard",
    component: () => import("@/views/admin/DashboardAdmin.vue"),
  },
];

export const admin_routes = routes;
