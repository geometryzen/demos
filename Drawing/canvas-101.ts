var popUp: Window = open("", "", "width=800, height=600");

var document = popUp.document;

var canvas = document.createElement("canvas");

canvas.setAttribute("id", "graph");
canvas.setAttribute("width", "400");
canvas.setAttribute("height", "400");

document.body.appendChild(canvas);

var context = canvas.getContext("2d");

context.fillStyle = "#0066CC";
context.fillRect(0, 0, 400, 400);


//popUp.close();