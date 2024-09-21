var grades = null; 
function calculateCGPA() {
    var numSubjects = parseInt(document.getElementById('numSubjects').value);
    var subjectGrades = document.getElementById('subjectGrades').value.toUpperCase().split(',');
    var numLabs = parseInt(document.getElementById('numLabs').value);
    var labGrades = document.getElementById('labGrades').value.toUpperCase().split(',');

    var result_of_subjects = printCombinedMarks(subjectGrades, true);
    var result_of_labs = printCombinedMarks(labGrades, false);

    var final_sum = (result_of_subjects + result_of_labs) / (numSubjects * 4 + numLabs * 2).toFixed(2);
    grades=final_sum
    document.getElementById('result').innerHTML = `
                <p>Total Subject Sum: ${result_of_subjects}</p>
                <p>Total Lab Sum: ${result_of_labs}</p>
                <p>Your CGPA is: ${final_sum}</p>
            `;
}

function printCombinedMarks(marks, isSubjectArray) {
    var total = 0;

    for (var i = 0; i < marks.length; i++) {
        switch (marks[i]) {
            case 'S':
                total += isSubjectArray ? 40 : 20;
                break;
            case 'A':
                total += isSubjectArray ? 36 : 18;
                break;
            case 'B':
                total += isSubjectArray ? 32 : 16;
                break;
            case 'C':
                total += isSubjectArray ? 28 : 14;
                break;
            case 'D':
                total += isSubjectArray ? 24 : 12;
                break;
            default:
                console.log("Invalid grade encountered for element " + i + ": " + marks[i]);
                break;
        }
    }

    return total;
}
