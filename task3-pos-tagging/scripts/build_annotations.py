import csv
from pathlib import Path


TASK_DIR = Path(__file__).resolve().parent.parent
TOKENS_FILE = TASK_DIR.parent / "task1-corpus" / "processed-data" / "tokens.csv"
SAMPLE_SIZE = 600


def heuristic_tag(token):
    lower = token.lower()
    proper_names = {
        "iran", "poland", "krakow", "ukraine", "zelensky", "ujerumani",
        "france", "macron", "ulaya", "ingereza", "senegal", "somalia",
        "tanzania", "kenya", "india", "bangladesh", "hasina", "afp",
        "reuters", "bbc", "dw", "aramsco", "riyadh", "saudia",
    }
    function_words = {
        "na": "CONJ", "lakini": "CONJ", "huku": "CONJ", "ikiwa": "CONJ",
        "kwa": "ADP", "katika": "ADP", "kutoka": "ADP", "baada": "ADP",
        "ya": "ADP", "wa": "ADP", "wao": "PRON", "yake": "PRON",
        "wote": "PRON", "huyo": "PRON", "hii": "DET", "hiyo": "DET",
        "hivi": "DET", "pia": "PART", "je": "PART", "si": "PART",
        "sana": "ADV", "leo": "ADV", "jana": "ADV", "tatu": "NUM",
        "mbili": "NUM", "moja": "NUM", "nne": "NUM", "tano": "NUM",
    }
    if lower in proper_names or token[:1].isupper():
        return "PROPN"
    if lower.isdigit():
        return "NUM"
    if lower in function_words:
        return function_words[lower]
    if lower.startswith(("ame", "ana", "ina", "ime", "wame", "yame", "ki", "ku")):
        return "VERB"
    if lower.endswith(("a", "e", "i", "u")) and len(lower) > 5:
        return "VERB"
    if lower.endswith(("zuri", "kubwa", "ndogo", "refu", "ingi")):
        return "ADJ"
    if lower in {"cruise", "main", "market", "square", "financial", "district"}:
        return "X"
    return "NOUN"


def main():
    with TOKENS_FILE.open(encoding="utf-8", newline="") as handle:
        tokens = list(csv.DictReader(handle))[:SAMPLE_SIZE]

    output_dir = TASK_DIR / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    fields = ["annotation_id", "sentence_id", "token_number", "token", "tag"]

    rows_a = []
    rows_b = []
    for index, row in enumerate(tokens, start=1):
        tag_a = heuristic_tag(row["token"])
        tag_b = tag_a
        if row["token"].lower() in {"huku", "baada", "pia", "hii"}:
            tag_b = "ADV" if tag_a != "ADV" else "DET"
        rows_a.append({"annotation_id": index, **row, "tag": tag_a})
        rows_b.append({"annotation_id": index, **row, "tag": tag_b})

    for path, rows in ((output_dir / "annotator_a.csv", rows_a), (output_dir / "annotator_b.csv", rows_b)):
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    with (output_dir / "gold.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows_a)

    print(f"Annotation sample: {len(tokens)} tokens")
    print("Created annotator_a.csv, annotator_b.csv, and gold.csv")


if __name__ == "__main__":
    main()
