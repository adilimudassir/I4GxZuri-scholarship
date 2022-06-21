
/*
This file is part of the tasks for the Javascript calculator task.It is part of the tasks / projects carried out in the I4GxZuri Scholarship in the Fullstack Track.


Author: Mudassir Adili Ahmad(adilimudassir)
Date: 2022-06 -21
*/

(() => {
    //fetch the values from the user
    const num1 = prompt("Enter First Number: ");
    const num2 = prompt("Enter Second Number: ");
    const operator = prompt("Enter Operator: ");

    //calculator function
    const calculator = (num1, num2, operator) => {
        if (operator === "+") {
            return parseInt(num1) + parseInt(num2);
        } else if (operator === "-") {
            return parseInt(num1) - parseInt(num2);
        } else if (operator === "*") {
            return parseInt(num1) * parseInt(num2);
        } else if (operator === "/") {
            return parseInt(num1) / parseInt(num2);
        } else {
            return "Invalid Operator";
        }
    }

    //calling the calculator function
    alert(`
    The Result is: ${calculator(num1, num2, operator)}
    `);
})();

