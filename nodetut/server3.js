var http = require('http');

const requestListner = function (request, response){
    const url = request.url;
    if (url === "/"){
        response.setHeader("Content-Type", "text/html");
        response.write("<html>");
        response.write("<head><title>My First Page</title></head>");
        response.write("<body><h1>My First Page</h1></body>");
        response.write("</html>");
        return response.end();
    }
    response.setHeader("Content-Type", "text/html");
    response.write("<html>");
    response.write("<head><title>My Second Page</title></head>");
    response.write("<body><h1>My Second Page</h1></body>");
    response.write("</html>");
    response.end();
}

const server = http.createServer(requestListner);
server.listen(8080);