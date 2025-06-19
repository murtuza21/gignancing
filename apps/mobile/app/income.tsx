import React, { useEffect } from "react";
import { Text, View } from "react-native";
import { useRouter } from "expo-router";
import { useI18n } from "../i18n";

export default function IncomeReview() {
  const { t } = useI18n();
  const router = useRouter();
  useEffect(() => {
    const id = setTimeout(() => router.push("/offer"), 1000);
    return () => clearTimeout(id);
  }, [router]);
  return (
    <View
      accessibilityLabel="income-screen"
      className="flex-1 items-center justify-center p-4"
    >
      <Text className="text-lg text-[#3BA3FF]">{t("income")}</Text>
    </View>
  );
}
