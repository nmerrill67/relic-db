
function addRestriction(table, tagLevel, tagText, tagQuantity, tagDifficulty, isCreatingExamTemplate){
     //Create the restriction table row
    var row = table.insertRow(-1);
    var rowIndex = row.rowIndex;
    var tagQuantityCell = row.insertCell(0); //<label>quantity</label>
    var tagDifficultyCell = row.insertCell(1);//<label>quantity</label>
    var tagLevelCell = row.insertCell(2); //<label>units</label>
    var tagLevelCell = row.insertCell(3);
    var tagTextCell = row.insertCell(4); //<label>Introduction to Python</label>
    var removeButtonCell = row.insertCell(5); //<button id="removeTag" onclick="deleteTags(\'' + this.parent  +'\')" class="tabHover">Remove</button>
    /*
    if(!isCreatingExamTemplate){
        tagQuantityCell.style.visibility = "hidden";
    }
    else
    {
        tagQuantityCell.style.visibility = "block";
    }
    */
    var tagQuantityLabel = document.createElement("label");
    var tagQuantityLabelText = document.createTextNode( tagQuantity + " Questions with ");
    tagQuantityLabel.appendChild(tagQuantityLabelText);
    tagQuantityCell.appendChild(tagQuantityLabel);

    var tagDifficultyLabel = document.createElement("label");
    var tagDifficultyLabelText = document.createTextNode( "Level " + tagDifficulty + " Difficulty");
    tagDifficultyLabel.appendChild(tagDifficultyLabelText);
    tagDifficultyCell.appendChild(tagDifficultyLabel);

    var tagLevelLabel = document.createElement("label");
    var tagLevelLabelText = document.createTextNode("("+ tagLevel +")");
    tagLevelLabel.appendChild(tagLevelLabelText);
    tagLevelCell.appendChild(tagLevelLabel);

    var tagTextLabel = document.createElement("label");
    var tagTextLabelText = document.createTextNode(tagText);
    tagTextLabel.appendChild(tagTextLabelText);
    tagTextCell.appendChild(tagTextLabel);

    //the remove button for each row will removes  the restriction and the table row (itself)
    var removeButton = document.createElement("button");
    var removeButtonText = document.createTextNode("Remove");
    removeButton.appendChild(removeButtonText);
    removeButton.addEventListener('click', function(){
        var deletedRowIndex = this.parentNode.parentNode.rowIndex;//reference to row index needs to be computed on delete time.
        // it can't be stored on creation.
        if(isCreatingExamTemplate){
            restrictions.splice(deletedRowIndex,1); //remove model
        }
        else{
         questionRestrictions.splice(deletedRowIndex,1)
        }
        table.deleteRow(deletedRowIndex); //remove view
        $("#tagRequirements").hide().show(0);//refresh table view. refresh() isn't supported in all browsers.
        updateDisplayedQuestions();
    });
    removeButtonCell.appendChild(removeButton);

    if(isCreatingExamTemplate){
        restrictions[rowIndex] = {"tag":tagText, "num":tagQuantity, "difficulty":tagDifficulty}
    }
    else{
        questionRestrictions[rowIndex] = {"tag":tagText, "difficulty":tagDifficulty}
    }
};

function updateRestrictions(){
    var table = document.getElementById("tagRequirements");
    var tagLevel = $("#tagFilter").val();
    var tagText = $("#tagSearch").val();
    var tagQuantity = $("#tagQuantity").val()
    var tagDifficulty = $("#tagDifficulty").val()
    var isCreatingExamTemplate  = $("#searchFormat").val() == "examTemplate";

    if(tagText.length == 0 ){//just a simple user case check to not add empty strings
        alert("check tag description");
        return;
    }
    if(tagQuantity.length == 0 && isCreatingExamTemplate){
        alert("check quantity of questions");
        return;
    }
    if(tagDifficulty.length == 0){
        alert("check quantity of questions");
        return;
    }

     $("#tagSearch").val("");//reset text after submission. =)
     $("#tagQuantity").val("")
     $("#tagDifficulty").val("")

    addRestriction(table, tagLevel, tagText, tagQuantity, tagDifficulty, isCreatingExamTemplate);
    //add restriction

    updateDisplayedQuestions();
};

function updateDisplayedQuestions(){
    alert("matt");
     var isCreatingExamTemplate  = $("#searchFormat").val() == "examTemplate";
     if(!isCreatingExamTemplate){

         alert("hi");
          $.ajax({
          url: "/questionsdisplayed",
          type: "POST",
          data: JSON.stringify({"tags":questionRestrictions,
                                "type" : "vpl"}),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function(result) {
              //$("#tagSearch" ).autocomplete({source:result["tags"]});
                alert("updatingDisplayedQuestions");
              updateSearchedQuestions(result);

          },
          failure: function(errMsg) {
                    alert(errMsg);
                }
        });
     }
};

function updateTable(){

    $("#tagRequirements tr").remove();
    var table = document.getElementById("tagRequirements");
    var isCreatingExamTemplate  = $("#searchFormat").val() == "examTemplate";
    alert(isCreatingExamTemplate);
    alert($("#searchFormat").val());
    var data = questionRestrictions;
    if(isCreatingExamTemplate) {
        data = restrictions;
        $("#tagQuantity").show();
    }
    else
    {
        $("#tagQuantity").hide();
    }


    data.forEach(function(restriction){
        var tagQuantity = 0
        if(isCreatingExamTemplate){
            tagQuantity = restriction["num"]
        }
        addRestriction(table, restriction["tagLevel"], restriction["tag"], tagQuantity, restriction["difficulty"], isCreatingExamTemplate)
    });
};
function updatePossibilities(possibilities){
    var possibilitiesString = removeJSONStuff(JSON.stringify(possibilities, null, 5));
    $("#tagPossibilities").html(possibilitiesString);
};

function updateSearchedQuestions(questions){
    var questionsString = getQuestionJSONstring(questions)

    $("#searchedQuestions").html(questionsString);
    alert("hi");
    console.log("updating search");
    console.log(questionsString);
};

function getQuestionJSONstring(questions){
    var result = "";
    questions.forEach(function(question){
        result += "Title:" + question["title"] + "\n";
        result += "Description:" + question["description"] + "\n";
        result += "Difficulty:" + question["difficulty"] + "\n";
        result += "Type:" + question["type"] + "\n";
        result += "Tags:" + JSON.stringify(question["tags"], null, 0) + "\n";
        result += "\n";
    });
    return result;
}
function removeJSONStuff(aJSONString){//regex sucks too much =(
    aJSONString = aJSONString.split('"').join('')
    aJSONString = aJSONString.split('[').join('')
    aJSONString = aJSONString.split('],').join('')
    aJSONString = aJSONString.split(']').join('')
    aJSONString = aJSONString.split('{').join('')
    aJSONString = aJSONString.split('},').join('')
    aJSONString = aJSONString.split('}').join('')
    aJSONString = aJSONString.split(',').join('')
    return aJSONString
}
function exportTemplate(){
    $.ajax({
          url: "/export_exam",
          type: "POST",
          data: JSON.stringify({"tags":restrictions, "type":"vpl"}),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function(result) {
                //TODO dont do it this way, please fix below
                $('#downloadLink').attr('style', 'visibility:visible; display:block');
                $('#downloadLink').attr('href', result['path']);

          },
          failure: function(errMsg) {
                    alert(errMsg);
                }
        });

}

function importQuestionsIntoServer()
{
    $.ajax({
          url: "/question",
          type: "POST",
          success: function(result) {
                alert("imported questions");

          },
          failure: function(errMsg) {
                    alert(errMsg);
                }
        });
}