import type { User } from "../models/user.type";

export interface RegisterResponse {
  success: boolean;
  message: string;
  data: User;
}
