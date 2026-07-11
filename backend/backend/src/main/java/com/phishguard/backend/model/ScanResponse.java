package com.phishguard.backend.model;

public class ScanResponse {

    private String url;
    private String prediction;
    private int riskScore;

    public ScanResponse(String url, String prediction, int riskScore) {
        this.url = url;
        this.prediction = prediction;
        this.riskScore = riskScore;
    }

    public String getUrl() {
        return url;
    }

    public String getPrediction() {
        return prediction;
    }

    public int getRiskScore() {
        return riskScore;
    }
}