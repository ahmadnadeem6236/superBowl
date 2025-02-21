import type React from "react";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Articles Landing Page",
  description: "A simple landing page to render articles",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <header className="bg-primary text-primary-foreground p-4 ">
          <div className="container mx-auto flex justify-center items-center">
            <h1 className="text-3xl font-bold tracking-wider">
              Super Bowl Hub
            </h1>
          </div>
        </header>
        <main className="container mx-auto py-8 h-full overflow-scroll">
          {children}
        </main>
      </body>
    </html>
  );
}
