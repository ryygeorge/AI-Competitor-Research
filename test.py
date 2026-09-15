def introduce_company(name):
    return f"Welcome to {name}!"


company = input("Enter the company name: ")

result = introduce_company(company)

print(result)

competitors = ["Disney+", "Prime Video", "Hulu"]

print("\nCompetitors:")

for competitor in competitors:
    print("-", competitor)

companies = [
    {
        "name": "Netflix",
        "industry": "Streaming"
    },
    {
        "name": "Disney+",
        "industry": "Streaming"
    },
    {
        "name": "Prime Video",
        "industry": "Streaming"
    }
]

for company in companies:
    print(company["name"], "-", company["industry"])