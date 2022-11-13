const express = require("express");
const router = express.Router();

router.get("/abc", (req, res, next) => {
    res.send(
      '<form action="/course" method="POST" name="msg"><input type="text" name="msg"><button type="submit">Submit</button></form>'
    );
});

router.post("/course", (req, res, next) => {
    console.log(req.body);
    res.redirect("/")
});

module.exports=router;
