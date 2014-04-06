# turtle-eight.py
var t = brd.create('turtle',[0, 0], {strokeOpacity:0.5});
t.setPenSize(3);
t.right(90);
var alpha = 0;
 
var run = function() {
   t.forward(2);
   if (Math.floor(alpha / 360) % 2 === 0) {
      t.left(1);        // turn left by 1 degree
   } else {
      t.right(1);       // turn right by 1 degree
   }
 
   alpha += 1;
 
   if (alpha < 1440) {  // stop after two rounds
       setTimeout(run, 20); 
   }
}
 
run();