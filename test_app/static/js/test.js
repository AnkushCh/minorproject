        /*
        On submiting the form, send the POST ajax
        request to server and after successfull submission
        display the object.
    */
   $(".next_ques").click(
    function (e) {
 // serialize the data for sending the form data.
 $("#ans").empty()
 var serializedData = $("#subject").serialize();
 // make POST ajax call
 $.ajax({
     type: 'GET',
     url: "ajax/next_ques",
     data: serializedData,
     success: function (response) {
         // on successfull creating object
         // 1. clear the form.
        //  $("#sub_form").trigger('reset');
         // 2. focus to nickname input 
         $("#start").remove();

         // display the newly friend to table.
         var instance = JSON.parse(response["data"]);
         
        // for (i = 0; i < instance.length; i++) {
        //var fields = instance[i]["fields"];
         $("#test").html(
            `<input type="hidden" name="qid" id="ques_id" value="${instance["pk"]||""}">
            <h1 id="ques">${instance["qn"]||""}</h1>
            <input type="radio" id="option1" name="option" value="1">
            <label for="option1">${instance["op1"]||""}</label><br>
            <input type="radio" id="option2" name="option" value="2">
            <label for="option2">${instance["op2"]||""}</label><br>
            <input type="radio" id="option3" name="option" value="3">
            <label for="option3">${instance["op3"]||""}</label><br>
            <input type="radio" id="option4" name="option" value="4">
            <label for="option4">${instance["op4"]||""}</label><br>`
            
         )
         
         //}
     },
     error: function (response) {
         // alert the error if any error occured
         alert(response["data"]["error"]);
     }
 })
}) 

var score = 0
//Get Answer
$("#ans_button").click(
    function(e){
        var serializedData = $('input[name="option"]:checked,#ques_id').serializeArray();

        $.ajax(
            {
                type:'GET',
                url:'ajax/get_ans',
                data:serializedData,
                success: function(response){
                    var instance = JSON.parse(response["data"]);
                    var ans = $(`input[name=option][value=${instance['ans']}] + label`).text();
                    // alert(ans)
                    $("#ans").text('ans is:'+ans)
                    
                    if ($('input[name="option"]:checked').val() == `${instance['ans']}`)
                    {
                        score=score+1;
                    }
                    $('#score').text('Score:'+score);

                },
                error: function(response){
                    alert(response["data"]["error"]);
                }
            }
        )
        
    }

)