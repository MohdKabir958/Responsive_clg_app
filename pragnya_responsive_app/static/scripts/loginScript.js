// function loginFormValidator() {

//     document.getElementById('loginForm').addEventListener('submit', function (event) {
//         event.preventDefault(); // Prevent form submission

//         const email = document.getElementById('email').value;
//         const password = document.getElementById('password').value;
//         const Flash = document.getElementById('flash');

//         let isValid = true;
//         Flash.innerHTML='';

//         // Email validation
//         const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
//         if (!email) {
//             Flash.innerHTML = 'Email is required.';
//             isValid = false;
//         } else if (!emailRegex.test(email)) {
//             Flash.innerHTML = 'Please enter a valid email address';
//             isValid = false;
//         }

//         // Password validation
//         if (!password) {
//             Flash.innerHTML += 'Password is required.';
//             isValid = false;
//         } else if (password.length < 5) {
//              Flash.innerHTML += 'Password must be at least 5 characters long.';
//             isValid = false;
//         } else {
//             const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
//             if (!passwordRegex.test(password)) {
//                 Flash.innerHTML = 'Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character.';
//                 isValid = false;
//             }
//         }

//         if (isValid) {
//             // Submit the form or proceed with login
//             Flash.innerHTML = 'Form is valid. Proceed with login.';
//         }
//     });

// }

// document.addEventListener('DOMContentLoaded', function () {
//     loginFormValidator();
// });


function validateLoginForm() {
    const email = document.getElementById('email_login').value.trim();
    const password = document.getElementById('password_login').value;
    const Flash = document.getElementById('flash');

    // Clear previous messages
    Flash.innerHTML = '';

    // Email validation
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailPattern.test(email)) {
        Flash.innerHTML = 'Please enter a valid email address.';
        return false;
    }

    // Password validation
    const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!password) {
        Flash.innerHTML = 'Password is required.';
        return false;
    } else if (!passwordPattern.test(password)) {
        Flash.innerHTML = 'Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character.';
        return false;
    }

    // If all validations pass
    return true;
}

// Attach the event listener to the login form
// document.addEventListener('DOMContentLoaded', function () {
//     document.getElementById('loginForm').addEventListener('submit', function (event) {
//         if (!validateLoginForm()) {
//             event.preventDefault(); // Prevent form submission if validation fails
//         }
//     });
// });

