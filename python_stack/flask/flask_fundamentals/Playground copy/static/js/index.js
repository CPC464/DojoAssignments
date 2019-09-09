$(document).ready(function(){
	console.log('The document is ready');

	$( "#button1" ).click(function() {
		console.log("button 1 clickked");
		$( "#button2, .jquery-test" ).slideDown()
		console.log("button 2 showing");
	});
	
	$('#button2').click(function() {
		console.log("button 2 clickked");
	}); 






}); // Closing of document ready listener