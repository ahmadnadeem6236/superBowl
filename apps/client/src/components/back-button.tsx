"use client";

import { Button } from "@/components/ui/button";
import { ArrowLeft } from "lucide-react";
import { useRouter } from "next/navigation";

export default function BackButton() {
  const router = useRouter();

  return (
    <Button variant="ghost" onClick={() => router.back()} className="mb-4">
      <ArrowLeft className="mr-2 h-4 w-4" />
      Back
    </Button>
  );
}
