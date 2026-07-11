package com.phishguard.backend.service;

import org.springframework.stereotype.service;

@Service
public class PhishService {

    public String analyzeUrl(String url){

        if(url.contains("login") || url.contains("verify")){
            return "Suspicious URL detected";
        }

        return "URL looks safe";
    }
}