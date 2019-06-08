$(document).ready(function() { 
    var winW = null;
    var winH = null;
    var phW = null;
    var phH = null;
    var ms = {
      x: 0,
      y: 0
    }
    var curPhoto = 0;
    var numOfPhotos = $(".photo").length;
    
    function loadBg(photoNum) {
      var url = $(".photo-" + photoNum).css("background-image");
      $(".transparent-bg").append("<div class='trans-bg trans-bg-" + photoNum + "'></div>");
      $(".trans-bg").last().css("background-image", url);
    }
    
    function handleSize() {
      winW = parseInt($(".demo-container").css("width"));
      winH = parseInt($(".demo-container").css("height"));   
      var k = 0.9;
      if (winW / 16 < winH / 9)
        $(".photo-container").css({
          "width": winW * k + "px",
          "height": winW * k * 9 / 16 + "px" });
      else 
        $(".photo-container").css({
          "height": winH * k + "px",
          "width": winH * k * 16 / 9 + "px"
        });
      phW = parseInt($(".photo").css("width"));
      phH = parseInt($(".photo").css("height"));
      $(".photo-container").css("perspective", (phW + phH) * 2);
    }
   
    $(".indicator").html((curPhoto + 1) + "/" + numOfPhotos);
    
    for (i = 0; i < numOfPhotos; i++)
      loadBg(i);
    $(".trans-bg-0").addClass("trans-bg-active");
    handleSize();
    
    $(window).on("resize", handleSize);
    
    $(".demo-container").on("mousedown touchstart", function(event) {
      if (event.type == "touchstart") {
        event.preventDefault();
        var st = {
          x: event.originalEvent.touches[0].pageX,
          y: event.originalEvent.touches[0].pageY
        }
      } else {
         var st = {
        x: event.pageX,
        y: event.pageY
      }
      }
      
      $(".demo-container").addClass("grabbing").find(".photo").removeClass("animation");
     
      $(".demo-container").on("mouseleave", function() {
        $(document).trigger("mouseup");
      });
      $(document).on("mousemove touchmove", function(event) {
        ms.x = (event.pageX || event.originalEvent.touches[0].pageX) - st.x;
        ms.y = (event.pageY || event.originalEvent.touches[0].pageY) - st.y;
        $(".photo-active").css("transform", "rotateX(" + Math.atan(-ms.y / phH) * 57.3 + "deg) rotateY(" + Math.atan(ms.x / phW) * 57.3 + "deg) translate3d(" + ms.x / 2.5 + "px, " + ms.y / 2.5 + "px, 0)");
      });
    });
    $(document).on("mouseup touchend", function(event) {
      $(".demo-container").removeClass("grabbing").find(".photo").addClass("animation");    
      $(document).off("mousemove touchmove");
      if (ms.x < -winW / 5 && curPhoto < numOfPhotos - 1) {
        curPhoto++;
        $(".photo-active").removeAttr("style").removeClass("photo-active").addClass("photo-left");
        $(".photo-" + curPhoto).addClass("photo-active");
        $(".trans-bg").removeClass("trans-bg-active");
        $(".trans-bg-" + curPhoto).addClass("trans-bg-active");
        $(".indicator").html((curPhoto + 1) + "/" + numOfPhotos)
      }
      else if (ms.x > winW / 5 && curPhoto > 0) {
        curPhoto--;
        $(".photo-active").removeAttr("style").removeClass("photo-active");
        $(".photo-" + curPhoto).addClass("photo-active").removeClass("photo-left");
        $(".trans-bg").removeClass("trans-bg-active");
        $(".trans-bg-" + curPhoto).addClass("trans-bg-active");
        $(".indicator").html((curPhoto + 1) + "/" + numOfPhotos)
      }
      else {
        $(".photo-active").removeAttr("style");
      }
      ms.x = 0;
      ms.y = 0;
    });
  });

/*Tearsheets*/

/*Mouse pos Requires JQuery / can be removed*/

var carousel = document.querySelector('#carousel');
var outerDiv = document.querySelector('#outerDiv');
var i = 0;
var j;
var accelerate;
var val;  
var isHovered;
var direction;
var lastVal;

setInterval(function(){
  $(outerDiv).mousemove(function(){
    mousePerc = (event.clientX/outerDiv.clientWidth) -0.5; 
  accelerate = 25*mousePerc;
  val = accelerate || 2;
    if(val < 0){
  direction = "left"
    }else {
  direction = "right"
    }
  })
  
    var isHovered = $(outerDiv).is(":hover"); // returns true or false

 
  if( val == null || val == undefined){
    val = 2;
  }
  
  if(isHovered == false && direction == "left"){
    val = lastVal + 0.2;
    if (val > -2){
    val = -2
    }
  }else if (isHovered == false && direction == "right"){
    val = lastVal - 0.2;
    if(val < 2){
      val = 2
    }
  }
  
  lastVal = val;
  i = i+(val);
  
  
  
  var wid = carousel.clientWidth;
  var outerWid = outerDiv.clientWidth;
  if (i < 0){
    i=0;
  }
  if (i > wid - outerWid){
    i = wid - outerWid;
  }
  updatePos(-i); 
},18);


function updatePos(k){
    
  carousel.style.transform = "translateX("+(k)+"px)";
  return k;
};


$(".square").hover(function(){
  // if mouse hover then add .flipping class
 $(this).addClass("flipping");

},function(){
 // if mouse unhover then remove the .flipping class
 $(this).removeClass("flipping");
});