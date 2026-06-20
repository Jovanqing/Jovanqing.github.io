"""Google Scholar crawler - fetches the author profile and writes JSON.

Output files (written to ./results):
  - gs_data.json              full author payload (used by the homepage script)
  - gs_data_shieldsio.json    citation count badge endpoint (legacy)
  - gs_stats.json             compact stats card payload
"""

from datetime import datetime, timezone
import json
import os
import signal
import sys

from scholarly import scholarly


FETCH_TIMEOUT_SECONDS = 180  # 3 min hard cap on the entire scholar fetch


def _timeout_handler(signum, frame):
    raise TimeoutError("Scholar fetch exceeded %d seconds" % FETCH_TIMEOUT_SECONDS)


def main() -> None:
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID")
    if not scholar_id:
        sys.exit("GOOGLE_SCHOLAR_ID environment variable is not set")

    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(FETCH_TIMEOUT_SECONDS)

    try:
        author = scholarly.search_author_id(scholar_id)
        scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
    finally:
        signal.alarm(0)

    updated_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    author["updated"] = updated_iso
    author["publications"] = {
        pub["author_pub_id"]: pub for pub in author["publications"]
    }

    os.makedirs("results", exist_ok=True)

    with open("results/gs_data.json", "w", encoding="utf-8") as fp:
        json.dump(author, fp, ensure_ascii=False)

    citedby = author.get("citedby", 0)
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as fp:
        json.dump(
            {"schemaVersion": 1, "label": "citations", "message": str(citedby)},
            fp,
            ensure_ascii=False,
        )

    stats = {
        "citations": citedby,
        "citations_5y": author.get("citedby5y", 0),
        "h_index": author.get("hindex", 0),
        "h_index_5y": author.get("hindex5y", 0),
        "i10_index": author.get("i10index", 0),
        "i10_index_5y": author.get("i10index5y", 0),
        "updated": updated_iso,
    }
    with open("results/gs_stats.json", "w", encoding="utf-8") as fp:
        json.dump(stats, fp, ensure_ascii=False)

    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
