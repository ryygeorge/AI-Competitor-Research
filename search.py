from dotenv import load_dotenv
import os
import json
from tavily import TavilyClient

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError("Tavily API key not found.")

client = TavilyClient(api_key=api_key)


def search_web(query):
    response = client.search(
        query=query,
        max_results=3
    )
    return response["results"]


company = input("Enter a company to research: ").strip()

if not company:
    raise ValueError("Company name cannot be empty.")

research_topics = [
    f"{company} company overview and products",
    f"{company} main competitors",
    f"{company} recent news",
]

report = {
    "company": company,
    "research": {}
}

for topic in research_topics:
    print(f"\nSearching: {topic}")

    results = search_web(topic)

    report["research"][topic] = []

    for result in results:
        report["research"][topic].append({
            "title": result["title"],
            "url": result["url"],
            "content": result["content"]
        })

with open("research_report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4, ensure_ascii=False)

print("\nResearch completed!")
print("Saved to research_report.json")