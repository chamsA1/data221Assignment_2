#problem 1
# def count_lines(filename):
#     count = 0
#     with open(filename) as file:
#         for line in file:
#             count += 1
#     return count
# print(count_lines("errors.txt"))








#problem 2


# def log_error(filename, message):
#     with open(filename, "a") as file:
#         file.write(message + "\n")
#
# log_error("errors.txt", "First error")
# log_error("errors.txt", "Second error")
# log_error("errors.txt", "Third error")



#problem 3
import csv
def read_student_data(csv_file):
    students = []
    with open(csv_file,"r",newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            students.append(row)

    return students

data = read_student_data("random.csv")

print(data)






