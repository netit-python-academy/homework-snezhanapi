student_scores = {
  "Susan": [67, 84, 75, 63],
  "Mike": [87, 98, 64, 71],
  "Jim": [90, 58, 73, 86]
}
sum = 0
average = 0
max_average = 0
i = 0
try:
        for key, val in student_scores.items():
            for score in val:
                sum += score
                i +=1
            average = sum/i
            i = 0
            sum=0
            if average > max_average:
                max_average = average
                best_student = key
        print (best_student)
except ValueError:
    print("Invalid Input")
