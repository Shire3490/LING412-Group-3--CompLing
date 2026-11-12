from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


@dataclass(frozen=True)
class Tree:
    label: str
    children: Tuple[object, ...]

    def bracketed(self) -> str:
        parts = []
        for child in self.children:
            parts.append(child.bracketed() if isinstance(child, Tree) else child)
        return f"({self.label} {' '.join(parts)})"


# Rules are deliberately small and right-branching for this assignment grammar.
RULES: Tuple[Tuple[str, Tuple[str, ...]], ...] = (
    ("S", ("NP", "VP")),
    ("VP", ("V",)),
    ("VP", ("V", "NP")),
    ("VP", ("V", "NP", "NP")),
    ("VP", ("V", "PP")),
    ("VP", ("V", "NP", "PP")),
    ("VP", ("COP", "ADJ")),
    ("VP", ("COP", "PP")),
    ("NP", ("N",)),
    ("NP", ("PROPN",)),
    ("NP", ("DET", "N")),
    ("NP", ("ADJ", "N")),
    ("PP", ("P", "NP")),
)

LEXICON: Dict[str, str] = {
    "watoto": "N",
    "wanacheza": "V",
    "mama": "N",
    "anatoa": "V",
    "kitambaa": "N",
    "tabo": "PROPN",
    "anampa": "V",
    "mfuko": "N",
    "kitabu": "N",
    "ni": "COP",
    "kizuri": "ADJ",
    "mtoto": "N",
    "yuko": "V",
    "katika": "P",
    "nyumba": "N",
    "bibi": "N",
    "anakuja": "V",
    "watu": "N",
    "wanakula": "V",
    "chakula": "N",
    "mwanafunzi": "N",
    "anasoma": "V",
    "mti": "N",
    "uko": "V",
    "bustani": "N",
    "anapika": "V",
    "jikoni": "N",
    "waalimu": "N",
    "wanafundisha": "V",
    "wanafunzi": "N",
    "wakulima": "N",
    "wanalima": "V",
    "shambani": "N",
    "gari": "N",
    "nyekundu": "ADJ",
}


def _add_unary_closure(chart, start, end):
    changed = True
    while changed:
        changed = False
        for parent, rhs in RULES:
            if len(rhs) != 1:
                continue
            child = rhs[0]
            for tree in list(chart[start, end].get(child, [])):
                candidate = Tree(parent, (tree,))
                rendered = candidate.bracketed()
                if rendered not in {item.bracketed() for item in chart[start, end].get(parent, [])}:
                    chart[start, end].setdefault(parent, []).append(candidate)
                    changed = True


def parse(tokens: Iterable[str]) -> List[Tree]:
    tokens = [token.lower() for token in tokens]
    chart = defaultdict(dict)

    for index, token in enumerate(tokens):
        category = LEXICON.get(token)
        if category is not None:
            chart[index, index + 1].setdefault(category, []).append(Tree(category, (token,)))
        _add_unary_closure(chart, index, index + 1)

    for width in range(2, len(tokens) + 1):
        for start in range(len(tokens) - width + 1):
            end = start + width
            for split in range(start + 1, end):
                left = chart[start, split]
                right = chart[split, end]
                for parent, rhs in RULES:
                    if len(rhs) != 2 or rhs[0] not in left or rhs[1] not in right:
                        continue
                    for left_tree in left[rhs[0]]:
                        for right_tree in right[rhs[1]]:
                            chart[start, end].setdefault(parent, []).append(
                                Tree(parent, (left_tree, right_tree))
                            )
            _add_unary_closure(chart, start, end)

    return chart[0, len(tokens)].get("S", [])
