export function track(event: string, data?: any) {
  const demo = (globalThis as any).process?.env?.DEMO_MODE === "true";
  if (demo) {
    console.log(`ANALYTICS ${event}`, data || {});
  }
}
