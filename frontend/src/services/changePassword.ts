import { apiClient } from "@/lib/axios";

export async function changePassword(
  old_password: string,
  new_password: string,
  token: string
) {
  const response = await apiClient.post(
    "users/change-password",
    { old_password, new_password },
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.data;
}
