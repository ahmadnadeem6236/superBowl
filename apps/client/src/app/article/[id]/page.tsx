import { notFound } from "next/navigation";
import Image from "next/image";
import { getArticleById } from "@/lib/types";
import BackButton from "@/components/back-button";

export default async function ArticlePage({
  params,
}: {
  params: { id: string };
}) {
  const article = await getArticleById(Number.parseInt(params.id));

  if (!article) {
    notFound();
  }

  return (
    <article className="max-w-3xl mx-auto">
      <BackButton />
      <h1 className="text-4xl font-bold mb-4">{article.title}</h1>
      <Image
        src={article.image || "/placeholder.svg"}
        alt={article.title}
        width={800}
        height={400}
        className="w-full h-64 object-cover rounded-lg mb-6"
      />
      <div className="prose prose-lg max-w-none">
        <p>{article.content}</p>
      </div>
    </article>
  );
}
