import React, { createContext, useContext, useState } from "react";
import en from "./locales/en.json";
import fr from "./locales/fr.json";

const translations = { en, fr } as const;
export type Lang = keyof typeof translations;

interface Ctx {
  t: (k: string) => string;
  lang: Lang;
  setLang: (l: Lang) => void;
}

const I18nContext = createContext({
  t: (k: string) => k,
  lang: "en",
  setLang: () => {},
});

export function I18nProvider(props: any) {
  const { children } = props;
  const [lang, setLang] = useState("en" as Lang);
  const t = (k: string) => (translations as any)[lang][k] ?? k;
  return (
    <I18nContext.Provider value={{ t, lang, setLang }}>
      {children}
    </I18nContext.Provider>
  );
}

export const useI18n = () => useContext(I18nContext);
