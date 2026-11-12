# Error Log

Complete this file after running `scripts/evaluate_heldout.py`.

## Expected limitations

- The analyser only covers four noun-class patterns.
- It depends on a small manually curated lexicon, so an otherwise plausible unknown stem fails.
- The broad `m-` prefix is class-ambiguous in Kiswahili; class-specific lexical entries reduce, but do not eliminate, ambiguity.
- Some Kiswahili nouns have irregular or non-transparent singular/plural relationships that are not represented by these concatenative rules.
- The analyser does not analyse verbs, modifiers, agreement prefixes, clitics, or borrowed nouns.

## Observed errors

No held-out forms failed in the current 22-form test set. This result should not be interpreted as broad language coverage because the test forms use the same four regular patterns and the analyser has a small curated lexicon.
