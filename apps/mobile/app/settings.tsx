import React from "react";
import { Text, View, Button } from "react-native";
import { useI18n } from "../i18n";
import { useSettings } from "./store";

export default function Settings() {
  const { t } = useI18n();
  const { lang, setLang } = useSettings();
  return (
    <View
      accessibilityLabel="settings-screen"
      className="flex-1 items-center justify-center p-4"
    >
      <Text className="text-lg text-[#3BA3FF] mb-2">{t("settings")}</Text>
      <Button
        title={lang === "en" ? "FR" : "EN"}
        onPress={() => setLang(lang === "en" ? "fr" : "en")}
      ></Button>
    </View>
  );
}
