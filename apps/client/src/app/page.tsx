import ArticleCard from "@/components/article-card";
import type { Article } from "../lib/types";

export default async function Home() {
  const data = await fetch(`${process.env.SERVER}/articles`);
  const articles = await data.json();
  console.log("server", articles);
  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Latest Super Bowl News:</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {articles.map((article: Article) => (
          <ArticleCard key={article.id} article={article} />
        ))}
      </div>
    </div>
  );
}
