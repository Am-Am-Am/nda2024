// Карусель на главная в блоке работаем для вас


$(document).ready(function(){
    $('.sliderInfo .slider ').slick({
      autoplay: true,          
      autoplaySpeed: 5000,      
      infinite: true,          
      slidesToShow: 1,          
      slidesToScroll: 1,        
      arrows: false,          
      dots: true,              
      dotsClass: 'slick-dots', 
      appendDots: '.slick-dots' 
    });
  });
  
  