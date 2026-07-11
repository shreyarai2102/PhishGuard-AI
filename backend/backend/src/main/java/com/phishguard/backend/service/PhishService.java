package com.phishguard.backend.service;

import com.phishguard.backend.features.UrlFeatureExtractor;
import com.phishguard.backend.model.ScanResponse;
import org.springframework.stereotype.Service;

@Service
public class PhishService {

    private final UrlFeatureExtractor extractor = new UrlFeatureExtractor();

    public ScanResponse checkUrl(String url) {

        int score = 0;

        if(!extractor.hasHttps(url))
            score++;

        if(extractor.getUrlLength(url) > 50)
            score++;

        if(extractor.countDots(url) > 3)
            score++;

        if(extractor.hasSuspiciousKeyword(url))
            score++;

        String prediction;

        if(score >= 2) {
            prediction = "PHISHING";
        } else {
            prediction = "SAFE";
        }

        return new ScanResponse(url, prediction, score);
    }
}
