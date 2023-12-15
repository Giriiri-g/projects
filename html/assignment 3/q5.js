document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        const inputString = prompt("Enter the input string:");
        const searchWord = prompt("Enter the search word:");

        const indexOfWord = inputString.indexOf(searchWord);

        if (indexOfWord !== -1) {
            alert(`Input String: ${inputString}\nSearch word: ${searchWord}\nThe index of '${searchWord}' is: ${indexOfWord}`);
        }
        else {
            alert(`Input String: ${inputString}\nSearch word: ${searchWord}\n'${searchWord}' not found in the string.`);
        }
    }, 1000);
});
