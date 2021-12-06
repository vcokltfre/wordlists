from dataclasses import dataclass
from pathlib import Path
from typing import Dict

from requests import get, RequestException


WL_CACHE = Path.home() / ".wordlist_cache"
WL_CACHE.mkdir(exist_ok=True)


@dataclass
class Wordlist:
    name: str
    url: str
    license: str


lists: Dict[str, Wordlist] = {
    "dwyl": Wordlist(
        "DWYL Words",
        "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt",
        "unlicense",
    ),
    "dwyl_alpha": Wordlist(
        "DWYL Words (alpha only)",
        "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt",
        "Unlicense",
    )
}

def update_lists(license: str = None) -> None:
    for filename, wordlist in lists.items():
        if license and wordlist.license != license:
            continue

        file = WL_CACHE / f"{filename}.txt"

        try:
            resp = get(wordlist.url)

            resp.raise_for_status()

            file.write_text(resp.text)
        except RequestException:
            print(f"Failed to download wordlist {wordlist.name}")

def read_words(wordlist: str) -> list[str]:
    if wordlist not in lists:
        raise ValueError(f"Unknown wordlist {wordlist}")

    file = WL_CACHE / f"{wordlist}.txt"

    if not file.exists():
        print("Updating word list cache...")
        update_lists()

    return file.read_text().splitlines()
