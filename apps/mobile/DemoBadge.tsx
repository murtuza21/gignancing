import React from "react";
import { Text, View } from "react-native";

export function DemoBadge() {
  const demo = (globalThis as any).process?.env?.DEMO_MODE === "true";
  if (!demo) return null;
  return (
    <View className="absolute top-2 right-2 bg-red-500 px-2 py-1 rounded">
      <Text className="text-white text-xs">Demo Mode</Text>
    </View>
  );
}
