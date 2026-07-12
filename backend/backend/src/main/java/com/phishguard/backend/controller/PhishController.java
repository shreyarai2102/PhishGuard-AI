package com.phishguard.backend.controller;

import com.phishguard.backend.model.MlResponse;
import com.phishguard.backend.model.UrlRequest;
import com.phishguard.backend.service.PhishService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class PhishController {

    private final PhishService phishService;

    public PhishController(PhishService phishService) {
        this.phishService = phishService;
    }

    @GetMapping("/test")
    public String test() {
        return "Backend Running";
    }

    @PostMapping("/check")
    public MlResponse check(@RequestBody UrlRequest request) {
        return phishService.checkUrl(request);
    }
}
