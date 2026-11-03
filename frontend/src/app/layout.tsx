import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Video Discovery Platform",
  description:
    "Discover videos, connect with creators, and promote content through transparent platform advertising.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
