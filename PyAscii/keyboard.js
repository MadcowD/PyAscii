window.onload = function() {
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
	var input_code;
	document.addEventListener("keydown", function(event) {
		input_code = input_map[event.keyCode];
	}, true);
	var request = new XMLHttpRequest();
	request.open("GET", window.location+"?input="+input_code); //async?
	request.send();
};