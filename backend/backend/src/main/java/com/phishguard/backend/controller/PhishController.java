package com.phishguard.backend.controller;

import com.phishguard.backend.model.UrlRequest;
import com.phishguard.backend.service.PhishService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class PhishController {

    private final PhishService phishService;

    public PhishController(PhishService phishService) {
        this.phishService = phishService;
    }

    @GetMapping("/test")
    public String test() {
        return "PhishGuard AI Backend Running!";
    }

     @PostMapping("/check")
      public Object checkUrl(@RequestBody UrlRequest request) {
    return phishService.checkUrl(request.getUrl());
    }
}
