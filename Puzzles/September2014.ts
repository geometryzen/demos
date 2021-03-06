/*
2009 unit cubes are glued together to form a cuboid. 
A pack, containing 2009 stickers, is opened, and there are enough stickers to place 1 sticker on each exposed face 
of each unit cube.

How many stickers from the pack are left?
*/
// The prime factors of 2009 are 7 (twice) and 41.
// There are only three factors so these must be the side lengths.
var x = 7
var height = 41
var volume = x * x * height
var area = x * x * 2 + x * height * 4
console.log("volume: " + volume)
console.log("area: " + area)
// The area is 1246 units squared so the number of stickers remaining is 2009 - 1246 = 763
console.log("#stickers remaining: " + (volume - area))
