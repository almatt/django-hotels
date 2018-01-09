$(document).ready(function(){
    $('#rate').submit(function(e){
        e.preventDefault()
        $.post(
            "http://localhost:8000/hotels/rate/",
            {
                id: 1,
                rate: 4
            },
            onAjaxSuccess
        );
        function onAjaxSuccess(data)
        {

            alert(data);
        }
    });
});
