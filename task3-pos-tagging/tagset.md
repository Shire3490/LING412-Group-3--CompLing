# Kiswahili POS Tagging Guidelines

## Scope

Use one label per token. Annotate tokens in their original order. The tagset is deliberately small and must be applied consistently.

| Tag | Meaning | Examples |
|---|---|---|
| `NOUN` | Common or abstract noun | `silaha`, `mji`, `watu` |
| `PROPN` | Proper name or place | `Iran`, `Poland`, `Krakow` |
| `VERB` | Main verb or auxiliary verb | `amesema`, `walikuwa`, `inaendelea` |
| `ADJ` | Descriptive adjective | `kubwa`, `mrefu` |
| `ADV` | Adverb or adverbial word | `sana`, `leo`, `hivi` |
| `PRON` | Independent pronoun or possessive pronoun | `yake`, `wote`, `huyo` |
| `DET` | Demonstrative, quantifier, or determiner-like word | `hii`, `hiyo`, `baadhi` |
| `ADP` | Preposition or relational marker | `kwa`, `katika`, `kutoka` |
| `CONJ` | Coordinating or subordinating conjunction | `na`, `lakini`, `ikiwa` |
| `NUM` | Number or numeric expression | `tatu`, `21`, `193` |
| `PART` | Particle, negator, or discourse marker | `si`, `je`, `pia` |
| `X` | Foreign, residual, or unresolved token | `cruise`, `AFP` |

## Decision rules

1. Tag proper names as `PROPN`, including countries, cities, people, and organisations.
2. Tag inflected or multi-morpheme words by their syntactic role, not by their individual morphemes.
3. Use `NOUN` for a nominal expression when no proper-name reading applies.
4. Use `VERB` for finite verbs and infinitive forms beginning with `ku-` when they function as verbs.
5. Use `X` only when the token cannot be assigned reliably using the available context.
6. When context is ambiguous, record the decision and apply the same decision to comparable cases.

## Annotation protocol

Annotators must label the same 600-token sample independently, without seeing the other annotation. They should record disagreements before reconciliation. The reconciled file is the gold-standard dataset.
