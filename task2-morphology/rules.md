# Morphological Rules

## Scope

The analyser models four selected Kiswahili noun-class patterns. A surface form is segmented into a noun-class prefix and a stem. The stem is then checked against a small development lexicon for that class.

## Rules

| Pattern | Singular prefix | Plural prefix | Development examples |
|---|---|---|---|
| Class 1/2 | `m-` | `wa-` | `mtoto/watoto`, `mzazi/wazazi` |
| Class 3/4 | `m-` | `mi-` | `mti/miti`, `mlima/milima` |
| Class 5/6 | `ji-` | `ma-` | `jicho/macho`, `jiwe/mawe` |
| Class 7/8 | `ki-` | `vi-` | `kitabu/vitabu`, `kisu/visu` |

## FST interpretation

Each prefix is a transition from the start state to a class-and-number state. The remaining characters are consumed as the stem. An accepting analysis is returned only when the class, prefix, and stem occur in the development lexicon.

The analyser does not model all Kiswahili noun classes, allomorphy, phonological alternation, semantic ambiguity, agreement, or productive unknown stems. Those limitations are reported in `error-log.md`.
