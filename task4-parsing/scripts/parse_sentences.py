import csv
from pathlib import Path

from nltk import CFG
from nltk.parse import ChartParser


TASK_DIR = Path(__file__).resolve().parent.parent
GRAMMAR_FILE = TASK_DIR / "kiswahili.cfg"
EXAMPLES_FILE = TASK_DIR / "data" / "examples.csv"
TREES_FILE = TASK_DIR / "results" / "parse-trees.txt"
RESULTS_FILE = TASK_DIR / "results" / "parse-results.csv"


def load_examples():
    with EXAMPLES_FILE.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main():
    grammar = CFG.fromstring(GRAMMAR_FILE.read_text(encoding="utf-8"))
    parser = ChartParser(grammar)
    examples = load_examples()
    results = []
    tree_lines = []

    for example in examples:
        tokens = example["sentence"].lower().split()
        trees = list(parser.parse(tokens))
        parsed = bool(trees)
        results.append(
            {
                "id": example["id"],
                "pattern": example["pattern"],
                "sentence": example["sentence"],
                "parsed": "yes" if parsed else "no",
                "tree_count": len(trees),
            }
        )
        tree_lines.append(f"{example['id']} | {example['pattern']} | {example['sentence']}")
        if trees:
            tree_lines.append(str(trees[0]))
        else:
            tree_lines.append("NO PARSE")
        tree_lines.append("")

    TREES_FILE.parent.mkdir(parents=True, exist_ok=True)
    TREES_FILE.write_text("\n".join(tree_lines), encoding="utf-8")
    with RESULTS_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    parsed_count = sum(row["parsed"] == "yes" for row in results)
    print(f"Examples: {len(results)}")
    print(f"Parsed: {parsed_count}/{len(results)}")
    print(f"Parse trees: {TREES_FILE}")
    print(f"Results: {RESULTS_FILE}")


if __name__ == "__main__":
    main()
