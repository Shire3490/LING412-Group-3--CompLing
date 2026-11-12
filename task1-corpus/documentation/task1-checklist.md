# Task 1 Completion Checklist

## Completed

- [x] 18 raw `.txt` files stored in `raw-data/`
- [x] News reporting and story text types represented
- [x] 3,452 processed tokens, exceeding the 2,000-word minimum
- [x] Unicode and whitespace normalisation implemented
- [x] Sentence and token CSV files generated
- [x] Per-source corpus statistics generated
- [x] Cleaning decisions documented
- [x] Source register created
- [x] No image files included in the corpus

## Still to verify

- [ ] Article-level publication details and permissions for BBC articles
- [ ] Original URLs and usage conditions for all DW articles
- [ ] Exact African Storybook page and attribution details for *Zawadi kwa bibi*
- [ ] Independent rerun by another group member

## Final reproducibility command

```bash
cd task1-corpus/scripts
python3 preprocess.py
```

Expected result: 18 input files and approximately 3,452 tokens, subject to any later source corrections.