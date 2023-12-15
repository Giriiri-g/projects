document.addEventListener("DOMContentLoaded", function() {
    const image = document.getElementById("img");
    const buttonLoad = document.getElementById("button-img");

    const images = ["https://1.bp.blogspot.com/-6ik1sXaqRug/Ttfb3pJPcVI/AAAAAAAADvU/oJN0_lK9P4U/s1600/puss+in+boots2.jpg", "https://wallpapers.com/images/hd/overlord-pictures-u9546qhh265ocp42.jpg", "https://moewalls.com/wp-content/uploads/2022/09/sukuna-skull-and-bones-jujutsu-kaisen-thumb.jpg"]; // Array of image URLs
    let currentImageIndex = 0;

    buttonLoad.addEventListener("click", function() {
      currentImageIndex = (currentImageIndex + 1) % images.length;
      image.src = images[currentImageIndex];
    });
  });