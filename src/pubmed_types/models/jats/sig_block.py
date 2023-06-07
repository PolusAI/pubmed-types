from dataclasses import field
from pydantic.dataclasses import dataclass
from typing import List, Optional
from .access_date import (
    Abbrev,
    Aff,
    AffAlternatives,
    Alternatives,
    Bold,
    ChemStruct,
    Contrib,
    Email,
    Etal,
    ExtLink,
    FixedCase,
    Fn,
    Graphic,
    IndexTerm,
    InlineFormula,
    InlineGraphic,
    InlineMedia,
    InlineSupplementaryMaterial,
    Italic,
    Media,
    Monospace,
    NamedContent,
    Overline,
    PrivateChar,
    RelatedArticle,
    RelatedObject,
    Role,
    Roman,
    Ruby,
    SansSerif,
    Sc,
    Strike,
    StyledContent,
    Sub,
    Sup,
    Target,
    Underline,
    Uri,
    X,
    Xref,
)
from .break_mod import Break
from .hr import Hr
from .index_term_range_end import IndexTermRangeEnd
from .milestone_end import MilestoneEnd
from .milestone_start import MilestoneStart
from .org.w3.pkg_1998.math.math_ml.math import Math
from .overline_end import OverlineEnd
from .overline_start import OverlineStart
from .sig import Sig
from .tex_math import TexMath
from .underline_end import UnderlineEnd
from .underline_start import UnderlineStart


@dataclass
class SigBlock:
    """
    <div> <h3>Signature Block</h3> </div>
    """
    class Meta:
        name = "sig-block"

    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "inline-supplementary-material",
                    "type": InlineSupplementaryMaterial,
                },
                {
                    "name": "related-article",
                    "type": RelatedArticle,
                },
                {
                    "name": "related-object",
                    "type": RelatedObject,
                },
                {
                    "name": "hr",
                    "type": Hr,
                },
                {
                    "name": "bold",
                    "type": Bold,
                },
                {
                    "name": "fixed-case",
                    "type": FixedCase,
                },
                {
                    "name": "italic",
                    "type": Italic,
                },
                {
                    "name": "monospace",
                    "type": Monospace,
                },
                {
                    "name": "overline",
                    "type": Overline,
                },
                {
                    "name": "overline-start",
                    "type": OverlineStart,
                },
                {
                    "name": "overline-end",
                    "type": OverlineEnd,
                },
                {
                    "name": "roman",
                    "type": Roman,
                },
                {
                    "name": "sans-serif",
                    "type": SansSerif,
                },
                {
                    "name": "sc",
                    "type": Sc,
                },
                {
                    "name": "strike",
                    "type": Strike,
                },
                {
                    "name": "underline",
                    "type": Underline,
                },
                {
                    "name": "underline-start",
                    "type": UnderlineStart,
                },
                {
                    "name": "underline-end",
                    "type": UnderlineEnd,
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "alternatives",
                    "type": Alternatives,
                },
                {
                    "name": "inline-graphic",
                    "type": InlineGraphic,
                },
                {
                    "name": "inline-media",
                    "type": InlineMedia,
                },
                {
                    "name": "private-char",
                    "type": PrivateChar,
                },
                {
                    "name": "chem-struct",
                    "type": ChemStruct,
                },
                {
                    "name": "inline-formula",
                    "type": InlineFormula,
                },
                {
                    "name": "tex-math",
                    "type": TexMath,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                },
                {
                    "name": "index-term",
                    "type": IndexTerm,
                },
                {
                    "name": "index-term-range-end",
                    "type": IndexTermRangeEnd,
                },
                {
                    "name": "milestone-end",
                    "type": MilestoneEnd,
                },
                {
                    "name": "milestone-start",
                    "type": MilestoneStart,
                },
                {
                    "name": "named-content",
                    "type": NamedContent,
                },
                {
                    "name": "styled-content",
                    "type": StyledContent,
                },
                {
                    "name": "fn",
                    "type": Fn,
                },
                {
                    "name": "target",
                    "type": Target,
                },
                {
                    "name": "xref",
                    "type": Xref,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "x",
                    "type": X,
                },
                {
                    "name": "break",
                    "type": Break,
                },
                {
                    "name": "contrib",
                    "type": Contrib,
                },
                {
                    "name": "graphic",
                    "type": Graphic,
                },
                {
                    "name": "media",
                    "type": Media,
                },
                {
                    "name": "aff",
                    "type": Aff,
                },
                {
                    "name": "aff-alternatives",
                    "type": AffAlternatives,
                },
                {
                    "name": "etal",
                    "type": Etal,
                },
                {
                    "name": "role",
                    "type": Role,
                },
                {
                    "name": "sig",
                    "type": Sig,
                },
            ),
        }
    )