window.onload = function(){
    document.getElementById('subject').selectedIndex = -1;
  }

$("#subject").click(
 function (e) {
// serialize the data for sending the form data.
var serializedData = $("#subject").serialize();
// make POST ajax call
$.ajax({
  type: 'GET',
  url: "ajax/quiz_data",
  data: serializedData,
  success: function (response) {
      var instance = JSON.parse(response["jsdata"]);
      $("#select").empty()
      for (i = 0; i < instance.length; i++) {
          var fields = instance[i]["fields"];
          $("#select").append(
              `<p><label for="${instance[i]["pk"]}" class="check" >
              <input type="checkbox" name="${instance[i]["pk"]}" id="${instance[i]["pk"]}" />
              ${fields["qn"]}</label></p>`
          )
      }
    }
})
 })


 $("#add_checked").click(
    function (e) {
        var selected_check = $("input[type='checkbox']:checked + label").text()
        // console.log(selected_check)
        $("#selected").append($selected_check)
    }
 )

 function myFunction() {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("id_search");
    filter = input.value.toUpperCase();
    li = document.getElementsByClassName("check")
    // li = document.getElementsByTagName("label");
    for (i = 0; i < li.length; i++) {
        a = li[i];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}