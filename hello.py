import requests

def search_archidekt_decks(name=None, colors=None, format="commander", page=1, page_size=10):
    query = """
    query Decks(
        $filters: DeckFilter!,
        $page: Int!,
        $pageSize: Int!
    ) {
        decks(
            filters: $filters,
            page: $page,
            pageSize: $pageSize
        ) {
            totalDecks
            decks {
                id
                name
                colors
                url
                likes
            }
        }
    }
    """

    variables = {
        "filters": {
            "name": name,        # Search term (e.g., "My Deck")
            "colors": colors,    # Array of colors (e.g., ["B", "U"])
            "format": format,     # Format (e.g., "commander")
        },
        "page": page,
        "pageSize": page_size
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Content-Type": "application/json"
    }

    response = requests.get(
        "https://archidekt.com/api/graphql/",
        json={"query": query, "variables": variables},
        headers=headers
    )

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


def main():
    result = search_archidekt_decks(
        name="Zombie",          # Partial name match
        colors=["B", "U"],      # Black (B) and Blue (U)
        format="commander",
        page=1,
        page_size=20
    )

    if result:
        decks = result["data"]["decks"]["decks"]
        for deck in decks:
            print(f"ID: {deck['id']}, Name: {deck['name']}, Colors: {deck['colors']}")


if __name__ == "__main__":
    main()
