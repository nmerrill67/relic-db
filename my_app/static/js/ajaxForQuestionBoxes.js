
$(document).ready(function(e) {
var $form = $('#searchBar');
var maxDivs = -1;
$form.submit(function(e){
e.preventDefault();
   $.ajax({
		type: 'GET',
		url:$form.attr('action'),
		data:$form.serialize(),
		dataType:'json',
       success:
	   function(response)
       {
			console.log(response);
			var len = Object.keys(response).length;
			//var diff = (len - maxDivs) - 1;
			//var eraseDiff = (maxDivs - len);
			if(maxDivs === -1)
			{
				makeDivs(len);
			}
			else if(len < maxDivs)
			{
				eraseDivs(len-1,maxDivs-1);
			}
			else if(len > maxDivs)
			{
				makeDivs(len);
			}
			maxDivs = len;
			showQuestions(response);
       }
    });
	return false;
});


$('#exportExam').submit(function(e){
	e.preventDefault();
	var arr = JSON.stringify(exportArray);
	//console.log(arr);
   $.ajax({
		type: 'GET',
		url:$('#exportExam').attr('action'),
		data:{myData: arr},
		dataType:'json',
       success:
	   function(response)
       {
			alert("exam has been exported");
       },
	   
	   error:function(f)
	   {
               console.log("export exam has error");
			   alert(f.responseText);
		}
	
    });
	return false;
});


});