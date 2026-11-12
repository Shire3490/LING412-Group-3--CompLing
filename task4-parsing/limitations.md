# Parser Limitations

## 1. Limited lexical coverage

The parser only accepts words listed in `kiswahili.cfg`. A grammatical sentence containing an unknown word receives no parse, even if its structure follows one of the supported patterns.

## 2. Limited agreement and morphology

The CFG treats inflected words such as `wanacheza` and `anatoa` as indivisible lexical verbs. It does not check subject-verb agreement, noun-class agreement, tense, or object markers. A sentence with incorrect agreement may still parse if its words are in the lexicon.

## 3. Ambiguity

The small lexicon and general rules can produce multiple parses. For example, `Tabo` is available as both `N` and `PROPN`, so `Tabo anampa Bibi mfuko` has more than one analysis. The parser reports the alternatives but does not rank them.

## 4. Incomplete syntactic coverage

The grammar does not yet cover relative clauses, negation, questions, coordination, modifiers with agreement, applicatives, passives, or richer subordinate clauses. These are expected failures, not evidence that the constructions are ungrammatical.

## Dependency comparison

A dependency parser would represent relations such as `anatoa -> Mama` (subject), `anatoa -> kitambaa` (object), and `anatoa -> katika jikoni` (oblique/location). The current implementation produces phrase-structure trees only. A dependency comparison is therefore presented conceptually rather than as a second trained parser because the project has no dependency-annotated Kiswahili treebank.
