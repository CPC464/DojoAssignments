$(document).ready(function (){

    console.log("start script")
    $( ".slidedown button" ).click(function() {
        console.log("slidedown clickked");
        $( "#slidedownimage" ).slideDown( "slow", function() {         
        });
    });

    $( ".slidetoggle button" ).click(function() {
        console.log("slidetoggle clickked");
        $( "#slidetoggleimage" ).slideToggle( "slow", function() {      
        });
    });

    $( ".before button" ).click(function() {
        console.log("before clickked");
        $(".before p" ).before("ricky thomas "); 
    });

    $( ".after button" ).click(function() {
        console.log("after clickked");
        $(".after p" ).after("ricky thomas ");   
    });

    $( ".hide-show .show" ).click(function() {
        console.log("show clickked");
        $( ".hide-show h2" ).show( "slow", function() {         
        });
    });

    $( ".hide-show .hide" ).click(function() {
        console.log("hide clickked");
        $( ".hide-show h2" ).hide( "slow", function() {         
        });
    });

    $( ".toggle button" ).click(function() {
        console.log("toggle clickked");
        $( ".toggle h2" ).toggle( "slow", function() {         
        });
    });

    $( ".fade-in-out .fade-in" ).click(function() {
        console.log("fade-in clickked");
        $( ".fade-in-out h2" ).fadeIn( "slow", function() {         
        });
    });

    $( ".fade-in-out .fade-out" ).click(function() {
        console.log("fade-out clickked");
        $( ".fade-in-out h2" ).fadeOut( "slow", function() {         
        });
    });

    $( ".add-rm-class .add-cl" ).click(function() {
        console.log("add class clickked");
        $( ".add-rm-class h1" ).addClass("yellow");
    });

    $( ".add-rm-class .remove-cl" ).click(function() {
        console.log("remove class clickked");
        $( ".add-rm-class h1" ).removeClass( "yellow");
    });


    $( ".appender button" ).click(function() {
        console.log("Append clickked");
        $(".appender h2" ).append("  This is appended!   ");   
    });


    

    function displayVals(){
        var vals=[1,];
        $( ".custom-checkbox" ).click(function() {
            console.log("checkbox clickked");
            vals += $(this).val();
            console.log(vals);
            $(".result p").after(vals);
            });
    };
       
     


}); //End of document ready

