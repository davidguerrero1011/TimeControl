$(document).ready(function() {
    window.location.hash="no-back-button";
    window.location.hash="Again-No-back-button";//esta linea es necesaria para chrome
    window.onhashchange=function(){window.location.hash="no-back-button";}

    $('#headerModalLabel').html("Cambio Contraseña");
    $('#changepassword').attr('disabled', 'disabled');
    $('#textHelp1').css('display', 'hidden')
});

$('#namesInput').on('blur', function() {
    let name = document.getElementById('namesInput').value;
    const REGEX = /^[a-zA-Z]*$/;
    $('#errorMessageName').append("");

    let validateName = REGEX.test(name);
    if(validateName == false) {
        $('#errorMessageName').append("Recuerde que solo debe ingresar letras");
    }
});

$('#lastNamesInput').on('blur', function() {
    let lastName = document.getElementById('lastNamesInput').value;
    const REGEX = /^[a-zA-Z]*$/;
    $('#errorMessageLastName').append("");

    let validateLastName = REGEX.test(lastName);
    if(validateLastName == false) {
        $('#errorMessageLastName').append("Recuerde que solo debe ingresar letras");
    }
});

$('#typeDocument').on('change', function() {
    let type = document.getElementById('typeDocument').value;
    if(type == 0) {
        Swal.fire({
              icon: "error",
              title: "¡Oooops algo esta mal!",
              text: "Debe seleccionar alguna opción valida",
            });
    }
});

$('#documentNumber').on('blur', function() {
    let documentNumber = document.getElementById('documentNumber').value;
    const REGEX = /^[0-9]*$/;
    $('#MessageDocument').append("");

    let validateNumberDocument = REGEX.test(documentNumber);
    if(validateNumberDocument == false) {
        $('#MessageDocument').append("Recuerde que solo debe ingresar números");
    }
});


function activateButton() {
    $('input').each(function() {
        if($(this).val() != '' && $(this).val() != 'on') {
            //$('#createBtn').removeAttr('disabled');
        } else {
            //$('#createBtn').attr('disabled', 'disabled');
        }
    });
}

$('#password1InputEmail1').on('blur', function() {

    let password1 = document.getElementById('password1InputEmail1').value;
    let regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$/;

    if(regex.test(password1)) {
       $('#textHelp1').append("");
       $('#textHelp1').css('display', 'none')
    } else {
       $('#textHelp1').append("");
       $('#textHelp1').css('display', 'inline-block');
       $('#textHelp1').append("Recuerde que la contraseña debe tener entre 8 y 15 caracteres, al menos una mayuscula y una minuscula, un número y un carácter especial");
    }

});

$('#password2InputPassword1').on('blur', function() {

    let password1 = document.getElementById('password1InputEmail1').value;
    let confirPassword = document.getElementById('password2InputPassword1').value;

    if(password1 == confirPassword) {
        $('#textHelp2').append("");
        $('#textHelp2').css('display', 'none');
        $('#changepassword').removeAttr('disabled');
    } else {
        $('#textHelp2').css('display', 'inline-block');
        $('#changepassword').attr('disabled', 'disabled');
        $('#textHelp2').append("Las contraseñas no coinciden, por favor verifique.");
    }

});

$('#buttonModal').on('click', function() {
    let userId = document.getElementById('userId').value;
    $('#userIdPassword').val(userId);
});
