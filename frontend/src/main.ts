import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { router } from "./routes";

import { createPinia } from "pinia";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";

// Import Google Sign-In
import GoogleSignInPlugin from "vue3-google-signin";

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

const app = createApp(App);
app.use(pinia);
app.use(router);

// Initialize Google Sign-In
app.use(GoogleSignInPlugin, {
  clientId: import.meta.env.VITE_GOOGLE_CLIENT_ID,
});

app.mount("#app");
