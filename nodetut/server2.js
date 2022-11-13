var http = require('http');

const requestListner = function (request, response){
    response.writeHead(200);
    response.end("Hello, World");
}

const server = http.createServer(requestListner);
server.listen(8080);