/**
 * Demonstrates launching a popup window.
 */

// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

class PopUp {
  private win: Window;
  constructor(width: number, height) {
    this.win = window.open("", "", "width=" + width + ", height=" + height, false);
  }
  public close() {
    this.win.close();
  }
}

var popUp = new PopUp(800, 600)

//popUp.close();
