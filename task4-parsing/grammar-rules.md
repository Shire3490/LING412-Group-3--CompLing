# Kiswahili CFG Rules

## Sentence patterns covered

1. **Intransitive:** `NP VP`, with `VP -> V`
   - `Watoto wanacheza`
2. **Transitive:** `NP V NP`, with `VP -> V NP`
   - `Mama anatoa kitambaa`
3. **Ditransitive:** `NP V NP NP`, with `VP -> V NP NP`
   - `Tabo anampa Bibi mfuko`
4. **Copular adjective:** `NP COP ADJ`, with `VP -> COP ADJ`
   - `Kitabu ni kizuri`
5. **Locative copular:** `NP COP PP`, with `VP -> COP PP`
   - `Mtoto yuko katika nyumba`
6. **Verb plus prepositional phrase:** `NP V PP`, with `VP -> V PP`
   - `Bibi anakuja katika nyumba`
7. **Transitive verb plus prepositional phrase:** `NP V NP PP`, with `VP -> V NP PP`
   - `Mama anatoa kitambaa katika jikoni`

## CFG

```text
S -> NP VP
VP -> V | V NP | V NP NP | V PP | V NP PP | COP ADJ | COP PP
NP -> N | PROPN | DET N | ADJ N
PP -> P NP
```

The complete lexicalized grammar is in `kiswahili.cfg`. The grammar is intentionally small and phrase-structure based.
