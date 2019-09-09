$(document).ready(function(){
    console.log('The document is ready');
    
    $('form').submit(function() {  
        // building the ULR with the city and API key
        var city = $('#inputCity').val();
        console.log("City input: ", city);
        var base = "http://api.openweathermap.org/data/2.5/weather?q=";
        var key = "a22bfd4f74cc86f8c2406a708adadfe0";
        var url = base + city + "&&appid=" + key;
        console.log("Generated URL: "+url);

        var kelvin = 0;
        var fahrenheit = 0;
        var celcius = 0;

        // Launch AJAX request to get data
        $.get(url, function(res) {
            console.log("API response:\n",res); // Log API response
            console.log("Temperature in kelvin is:\n",res.main.temp); // Log the temperature from the API response

            // Default unit is Kelvin. Convert to F and C
            kelvin = res.main.temp;
            fahrenheit = (kelvin-273.15)*9/5+32;
            celcius = (kelvin-273.15);
            
            // .toFixed(2) converts to string with two decimals
            kelvin = kelvin.toFixed(2);
            fahrenheit = fahrenheit.toFixed(2);
            celcius = celcius.toFixed(2);

            // Insert output into DOM and show text and selector (these are hidden until a city is submitted, using display: none; in CSS)
            $('.output .city').text(city);
            $('.output .temperature').text(fahrenheit); 
            $('.output').show("slow", function() {});
            // $('.output select').slideDown("slow", function() {});
        },'json');  //Not entirely sure how this should be indented
       
            // Listen for changes to the selected unit and put value into a string
            // $('.output select').change(function() {
            //     var str = "";
            //     $( "select option:selected" ).each(function() {
            //     str += $( this ).text() + " ";
            //     str = str.toLowerCase();
            // });
                // if(str="celcius"){
                //     console.log("str:" + str);
                //     $('.output .temperature').text(celcius);
                // } if(str="kelvin"){
                //     $('.output .temperature').text(kelvin);
                //     console.log("str:" + str);
                // }
                // if(str="fahrenheit"){
                //     console.log("str:" + str);
                //     $('.output .temperature').text(fahrenheit);
                // };    
                // $('.output .test').text(str);
               // $('.output .temperature').text(str);  // Could not get this one to work
               
            // });
            // .change();

        // Don't forget to return false so the page doesn't refresh
        return false;
    });  // Closing of form submit function
}); // Closing of document ready listener

