package com.phishguard.backend.service;

import com.phishguard.backend.model.MlResponse;
import com.phishguard.backend.model.UrlRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class PhishService {

    @Autowired
    private RestTemplate restTemplate;

    public MlResponse checkUrl(UrlRequest request) {

        String flaskUrl = "http://localhost:5000/predict";

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<UrlRequest> entity = new HttpEntity<>(request, headers);

        ResponseEntity<MlResponse> response =
                restTemplate.postForEntity(flaskUrl, entity, MlResponse.class);

        return response.getBody();
    }
}
