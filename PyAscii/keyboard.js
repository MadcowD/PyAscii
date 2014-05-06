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
		input_code = input_map[event.keyCode];
		var request = new XMLHttpRequest();
		request.open("GET", window.location+"?input="+input_code); //async?
		request.send();
	}, true);	
};