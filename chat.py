# Software Engineering Final Project
# Classroom Base Note Collaborating P2P System
# Ian Lam (iil209)
# Runxi Bai (rb4287)

# start of the application

from users import User, Professor, Administrator
from course import Course

class SystemInfo:
    users_info = {
    "alice": {"role": "student", "course": {"DB", "FA"}},
    "bob": {"role": "student", "course": {"DB", "FA"}},
    "charlie": {"role": "student", "course": {"DB", "OS"}},
    "david": {"role": "student", "course": {"DB", "SE"}},
    "erin": {"role": "student", "course": {"OS", "SE"}},
    "ian": {"role": "student", "course": {"OS", "FA"}},
    "vicky": {"role": "student", "course": {"OS", "SE"}},
    "judy": {"role": "professor", "course": {"DB"}},
    "frank": {"role": "professor", "course": {"FA"}},
    "kelly": {"role": "professor", "course": {"OS"}},
    "jen": {"role": "professor", "course": {"SE"}},
    "victor": {"role": "admin", "course": {}},
    "wendy": {"role": "admin", "course": {}}
    }

    course_info = {
    "SE": 5000,
    "FA": 5001,
    "DB": 5002,
    "OS": 5003
    }

class NotetakingApp:
    def login(self):
        username = input("What is your name? ")
        if username.lower() not in SystemInfo.users_info:
            print("You are not part of the system. Contact the admin.")
            sys.exit(0)

        else:
            if SystemInfo.users_info[username]["role"] == "student":
                course = input("What course is this for? ").upper()
                if course not in SystemInfo.users_info[username]["course"]:
                    print("You are not enrolled in this course.")
                    sys.exit(0)
                else:
                    join_this_course = Course(course, SystemInfo.course_info[course])
                    student = User(username, join_this_course)
                    student.startCollab(join_this_course)

            elif SystemInfo.users_info[username]["role"] == "professor":
                course = input("What course are you here for? ").upper()
                if course not in SystemInfo.users_info[username]["course"]:
                    print("You are not teaching this course.")
                    sys.exit(0)
                else:
                    join_this_course = Course(course, SystemInfo.course_info[course])
                    professor = Professor(username, join_this_course)
                    professor.uploadLectureOutline()
                    professor.startCollab(join_this_course)

            elif SystemInfo.users_info[username]["role"] == "admin":
                admin = Administrator(username)
                admin.maintainSystem()

def main():
    app = NotetakingApp()
    app.login()

if __name__ == '__main__':
    main()
