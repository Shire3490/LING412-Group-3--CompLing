from pathlib import Path
import csv
import re
import unicodedata


PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "raw-data"
CLEAN_FILE = PROJECT_DIR / "processed-data" / "kiswahili_clean.txt"
SENTENCES_FILE = PROJECT_DIR / "processed-data" / "sentences.csv"
TOKENS_FILE = PROJECT_DIR / "processed-data" / "tokens.csv"
STATS_FILE = PROJECT_DIR / "processed-data" / "corpus-stats.csv"

SOURCE_IDS = {
    "bbc_news_001.txt": "SRC002",
    "bbc_news_002.txt": "SRC003",
    "bbc_news_003.txt": "SRC012",
    "bbc_news_004.txt": "SRC013",
    "bbc_news_005.txt": "SRC014",
    "bbc_news_006.txt": "SRC015",
    "bbc_news_007.txt": "SRC016",
    "bbc_news_008.txt": "SRC017",
    "bbc_news_009.txt": "SRC018",
    "story_zawadi_kwa_bibi.txt": "SRC019",
    "dw_news_001.txt": "SRC004",
    "dw_news_002.txt": "SRC005",
    "dw_news_003.txt": "SRC006",
    "dw_news_004.txt": "SRC007",
    "dw_news_005.txt": "SRC008",
    "dw_news_006.txt": "SRC009",
    "dw_news_007.txt": "SRC010",
    "dw_news_008.txt": "SRC011",
}


def normalize_text(text):
    """Remove formatting noise while preserving linguistic content."""
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()


def split_sentences(text):
    """Split on sentence punctuation or non-empty source lines."""
    return [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+|\n+", text)
        if sentence.strip()
    ]


def tokenize(sentence):
    """Tokenize words, numbers, apostrophes, and internal hyphens."""
    return re.findall(
        r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:['-][A-Za-zÀ-ÖØ-öø-ÿ]+)*|\d+",
        sentence,
    )


def process_file(path):
    text = path.read_text(encoding="utf-8")
    text = normalize_text(text)
    records = []

    for sentence_number, sentence in enumerate(split_sentences(text), start=1):
        tokens = tokenize(sentence)
        if tokens:
            records.append(
                {
                    "source_id": SOURCE_IDS.get(path.name, "UNREGISTERED"),
                    "source_file": path.name,
                    "sentence_number": sentence_number,
                    "text": sentence,
                    "tokens": tokens,
                }
            )

    return records


def main():
    CLEAN_FILE.parent.mkdir(parents=True, exist_ok=True)
    records = []
    input_files = sorted(RAW_DIR.glob("*.txt"))

    for path in input_files:
        records.extend(process_file(path))

    with CLEAN_FILE.open("w", encoding="utf-8") as output:
        for record in records:
            output.write(record["text"] + "\n")

    with SENTENCES_FILE.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(
            output,
            fieldnames=[
                "sentence_id",
                "source_id",
                "source_file",
                "sentence_number",
                "text",
            ],
        )
        writer.writeheader()
        for sentence_id, record in enumerate(records, start=1):
            writer.writerow(
                {
                    "sentence_id": sentence_id,
                    "source_id": record["source_id"],
                    "source_file": record["source_file"],
                    "sentence_number": record["sentence_number"],
                    "text": record["text"],
                }
            )

    with TOKENS_FILE.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(
            output,
            fieldnames=["sentence_id", "token_number", "token"],
        )
        writer.writeheader()
        for sentence_id, record in enumerate(records, start=1):
            for token_number, token in enumerate(record["tokens"], start=1):
                writer.writerow(
                    {
                        "sentence_id": sentence_id,
                        "token_number": token_number,
                        "token": token,
                    }
                )

    source_stats = {}
    for record in records:
        key = (record["source_id"], record["source_file"])
        stats = source_stats.setdefault(key, {"sentences": 0, "tokens": 0})
        stats["sentences"] += 1
        stats["tokens"] += len(record["tokens"])

    with STATS_FILE.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(
            output,
            fieldnames=["source_id", "source_file", "sentences", "words"],
        )
        writer.writeheader()
        for (source_id, source_file), stats in sorted(source_stats.items()):
            writer.writerow(
                {
                    "source_id": source_id,
                    "source_file": source_file,
                    "sentences": stats["sentences"],
                    "words": stats["tokens"],
                }
            )

    word_count = sum(len(record["tokens"]) for record in records)

    print(f"Input files: {len(input_files)}")
    print(f"Sentences: {len(records)}")
    print(f"Tokens: {word_count}")
    print(f"Clean text: {CLEAN_FILE}")
    print(f"Sentences: {SENTENCES_FILE}")
    print(f"Tokens: {TOKENS_FILE}")
    print(f"Statistics: {STATS_FILE}")

    if word_count < 2000:
        print("WARNING: The assignment requires at least 2,000 words.")


if __name__ == "__main__":
    main()
