var url = "";
var target = "";
var features = "width=800, height=600";

var unused: Window = window;
var popUp = window.open(url, target, features, false);

var document = popUp.document;

var canvas = document.createElement("canvas");

canvas.setAttribute("id", "graph");
canvas.setAttribute("width", "400");
canvas.setAttribute("height", "400");

document.body.appendChild(canvas);

var context = canvas.getContext("2d");

context.beginPath();
context.moveTo(150, 100);
context.lineTo(200, 225);
context.closePath();
context.stroke();

//popUp.close();