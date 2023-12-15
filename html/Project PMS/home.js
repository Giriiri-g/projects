let loggedin = false;

function loginpopup(){
    document.getElementById("login").style.display = "flex";
    document.getElementById("container").classList.add("blur");
}

function checkredirect(classname){
    
}

function loginhide(){
    const userTypeRadios = document.getElementsByName("userType");
    let selectedUserType = "";

    userTypeRadios.forEach(function(radio) {
        if (radio.checked) {
            selectedUserType = radio.value;
        }
    });
    loggedin = true;
    if (selectedUserType === "faculty") {
        window.location.href = "homenew_staff.html";
    } else if (selectedUserType === "student") {
        window.location.href = "homenew.html";
    }
}


for (let i = 0; i <= 100; i++){
    setTimeout(() => {
      const div = document.querySelector('.loadertext');
      const loader = document.querySelector('.loaderbar');
      loader.style.width = i * 5 + "px";
      div.textContent = i + '%';
      if (i === 100) {
        setTimeout(() => {
          load();
        }, 500);
      }
    }, i * 10);
  }
  
  function load() {
    const loader = document.querySelector('.loader');
    const container = document.getElementById('container');
    loader.classList.add("fade");
    container.classList.add("fadein");
    setTimeout(() => { loader.style.display = 'none'; }, 500);
    setTimeout(() => { container.style.display = 'flex'; }, 500);
  }
  
  function check() {
    const name = document.getElementById("Email").value;
    const password = document.getElementById("password").value;
    if (!checkNullFields([name, password])) {
        alert("All fields must be filled.");
    } else if (!checkpasswordLength(password)) {
        alert("Password should be more than 7 characters.");
    }else {
      loginhide();
    }
}
function checkNullFields(fields) {
  for (const field of fields) {
      if (!field || field.trim() === '') {
          return false;
      }
  }
  return true;
}

function checkpasswordLength(password) {
  return password.length > 7;
}

document.getElementById("button-login-submit").addEventListener("click", check);