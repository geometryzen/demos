/**
 * Demonstrates launching a popup window.
 */

// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
//var unused: Window = window;

var WINDOW_HEIGHT = 800;
var WINDOW_WIDTH  = 800;
var WINDOW_HALF_HEIGHT = WINDOW_HEIGHT / 2;
var WINDOW_HALF_WIDTH  = WINDOW_WIDTH / 2;

// Global Variables.
var popUp: Window = open("", "", "width=" + WINDOW_WIDTH + ", height=" + WINDOW_HEIGHT, false);

popUp.close()
