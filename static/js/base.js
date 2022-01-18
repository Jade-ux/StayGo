var myIndex = 0;
carousel();
var myIndex2 = 0;
carousel2();

function carousel() {
  var i;
  var x = document.getElementsByClassName("staySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";  
  setTimeout(carousel, 6000); //6 seconds    
}

function carousel2() {
  var i;
  var x = document.getElementsByClassName("goSlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  myIndex2++;
  if (myIndex2 > x.length) {myIndex2 = 1}    
  x[myIndex2-1].style.display = "block";  
  setTimeout(carousel, 5000); //5 seconds    
}