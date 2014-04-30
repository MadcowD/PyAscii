var w;
var h;

var player = [0,0];

function main() {
  var world = [];
  var colors = [];
  for(var i=0; i<=h; i++) {
    var row = [];
    for(var j=0; j<=w; j++) {
      row.push("a");
    }
    world.push(row);
  }

  world[player[1]][player[0]] = "@";

  //you shouldn't need to change below here, instead insert things while it's still an array, above
  var world_str = world.map(function(row){
    return row.map(function(x){
      return "<span style='color: #"+x+";'>"+x+"</span>";
    }).join("");
  }).join("<br />");
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

function update_world_dimensions() {
    w = document.getElementById("world-width").value;
    h = document.getElementById("world-height").value;
}

window.onload = function() {
	update_world_dimensions();
	setInterval(main, 50);
}