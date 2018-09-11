"""
result = {
        "tags":[{"tag":"unit1", "num": 3, "difficulty": 1}, 
              {"tag":"for loops in matlab", "num": 2, "difficulty": 1}],    
        "type" : "vpl"
        }
"""
"""
The above JSON means the user needs an exam containing
3 unit1 questions of difficulty 1, and 2 questions tagged
with for loops in matlab of difficulty 1. The questions are 
for VPL based exam i.e. open-ended types

A dummy function that returns us questions for now would be
get_questions_with(tag_name, exam_type, difficulty, num_questions, excluded_ids=[])
"""

import pprint, json, ast
import my_app.scripts.backup_extract as BE
import my_app.scripts.parse_groups as PG
import my_app.scripts.write_groups as WG
import my_app.config.settings as settings
from os.path import join
from random import sample
from pymongo import MongoClient

#reduces a full list of questions to contain only
#a specified number of randomly selected questions
def randomize(questions, num):
    
    randomized_questions = sample(questions, min(num, len(questions)))
    
    return randomized_questions

#gets a set of questions for an exam
def get_questions_with(tag_name, exam_type, difficulty, num_questions, excluded_ids=[]):
    questions = []

    client = MongoClient('localhost', 27017)
    db = client['relic']
    questions = db['questions']
    list_of_questions = []
    # TODO NEED TO INCLUDE exam_type when searching to have VPL or canvas questions returned.
    db_questions = questions.find({'tags':{'tag':tag_name}, 'difficulty':difficulty, 'moduleid':{'$nin':excluded_ids}})
    for items in db_questions:
        list_of_questions.append(items)
    print(list_of_questions[0])
    '''
    big_list_of_questions = [{"id": (2), "question": ("this question" ) , "tags":{"tag":  ["unit1"]}, "difficulty" : 1},
                             {"id": (3), "question": ("this question" ) , "tags":{"tag":  ["unit2"]}, "difficulty" : 1},
                             {"id": (4), "question": ("this question" ) , "tags":{"tag":  ["for loops in matlab"]}, "difficulty" : 1},
                             {"id": (5), "question": ("this question" ) , "tags":{"tag":  ["unit1","for loops in matlab"]}, "difficulty" : 1},
                             {"id": (7), "question": ("this question" ) , "tags":{"tag":  ["for loops in matlab"]}, "difficulty" : 1},
                             {"id": (8), "question": ("this question" ) , "tags":{"tag":  ["unit1","for loops in matlab"]}, "difficulty" : 1},]
    '''
    
    #database queries should be below. I have assumed that the database returns
    #some specific number of questions which we then randomize to keep only 'n' questions
    '''
    if exam_type == "vpl":

        questions = list(filter(lambda x: x["id"] not in excluded_ids and tag_name in x["tags"]["tag"] and difficulty==x["difficulty"], big_list_of_questions))

    else:
        print("Non VPL questions unavailable for now!")
    '''
    randomized = randomize(list_of_questions, int(num_questions))
    
    return randomized

#creates a set of questions for an exam
def create_exam(result):
    
    exam_questions = [] #will be a list of lists
    
    result_dict = json.loads(result)
    
    exam_type = result_dict["type"]
    
    tags = result_dict["tags"]
    
    excluded_ids = []
    for index, tag in enumerate(tags):
        exam_questions_i = get_questions_with(tag["tag"], exam_type, tag["difficulty"], tag["num"], excluded_ids)
        excluded_ids += [x["activity"]["@moduleid"] for x in exam_questions_i]
        exam_questions += exam_questions_i
    
    print(excluded_ids)
    
    return exam_questions, excluded_ids

#print XML tags for group specification in module.xml file

def create_group_exams(result):
    
    #Checking the functions using the JSON representation
    #of a user request
    '''
    result = {
        "tags":[{"tag":"unit1", "num": 2, "difficulty": 1}, 
              {"tag":"for loops in matlab", "num": 1, "difficulty": 1}],    
        "type" : "vpl"
        }
    '''
    result_json = json.dumps(result)
    exams = []
    question_ids = []
    set_questions = set()
    question_groups = {}
    
    questions_to_groups = {}
    
    '''
    code for extracting grousp from MBZ file
    '''
    #extract the vpl course backup into a structured folder
    #BE.extract_tar_file("backup-moodle.mbz","vpl")
    BE.extract_tar_file(settings.MOODLE_EXTRACTION_PATH + settings.MOODLE_EXTRACTION_NAME,
                             settings.MOODLE_EXTRACTION_PATH + "vpl")
    groups_xml_file = join(settings.MOODLE_EXTRACTION_PATH, "vpl","groups.xml")
    
    group_list, staff = PG.get_groups(PG.get_root(groups_xml_file))
    
    
    #ranges from 1 to number of groups we want to have + 1. Here we want 6 groups
    for i in group_list:
        print("--Group"+str(i)+"--")
        exams_i, q_ids_i = create_exam(result_json)
        exams.append(exams_i)
        question_ids.append(q_ids_i)
        
        #creating a set of questions
        for items in q_ids_i:
            set_questions.add(items)
    
    print("\nUnique questions:"+str(set_questions)+"\n")
    
    #creating a list of groups associated with each question using list comprehension
    #basically the exam id is mapped to a group
    for items in list(set_questions):
        question_groups.update({items: ["{}".format(group_list[exam_id]) for exam_id,value1 in enumerate(question_ids) for position_id,value2 in enumerate(value1) if value2==items]})
    
    pprint.pprint(question_groups)
    WG.staff_tags(join(settings.MOODLE_EXTRACTION_PATH,'vpl','activities'), staff)
    WG.create_exam_group_tags(question_groups)
    

