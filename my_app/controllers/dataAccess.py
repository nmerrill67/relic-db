
import json
from ..config import settings
from os.path import join
from ..scripts import scripts
from flask import render_template
import xmltodict
import pprint
from io import open
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
import sys
from tkinter import filedialog
from tkinter import *
import os, ast
import my_app.config.settings as settings
import xml.etree.ElementTree as ET

def importQuestions():
    raise Exception("TODO Not fully implemented")
    """
    client = MongoClient('localhost', 27017)
    db = client['relic']
    questions = db['questions']
    # user selects file from gui
    # root = Tk()
    # root.filename = filedialog.askopenfilename(initialdir="/", title="Select file")
    xmlLoc = ""
    with open(xmlLoc, encoding='UTF-8') as fd:
        doc = xmltodict.parse(fd.read())
        jsonDoc = json_util.loads(json.dumps(doc))
    # for canvas qti only
    itemsArray = jsonDoc['questestinterop']['assessment']['section']['section'][0]['item']
    for doc in itemsArray:
        questions.insert(doc)

        # questions.insert(newDoc)
    client.close()
    print("imported stuff")
    """

def getTags(tag_level, search_text):
   #tag_level is either units, unit_slos, skills, skill_slos
   #search_text is the user's response (e.g. "the") Need to return all units/sklls/etc with "the" inside.
    """
    client = MongoClient('localhost', 27017)
    db = client['relic']
    tags = db['tags']
    select = request.args.get('tagFilter')
    # have to change 'function' to whatever the first entry for that tag is
    tagData = tags.find({select :{'$exists' :True}})
    for items in tagData:
        tagList = items[select]
    return jsonify(result = tagList)
    """
    data = {'units': [{'skills': [{'skill_name': 'algorithms', 'skill_slos': ['write algorithm for solving simple mathematical problems', 'understand the difference between an algorithm and a program']}, {'skill_name': 'variables', 'skill_slos': ['identify invalid variable names', 'choose meaningful variable names']}, {'skill_name': 'data types - float, int, string', 'skill_slos': ['use type() to determine variable names', 'use int(), float(), string() to case', 'recognize data types without type() function']}, {'skill_name': 'operators +,-,*,/,**,//,%', 'skill_slos': ['evaluate expressions containing these operators', 'understand the difference between floating point and integer division', 'convert a mathematical formula into a Python expression']}, {'skill_name': 'statements', 'skill_slos': ['assign a value to a variable', "'=' - understand assignment vs mathematical equals", 'determine the value of variables after sequence of assignment statements']}, {'skill_name': 'input function', 'skill_slos': ['use input statement to retrieve float, int, string values from keyboard']}, {'skill_name': 'print function', 'skill_slos': ['use print statements to display to user and debug/observe output']}], 'topics': ['OperatorsVariablesAssignment StatementsExpressionsData Types float, int, string (+,*)print function - including use for debugginginput functioninterpretting error messages: division by zero, data type mismatch, name errorDebuggingComments - How and When to Use them'], 'unit_SLO': 'Write a program that asks a user to enter the radius of a circle and computes and displays the area of the circle to the screen.', 'unit_name': 'Simple Python Data'}, {'skills': [{'skill_name': 'modules/libraries (math)', 'skill_slos': ['call functions from other modules', 'use help function', 'find existing Python libraries']}, {'skill_name': 'random module', 'skill_slos': ['use random module functions to generate random values']}, {'skill_name': 'build-in functions', 'skill_slos': ['call functions from Python Standard Library']}, {'skill_name': 'anatomy of function - header, parameters, body, return', 'skill_slos': ['identify parts of a function']}, {'skill_name': 'design recipe', 'skill_slos': ['use design receipe to develop functions and programs']}, {'skill_name': 'docstring', 'skill_slos': ['know what the docstring is used for', 'know how to write/read a docstring', 'write a function using a docstring']}, {'skill_name': 'testing', 'skill_slos': ['use asserts to test functions']}, {'skill_name': 'program composition', 'skill_slos': ['develop programs using functions']}, {'skill_name': 'scope', 'skill_slos': ['develop programs using functions']}, {'skill_name': 'flow of execution', 'skill_slos': ['trace the flow of execution of a program containing functions']}, {'skill_name': 'print vs return', 'skill_slos': ['know the difference between printing a value within a function and returning a value from a function']}], 'topics': ['Using Functions - modules/libraries', 'User Defined Functions', 'Design Recipe', 'Returning multiple arguments from functions', 'Modularity, program composition', 'Debugging functions', 'Interpretting error messages: name error, type error'], 'unit_SLO': 'Script/Program is solely comprised of user-defined functions and may call functions from libraries/modules as needed to solve the problem.', 'unit_name': 'Functions'}, {'skills': [{'skill_name': 'while loop', 'skill_slos': ['understand when to use a while loop vs a selection statement', 'trace the flow of execution', 'understand difference between indefinite and definite loops', 'use a loop to solve a problem', 'write a flowchart representing while loop problem']}, {'skill_name': 'while loop - validating input', 'skill_slos': ['recall sentinel value', 'write a loop to check for valid input']}, {'skill_name': 'while loop - accumulation', 'skill_slos': ['solve a problem requiring an interative solution', 'recall accumulation pattern']}, {'skill_name': 'indefinite loops', 'skill_slos': ['recall definition of infinite loop', 'identify/correct conditional expression to avoid infinite loop']}, {'skill_name': 'multiple return values from functions', 'skill_slos': ['write a function that returns multiple return values', 'call a function that returns multiple return values and assign the return values to variables']}], 'topics': ['While loops - (flow charts)', 'Accumulatoin - (flow charts)', 'Debugging loops and loop conditions', 'Interpretting error messages'], 'unit_SLO': 'SLO2+Program includes conditional and repetitive execution flows', 'unit_name': 'Iteration'}, {'skills': [{'skill_name': 'boolean values and expressions', 'skill_slos': ["understand the difference between string iteral 'True' 'False' and boolean values True False"]}, {'skill_name': 'equality operators ==,!=', 'skill_slos': ["understand the difference between '=' and '=='", "understand danger of using '==' with float values"]}, {'skill_name': 'relational operators <,<=,>,>=', 'skill_slos': ['evaluate boolean expressions']}, {'skill_name': 'logical operators and, or, not', 'skill_slos': ['evaluate boolean expressions containing logical operators', 'write boolean expressions using equality, relational, logical operators', "be able to show that 'not (A and B)' is equivalent to 'not A or not B' and NOT equivalent to 'not A and not B'"]}, {'skill_name': 'unary selection (if)', 'skill_slos': ['trace the flow of execution of an if statement', 'write if statements']}, {'skill_name': 'binary selection (if - else)', 'skill_slos': ['trace the flow of execution of an if-else statement', 'write if statements']}, {'skill_name': 'chained conditionals (if - elif)', 'skill_slos': ['trace the flow of execution of chained conditionals', 'write chained conditionals']}], 'topics': ['Branching (flowcharts)', 'Boolean', 'Logical Operators', 'Debugging selection statements and boolean expressions', 'Interpretting error messages'], 'unit_SLO': 'SLO2+Program includes conditional and repetitive execution flows', 'unit_name': 'Selection'}, {'skills': [{'skill_name': 'list data type', 'skill_slos': ['understand definition of sequential/collection data type', 'understand elements can be different data types, including lists', 'create lists including empty list (syntax for a list)']}, {'skill_name': 'len function', 'skill_slos': ['use len function to return TOPMOST length']}, {'skill_name': 'indexing', 'skill_slos': ['use indexing to access to elements in list including nested lists']}, {'skill_name': 'operators +,*', 'skill_slos': ['know operands must both be lists for list concatenation using +', 'evaluate expressions containing list concatenation using +', 'know one operand must be a list and the other an int for list repetition using *', 'evaluate expressions containing list repetition']}, {'skill_name': 'slicing', 'skill_slos': ['know how to use slicing']}, {'skill_name': 'mutability', 'skill_slos': ['understand definition - mutable']}, {'skill_name': 'del operator', 'skill_slos': ['evaluate and write expressions using hte del operator with lists']}, {'skill_name': 'in operator (not in)', 'skill_slos': ['evaluate and write expressions using del operator with lists', 'understand in operator evaluates only TOPMOST list level']}, {'skill_name': 'aliasing vs cloning', 'skill_slos': ['understand reference diagram for list objects', 'identify statement/syntax that create an alias to a list', 'identify statement/syntax that create a clone of a list', 'understand the difference between an alias and a clone', "evaluate expressions using the 'is' operator"]}, {'skill_name': 'built-in-list methods cover at least append and encourage students to look up other methods for their own use', 'skill_slos': ['call and evaluate expressions using list methods']}, {'skill_name': 'iterate through elements to a list - this is where the for loop discussion could go', 'skill_slos': ['write code using while loops to iterate and process elements of a list', 'write code using for each loops to iterate a process elements of a list', 'write code using indexes with range() function to iterate and process elements of a list using']}, {'skill_name': 'iterate using recursion', 'skill_slos': ['identify recursive components of recursive functions (base case, recursive case)', 'determining the relationship between the first element of a list with the rest of the list']}, {'skill_name': 'lists as parameters', 'skill_slos': ['how lists are passed to functions', 'understand difference between function with side effects and pure functions', 'trace execution of functions that accept and/or return lists']}, {'skill_name': 'list as return value', 'skill_slos': ['create a list within a function and the return list']}, {'skill_name': 'tuples', 'skill_slos': ['create tuples (syntax for a list)', 'use an assignment statement to unpack a tuple']}, {'skill_name': 'tuple - immutable', 'skill_slos': ['understand how immutability affects tuples']}, {'skill_name': 'tuple as parameters and returns', 'skill_slos': ['define functions using tuples as parameters and return value']}, {'skill_name': 'string data type', 'skill_slos': ['recall string is a sequential/collection data type']}, {'skill_name': 'len function', 'skill_slos': ['use use len function to return string length']}, {'skill_name': 'indexing with strings', 'skill_slos': ['use indexing to access characters in a string']}, {'skill_name': 'string operators +,*', 'skill_slos': ['know operands must both be strings for string concenation using +', 'evaluate expressions containing string concatenation', 'know one operand must be a string and the other an int for string repetition using *', 'evaluate expressions containing string repetition']}, {'skill_name': 'string slicing', 'skill_slos': ['know how to use slicing']}, {'skill_name': 'string - immutability', 'skill_slos': ['understand how immutability affects strings']}, {'skill_name': 'ASCII', 'skill_slos': ['']}, {'skill_name': 'string comparison', 'skill_slos': ['']}], 'topics': ['Lists', 'Tuples', 'Strings'], 'unit_SLO': 'SLO3+organize data into appropriate data structures so that it can be effectively accessed and worked with to solve a problem.', 'unit_name': 'Iterables'}, {'skills': '', 'topics': 'File Processing - readline only', 'unit_SLO': '', 'unit_name': 'File I/O'}, {'skills': '', 'topics': ['Plotting (taught as part of lab/project and not in lecture)', 'Project #2 Discussion'], 'unit_SLO': 'using visual representation of data to aid in analysis of data', 'unit_name': 'Project #2 Discussion'}, {'skills': '', 'topics': 'Classes - structs/methods', 'unit_SLO': '', 'unit_name': 'Classes/Objects'}, {'skills': '', 'topics': 'MATALB & Project 3 Discussion', 'unit_SLO': '', 'unit_name': 'MATLAB'}, {'skills': '', 'topics': ['Searching/sorting/recursion', 'Algorithm analysis'], 'unit_SLO': '', 'unit_name': 'Searching/sorting/algorithm analysis'}]}


    #replace with call from db
    #data =  {"units":[{"unit_name":"Simple Python Data","unit_SLO":"Write a script/program that asks a user for input values from the keyboard, performs a mathematical computation and displays the result to the screen.","topics":["operators","variables"],"skills":[{"skill_name":"algorithms","skill_slos":["write algorithm for solving simple mathematical problems","understand the difference between an algorithm and a program"]},{"skill_name":"operators","skill_slos":["evaluate expressions containing these operators","understand the difference between floating point and integer division","convert a mathematical formula into a Python expression"]}]}]}
    if tag_level == "units":
       results = [unit.get("unit_name","") for unit in data.get("units", []) ]
    elif tag_level == "unit_slos":
       results= [unit.get("unit_SLO", "") for unit in data.get("units", [])]
    elif tag_level == "skills":
       results= [skill.get("skill_name", "") for unit in data.get("units", []) for skill in unit.get("skills", {})]
    elif tag_level == "skill_slos":
       results = []
       for unit in data.get("units", []):
          for skill in unit.get("skills", []):
             for skill_slo in skill.get("skill_slos", []):
                results.append(skill_slo)
    else:
       results = ["Error"]
    return list(filter(lambda text: search_text.lower() in text.lower(), results))

