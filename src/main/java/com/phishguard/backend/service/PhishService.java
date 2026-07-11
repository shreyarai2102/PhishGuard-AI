package com.phishguard.backend.service;

import org.springframework.stereotype.Service;

@Service
public class PhishService {

    public String checkUrl(String url) {

        // Temporary logic
        if(url.contains("login") || url.contains("verify")) {
            return "Potential Phishing URL";
        }

        return "URL Looks Safe";
    }
}
