
(function ($) {
    "use strict";
    
    
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');
    

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        
        if(check)
        {
            $.ajax({
                async: false,
                url:"http://localhost:8081/log",
                type:"POST",
                data:{
                    id: $(input[0]).val(),
                    password: $(input[1]).val()
                }}).
                always(function(txt){
                if (txt.responseText == "S"){
                    var x ="Log in successfully! Welcome back, "+$(input[0]).val();
                    alert(x);

                }
                else{
                    alert("Log in failed! Please try again!");
                    check=false;
                }
                
            });
            
        }
        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        if ($(input).attr('name') == 'id'){
            if($(input).val().trim() == '')
            {
                $('#log_username_text').text("Empty id!");
                return false;
            }
            else if($(input).val().length < 5 || $(input).val().length > 16){
                $('#log_username_text').text("id: 10 digits!");
                return false;
            }
            else{
                $('#log_username_text').text("");
            }
        }
        if ($(input).attr('name') == 'pass'){
            if($(input).val().trim() == '')
            {
                $('#log_password_text').text("Empty password!");
                return false;
            }
            else if($(input).val().length < 5 || $(input).val().length > 16){
                $('#log_password_text').text("password: 5-16 letter or numbers!");
                return false;
            }
            else{
                $('#log_password_text').text("");
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);
