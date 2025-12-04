# src/mcpscan/core/lang_utils.py
from pathlib import Path

JS_EXTS = {".js", ".ts", ".jsx", ".tsx", ".mjs", ".cjs"}
PY_EXTS = {".py"}
JAVA_EXTS = {".java"}


def detect_primary_language(root: Path) -> str:
    js_cnt = py_cnt = java_cnt = 0

    for f in root.rglob("*"):
        if not f.is_file():
            continue

        suffix = f.suffix

        if suffix in JS_EXTS:
            js_cnt += 1
        elif suffix in PY_EXTS:
            py_cnt += 1
        elif suffix in JAVA_EXTS:
            java_cnt += 1

    # 比较数量
    if java_cnt >= js_cnt and java_cnt >= py_cnt:
        return "java"
    elif js_cnt >= py_cnt:
        return "js"
    else:
        return "py"
