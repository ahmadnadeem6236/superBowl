export interface Article {
  id: number;
  title: string;
  content: string;
  description: string;
  image: string;
  publishedAt: Date;
  createdAt: Date;
  source: string;
  url: string;
}

export async function getArticleById(id: number): Promise<Article | undefined> {
  try {
    const response = await fetch(`${process.env.SERVER}/articles/${id}`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const article: Article = await response.json();
    return article;
  } catch (error) {
    console.error("Failed to fetch article:", error);
    return undefined;
  }
}
