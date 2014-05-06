window.onload = function() {
	document.addEventListener("keydown", function(event) {
		var input_map = {
			37: "LEFT", //these four are arrow keys
			38: "UP",
			39: "RIGHT",
			40: "DOWN",

			65: "LEFT", //these four are WASD
			87: "UP",
			68: "RIGHT",
			83: "DOWN",
		};
		var input_code = input_map[event.keyCode];
		if(typeof input_code == "string"){
			var request = new XMLHttpRequest();
			request.open("POST", window.location); //async?
			request.send("{input: "+input_code+"}");
			log("{input: "+input_code+"}");
		}
	}, true);
	function log(text) {
		document.getElementById("log").innerHTML += text + "<br />";
	}
};