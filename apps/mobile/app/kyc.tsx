import React, { useEffect } from "react";
import { Text, View } from "react-native";
import { useRouter } from "expo-router";
export default function KYCStart() {
  const router = useRouter();
  useEffect(() => {
    const id = setTimeout(() => router.push("/connect"), 1000);
    return () => clearTimeout(id);
  }, [router]);
  return (
    <View accessibilityLabel="kyc-screen">
      <Text>KYC Start</Text>
    </View>
  );
}
