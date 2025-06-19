import React from "react";
import { Text, View, Button } from "react-native";
import { useI18n } from "../i18n";
import { track } from "../analytics";

export default function Repayment() {
  const { t } = useI18n();
  return (
    <View
      accessibilityLabel="repayment-screen"
      className="flex-1 items-center justify-center p-4"
    >
      <Text className="text-lg text-[#3BA3FF] mb-2">{t("repayment")}</Text>
      <Button title="Pay" onPress={() => track("repayment_success")}></Button>
      <Text className="mt-2 text-xs">Paid 1/6</Text>
    </View>
  );
}
