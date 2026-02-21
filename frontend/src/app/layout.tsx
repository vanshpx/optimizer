import type { Metadata } from "next";
import { Inter_Tight } from "next/font/google";
import "./globals.css";
import { ItineraryProvider } from "@/context/ItineraryContext";

const interTight = Inter_Tight({
  subsets: ["latin"],
  display: "swap",
  weight: ["300", "400", "500", "600", "700"],
});

export const metadata: Metadata = {
  title: "Voyage - AI Co-Pilot for Travel Agents",
  description: "Plan, monitor, and adapt trips in real-time with AI-powered tools.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={interTight.className} suppressHydrationWarning>
      <body className="antialiased">
        <ItineraryProvider>
          {children}
        </ItineraryProvider>
      </body>
    </html>
  );
}
