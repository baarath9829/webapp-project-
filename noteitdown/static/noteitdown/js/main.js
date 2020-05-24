$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
  $("a").click(function(){
    var id_val = $(this).attr("id");
    $.post("noteitdown/home",{ id: id_val },fuction(status){
        alert("sent");
    });
  });
});