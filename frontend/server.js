// server.js
const serve = require('serve');
const port = process.env.PORT || 3000; // Railway sets process.env.PORT
serve('dist', { port });
console.log(`Server running on port ${port}`);
