// server.js
import serve from "serve";

const port = process.env.PORT || 8080;  // Railway injects PORT automatically
const server = serve("dist", { port });

console.log(`Server running on port ${port}`);
