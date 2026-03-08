class StudentPerformance:
    def __init__(self, scores):
        # List of the csores when object is created
        self.scores = scores

    def score_difference(self):
        try:
            # If the list is empty raise an exception
            if len(self.scores) == 0:
                raise ValueError
            # Difference bewtween last score and first score
            diff = self.scores[-1] - self.scores[0]
            print("The difference between the last and first score is:",diff)
        except:
            print("No scores available to calculate difference")

#Creating list of scores
scores_list = [55, 65, 75, 85]
student = StudentPerformance(scores_list)
student.score_difference()