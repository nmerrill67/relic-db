from os.path import join, dirname, realpath, pardir

APP_NAME = 'my_app'

DEBUG = True

# Paths
ROOT_DIR = realpath(join(join(dirname(__file__), pardir), pardir))
DATA_DIR = join(ROOT_DIR, 'data')
STATIC_FOLDER = join(ROOT_DIR, APP_NAME, 'static')
TEMPLATE_FOLDER = join(ROOT_DIR, APP_NAME, 'templates')

# Logging
LOGGING_PATH = join(ROOT_DIR, 'log.txt')
LOGGING_LEVEL = 'DEBUG'


#Moodle Extraction Path
MOODLE_EXTRACTION_PATH = "C:\\Users\\OG AppleJacks\\Documents\\cisc106rework\\thisIsQti\\"

#Moodle Extraction Name
MOODLE_EXTRACTION_NAME = "moodle-bu.mbz"

