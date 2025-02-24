// Выделение активного элемента в миниатюрах карусели внутри товара


document.addEventListener('DOMContentLoaded', function() {
    const thumbnailDivs = document.querySelectorAll('.tumbnails-list div');
    const carouselElement = document.getElementById('carouselExampleIndicators');
    const carousel = new bootstrap.Carousel(carouselElement);


    function setActiveThumbnail(slideIndex) {
        thumbnailDivs.forEach(div => div.classList.remove('active'));
        thumbnailDivs[slideIndex].classList.add('active');
    
    }

      carouselElement.addEventListener('slid.bs.carousel', function(e) {
         const activeSlideIndex = e.to;

         setActiveThumbnail(activeSlideIndex);
        });

    thumbnailDivs.forEach(div => {
        div.addEventListener('click', function() {
            const slideTo = parseInt(this.getAttribute('data-bs-slide-to'));
            carousel.to(slideTo);
            setActiveThumbnail(slideTo);
         
        });
    });


      // Инициализируем активную миниатюру при загрузке страницы
      const initialActiveSlide = document.querySelector('.carousel-item.active');
      if (initialActiveSlide) {
           const initialActiveIndex = Array.from(document.querySelectorAll('.carousel-item')).indexOf(initialActiveSlide);
            setActiveThumbnail(initialActiveIndex);
    
        }

});



