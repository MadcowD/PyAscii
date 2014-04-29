var w = 30;
var h = 10;

var player = [0,0];

function main() {
  var world = [];
  for(var i=0; i<=h; i++) {
    var row = [];
    for(var j=0; j<=w; j++) {
      row.push("_");
    }
    world.push(row);
  }

  world[player[1]][player[0]] = "@";

  var world_str = world.map(function(x){
    return x.join("");
  }).join("\n");
  document.getElementById("game").innerHTML = world_str;
}

document.addEventListener("keydown", function(event) {
    if (event.keyCode == 37) { //left
      if(player[0] > 0) {
        player[0]--;
      }
    }
    else if (event.keyCode == 38) { //up
      if(player[1] > 0) {
        player[1]--;
      }
    }
    else if (event.keyCode == 39) { //right
      if(player[0] < w) {
        player[0]++;
      }
    }
    else if (event.keyCode == 40) { //down
      if(player[1] < h) {
        player[1]++;
      }
    }
}, true);

window.onload = function() {
	setInterval(main, 50);
}