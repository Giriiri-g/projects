document.addEventListener("DOMContentLoaded", function () {
    function formatTime(num) {
        return num < 10 ? `0${num}` : num;
    }

    setTimeout(function () {
        const currentDate = new Date();
        const day = currentDate.getDate();
        const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        const month = monthNames[currentDate.getMonth()];
        const hours = formatTime(currentDate.getHours());
        const minutes = formatTime(currentDate.getMinutes());
        const seconds = formatTime(currentDate.getSeconds());

        const formattedDate = `Date is: ${day} ${month} Time is: ${hours} Hours : ${minutes} Minutes : ${seconds} Seconds`;
        alert(formattedDate);
    }, 1000);
});
