from flask import render_template, request, jsonify, abort, send_from_directory
from run_server import app
from bson.objectid import ObjectId
import my_app.controllers.dataAccess as dataAccess
import my_app.controllers.reverse_indexing as reverse_indexing
import my_app.scripts.backup_extract as extract
import my_app.config.settings as settings
import my_app.scripts.create_exam as select
from os.path import join
import ast
@app.route("/home")
def mainPage():
    return render_template("searchBar.html")

# add param for different lti i.e. canvas, respondus etc
@app.route("/import")
def importQuestions():
    return dataAccess.importQuestions()

@app.route("/getTagsFromDB", methods = ["POST"])
def getTagsFromDB():
    if not request.json:
        abort(400)
    tag_level =  request.json.get("tag_level","")
    search_text = request.json.get("search_text","")
    tags = dataAccess.getTags(tag_level, search_text)
    return jsonify({'status': "success", "tags": tags})

@app.route("/question", methods= ["POST"])
def testQues():
            extract.extract_tar_file(settings.MOODLE_EXTRACTION_PATH + settings.MOODLE_EXTRACTION_NAME,
                             settings.MOODLE_EXTRACTION_PATH + "vpl")
            #result = dataAccess.get_Questions("VPL", "function", 1,[ObjectId('5b7056d29541f93030da381c')])
            dataAccess.tag_and_insert_q()
            return jsonify({'status': "success"})

@app.route("/questionsdisplayed", methods = ['POST'])
def retrieve_questions():
    if not request.json:
        abort(400)
    print(request.json)
    return jsonify(dataAccess.get_all_questions_with(request.json))

@app.route("/export_exam", methods = ['POST'])
def export_exam():
    #print(request.json)
    if not request.json:
        abort(400)
    #print(request.json['restrictions'])
    select.create_group_exams(request.json)
    #results = select.get_questions_with("vpl", "unit1", )
    #print(request.json['restrictions'])
    extract.make_tarfile(join(settings.MOODLE_EXTRACTION_PATH, "new-backup.mbz"),
                          join(settings.MOODLE_EXTRACTION_PATH, "vpl"))

    return jsonify({'status': "success"})

@app.route("/return-files/")
def return_files():
    return send_from_directory(settings.MOODLE_EXTRACTION_PATH,"new-backup.mbz",as_attachment = True)

def setup_logging(logging_path, level):
    '''Setups logging in app'''
    from logging.handlers import RotatingFileHandler
    from logging import getLogger, getLevelName
    file_handler = RotatingFileHandler(logging_path)
    file_handler.setLevel(getLevelName(level))
    loggers = [app.logger]
    for logger in loggers:
        logger.addHandler(file_handler)
