var exportArray = [];
//creates physical divs for questions
function makeDivs(total)
{
				for(var count  = 0; count < total; count++)
				{
					if(document.getElementById('divId'+count)===null)
					{
						var clearDiv = document.createElement('div');
						var newDiv = document.createElement('div');
						clearDiv.id = 'clearDiv'+count;
						clearDiv.className = "searchStyle tabPage search clearDiv";
						newDiv.id = 'divId'+count;
						newDiv.className = "tabPage search questionStyle divId"+count;
						newDiv.style.display = "block";
						clearDiv.style.display = "block";
						clearDiv.appendChild(newDiv);
						clearDiv.addEventListener('click', function (event) {
								//name of clear div
								var name = event.currentTarget.id;
								var idName = document.getElementById(name).childNodes[0].id;
								//add method to add questions text and answers to array
								//copies html of clicked element
								//gets id of the question which is stored in a <p>
								//idhidden only used for id of ques so at [0]
								var qId = document.getElementById(idName).getElementsByClassName('idHidden')[0].id;
								//use for duplicating divs in another tab
								var clickedDiv = $("#"+idName).html();
								//idName[0]
								checkArray(idName, qId);	
								
						});
						document.body.appendChild(clearDiv);
					}
				}
}

//gets rid of excess divs on new search if too many
function eraseDivs(curr, total)
{
		for(var count = total; count > curr; count--)
		{
			var foundDiv = document.getElementById('clearDiv'+count);
			document.body.removeChild(foundDiv);
		}
}

function showQuestions(response)
{
	var result ="";
			var ansCount = 0;
			var ansLett = "";
			var count = 0;
			 $.each(response, function(index, questions){
				result = "";		
				var quesId = questions.questionId;
				result+=questions.questionText;
				$.each(questions.answers, function(index2, answer){
					ansLett = String.fromCharCode('a'.charCodeAt() + ansCount);
					result+="<pre class = 'answers'>"+ansLett+". "+answer+"</pre>";
					ansCount++;
				});
				//adds ques id as a <p>
				result+= "<pre class = 'idHidden' id = "+quesId+">"+quesId+"</pre>";
				ansCount = 0;
				$("#divId"+count).html(result);
				checkColor(count, quesId);
				var list = document.getElementById("divId"+count).getElementsByTagName('pre');
				for (var i = 0; i < list.length; i++) 
				{
					list[i].classList.add("divId"+count);
				}
				var listQues = document.getElementById("divId"+count).getElementsByTagName('p');
				for (var i = 0; i < listQues.length; i++) 
				{
					listQues[i].classList.add("question");
				}
				count++;
			  });
}

function checkColor(count, quesId)
{
	var cDiv = document.getElementById("divId"+count);
	var color = "white";
	for(var i = 0; i < exportArray.length;i++)
	{
		console.log(exportArray[i]["questionId"] +" "+ quesId);
		if(exportArray[i]["questionId"] == quesId)
		{
			color = "#ccffb3";
		}
	}
	cDiv.style.backgroundColor=color;
}

function checkArray(idName, qId)
{
	//check to see if id exists in array
	//if not add the entry 
	var cDiv = document.getElementById(idName);
	var quesArr = document.getElementById(idName).getElementsByClassName("question");
	var quesText = "";
	//adds text to one string
	for(var i = 0; i < quesArr.length;i++)
	{
		quesText+=quesArr[i].innerText+"\n";
	}
	var ansArr = document.getElementById(idName).getElementsByClassName("answers");
	var ansText = "";
	
	for(var i = 0; i < ansArr.length;i++)
	{
		ansText+=ansArr[i].innerText+"\n";
	}
	
	var removeIndex = -1;
	var entry = {"questionId":qId, "questionText":quesText, "answerText":ansText};
	
	for(var i = 0; i < exportArray.length;i++)
	{
		if(exportArray[i]["questionId"] === qId)
		{
			removeIndex = i;
		}
	}
	if(removeIndex > -1)
	{
		cDiv.style.backgroundColor="white";
		exportArray.splice(removeIndex,1);
	}
	else
	{
		cDiv.style.backgroundColor="#ccffb3";
		exportArray.push(entry);
	}
}

function chooseDisplay(click_id) 
{
    var searchElements = document.getElementsByClassName("tabPage");
	for(var i=0; i<searchElements.length; i++) 
	{	
		//checks to see if tab open matches elements open
		if(searchElements[i].classList.contains(click_id))
		{
			searchElements[i].style.display = "block";
		}
		else
		{
			searchElements[i].style.display = "none";
		}
	}
	
}