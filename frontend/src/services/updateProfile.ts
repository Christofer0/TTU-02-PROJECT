import { apiClient } from "@/lib/axios";
import type { Profile } from "@/types/models/user.type";

export async function updateProfile(payload: Partial<Profile>) {
  const res = await apiClient.put("/users/profile", payload);
  return res.data; // { status, msg, data }
}
