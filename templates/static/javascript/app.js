const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    //Toggle Nav
    burger.addEventListener('click',()=>{
        nav.classList.toggle('nav-active');
    });
    //Animate Links
    navLinks.forEach((link, index) => {
        link.style.animation = navLinkFade `navLinkFade 3s ease forwards ${index / 7 + 3}s`
    });
}

navSlide();