import re
import math
from collections import Counter
from urllib.parse import urlparse


SUSPICIOUS_KEYWORDS = [
    "login", "signin", "sign-in", "verify", "verification",
    "update", "secure", "security", "account", "bank",
    "paypal", "amazon", "wallet", "free", "gift", "bonus",
    "confirm", "confirmation", "password", "credential",
    "crypto", "bitcoin", "support", "unlock", "validate",
    "authenticate", "authentication", "recover", "suspend",
    "limited", "alert"
]

SHORTENERS = [
    "bit.ly",
    "tinyurl.com",
    "goo.gl",
    "t.co",
    "ow.ly",
    "is.gd",
    "buff.ly",
    "rebrand.ly"
]

SUSPICIOUS_TLDS = [
    "xyz", "top", "gq", "tk", "ml",
    "cf", "ga", "work", "click", "zip",
    "fit", "support", "buzz"
]

BRANDS = [
    "paypal",
    "amazon",
    "microsoft",
    "apple",
    "google",
    "facebook",
    "instagram",
    "netflix",
    "linkedin",
    "twitter",
    "bank",
    "wallet",
    "coinbase"
]


def entropy(text):
    """Calculate Shannon entropy of a string."""
    if not text:
        return 0.0

    counts = Counter(text)
    length = len(text)

    return -sum(
        (count / length) * math.log2(count / length)
        for count in counts.values()
    )


def is_ip_address(domain):
    """Check whether hostname is an IPv4 address."""
    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    return 1 if re.match(ip_pattern, domain) else 0


def extract_features(url):

    parsed = urlparse(url)

    domain = parsed.hostname.lower() if parsed.hostname else ""
    path = parsed.path or ""
    query = parsed.query or ""

    url_lower = url.lower()
    domain_lower = domain.lower()
    path_lower = path.lower()

    features = {}

    # ============================================================
    # 1. BASIC URL FEATURES
    # ============================================================

    features["url_length"] = len(url)
    features["domain_length"] = len(domain)
    features["path_length"] = len(path)
    features["query_length"] = len(query)

    # ============================================================
    # 2. CHARACTER COUNTS
    # ============================================================

    features["dot_count"] = url.count(".")
    features["hyphen_count"] = url.count("-")
    features["underscore_count"] = url.count("_")
    features["slash_count"] = url.count("/")
    features["question_count"] = url.count("?")
    features["equal_count"] = url.count("=")
    features["ampersand_count"] = url.count("&")
    features["at_count"] = url.count("@")
    features["percent_count"] = url.count("%")

    digits = sum(c.isdigit() for c in url)
    letters = sum(c.isalpha() for c in url)

    features["digit_count"] = digits
    features["letter_count"] = letters

    total = len(url)

    features["digit_ratio"] = digits / total if total else 0
    features["letter_ratio"] = letters / total if total else 0

    # ============================================================
    # 3. PROTOCOL
    # ============================================================

    features["https"] = 1 if parsed.scheme.lower() == "https" else 0

    # ============================================================
    # 4. IP ADDRESS
    # ============================================================

    features["has_ip"] = is_ip_address(domain)

    # ============================================================
    # 5. SUBDOMAIN
    # ============================================================

    parts = domain.split(".") if domain else []

    features["subdomain_count"] = max(len(parts) - 2, 0)

    # ============================================================
    # 6. PORT
    # ============================================================

    features["has_port"] = 1 if parsed.port else 0

    # ============================================================
    # 7. SUSPICIOUS KEYWORDS
    # ============================================================

    keyword_count = sum(
        1 for word in SUSPICIOUS_KEYWORDS
        if word in url_lower
    )

    features["keyword_count"] = keyword_count

    # Keywords specifically inside domain
    domain_keyword_count = sum(
        1 for word in SUSPICIOUS_KEYWORDS
        if word in domain_lower
    )

    features["domain_keyword_count"] = domain_keyword_count

    # Keywords specifically inside path
    path_keyword_count = sum(
        1 for word in SUSPICIOUS_KEYWORDS
        if word in path_lower
    )

    features["path_keyword_count"] = path_keyword_count

    # ============================================================
    # 8. BRAND IMPERSONATION
    # ============================================================

    brand_count = sum(
        1 for brand in BRANDS
        if brand in domain_lower
    )

    features["brand_count"] = brand_count

    # ============================================================
    # 9. URL SHORTENER
    # ============================================================

    features["is_shortened"] = int(
        any(shortener in domain_lower for shortener in SHORTENERS)
    )

    # ============================================================
    # 10. SUSPICIOUS TLD
    # ============================================================

    tld = parts[-1] if len(parts) > 1 else ""

    features["suspicious_tld"] = int(
        tld in SUSPICIOUS_TLDS
    )

    # ============================================================
    # 11. DOMAIN STRUCTURE
    # ============================================================

    features["domain_hyphen_count"] = domain.count("-")

    features["domain_digit_count"] = sum(
        c.isdigit() for c in domain
    )

    features["domain_digit_ratio"] = (
        features["domain_digit_count"] / len(domain)
        if domain else 0
    )

    features["domain_hyphen_ratio"] = (
        domain.count("-") / len(domain)
        if domain else 0
    )

    # ============================================================
    # 12. PATH STRUCTURE
    # ============================================================

    features["path_digit_count"] = sum(
        c.isdigit() for c in path
    )

    features["path_digit_ratio"] = (
        features["path_digit_count"] / len(path)
        if path else 0
    )

    features["path_special_char_count"] = sum(
        not c.isalnum() for c in path
    )

    # ============================================================
    # 13. SPECIAL CHARACTERS
    # ============================================================

    special_chars = sum(
        not c.isalnum() for c in url
    )

    features["special_char_count"] = special_chars

    features["special_char_ratio"] = (
        special_chars / total if total else 0
    )

    # ============================================================
    # 14. ENTROPY
    # ============================================================

    features["domain_entropy"] = entropy(domain)

    features["path_entropy"] = entropy(path)

    # ============================================================
    # 15. OBFUSCATION
    # ============================================================

    features["has_at_symbol"] = int("@" in url)

    features["has_hex_encoding"] = int(
        bool(re.search(r"%[0-9a-fA-F]{2}", url))
    )

    features["has_double_slash"] = int(
        "//" in path
    )

    # ============================================================
    # 16. LONG URL
    # ============================================================

    features["long_url"] = int(len(url) > 75)

    # ============================================================
    # 17. SUSPICIOUS DOMAIN PATTERN
    # ============================================================

    # Multiple hyphenated words in domain
    features["hyphenated_domain"] = int(
        domain.count("-") >= 2
    )

    # Domain containing security-related terms
    security_words = [
        "login",
        "secure",
        "verify",
        "account",
        "update",
        "confirm"
    ]

    features["security_domain_pattern"] = int(
        sum(word in domain_lower for word in security_words) >= 1
    )

    return features