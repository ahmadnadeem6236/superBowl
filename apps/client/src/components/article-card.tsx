import Image from "next/image";
import Link from "next/link";
import type { Article } from "../lib/types";

interface ArticleCardProps {
  article: Article;
}

export default function ArticleCard({ article }: ArticleCardProps) {
  return (
    <Link href={`/article/${article.id}`} className="block">
      <div className="bg-card text-card-foreground rounded-lg shadow-md overflow-hidden transition-transform hover:scale-105">
        <Image
          src={article.image || "/placeholder.svg"}
          alt={article.title}
          width={400}
          height={200}
          className="w-full h-48 object-cover"
        />
        <div className="p-4">
          <h2 className="text-xl font-semibold mb-2">{article.title}</h2>
          <p className="text-muted-foreground">{article.description}</p>
        </div>
      </div>
    </Link>
  );
}
