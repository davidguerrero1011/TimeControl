
function showModal(id) {
    let post_url = $('#registerEdit').data('post-url');
    $('#registersModalLabel').append('Edición Registros');
    $('#registersModal').modal('show');

    console.log(id);
    let data = new FormData();
    data.append('id', id);

    axios.post('/updateRegister/', data, {headers:{'X-CSRFToken':Cookies.get('csrftoken')}})
    .then(function (response) {
        console.log(response);
    })
    .catch(function (error) {
        console.log(error.response.data);
    });

    return false;
}

