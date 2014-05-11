
window.onload = function () {
	setInterval(function() {
		getWorld();
	},1000);

	// getWorld();
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
		if (typeof input_code == "string") {
		    $.post("/world", { input: input_code }, function(data){
			    
		    });
		    getWorld();
		}
	}, true);
};


function getWorld(){
	$.get("/world", function(data){
		$('#game').html(data);
	});
}