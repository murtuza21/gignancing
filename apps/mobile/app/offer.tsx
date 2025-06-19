import React from "react";
import { Text, View, Button } from "react-native";
import { useRouter } from "expo-router";
import { useI18n } from "../i18n";
import { track } from "../analytics";

export default function Offer() {
  const { t } = useI18n();
  const router = useRouter();
  return (
    <View
      accessibilityLabel="offer-screen"
      className="flex-1 items-center justify-center p-4"
    >
      <Text className="text-lg text-[#3BA3FF] mb-2">{t("offer")}</Text>
      <Button
        title="Accept"
        onPress={() => {
          track("loan_disbursed");
          router.push("/dashboard");
        }}
      ></Button>
    </View>
  );
}
