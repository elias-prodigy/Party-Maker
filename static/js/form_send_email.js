$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})


//function myFunction(){
//    $("select").on("change", function() {
//      var id = $(this).attr("id");
//      alert(id);
//    });

function myFunction(){
    var x = 0
    var x =$("#chouseEvent option:selected").attr("data-event-id");
//     document.getElementById("chouseEvent").attr("data-event-id");

//    var id = $(this).attr('id');
    alert(x);

    $('#send_m').click(function () {

    var act = $('#for_mail').attr('action').replace("0",x)


    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $.ajax({
        url: act,
        type: 'POST',
        data: {},
        headers: {'X-CSRFToken': csrftoken},

        })

    })


    }




