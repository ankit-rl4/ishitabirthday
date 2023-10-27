// Calculate the total height of the carousel to reset animation
const carouselHeight = document.querySelector(".background-carousel").clientHeight;
const imageHeight = document.querySelector(".background-image").clientHeight;
const numImages = carouselHeight / imageHeight;

// Reset the animation when it reaches the total height
document.querySelector(".background-carousel").addEventListener("animationiteration", () => {
    document.querySelector(".background-carousel").style.animation = "none";
    void document.querySelector(".background-carousel").offsetWidth; // Trigger reflow
    document.querySelector(".background-carousel").style.animation = "scroll 10s linear infinite"; // Adjust the duration as needed
});
