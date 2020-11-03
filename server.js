const bodyParser = require('body-parser');
const express = require("express");
const app = express();
const { spawn } = require('child_process');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: false
}));

app.use(express.static('public'));
app.get("/", function (req, res) {
    res.sendFile(__dirname + "/index.html");
});
app.get("/visualization", function (req, res) {
    res.render(__dirname + "/public/src/index.ejs",{distanceVar:" "});
});
app.get("/contact", function (req, res) {
    res.sendFile(__dirname + "/public/src/contact.html");
});
app.listen(process.env.PORT, process.env.IP, function () {
    console.log("Server has started");
});

app.post("/visualization", function (req, res) {
    var pos1 = req.body.input_origin;
    var pos2 = req.body.input_dest;
    // res.send(pos1);
    //console.log(pos1, pos2);
    // spawn new child process to call the python script
    const pythonProcess = spawn('python', [__dirname +'/public/src/time.py', pos1, pos2]);
    pythonProcess.stdout.on('data', function (data) {
        //console.log('Pipe data from python script ...');
        dataToSend = data.toString();
        //console.log(dataToSend);
        res.render(__dirname + "/public/src/index.ejs",{distanceVar:dataToSend});
    });
    
})
