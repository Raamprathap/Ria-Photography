let slider = document.querySelector('.slider')
let sliderList = slider.querySelector('.slider .list')

function moveSlider() {
    let sliderItems = sliderList.querySelectorAll('.item')
    
    sliderList.appendChild(sliderItems[0])
    slider.classList.add('next')


    slider.addEventListener('animationend', function() {
        slider.classList.remove('next')
    }, {once: true})
}

setInterval(function(){
    moveSlider()
}, 5000)

const imgSlide = document.querySelector('.img-slide .images');
const slideImages = imgSlide.children;
const slideInterval = 5000;

setInterval(() => {
    imgSlide.style.transition = 'transform 0.8s ease';
    imgSlide.style.transform = `translateX(-${imgSlide.children[0].offsetWidth}px)`;

    setTimeout(() => {
        const firstImage = imgSlide.children[0];
        imgSlide.appendChild(firstImage);

        imgSlide.style.transition = 'none';
        imgSlide.style.transform = 'translateX(0)';

        setTimeout(() => {
            imgSlide.style.transition = 'transform 0.8s ease';
        }, 50);
    }, 500);
}, slideInterval);

function toggleMenu() {
    const popupMenu = document.getElementById('popupMenu');
    popupMenu.style.display = popupMenu.style.display === 'block' ? 'none' : 'block';
}

// Optional: Close the popup if clicking outside of it
window.onclick = function(event) {
    if (!event.target.matches('.menu-icon')) {
        const popupMenu = document.getElementById('popupMenu');
        if (popupMenu.style.display === 'block') {
            popupMenu.style.display = 'none';
        }
    }
}
