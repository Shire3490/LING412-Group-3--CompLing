# Task 1: Kiswahili Corpus Compilation and Pre-processing

This folder contains the corpus, source records, preprocessing script, and documentation for Task 1 of the LING 412 / ENGL 416 computational linguistics project.

## Folder structure

```text
raw-data/          Unchanged source texts
processed-data/    Generated clean text, CSV files, and corpus statistics
scripts/           Reproducible preprocessing code
documentation/     Source records, audit, cleaning note, and README
```

## Workflow

1. Keep authorised `.txt` files unchanged in `raw-data/`.
2. Record every file in `documentation/sources.csv`, including its text type and provenance.
3. Run the preprocessing script:

```bash
cd scripts
python3 preprocess.py
```

4. Confirm that the output reports at least 2,000 tokens. Per-source counts are written to `processed-data/corpus-stats.csv`.
5. Confirm that the source records identify at least two genuine text types. Different subjects within one genre do not count as different text types.
6. Complete `documentation/cleaning-note.md` with the actual corpus statistics and decisions.

The raw files must not be overwritten by preprocessing. The Makerere corpus is still unverified; the two news files are also awaiting original URLs, publisher confirmation, publication dates, and permissions.

## Current corpus status

The corpus currently contains 18 raw files, 17 news-reporting articles, and one story. It contains 3,452 processed tokens and represents two text types. See `task1-checklist.md` for completed work and remaining verification items.
