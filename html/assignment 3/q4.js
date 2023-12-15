document.addEventListener("DOMContentLoaded", function () {
    function daysUntilNewYear() {
        const currentDate = new Date();
        const nextYear = new Date(currentDate.getFullYear() + 1, 0, 1);
        const millisecondsPerDay = 24 * 60 * 60 * 1000;

        const daysLeft = Math.floor((nextYear - currentDate) / millisecondsPerDay);
        return daysLeft;
    }

    setTimeout(function () {
        const daysLeft = daysUntilNewYear();
        alert(`Number of days left until the next new year: ${daysLeft}`);
    }, 1000);
});
