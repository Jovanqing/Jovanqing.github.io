"""Fetch the Google Scholar citation count via SerpApi and write a shields.io badge file.

Google Scholar blocks direct scraping from GitHub-hosted runners; SerpApi's
google_scholar_author engine (free tier) does not. Approach adapted from
https://github.com/utomm/Unblock-Google-Scholar-Action

Output: results/gs_data_shieldsio.json (shields.io endpoint schema).
Any failure exits non-zero and writes nothing, so the last good count stays published.
"""

import json
import os
import sys
import urllib.parse
import urllib.request


def citations_from(data: dict) -> int:
    """Total citations from a google_scholar_author response; raises if absent."""
    value = data["cited_by"]["table"][0]["citations"]["all"]
    if not isinstance(value, int):
        raise TypeError("citations.all is not an int: %r" % (value,))
    return value


def main() -> None:
    api_key = os.environ.get("SERPAPI_API_KEY")
    author_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not api_key or not author_id:
        sys.exit("SERPAPI_API_KEY and GOOGLE_SCHOLAR_ID must be set")

    query = urllib.parse.urlencode(
        {"engine": "google_scholar_author", "author_id": author_id, "hl": "en", "api_key": api_key}
    )
    with urllib.request.urlopen("https://serpapi.com/search.json?" + query, timeout=60) as resp:
        data = json.load(resp)

    try:
        citations = citations_from(data)
    except (KeyError, IndexError, TypeError) as exc:
        sys.exit("No citation count in SerpApi response (%s): %s" % (exc, data.get("error", "unexpected format")))

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as fp:
        json.dump({"schemaVersion": 1, "label": "citations", "message": str(citations)}, fp)
    print("citations:", citations)


if __name__ == "__main__":
    main()
