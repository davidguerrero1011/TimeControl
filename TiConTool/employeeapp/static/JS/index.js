$(document).ready(function() {
    $('#registerBtn').attr('disabled', 'disabled');

    window.location.hash="no-back-button";
    window.location.hash="Again-No-back-button";//esta linea es necesaria para chrome
    window.onhashchange=function(){window.location.hash="no-back-button";}

});

$('#typeEvents').on('change', function() {
    let eventsType = document.getElementById('typeEvents').value;
    let identificationValue = document.getElementById('identificationInput').value;

    if(eventsType == 0 || identification == false && eventsType >= 0) {
        $('#registerBtn').attr('disabled', 'disabled');
        Swal.fire({
          icon: "error",
          title: "¡Oooops algo esta mal!",
          text: "Debe seleccionar alguna opción valida",
        });
    } else {
        $('#registerBtn').removeAttr('disabled');
    }
});

$('#identificationInput').on('blur', function() {
    const REGEX = /^[0-9]*$/;
    let identificationValue = document.getElementById('identificationInput').value;
    let eventsType = document.getElementById('typeEvents').value;

    let identification = REGEX.test(identificationValue);
    if(identification == false && eventsType == 0 || identification == true && eventsType == 0 || identification == false && eventsType >= 0) {
        $('#registerBtn').attr('disabled', 'disabled');
    } else {
        $('#registerBtn').removeAttr('disabled');
    }
});