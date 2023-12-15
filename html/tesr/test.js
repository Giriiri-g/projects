for (let i = 0; i <= 100; i++) {
  const div = document.querySelector('.loadertext');
  const loader = document.querySelector('.loaderbar');
  loader.width = i*2;
  div.textContent = i + '%';
}
