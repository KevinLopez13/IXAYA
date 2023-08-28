
$(document).ready(function () {
    var multipleCardCarousel = document.querySelector("#sponsorCarousel");
    
  if (window.matchMedia("(min-width: 992px)").matches) {
    var carousel = new bootstrap.Carousel(multipleCardCarousel, {
      interval: false,
      wrap: false
    });

    $(multipleCardCarousel).removeClass("slide");

    var carouselWidth = $("#sponsorCarousel .carousel-inner")[0].scrollWidth;
    var cardWidth = $("#sponsorCarousel .carousel-item").width();
    var scrollPosition = 0;
    console.log(window.innerWidth);
    
    $("#sponsorCarousel .carousel-control-next").on("click", function () {
      if (scrollPosition < carouselWidth - (cardWidth * 4)) {
        scrollPosition += cardWidth;
        $("#sponsorCarousel .carousel-inner").animate( { scrollLeft: scrollPosition }, 600);
      }
    });
    $("#sponsorCarousel .carousel-control-prev").on("click", function () {
        if (scrollPosition > 1) {
        scrollPosition -= cardWidth;
        $("#sponsorCarousel .carousel-inner").animate( { scrollLeft: scrollPosition }, 600);
      }
    });
  }
  else {
    $(multipleCardCarousel).addClass("slide");
    console.log("slide");
  }
});