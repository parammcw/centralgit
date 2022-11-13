const express = require("express");
const router = express.Router();

router.get("/", (req, res, next) => {
    res.send("<h1>Hello it is me express</h1>");
});

module.exports = router;
