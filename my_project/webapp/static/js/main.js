$(document).on('click', '.add_to_bookcase', function () {
    const formId = $(this).data('form_id');
    $.ajax({
        url: $('#' + formId).attr('action'),
    }).done((response) => {
        alert(response.status);
    }).fail(function() {
        alert('Запрос не ушел!');
    });
});

$(document).on('click', '.remove_from_bookcase', function () {
    var pathname = window.location.pathname;
    const formId = $(this).data('form_id');
    const bookId = $(this).data('book_id');
    $.ajax({
        url: $('#' + formId).attr('action'),
    }).done((response) => {
        if (pathname.substring(0, 5) === '/user')
            $('#' + bookId).remove();
        alert(response.status);
    }).fail(function() {
        alert('Запрос не ушел!');
    });
});

$(document).on('click', '.delete_item', function () {
    let url = $(this).data('url');
    let modal = $('#confirm_delete');
    modal.attr('href', url);
});