$(function () {

  /* Functions */

  var loadForm = function () {

    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-rule .modal-content").html("");
        $("#modal-rule").modal("show");
      },
      success: function (data) {
        $("#modal-rule .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#rule-table tbody").html(data.html_rule_list);
          $("#modal-rule").modal("hide");
            setTimeout(function() {
            $('#message').text(data.message);
          }, 3000);


        }
        else {
          $("#modal-rule .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create rule
  $(".js-create-rule").click(loadForm);
  $("#modal-rule").on("submit", ".js-rule-create-form", saveForm);


  // Update rule
  $("#rule-table").on("click", ".js-update-rule", loadForm);
  $("#modal-rule").on("submit", ".js-rule-update-form", saveForm);

  // Delete rule
  $("#rule-table").on("click", ".js-delete-rule", loadForm);
  $("#modal-rule").on("submit", ".js-rule-delete-form", saveForm);


});
