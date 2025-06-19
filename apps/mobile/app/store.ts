import { create } from "zustand";
import { persist } from "zustand/middleware";
import * as SecureStore from "expo-secure-store";

export const useAuth = create(
  persist(
    (set: any) => ({
      accessToken: null as string | null,
      setToken: (t: string | null) => set({ accessToken: t }),
    }),
    {
      name: "auth",
      getStorage: () => ({
        getItem: SecureStore.getItemAsync,
        setItem: (_: string, v: string) => {
          SecureStore.setItemAsync("auth", v);
          return Promise.resolve();
        },
        removeItem: () => SecureStore.deleteItemAsync("auth"),
      }),
    },
  ),
);

export const useSettings = create(
  persist(
    (set: any) => ({
      lang: "en" as "en" | "fr",
      setLang: (l: "en" | "fr") => set({ lang: l }),
    }),
    {
      name: "settings",
      getStorage: () => ({
        getItem: SecureStore.getItemAsync,
        setItem: (_: string, v: string) => {
          SecureStore.setItemAsync("settings", v);
          return Promise.resolve();
        },
        removeItem: () => SecureStore.deleteItemAsync("settings"),
      }),
    },
  ),
);
