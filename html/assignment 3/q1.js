function sqrt(number) {
    if (typeof number !== 'number' || isNaN(number)) {
        return "Invalid input. Please enter a valid number.";
    }
    if (number < 0) {
        return "Square root of a negative number is not real.";
    }
    return Math.sqrt(number);
}

document.addEventListener("DOMContentLoaded", function () {
    setTimeout(() => {
        const input = prompt("Enter a number to calculate its square root:");
        const number = parseFloat(input);

        const result = sqrt(number);
        alert(`The Square Root of the Number ${number} is ${result}`);
    }, 1000);
});
