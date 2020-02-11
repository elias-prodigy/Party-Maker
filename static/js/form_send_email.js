function ChangeTableFunction(){
    var x = $("#main_choose_event option:selected").attr("data-id-of-event");
    var act = $('#for_partner_event_table').attr('action').replace("0",x);
    window.location = act;
};

function myFunction(){
    var x = $("#chouseEvent option:selected").attr("data-event-id");
    var act = $('#for_mail').attr('action').replace("0",x);
    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $.ajax({
        url: act,
        type: 'POST',
        data: {},
        headers: {'X-CSRFToken': csrftoken},
    });
}


//function SendTicketFunction(){
//    var x =$("#main_choose_event option:selected").attr("data-event-id");
//    $('#send_ticket').click(function () {
////    var act = $('#for_mail').attr('action').replace("0",x);
//    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//
//    $.ajax({
//        url: $(this).attr('x'),
//        type: 'POST',
//        data: {},
//        headers: {'X-CSRFToken': csrftoken},
//        });
//    });
//};


$(document).ready(function(){
  var token = document.querySelector('[name=csrfmiddlewaretoken]').value;

  $('#main_choose_event').change(function() {
    ChangeTableFunction()
    });

  $("button.js-delete").click(function(){
    $.ajax({
            headers: { "X-CSRFToken": token },
            type: 'DELETE',
            url: $(this).attr('delete-link'),
            success: $(this).parents("tr").remove()
            });
  });

  $("button.js-update").click(function() {
      var name = $(this).parents('tr').find('td[class="name"]').text();
      $('input[name="name"]').val(name);
      var surname = $(this).parents('tr').find('td[class="surname"]').text();
      $('input[name="surname"]').val(surname);
      var sponsor = $(this).parents('tr').find('td[class="sponsor"]').text();
      $('input[name="sponsor"]').val(sponsor);
      var manager_name = $(this).parents('tr').find('td[class="manager_name"]').text();
      $('input[name="manager_name"]').val(manager_name);


      var check_site = $("button.js-update").parents('tr').find('td[class="manager_approve"]').is(":checked")
      var check_modal = $('input[name="modal_manager_approve"]').is(":checked")
      check_modal = check_site


      var partner_url = $(this).attr('update_link');
      $('#update_partner').attr('action', partner_url);

  });

  $('#update_partner').on('submit', function (event) {
      event.preventDefault();
       $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: function () {
                location.reload();
            }
       });
  });

  $("button#update").click(function() {
      $('#update_partner').submit();

  });

  $("button#send_m").click(function() {
    myFunction();
  });
});