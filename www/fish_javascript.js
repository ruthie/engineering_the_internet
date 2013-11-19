say_help = function() {
    alert("help");
};

make_fish_picture_larger = function () {
    document.getElementById("breadfish").width = 1.5*document.getElementById("breadfish").width;
};

move_right = function() {
    document.getElementById("fish_button").style = ";"
};

make_fish_opaque = function(opacity, id){
    document.getElementById(id).style.opacity=opacity;
};

interval = null;
start_button_moving = function () {
    interval = window.setInterval(move_button, 10)
}

x_position = 0;

move_button = function() {
    if (x_position >= 100){
	window.clearInterval(interval)
    }   
    x_position = x_position + 1;
    document.getElementById("fish_button").style.left = x_position;
}

change_sushi_text = function () {
    document.getElementById("sushi_text").innerHTML = "<b>bold text</b> not bold text";
}

remove_breadfish = function () {
    document.getElementById("breadfish").remove()
}

add_breadfish_gif = function () {
    num_breadfish = 0;
    while(false) {
	breadfish_gif = document.createElement("img");
	breadfish_gif.src = "http://stream1.gifsoup.com/view4/1396665/breadfish-o.gif";
	document.getElementById("text").appendChild(breadfish_gif);
	num_breadfish = num_breadfish + 1;
    }
}