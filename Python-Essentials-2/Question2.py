class StudentScores:
    def __init__(self, scores):
        # This gives us the list of the scores provided while creating the object
        self.scores = scores

    def highest_last_two(self):
        try:
            # To check if there are at least 2 scores
            if len(self.scores) < 2:
                raise ValueError

            # This is Used for negative indexing to get last two scores
            last_two = self.scores[-2:]

            # For finding the highest score
            highest = max(last_two)

            print("Highest score among the last two:", highest)

        except:
            print("Not enough scores to find the highest value")


# List scores taken from the provided input in the question given 
scores_list = [45, 67, 89, 72]

student = StudentScores(scores_list)

# Calling the method as mentioned
student.highest_last_two()