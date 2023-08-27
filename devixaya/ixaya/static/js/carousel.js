
// const sponsorCarousel = document.querySelector('#sponsorCarousel');

if( window.matchMedia("(min-width:576px)").matches){
    // const carousel = new bootstrap.Carousel(sponsorCarousel,
    //     {
    //         interval:false
    //     })
    var carouselWidth = $('.carousel-inner')[1].scrollWidth;
    var cardWidth = $('.carousel-item').width();
    var scrollPosition = 0;

    $('.carousel-control-next').on('click', function(){
        console.log('next');
        if( scrollPosition < (carouselWidth - (cardWidth * 3 ))){
            scrollPosition = scrollPosition + cardWidth;
            $('.carousel-inner').animate({scrollLeft:scrollPosition}, 600);
        }
    });

    $('.carousel-control-prev').on('click', function(){
        console.log('prev');
        if( scrollPosition > 0){
            scrollPosition = scrollPosition - cardWidth;
            $('.carousel-inner').animate({scrollLeft:scrollPosition}, 600);
        }
    });
}
// else{
//     $(sponsorCarousel).addClass('slide')
// }