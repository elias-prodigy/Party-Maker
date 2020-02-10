$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
});


function myFunction(){
    var x =$("#chouseEvent option:selected").attr("data-event-id");
    $('#send_m').click(function () {
    var act = $('#for_mail').attr('action').replace("0",x);
    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $.ajax({
        url: act,
        type: 'POST',
        data: {},
        headers: {'X-CSRFToken': csrftoken},
        });
    });
}


$(document).ready(function(){
  var token = '{{csrf_token}}';

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
      $('input[name="manager_name"]').val(manager_name)
      var partner_url = $(this).attr('update_link');
      $('#update_partner').attr('action', partner_url)
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

  $("button.save").click(function() {
      $('#update_partner').submit();

    });
});