def get_all_questions_with(restrictions):
    exam_questions = []  # will be a list of lists
    #print(restrictions)
    result_dict = restrictions

    exam_type = result_dict["type"]

    tags = result_dict["tags"]

    client = MongoClient('localhost', 27017)
    db = client['relic']
    questions = db['questions']


    excluded_ids = []
    for index, tag in enumerate(tags):
        list_of_questions = []
        #TODO NEED TO INCLUDE exam_type when searching to have VPL or canvas questions returned.
        db_questions = questions.find(
            {'tags': {'tag': tag["tag"]}, 'difficulty': tag["difficulty"],'moduleid': {'$nin': excluded_ids}})
        for items in db_questions:
            title = items['activity']['vpl']['name']
            description = items['activity']['vpl']['intro']
            type = "vpl"
            difficulty = items['difficulty']
            tags = items['tags']
            moduleid = items['activity']['@moduleid']
            question_dict = {
                "title":title,
                "description":description,
                "type":type,
                "difficulty":difficulty,
                "tags":tags,
                "moduleid":moduleid
            }

            list_of_questions.append(question_dict)

        exam_questions_i = list_of_questions
        print(exam_questions_i)
        excluded_ids += [x["moduleid"] for x in exam_questions_i]
        exam_questions += exam_questions_i



    #print(exam_questions)
    return exam_questions


