$(document).ready(function(){
    console.log('The document is ready');

    $('.jQueryFun1 button').click(function(){
        $('.jQueryFun1 h1').addClass('red');
    });
  
    $('.jQueryFun2 button').click(function(){
        $( "#toggleThis" ).slideToggle( "slow", function() {
            // Animation complete.
          });
    });

    $('.jQueryFun3 button').click(function(){
        $('.jQueryFun3 p').append(' APPENDED!');
    });


    $('.jQueryFun4 button').click(function(){
        $('.jQueryFun3 p').append(' APPENDED!');
    });

    $.get("https://pokeapi.co/api/v2/pokemon/1/", function(res) {
        for(var i = 0; i < res.types.length; i++) {
            console.log(res.types[i].type.name);
        }},  "json"
    );

    $.get("https://pokeapi.co/api/v2/pokemon/1/", function(res) {
                    console.log('API rsponse returned');
                    var html_str = "";
                    html_str += "<h4>Types</h4>";
                    html_str += "<ul>"; 
                    for(var i = 0; i < res.types.length; i++) {
                        html_str += "<li>" + res.types[i].type.name + "</li>";
                    }
                    html_str += "</ul>";
                    $("#bulbasaur").html(html_str);
                }, "json");
        
    for var(i=0;i<5;i++){
        $.get("https://pokeapi.co/api/v2/pokemon/i/", function(res)
        var html_str = "";
        html_str += "</ul>";
    }            
    $.get("https://pokeapi.co/api/v2/pokemon/1/", function(res) {
        console.log('API rsponse returned');
        var html_str = "";
        for(var i = 0; i < res.types.length; i++) {
            html_str += "<li>" + res.types[i].type.name + "</li>";
        }
        html_str += "</ul>";
        $("#bulbasaur").html(html_str);
    }, "json");




}); // Closing of document ready listener