# Simple data logging tool. 

import random
import time

class Student:
    def __init__(self, fname, lname, graduation):
        self.lastname = lname
        self.firstname = fname
        self.grad = graduation

    def addata(self):
        with open("DATABASE.txt", "a") as db:
            db.write("\nSTUDENT ID: {}".format(self.student_id))
            db.write("\nFIRSTNAME: {}\n".format(self.firstname))
            db.write("LASTNAME: {}\n".format(self.lastname))
            db.write("D.O.B: {}\n".format(self.grad))

    def generate_id(self):
        with open("student_ids.txt", "a") as file:
            pass
        id = random.randrange(10000, 10000000)
        with open("student_ids.txt", "r") as id_read:
            id_file = id_read.readlines()
            for ids in id_file:
                if int(ids) == int(id):
                    print("\nFATAL ERROR: Please try again")
                    exit()
                else:
                    continue
            with open("student_ids.txt", "a") as id_write:
                id_write.write("{}\n".format(str(id)))
            self.student_id = id


if __name__ == "__main__":
    print("Data submission Panel - coolpancakes")
    name = input("\nNAME: ")
    lname = input("LAST NAME: ")
    date_of_birth = input("D.O.B: ")
    time.sleep(0.05)
    print("\nDATA SUBMITTED! ")

    student_data = Student(name, lname, date_of_birth)
    student_data.generate_id()
    student_data.addata()

