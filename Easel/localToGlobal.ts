function removeElementsByTagName(tagName) {
  var elements = document.getElementsByTagName(tagName);
  for (var i = elements.length - 1; i >= 0; i--) {
    var e = elements[i];
    e.parentNode.removeChild(e);
  }
}

class Workbench2D
{
  public canvas;
  private sizer: EventListener;
  constructor(canvas: HTMLCanvasElement)
  {
    this.canvas = canvas;
    function onWindowResize(event)
    {
      var width  = window.innerWidth;
      var height = window.innerHeight;
      canvas.width  = width;
      canvas.height = height;
    }
    this.sizer = onWindowResize;
  }
  setUp()
  {
    document.body.insertBefore(this.canvas, document.body.firstChild);
    window.addEventListener('resize', this.sizer, false);
    this.sizer(null);

  }
  tearDown()
  {
    window.removeEventListener('resize', this.sizer, false);
    removeElementsByTagName("canvas");
  }
}

var element: any = canvas.node();
var elemCanvas = element;
