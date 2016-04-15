$(document).ready(function(){

  $("#wat").css("color", "red");

  $("#same").on("click", function(){

	$.get("/", function(data){
	  console.log(data);	
	});
	
  
  
  });

});
