"""
metric.py
---------

Core implementation of the Prescriptive Discourse Confidence Index (PDCI).
"""

import re
from typing import Dict, Tuple

# Config
LAMBDA = 0.5
ALPHA, BETA, GAMMA = 0.4, 0.2, 0.4  # PDS component weights
CATS = ["hedges", "modals", "disfluencies", "conditionals"]

# Regex patterns
LEX = {
    "hedges_uncertain": r"\b(think|believe|suppose|assume|suggest|seem|appear|tend|guess|reckon|figure|imagine|suspect)\b",
    "modals":           r"\b(may|might|could|should|would|can|must)\b",
    "disfluencies":     r"\b(um+|uh+|er+|ah+|hmm+)\b|\b(you\s+know|like)\b|\b(i\s+mean)\b",
    "conditionals":     r"\bif\b|\bunless\b|\bassuming\b|\bwhether\b",
    "cii_uncertain":    r"\b(i\s+think|i\s+believe|i\s+suppose|i\s+guess)\b",
    "cii_certain_high": r"\b(definitely|certainly|clearly|absolutely|undoubtedly|without\s+doubt)\b",
}

R = {k: re.compile(v, flags=re.IGNORECASE) for k, v in LEX.items()}

# ---------- Core helpers ----------
def count_matches(pattern: re.Pattern, text: str) -> int:
    return len(pattern.findall(text)) if text else 0

def feature_counts(text: str) -> Dict[str, int]:
    return {
        "hedges":       count_matches(R["hedges_uncertain"], text),
        "modals":       count_matches(R["modals"], text),
        "disfluencies": count_matches(R["disfluencies"], text),
        "conditionals": count_matches(R["conditionals"], text),
        "uncertain":    count_matches(R["cii_uncertain"], text),
        "certain_high": count_matches(R["cii_certain_high"], text),
    }

def certainty_inflation_index(src: Dict[str, int], summ: Dict[str, int], w_add: float = 0.5) -> float:
    src_unc = max(src["uncertain"], 0)
    denom = max(src_unc, 1)
    C_add = max(0, summ["certain_high"] - src["certain_high"]) / denom
    C_sup = max(0, src["uncertain"] - summ["uncertain"]) / denom
    return max(0.0, min(1.0, w_add * C_add + (1 - w_add) * C_sup))

def loss_rate(src: Dict[str, int], summ: Dict[str, int]) -> float:
    src_total = sum(src[c] for c in CATS)
    if src_total == 0:
        return 0.0
    preserved = sum(min(src[c], summ[c]) for c in CATS)
    return max(0, src_total - preserved) / src_total

def hallucination_rate(src: Dict[str, int], summ: Dict[str, int]) -> float:
    summ_total = sum(summ[c] for c in CATS)
    if summ_total == 0:
        return 0.0
    hallucinated = sum(max(0, summ[c] - src[c]) for c in CATS)
    return hallucinated / summ_total

def pds(src: Dict[str, int], summ: Dict[str, int]) -> float:
    L = loss_rate(src, summ)
    H = hallucination_rate(src, summ)
    C = certainty_inflation_index(src, summ)
    return max(0.0, min(1.0, ALPHA * L + BETA * H + GAMMA * C))

def pdci(src: Dict[str, int], summ: Dict[str, int], lambda_: float = LAMBDA) -> Tuple[float, float, float]:
    C = certainty_inflation_index(src, summ)
    P = pds(src, summ)
    combined = lambda_ * C + (1 - lambda_) * P
    return round(combined, 4), round(C, 4), round(P, 4)

def analyze_pair(source_text: str, summary_text: str) -> Dict[str, float]:
    src = feature_counts(source_text or "")
    summ = feature_counts(summary_text or "")
    combined, C, P = pdci(src, summ, LAMBDA)
    return {
        "loss_rate": round(loss_rate(src, summ), 4),
        "hallucination_rate": round(hallucination_rate(src, summ), 4),
        "CII": C,
        "PDS": P,
        "PDCI": combined,
    }

