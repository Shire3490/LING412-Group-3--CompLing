# Corpus Cleaning Note

## Language

The corpus is written in Kiswahili. Confirm the selected language before final submission.

## Corpus composition

The corpus consists of seventeen news-reporting articles and one story. This provides two text types: news reporting and story.

The processed corpus contains 3,452 tokens from eighteen raw files:

- BBC news article 001 (publisher and URL unverified): 152 tokens
- BBC news article 002 (publisher and URL unverified): 188 tokens
- DW news article 001: 242 tokens
- DW news article 002: 134 tokens
- DW news article 003: 170 tokens
- DW news article 004: 133 tokens
- DW news article 005: 147 tokens
- DW news article 006: 186 tokens
- DW news article 007: 191 tokens
- DW news article 008: 137 tokens
- BBC news article 003: 193 tokens
- BBC news article 004: 277 tokens
- BBC news article 005: 327 tokens
- BBC news article 006: 215 tokens
- BBC news article 007: 170 tokens
- BBC news article 008: 246 tokens
- BBC news article 009: 161 tokens
- African Storybook story *Zawadi kwa bibi*: 183 tokens

The BBC articles were supplied on 2026-11-09 with a BBC Kiswahili live-page URL recorded in `sources.csv`; article-level publication details and usage conditions still require confirmation. The DW articles are documented as news reporting, with the supplied DW URL recorded for the first article; usage conditions still require confirmation.

## Sources and permissions

Describe where the texts came from, when they were collected, and whether they were publicly available or collected with permission.

See `sources.csv` for the complete source record.

The processed corpus exceeds the 2,000-word minimum. The African Storybook homepage states a Creative Commons Attribution 4.0 licence. The story was transcribed from photographed pages; verify the exact story URL and attribution details before submission.

## Cleaning performed

We removed:

- Extra whitespace
- Repeated blank lines
- Webpage navigation, advertisements, or other irrelevant material
- Duplicate text, if applicable

## Features retained

We retained meaningful linguistic content, including word order, sentence punctuation, Kiswahili orthography, numbers, and naturally occurring apostrophes or hyphens.

## Tokenisation decisions

Sentences were separated using sentence-final punctuation and non-empty line boundaries. Words were tokenised using the regular expression in `scripts/preprocess.py`.

## Limitations

The sentence splitter may make mistakes with abbreviations, quotations, or unusual punctuation. The corpus is small and may not represent every variety or register of Kiswahili.

## Reproducibility

Run the following command from this directory:

```bash
cd scripts
python3 preprocess.py
```
