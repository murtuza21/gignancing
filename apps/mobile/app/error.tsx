import React, { useEffect } from "react";
import { Text, View } from "react-native";
import { useI18n } from "../i18n";
import { track } from "../analytics";

export default function ErrorScreen() {
  const { t } = useI18n();
  useEffect(() => track("error_occurred"), []);
  return (
    <View
      accessibilityLabel="error-screen"
      className="flex-1 items-center justify-center p-4"
    >
      <Text className="text-lg text-red-500">Error</Text>
    </View>
  );
}
