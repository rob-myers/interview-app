import type { Metadata } from "next";
import "./globals.css";
import Root from "@/components/Root";

export const metadata: Metadata = {
  title: "Interview App",
  description: "For interviews",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <Root>
          {children}
        </Root>
      </body>
    </html>
  );
}
