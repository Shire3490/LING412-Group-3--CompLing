import csv
from pathlib import Path

from fst_analyser import KiswahiliNounFST


PROJECT_DIR = Path(__file__).resolve().parent.parent
TEST_FILE = PROJECT_DIR / "data" / "heldout.csv"
RESULTS_FILE = PROJECT_DIR / "results" / "heldout-results.csv"


def main():
    analyser = KiswahiliNounFST()
    rows = []
    correct = 0

    with TEST_FILE.open(encoding="utf-8", newline="") as handle:
        for expected in csv.DictReader(handle):
            analyses = analyser.analyse(expected["form"])
            match = next(
                (
                    analysis
                    for analysis in analyses
                    if analysis.noun_class == expected["expected_class"]
                    and analysis.number == expected["expected_number"]
                    and analysis.prefix == expected["expected_prefix"]
                    and analysis.stem == expected["expected_stem"]
                    and analysis.gloss == expected["expected_gloss"]
                ),
                None,
            )
            passed = match is not None
            correct += int(passed)
            rows.append(
                {
                    "form": expected["form"],
                    "expected_class": expected["expected_class"],
                    "expected_number": expected["expected_number"],
                    "expected_prefix": expected["expected_prefix"],
                    "expected_stem": expected["expected_stem"],
                    "predicted": "yes" if analyses else "no",
                    "correct": "yes" if passed else "no",
                    "returned_analyses": " | ".join(
                        f"{item.noun_class}:{item.number}:{item.prefix}+{item.stem}"
                        for item in analyses
                    ),
                }
            )

    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with RESULTS_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    total = len(rows)
    print(f"Held-out forms: {total}")
    print(f"Correct analyses: {correct}")
    print(f"Accuracy: {correct / total:.2%}")
    print(f"Results: {RESULTS_FILE}")


if __name__ == "__main__":
    main()