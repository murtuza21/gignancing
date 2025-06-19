import React, { useEffect } from "react";
import { Text } from "react-native";
import { useRouter } from "expo-router";
import { MotiView } from "moti";
import { useI18n } from "../i18n";

export default function Splash() {
  const { t } = useI18n();
  const router = useRouter();
  useEffect(() => {
    const id = setTimeout(() => router.push("/kyc"), 1000);
    return () => clearTimeout(id);
  }, [router]);
  return (
    <MotiView
      from={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      accessibilityLabel="splash-screen"
      className="flex-1 items-center justify-center bg-white"
    >
      <Text className="text-lg text-[#3BA3FF]">{t("welcome")}</Text>
    </MotiView>
  );
}
