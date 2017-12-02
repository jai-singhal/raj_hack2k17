$(document).foundation();

function search_focus() {
    setTimeout(function () {
        setTimeout(function x() {
            $('#search-input').focus();
        }, 10);
        x();
    }, 100);
}
var codes = document.getElementsByTagName("code");
for(var i = 0; i < codes.length; i++){
    $(codes[i]).attr('id','id_code'+(i+1));
}


// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

    var $myForm = $('#subscription_ajax')
    $myForm.submit(function(event){
        event.preventDefault()
        var $formData = $(this).serialize()
        $.ajax({
            method: "POST",
            url: '/subscribe/',
            data: $formData,
            success: handleFormSuccess,
            error: handleFormError,
        })
    });

    function handleFormSuccess(response){
        // console.log(data)
        if(response.status == 404) {
            snake_alert('Email already registered !','warning');
        }

        else{
            snake_alert('Your email is successfully subscribed','success');
        }

    }

    function handleFormError(jqXHR, textStatus, errorThrown){
        console.log(jqXHR)
        console.log(textStatus)
        console.log(errorThrown)

        snake_alert('Error occurred !','error');
    }




