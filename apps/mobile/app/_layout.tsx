import React from "react";
import { Stack } from "expo-router";
import { StatusBar } from "expo-status-bar";
import { I18nProvider } from "../i18n";
import { DemoBadge } from "../DemoBadge";
export default function Layout() {
  return (
    <I18nProvider>
      <Stack />
      <DemoBadge />
      <StatusBar style="auto" />
    </I18nProvider>
  );
}
