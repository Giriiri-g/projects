document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        function guessNumber() {
            const randomNumber = Math.floor(Math.random() * 10) + 1;
            const userGuess = prompt("Guess a number between 1 and 10:");
            const guessedNumber = parseInt(userGuess);

            if (isNaN(guessedNumber)) {
                alert("Invalid input. Please enter a valid number.");
            }
            else if (guessedNumber < 1 || guessedNumber > 10) {
                alert("Please enter a number between 1 and 10.");
            }
            else if (guessedNumber === randomNumber) {
                alert(`Congratulations! You guessed the correct number: ${randomNumber}`);
            }
            else {
                alert(`Guessed: ${guessedNumber}\nSorry, the correct number was ${randomNumber}. Try again!`);
                guessNumber();
            }
        }
        guessNumber();
    }, 1000);
});
