//http
const http = require("http");

const server = http.createServer((req,res) => {
    console.log("Hello World");
});

server.listen(3000);
