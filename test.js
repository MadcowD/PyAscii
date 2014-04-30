var w;
var h;

var player = {body: "@", color: ["FF0000", "000000"], pos: [0,0]};
var ground = {body: "#", color: "0000CC"};

function main() {
  var world = [];
  var colors = [];

  function add_entity(entity, pos) {
    var x = pos[0]; var y = pos[1];
    world[x][y] = entity.body;
    colors[x][y] = entity.color;
  }

  for(var i=0; i<h; i++) {
    world[i] = [];
    colors[i] = [];

    for(var j=0; j<w; j++) {
      add_entity(ground, [i, j]);
    }
  }

  add_entity(player, player.pos);

  var world_str = "";
  for(var i=0; i<h; i++) {
    for(var j=0; j<w; j++) {
      world_str += "<span style='color: #"+colors[i][j][0]+
      "; background-color: #"+colors[i][j][1]+";'>"+world[i][j]+"</span>";
    }
    world_str += "<br />";
  }
  document.getElementById("game").innerHTML = world_str;
}

document.addEventListener("keydown", function(event) {
    if (event.keyCode == 37) { //left
      if(player.pos[1] > 0) {
        player.pos[1]--;
      }
    }
    else if (event.keyCode == 38) { //up
      if(player.pos[0] > 0) {
        player.pos[0]--;
      }
    }
    else if (event.keyCode == 39) { //right
      if(player.pos[1] < w-1) {
        player.pos[1]++;
      }
    }
    else if (event.keyCode == 40) { //down
      if(player.pos[0] < h-1) {
        player.pos[0]++;
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