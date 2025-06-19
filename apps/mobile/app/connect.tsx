import React, { useEffect } from "react";
import { Text, View } from "react-native";
import { useRouter } from "expo-router";
import { useI18n } from "../i18n";
import { track } from "../analytics";

export default function PlatformConnect() {
  const { t } = useI18n();
  const router = useRouter();
  useEffect(() => {
    track("platform_link_success");
    const id = setTimeout(() => router.push("/income"), 1000);
    return () => clearTimeout(id);
  }, [router]);
  return (
    <View
      accessibilityLabel="connect-screen"
      className="flex-1 items-center justify-center p-4"
    >
      <Text className="text-lg text-[#3BA3FF]">{t("connect")}</Text>
    </View>
  );
}
