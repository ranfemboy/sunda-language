"""
Transpiler SundaPy.

Cara gawena: source ditokenisasi ku modul `tokenize` bawaan Python (sanes regex
biasa), sangkan kecap di jero string atawa komentar teu milu robah, ngan
token NAME (ngaran variabel/kecap kunci) nu dicek kana kamus KEYWORDS.
"""

import io
import tokenize

from .keywords import KEYWORDS


def transpile(source: str) -> str:
    """Robah kode SundaPy (basa Sunda) jadi kode Python nu sah."""
    result = []
    tokens = tokenize.generate_tokens(io.StringIO(source).readline)

    for tok_type, tok_string, *_rest in tokens:
        if tok_type == tokenize.NAME and tok_string in KEYWORDS:
            tok_string = KEYWORDS[tok_string]
        result.append((tok_type, tok_string))

    return tokenize.untokenize(result)


def compile_sunda(source: str, filename: str = "<sunda>"):
    """Transpile terus compile jadi code object Python, siap di-exec."""
    python_code = transpile(source)
    return compile(python_code, filename, "exec")
