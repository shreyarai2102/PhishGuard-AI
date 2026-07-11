package com.phishguard.backend.controller;

import com.phishguard.backend.model.UrlRequest;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class PhishController {

    @GetMapping("/test")
    public String test() {
        return "PhishGuard AI Backend Running";
    }

    @PostMapping("/check")
    public String checkUrl(@RequestBody UrlRequest request) {

        String url = request.getUrl();

        return "Checking URL: " + url;
    }
}