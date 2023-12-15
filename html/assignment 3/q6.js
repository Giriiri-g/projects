document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
      const inputString = prompt("Enter a string:");
      
      const capitalizedString = inputString.charAt(0).toUpperCase() + inputString.slice(1);
  
      alert(`Original string: ${inputString}\nCapitalized string: ${capitalizedString}`);
    }, 1000);
  });
  