# Task 4: Syntactic Parsing

This task uses an explicit context-free grammar (CFG) and NLTK's chart parser to analyse selected Kiswahili sentence patterns.

## Files

- `kiswahili.cfg`: lexicalized CFG
- `grammar-rules.md`: sentence patterns and rule explanation
- `data/examples.csv`: ten example sentences
- `scripts/parse_sentences.py`: parser and output generator
- `results/parse-trees.txt`: generated bracketed parse trees
- `results/parse-results.csv`: parse success and ambiguity counts
- `limitations.md`: limitations and dependency-parsing comparison

## Run

The project-local virtual environment contains NLTK:

```bash
cd task4-parsing
.venv/bin/python scripts/parse_sentences.py
```

Expected result:

```text
Examples: 10
Parsed: 10/10
```

The grammar covers at least six patterns: intransitive, transitive, ditransitive, copular-adjectival, locative, verb-plus-PP, and transitive-plus-PP. One example has two trees because the small lexicon allows an ambiguity; this is recorded rather than hidden.
