
/* Todo - add delete individual kendama function through button click
 * first user story make the parent element dissappear
*/

$("#gone").on("click", function(){

	var parentelement = $(this).parent();

	//use this to refer to current element
	console.log("this is the parent ", parentelement);

	//it's not logging the same thing but seems to target the same element
	parentelement.fadeOut("slow", function(){
		//should be the same element being removed
		console.log("this is hopefully still the parent ", $(this) );

		$(this).remove();	
	});

});


//from the delete button, two levels up to target the kendama block
$(".delete-ken").on("click", function(){

	//first parent is the header, then the div
	var parentEle = $(this).parent().parent();

	parentEle.fadeOut("slow", function(){
		$(this).remove();
	});

});



