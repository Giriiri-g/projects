document.addEventListener("DOMContentLoaded", function() {
    const backwardBtn = document.getElementById("button-back");
    const forwardBtn = document.getElementById("button-forward");

    backwardBtn.addEventListener("click", function() {
      const previousURL = document.referrer;
      alert(`Previous URL: https://amritauniv-my.sharepoint.com/personal/vishnuss_am_amrita_edu/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fvishnuss%5Fam%5Famrita%5Fedu%2FDocuments%2F22AIE%20115%20USER%20INTERFACE%20DESIGN%202023%20COURSE%20MATERIALS&view=0`);
    //   if (previousURL) {
    //   } else {
    //     alert("No previous URL available.");
    //   }
    });

    forwardBtn.addEventListener("click", function() {
      history.forward();
    });
  });