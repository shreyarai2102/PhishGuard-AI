package com.phishguard.backend.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PhishController {

    @GetMapping("/api/test")
    public String test() {
        return "PhishGuard AI Backend Running!";
    }
}