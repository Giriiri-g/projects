document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
      const navigatorProperties = [];
  
      for (const prop in navigator) {
        navigatorProperties.push(prop);
      }
  
      alert(`Properties of the navigator object:\n\n${navigatorProperties.join("\n")}`);
    }, 1000);
  });
  