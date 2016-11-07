var imgs = document.getElementsByClassName("intro-header");
var L1 = document.getElementById("L1");
var L2 = document.getElementById("L2");
var L3 = document.getElementById("L3");
img = imgs[0];

function changeImg () {
    if (i == 1) {
        clearInterval(intervalId)
        img.style = "background-image: url('/static/blog/img/logo_white.png');";
        L1.style = "color: black;";
        L2.style = "color: black;";
        L3.style = "color: black;";
        i = 2;
        intervalId = setInterval(changeImg, 10000);
    }
    else if (i == 2) {
        clearInterval(intervalId)
        img.style = "background-image: url('/static/blog/img/index.png');";
        L1.style = "color: white;";
        L2.style = "color: white;";
        L3.style = "color: white;";
        i = 1;
        intervalId = setInterval(changeImg, 10000);
    }

}

i = 1;
intervalId = setInterval(changeImg, 10000);