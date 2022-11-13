//http
const http = require("http");
const express = require("express");
const bodyParser = require("body-parser");

const app = express(); //request handler
const adminRoutes = require("./routes/admin");
const courseRoutes = require("./routes/course")
app.use(bodyParser.urlencoded({ extended: false}));

app.use(adminRoutes);
app.use(courseRoutes);
app.use((req,res,next)=>{
    res.status(404).send('<h1> Page not found </h1>');
});
app.listen(4000)