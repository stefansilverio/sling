$(function() {
    $('submit').click(function() {
        $.ajax({
            url: '/landing',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
