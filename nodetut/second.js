//http
const http = require("http");

const server = http.createServer((req,res) => {
    //req: request process
    //res: for writing response
    res.writeHead(200,{"content-type": "text/html"});
    res.write("<h1>Wow this is response from first server</h1>");
    res.end("Ok Bye Bye");
});

server.listen(8082);