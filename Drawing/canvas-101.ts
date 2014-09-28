var popUp: Window = open("", "", "width=800, height=600");

var document = popUp.document;

var canvas = document.createElement("canvas");

canvas.setAttribute("id", "graph");
canvas.setAttribute("width", "320");
canvas.setAttribute("height", "160");

document.body.appendChild(canvas);


//popUp.close();