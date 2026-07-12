import re
from urllib.parse import urlparse


SUSPICIOUS_KEYWORDS = [
    "login", "signin", "verify", "update", "secure",
    "account", "bank", "paypal", "amazon", "wallet",
    "free", "gift", "bonus", "confirm", "password",
    "crypto", "bitcoin", "support"
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
    "cf", "ga", "work", "click", "zip"
]


def extract_features(url):
    parsed = urlparse(url)

    domain = parsed.netloc.lower()
    path = parsed.path
    query = parsed.query

    features = {}

    # Basic Length Features
    features["url_length"] = len(url)
    features["domain_length"] = len(domain)
    features["path_length"] = len(path)
    features["query_length"] = len(query)

    # Character Counts
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

    # Ratios
    total = len(url)

    features["digit_ratio"] = digits / total if total else 0
    features["letter_ratio"] = letters / total if total else 0

    # HTTPS
    features["https"] = 1 if parsed.scheme == "https" else 0

    # IP Address
    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    features["has_ip"] = 1 if re.match(ip_pattern, domain) else 0

    # Subdomains
    parts = domain.split(".")
    features["subdomain_count"] = max(len(parts) - 2, 0)

    # Port
    features["has_port"] = 1 if ":" in domain else 0

    # Suspicious Keywords
    url_lower = url.lower()

    keyword_count = 0

    for word in SUSPICIOUS_KEYWORDS:
        if word in url_lower:
            keyword_count += 1

    features["keyword_count"] = keyword_count

    # URL Shortener
    features["is_shortened"] = 1 if any(s in domain for s in SHORTENERS) else 0

    # Suspicious TLD
    tld = parts[-1] if len(parts) > 1 else ""

    features["suspicious_tld"] = 1 if tld in SUSPICIOUS_TLDS else 0

    # Double Slash
    features["double_slash"] = 1 if "//" in parsed.path else 0

    # Long URL
    features["long_url"] = 1 if len(url) > 75 else 0

    return features