def get_Questions(type, tag, difficulty, excludeIDs):
    #type  = VPL or quiz
    #tag = list
    #difficulty = number
    #list of excluded ids
    client = MongoClient('localhost', 27017)
    db = client['relic']
    tags = db['tags']
    questions = db['questions']
    print("connected to db")
    results = ""
    return results

def tag_and_insert_q():
    client = MongoClient('localhost', 27017)
    db = client['relic']
    questions = db['questions']
    #change this to user input
    root = Tk()
    root.filename = join(settings.MOODLE_EXTRACTION_PATH ,"vpl","activities")
    xmlLoc = root.filename
    directory = root.filename
    for sub_folder in os.listdir(directory):
            vpl = join(settings.MOODLE_EXTRACTION_PATH,"vpl","activities",sub_folder, "vpl.xml")
            module = join(settings.MOODLE_EXTRACTION_PATH,"vpl","activities",sub_folder, "module.xml")

            tags = []
            difficulty = ""
            doc = {}

            with open(vpl, encoding='UTF-8') as fd:
                doc = xmltodict.parse(fd.read())

            tree = ET.parse(module)
            root = tree.getroot()

            for tag in root.findall('./tags/tag'):
                name = tag.find('name').text
                print("thi is our name " + name)
                if "difficulty-"in name:
                    difficulty = name
                else:
                    tags.append({"tag": name})
            doc.update({'tags': tags})
            doc.update({'difficulty': difficulty})

            questions.insert_one(doc)


    #xmlLoc = "C:\\Users\\OG AppleJacks\\Documents\\cisc106rework\\thisIsQti\\vpl.xml"
    #add script to parse mbz and load xml
    #with open(xmlLoc, encoding='UTF-8') as fd:
    #    doc = xmltodict.parse(fd.read())
    #format only for moodle vpl.xml
    title = doc['activity']['vpl']['name']
    description = doc['activity']['vpl']['intro']

    print("question inserted into db")





