import json


class myDatabase:
    def __init__(self):
        self.users = json.loads(open("./data/user.json", "r", encoding="utf-8").read())
        self.student_grade = json.loads(open("./data/student_grade.json", "r", encoding="utf-8").read())

    def check_login(self, username, password):
        """Check username and password in Login Page"""
        for user in self.users:
            if user["username"] == username:
                if user["password"] == password:
                    return True, "Login successful"
                else:
                    return False, "Login failed. Password is incorrect"
        return False, "Login failed. Username doesn't exist"

    def student_grade_list(self):
        """Return all student grade"""
        return self.student_grade

    def insert_student(self, student):
        """Insert student into database and file"""
        if self.check_student_name(student["name"]):
            return False, "Student already exists \n Submit failed"
        else:
            self.student_grade.append(student)
            with open("../data/student_grade.json", "w", encoding="utf-8") as f:
                json.dump(self.student_grade, f, indent=4)
            return True, "submitted successfully"

    def check_student_name(self, name):
        """Check student name in database"""
        for student in self.student_grade:
            if student["name"].lower() == name.lower():
                return True
        return False

    def delete_by_name(self, name):
        """Delete student by name"""
        for student in self.student_grade:
            if student["name"].lower() == name.lower():
                self.student_grade.remove(student)
                with open("../data/student_grade.json", "w", encoding="utf-8") as f:
                    json.dump(self.student_grade, f, indent=4)
                return True, "deleted successfully"
        return False, f'The student "{name}" doesn\'t exist in database'

    def search_by_name(self, name):
        """Search student by name"""
        for student in self.student_grade:
            if student["name"].lower() == name.lower():
                return True, student
        return False, f'The student "{name}" doesn\'t exist in database'

    def update_by_name(self, student_info):
        """Update student by name"""
        for student in self.student_grade:
            if student["name"].lower() == student_info["name"].lower():
                student.update(student_info)
            with open("../data/student_grade.json", "w", encoding="utf-8") as f:
                json.dump(self.student_grade, f, indent=4)
            return True, "updated successfully"
        return False, f'The student "{student_info["name"]}" doesn\'t exist in database'


db = myDatabase()

if __name__ == "__main__":
    print(db.check_login("admin", "admin1"))
    print(db.student_grade())
