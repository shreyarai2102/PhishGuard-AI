package com.phishguard.backend.features;

import org.springframework.stereotype.Component;

public class UrlFeatureExtractor {

    public int getUrlLength(String url) {
        return url.length();
    }

    public boolean hasHttps(String url) {
        return url.startsWith("https");
    }

    public int countDots(String url) {
        return url.length() - url.replace(".", "").length();
    }

    public boolean hasSuspiciousKeyword(String url) {

        String lowerUrl = url.toLowerCase();

        return lowerUrl.contains("login") ||
               lowerUrl.contains("verify") ||
               lowerUrl.contains("update") ||
               lowerUrl.contains("secure");
    }
}