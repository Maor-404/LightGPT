# Wikipedia data collection script
# ----------------------------------
# This script uses the ``wikipedia`` Python package to fetch the plain text of
# a list of topic titles and writes them to a single text file. The resulting
# file can be used directly with the existing ``train.py`` finetuning
# script.
# ----------------------------------

import argparse
import wikipedia
import os

def fetch_topics(topics, output_path, lang="en"):
    wikipedia.set_lang(lang)
    with open(output_path, "w", encoding="utf-8") as out_file:
        for topic in topics:
            try:
                page = wikipedia.page(topic)
                out_file.write(page.title + "\n")
                out_file.write(page.content + "\n\n")
                print(f"Fetched: {topic}")
            except Exception as e:
                print(f"Failed to fetch {topic}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Wikipedia articles to a training file")
    parser.add_argument("--topics", nargs="+", required=True, help="List of Wikipedia page titles to fetch")
    parser.add_argument("--output", default="wiki_corpus.txt", help="Output text file")
    parser.add_argument("--lang", default="en", help="Language code (default: en)")
    args = parser.parse_args()
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    fetch_topics(args.topics, args.output, args.lang)
