var formFields;
document.addEventListener("DOMContentLoaded", () => {
    formFields = document.querySelectorAll('.form-group .form-control');
    formFields.forEach((e) => {
        if(e.value != '') {
            e.parentNode.querySelector('label').classList.add('active');
        } else {
            e.parentNode.querySelector('label').classList.remove('active');
        }
        e.onblur = function() {
            if(e.value != '') {
                e.parentNode.querySelector('label').classList.add('active');
            } else {
                e.parentNode.querySelector('label').classList.remove('active');
            }
        }
    });
});
var passwords;
function visibility() {
    if(!passwords) {
        passwords = document.querySelectorAll('input[type="password"]');
    }
    passwords.forEach(field => {
        if(field.type == 'text') {
            field.type = 'password';
        } else {
            field.type = 'text';
        }
    });
}