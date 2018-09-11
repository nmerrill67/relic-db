from os.path import exists
import sys,os
from pathlib import Path

# Seems simple but this allows us to change how files are accessed without changing the apps source code
class ExamFolder:

    path = Path(__file__).parents[2].joinpath(Path("exams/"))

    def getFileLoc(self,filename):

        p = str(self.path.joinpath(Path(filename+".cpe")))

        if not exists(p):
            file = open(p,"w")
            file.close()

        return p

    def getAllExams(self,extensions=True):

        directories = os.listdir(str(self.path))

        if extensions == False:
            for i in range(len(directories)):
                directories[i] = directories[i][:-4]
            
        return directories