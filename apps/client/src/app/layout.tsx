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
        <header className="bg-primary text-primary-foreground p-4">
          <div className="container mx-auto flex justify-between items-center">
            <h1 className="text-2xl font-bold">Super Bowl Hub</h1>
            <button className="bg-secondary text-secondary-foreground px-4 py-2 rounded hover:bg-secondary/90 transition-colors">
              Subscribe
            </button>
          </div>
        </header>
        <main className="container mx-auto py-8 h-full overflow-scroll">
          {children}
        </main>
      </body>
    </html>
  );
}
