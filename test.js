var world_width;
var world_height;

var ground = {body: "^", color: ["3C3", "630"]};

var actors = [];
var player = {body: "@", color: ["F00", "000"], pos: [0,0]};
  actors.push(player);
var spawner = {body: "#", color: ["C09", "9CF"], pos: [0,0]};
  actors.push(spawner);

function main() {
  var world = [];
  var colors = [];

  function add_entity(entity, pos) {
    if(typeof pos === "undefined")
      pos = entity.pos;
    var x = pos[0]; var y = pos[1];
    world[x][y] = entity.body;
    colors[x][y] = entity.color;
  }

  for(var i=0; i<world_height; i++) {
    world[i] = [];
    colors[i] = [];

    for(var j=0; j<world_width; j++) {
      add_entity(ground, [i, j]);
    }
  }

  add_entity(player);

  var world_str = "";
  for(var i=0; i<world_height; i++) {
    for(var j=0; j<world_width; j++) {
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
      if(player.pos[1] < world_width-1) {
        player.pos[1]++;
      }
    }
    else if (event.keyCode == 40) { //down
      if(player.pos[0] < world_height-1) {
        player.pos[0]++;
      }
    }
}, true);

window.onload = function() {
	world_width = document.getElementById("world-width").value;
  world_height = document.getElementById("world-height").value;
	
  setInterval(main, 50);
}