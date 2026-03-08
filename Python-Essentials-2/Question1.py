class Student_Marks:
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            # This is to check if there are at least 3 marks
            if len(self.marks) < 3:
                raise Exception("Not enough marks to calculate average")

            # We are using Negative indexing to get last three marks
            last_three = self.marks[-3:]

            avg = sum(last_three) / 3
            print("Average of last 3 marks is:", avg)

        except Exception:
            print("Not enough marks to calculate average")


# Example usage take from the provided input in assignment 
marks_list = [50, 60, 70, 80, 90]

student = Student_Marks(marks_list)
student.last_three_avg()