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


function SendTicketFunction(){
    var CEO_approve = $('input[name="CEO_approve"]').val();
    var manager_approve = $('input[name="manager_approve"]').val();
    var x = window.location.pathname.replace(/[^0-9]/gim,'')
    var act = $('#send_ticket_form').attr('action').replace("0",x);
    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    if (CEO_approve=="True" && manager_approve=="True") {
            $.ajax({
                url: act,
                type: 'POST',
                data: {},
                headers: {'X-CSRFToken': csrftoken},
                });
    } else {alert('You need to update the partners')}
};


$(document).ready(function(){
  var token = document.querySelector('[name=csrfmiddlewaretoken]').value;

  $('#send_ticket').click(function() {
    SendTicketFunction()
  });

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

    $("button.partner-event-update").click(function() {
      var name = $(this).parents('tr').find('td[class="modal_name"]').text();
      $('input[name="modal_name"]').val(name);

      var surname = $(this).parents('tr').find('td[class="modal_surname"]').text();
      $('input[name="modal_surname"]').val(surname);

      var sponsor = $(this).parents('tr').find('td[class="modal_sponsor"]').text();
      $('input[name="modal_sponsor"]').val(sponsor);

      var manager_name = $(this).parents('tr').find('td[class="modal_manager_name"]').text();
      $('input[name="modal_manager_name"]').val(manager_name);

      var manager_approve = $(this).parents('tr').find('td[class="manager_approve"]').text();
      manager_approve = $('input[name="modal_manager_approve"]').val(manager_approve);


      var CEO_approve = $(this).parents('tr').find('input[name="CEO_approve"]').val();
      if (CEO_approve = "True") {
        $('select[id="modal_CEO_approve"]').val(CEO_approve)
      } else if (CEO_approve = "False") {
        $('select[id="modal_CEO_approve"]').val(CEO_approve)
      };


      var partner_on_event_url = $(this).attr('update_partner_on_event_link');
      $('#update_partner_on_event').attr('action', partner_on_event_url);
  });

    $('#update_partner_on_event').on('submit', function (event1) {
      event1.preventDefault();
       $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: function () {
                location.reload();
            }
       });
  });

    $("button#update_event_partner").click(function() {
          $('#update_partner_on_event').submit();
      });

  $('button#add_partner_to_event').click(function() {
    var newurl = $(this).attr('href').replace("/event/1/register/", "/event/" + window.location.pathname.replace(/[^0-9]/gim,'') + "/register/");
    window.location = newurl
  });

  $("button#send_m").click(function() {
    myFunction();
  });
});