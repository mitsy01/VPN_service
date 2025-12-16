$(document).ready(function () {
    $(".form").submit(function (event) {
        event.preventDefault();
        var form = $(this);
        var url = form.attr("action");
        var data = form.serialize();


        $.ajax({
            type: "POST",
            url: url,
            data: data,
            success: function (response) {
                if (response.status === "success") {
                    $('.message').text("Ура!!! Нам вдалось!").css('color', 'green');
                    form[0].reset();
                }
            },
            error: function (responseError) {
                $('.message').css('color', 'red');
                const response = responseError.responseJSON;
                if (response && response.errors) {
                    let errorText = "Будь ласка, виправте наступні помилки:<br>";
                    $.each(response.errors, (key, value) => {
                        errorText += `&bull; ${value[0]}<br>`;
                    });
                    $('.message').html(errorText);
                }
            },
        })
    })
})