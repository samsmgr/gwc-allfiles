var guy = document.getElementById("guy");
var guyLeft = 590;
var y = 250;
console.log();

var food1 = document.getElementById("food1");

function anim(e) {
if (e.keyCode == 39) {
  if(guyLeft !== 1180) {
    guyLeft += 5; guy.style.left = guyLeft + "px";
  }
}
else if (e.keyCode == 37) {
  if(guyLeft !== 10) {
    guyLeft -= 5; guy.style.left = guyLeft + "px";
  }
}
else if (e.keyCode == 40) {
  if(y !== 500) {
    y += 5; guy.style.top = y + "px";
  }
}
else if (e.keyCode == 38) {
  if(y !== 10) {
    y -= 5; guy.style.top = y + "px";
  }
}

}

document.onkeydown = anim;
