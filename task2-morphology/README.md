# Task 2: Finite-State Morphological Analyser

This task implements a small finite-state analyser for selected Kiswahili noun-class patterns.

## Selected patterns

- Class 1/2: `m-/wa-`, for example `mtoto/watoto`
- Class 3/4: `m-/mi-`, for example `mti/miti`
- Class 5/6: `ji-/ma-`, for example `jicho/macho`
- Class 7/8: `ki-/vi-`, for example `kitabu/vitabu`

The analyser is intentionally limited. It is a class-sensitive lexicon and prefix transducer, not a complete Kiswahili morphological grammar.

## Run the analyser

```bash
cd task2-morphology/scripts
python3 fst_analyser.py
```

## Run held-out evaluation

```bash
python3 evaluate_heldout.py
```

The evaluation writes `results/heldout-results.csv` and prints accuracy. The test forms are kept separate from the development examples in `fst_analyser.py`. The current held-out result is 22/22 correct (100%).
