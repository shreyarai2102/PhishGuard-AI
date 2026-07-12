import axios from "axios";

const api = axios.create({
    baseURL: "https://bug-free-lamp-pjp6994xpv49h9rjr-8080.app.github.dev/api",
});

export default api;