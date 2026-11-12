from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass(frozen=True)
class Analysis:
    surface: str
    noun_class: str
    number: str
    prefix: str
    stem: str
    gloss: str


class KiswahiliNounFST:
    """Finite-state lexicon for selected Kiswahili noun-class prefixes.

    The analyser consumes a surface form by matching a class prefix and
    looking up the remaining stem in the development lexicon.
    """

    PREFIXES: Tuple[Tuple[str, str, str, str], ...] = (
        ("class_1_2", "singular", "m/wa", "m"),
        ("class_1_2", "plural", "m/wa", "wa"),
        ("class_3_4", "singular", "m/mi", "m"),
        ("class_3_4", "plural", "m/mi", "mi"),
        ("class_5_6", "singular", "ji/ma", "ji"),
        ("class_5_6", "plural", "ji/ma", "ma"),
        ("class_7_8", "singular", "ki/vi", "ki"),
        ("class_7_8", "plural", "ki/vi", "vi"),
    )

    LEXICON: Dict[Tuple[str, str], str] = {
        ("class_1_2", "toto"): "child",
        ("class_1_2", "zazi"): "parent",
        ("class_1_2", "geni"): "guest",
        ("class_1_2", "falme"): "king",
        ("class_3_4", "ti"): "tree",
        ("class_3_4", "zizi"): "root",
        ("class_3_4", "lima"): "mountain",
        ("class_3_4", "to"): "river",
        ("class_5_6", "cho"): "eye",
        ("class_5_6", "embe"): "mango",
        ("class_5_6", "tunda"): "fruit",
        ("class_5_6", "we"): "stone",
        ("class_7_8", "tabu"): "book",
        ("class_7_8", "su"): "knife",
        ("class_7_8", "ti"): "chair",
        ("class_7_8", "kapu"): "basket",
    }

    def analyse(self, surface: str) -> List[Analysis]:
        """Return analyses for a lower-case surface form."""
        surface = surface.strip().lower()
        analyses = []

        for noun_class, number, pair, prefix in self.PREFIXES:
            if not surface.startswith(prefix):
                continue

            stem = surface[len(prefix):]
            gloss = self.LEXICON.get((noun_class, stem))
            if gloss is not None:
                analyses.append(
                    Analysis(
                        surface=surface,
                        noun_class=noun_class,
                        number=number,
                        prefix=prefix,
                        stem=stem,
                        gloss=gloss,
                    )
                )

        return analyses

    def generate(self, noun_class: str, number: str, stem: str) -> Optional[str]:
        """Generate a surface form from a class, number, and stem."""
        for class_name, form_number, _pair, prefix in self.PREFIXES:
            if class_name == noun_class and form_number == number:
                return prefix + stem
        return None


def format_analysis(analysis: Analysis) -> str:
    return (
        f"{analysis.surface}\t{analysis.noun_class}\t{analysis.number}\t"
        f"{analysis.prefix}+{analysis.stem}\t{analysis.gloss}"
    )


if __name__ == "__main__":
    analyser = KiswahiliNounFST()
    for form in ("mtoto", "watoto", "mti", "miti", "jicho", "macho"):
        analyses = analyser.analyse(form)
        print(form)
        for analysis in analyses:
            print(f"  {format_analysis(analysis)}")
