import React from "react";
import { Text, View, Button } from "react-native";
import { useRouter } from "expo-router";
import { useI18n } from "../../i18n";

export default function Dashboard() {
  const { t } = useI18n();
  const router = useRouter();
  return (
    <View
      accessibilityLabel="dashboard-screen"
      className="flex-1 items-center justify-center p-4"
    >
      <Text className="text-lg text-[#3BA3FF]">{t("dashboard")}</Text>
      <Button title="Repay" onPress={() => router.push("/repayment")}></Button>
    </View>
  );
}
