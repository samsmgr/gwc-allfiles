//Javascript for website.html
var spamlist = ["WOW!!!!!!! CLICK HERE TO GET FREE IPHONE TODAY!!! CLICK NOW OR YOUR PRIZE WILL BE GIVEN AWAY!!!!!!!", "Click OK to download FREE SOFTWARE", "Congratulations! You have been randomly selected to receive a free Microsoft Surface Pro.", "Win $5000 a week... FOREVER!!! Guaranteed to WIN, click OK to FIND OUT MORE!!"]

function cookies() {
  alert("By clicking 'OK', you agree to accept this site's cookies.");
}

function spam_ads() {
  for (i = 0; i < 4; i++) {
    alert(spamlist[i])
  }
}

function loop_spam() {
  var i;
  for (i = 0; i < 4; i++) {
    spam_ads();
  window.location.assign("FREE_IPHONE.html")
}
}

function readmore() {
  var moreImg = document.getElementById("morefolio");
  var btnText = document.getElementById("readmorebtn");

  if (btnText.innerHTML === "SEE LESS") {
    btnText.innerHTML = "SEE MORE";
    moreImg.style.display = "none";
  } else if (btnText.innerHTML === "SEE MORE"){
    btnText.innerHTML = "SEE LESS";
    moreImg.style.display = "inline";
  }
}
