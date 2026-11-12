import csv
from collections import Counter, defaultdict
from pathlib import Path


TASK_DIR = Path(__file__).resolve().parent.parent
GOLD_FILE = TASK_DIR / "data" / "gold.csv"
RESULT_FILE = TASK_DIR / "results" / "tagger-evaluation.txt"


def main():
    with GOLD_FILE.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    split = int(len(rows) * 0.8)
    train_rows = rows[:split]
    test_rows = rows[split:]
    word_tags = defaultdict(Counter)
    tag_counts = Counter()

    for row in train_rows:
        word = row["token"].lower()
        tag = row["tag"]
        word_tags[word][tag] += 1
        tag_counts[tag] += 1

    majority_tag = tag_counts.most_common(1)[0][0]
    correct = 0
    errors = []
    for row in test_rows:
        word = row["token"].lower()
        predicted = word_tags[word].most_common(1)[0][0] if word in word_tags else majority_tag
        if predicted == row["tag"]:
            correct += 1
        elif len(errors) < 20:
            errors.append((row["token"], row["tag"], predicted))

    accuracy = correct / len(test_rows) if test_rows else 0
    RESULT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with RESULT_FILE.open("w", encoding="utf-8") as output:
        output.write("Task 3 baseline POS tagger evaluation\n")
        output.write("Model: word-to-tag majority lookup with training-set fallback\n")
        output.write(f"Training tokens: {len(train_rows)}\n")
        output.write(f"Test tokens: {len(test_rows)}\n")
        output.write(f"Accuracy: {accuracy:.4f}\n")
        output.write("Common recorded errors:\n")
        for token, expected, predicted in errors:
            output.write(f"- {token}: expected={expected}, predicted={predicted}\n")

    print(f"Training tokens: {len(train_rows)}")
    print(f"Test tokens: {len(test_rows)}")
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Results: {RESULT_FILE}")


if __name__ == "__main__":
    main()
