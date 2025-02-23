// Карусель с рекламой на главной

$(document).ready(function(){
    $('.slider').slick({
      autoplay: true,
      autoplaySpeed: 5000, 
      speed: 500,          
      slidesToShow: 1,      
      slidesToScroll: 1,    
      arrows: false,       
      dots: false,          
    });
});