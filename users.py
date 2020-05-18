# Software Engineering Final Project
# Classroom Base Note Collaborating P2P System
# Ian Lam (iil209)
# Runxi Bai (rb4287)

import sys
from server import Server
from client import Client, P2P
from db_firestore import addOutline
from course import Course
from note import Note
import time
from random import randint

class User:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.note = Note(course)

    def startCollab(self, course):

        while True:
            try:
                print("Trying to connect...")
                time.sleep(randint(1, 5))
                for peer in P2P.peers:
                    try:
                        client = Client(self.name, peer, course, self.note)

                    except KeyboardInterrupt:
                        sys.exit(0)
                    except:
                        pass

                    try:
                        server = Server(self.name, course, self.note)

                    except KeyboardInterrupt:
                        sys.exit(0)
                    except:
                        print("Couldn't start the server...")
            except KeyboardInterrupt:
                # break
                sys.exit(0)

# Professor extends from User
class Professor(User):
    def __init__(self, name, course):
        super().__init__(name, course)

    def uploadLectureOutline(self):
        filepath = input("What is the filename for the lecture outline? ")
        if len(filepath) > 0:
            with open(filepath, "r") as f:
                outline = f.read()
            f.close()
            print(outline)
            print("Uploading lecture outline to cloud database")
            addOutline(self.course.course_name, outline)

# Administrator doesn't get to collab notes
class Administrator:
    def __init__(self, name):
        self.name = name

    def maintainSystem(self):
        print("Make some changes to database")

    def addCourse(self, course, port):
        print("Adding course to database with Port " + port)

    def deleteCourse(self, course):
        print("Delete record from database")

    def updateCourse(self, course, port):
        print("Updating the course to Port " + port)
