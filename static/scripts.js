window.onload = function(){
var currentUrl = window.location.href;
var curStr = currentUrl.toString();
var split = curStr.split('/');
var page = split[3];

  if (page == ''){
    var remove = document.getElementById('home').classList.remove('w3-text-pink');
    var add = document.getElementById('home').classList.add('w3-text-black');
  }
  else{
    var remove = document.getElementById(page).classList.remove('w3-text-pink');
    var add = document.getElementById(page).classList.add('w3-text-black');
  }

};

function countText() {

var text = document.getElementById('blogpost').value;
var textlength = text.length;
var remaining = 10000-textlength;
document.getElementById('remainingtext').innerHTML = remaining;

}
