/**
 * Demonstrates creating a 2D canvas and context.
 */

// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

class Canvas {
  private win: Window;
  private context;
  constructor(width: number, height: number) {
    this.win = window.open("", "", "width=" + width + ", height=" + height, false);
    
    var popDoc = this.win.document;
    
    var canvas = popDoc.createElement("canvas");
    
    canvas.setAttribute("id", "graph");
    canvas.setAttribute("width",  width.toString());
    canvas.setAttribute("height", height.toString());
    
    popDoc.body.appendChild(canvas);
    // Remove the margin that pushes the canvas.
    popDoc.body.style.margin = "0";
    
    this.context = canvas.getContext("2d");

    this.context.fillStyle = "#555555";
    this.context.fillRect(0, 0, width, height);
  }

  public close() {
    this.win.close();
  }
}

var canvas = new Canvas(800, 600)
