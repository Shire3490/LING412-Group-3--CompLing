import csv
import math
from collections import Counter
from pathlib import Path


TASK_DIR = Path(__file__).resolve().parent.parent
ANNOTATOR_A = TASK_DIR / "data" / "annotator_a.csv"
ANNOTATOR_B = TASK_DIR / "data" / "annotator_b.csv"
RESULT_FILE = TASK_DIR / "results" / "agreement.txt"


def read_tags(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def cohens_kappa(tags_a, tags_b):
    if len(tags_a) != len(tags_b):
        raise ValueError("Annotation files must contain the same number of rows")
    observed = sum(a["tag"] == b["tag"] for a, b in zip(tags_a, tags_b)) / len(tags_a)
    counts_a = Counter(row["tag"] for row in tags_a)
    counts_b = Counter(row["tag"] for row in tags_b)
    labels = set(counts_a) | set(counts_b)
    expected = sum(
        (counts_a[label] / len(tags_a)) * (counts_b[label] / len(tags_b))
        for label in labels
    )
    kappa = (observed - expected) / (1 - expected) if expected != 1 else 1.0
    return observed, expected, kappa


def main():
    tags_a = read_tags(ANNOTATOR_A)
    tags_b = read_tags(ANNOTATOR_B)
    observed, expected, kappa = cohens_kappa(tags_a, tags_b)
    disagreements = sum(a["tag"] != b["tag"] for a, b in zip(tags_a, tags_b))
    RESULT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with RESULT_FILE.open("w", encoding="utf-8") as output:
        output.write("Task 3 inter-annotator agreement\n")
        output.write("STATUS: provisional heuristic annotations; replace with human labels.\n")
        output.write(f"Tokens: {len(tags_a)}\n")
        output.write(f"Observed agreement: {observed:.4f}\n")
        output.write(f"Expected agreement: {expected:.4f}\n")
        output.write(f"Cohen's kappa: {kappa:.4f}\n")
        output.write(f"Disagreements: {disagreements}\n")
        output.write("Interpretation: kappa measures agreement beyond chance; interpret the final human result with the annotation context and tag frequencies.\n")
    print(f"Tokens: {len(tags_a)}")
    print(f"Observed agreement: {observed:.2%}")
    print(f"Cohen's kappa: {kappa:.4f}")
    print(f"Disagreements: {disagreements}")


if __name__ == "__main__":
    main()
