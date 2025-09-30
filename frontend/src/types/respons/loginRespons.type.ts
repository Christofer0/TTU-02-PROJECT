import type { User, DosenData } from "../models/user.type";

export interface LoginResponse {
  access_token: string;
  refresh_token: string;
  expires_in: number;
  user: User;
  dosen?: DosenData;
}
