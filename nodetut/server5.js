var http = require('http');
const fs = require("fs");

const requestListner = function (request, response){
    const url = request.url;
    const method = request.method;
    if (url === "/"){
        response.setHeader("Content-Type", "text/html");
        response.write("<html>");
        response.write("<title>My First Page</title>");
        response.write('<body><form action="/file" method="POST" name="msg"><input type="text" name="msg"><button type="submit">Submit</button></body>');
        response.write("</html>");
        return response.end();
    }
    if(url === "/file" && method === "POST"){
        const body = [];
        request.on("data", (chunk) => {
            body.push(chunk);
        });
        request.on("end", () => {
            const parsedBody = Buffer.concat(body).toString();
            const message = parsedBody.split("=")[1];
            fs.writeFileSync("NewFile.txt", message);
        });
        response.statusCode = 302;
        response.setHeader("Location", "/");
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
server.listen(8081);