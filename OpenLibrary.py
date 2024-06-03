import requests
import click


# @click.Command(name="openlibrary-search")
@click.argument("query")
def open_library(query):
    url = f"https://openlibrary.org/search.json?q={query}"
    response = requests.get(url)
    data = response.json()

    if "docs" in data:
        for book in data["docs"]:
            click.echo(f"Title: {book.get('title', 'Unknown')}")
            click.echo(f"Author: {', '.join(book.get('author_name', ['Unknown']))}")
            click.echo()


if __name__ == "__main__":
    open_library("query")
