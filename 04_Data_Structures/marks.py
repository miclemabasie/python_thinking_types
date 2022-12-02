"""
Dictionary:
-----------

Louis has given his exams and received marks. Let's check
out how did he fare.

Dictionary makes it easy to have a key-value pairs.

Info:
-----
LookUps are very fast!!!
All immutable datatypes can be used as keys for dictionaries
"""

marks: dict[str, int] = {
    'Maths': 80,
    'Science': 85,
    'History': 75,
    'Python': 90,
    'English': 30,
    'Physics': 76,
}

# ------------------------------------------------------------
# Louis wants to check out all the subjects (keys)
# ------------------------------------------------------------


for subject in marks.keys():
    print(subject)

# ------------------------------------------------------------
# Louis wnat to check out all the marks (Values)
# ------------------------------------------------------------

# for value in marks.values():
#     print(value)

# ------------------------------------------------------------
# Louis wants to know the exact mark for each subject (key-value)
# ------------------------------------------------------------

# for subject, mark in marks.items():
#     print(f"The value for {subject} is {mark}/100")

# ----------------------------------------------------------------------------------------
# Louis want to check if he made it in all of the subjects and the passing marks is 50/100
# ----------------------------------------------------------------------------------------


def check_if_passed_in_all_subjects(marks):
    passed_subjects = []
    subjects = []
    for subject, mark in marks.items():
        subjects.append(subject)
        # check if the mark is less than 50.
        if mark < 50:
            print(f"{subject}: Failed")
        else:
            passed_subjects.append(subject)
            print(f"{subject}: PASS")

    if len(subjects) == len(passed_subjects):
        print("Louis passed all his subjects.!!")


check_if_passed_in_all_subjects(marks)

# ----------------------------------------------------------------------------------------
# Louis requests revauation of his English paper, there was a totalling mistake adn right
# marks are 70
# ----------------------------------------------------------------------------------------

marks['English'] = 70
print(f"Louis marks of Englise are now {marks['English']}")

# ----------------------------------------------------------------------------------------
# Louis also took a Geography exam and he scored 78
# ----------------------------------------------------------------------------------------

marks['Geography'] = 78
print(f"Louis marks of Geography are now {marks['Geography']}")
# ----------------------------------------------------------------------------------------
# Louis wants to check if he made in all the subjects or not
# ----------------------------------------------------------------------------------------

check_if_passed_in_all_subjects(marks)

# ----------------------------------------------------------------------------------------
# Friends on Zortan wants to know how much Louis scored in Python
# ----------------------------------------------------------------------------------------

# Alternative 1
# -------------

print(f"Python marks are: {marks['Python']}")

# Alternative 2
# -------------

python_score = marks.get('Python')
print(f"Louis score {python_score} in Python.")

# ----------------------------------------------------------------------------------------
# Friends from earth want to know how many Louis scored in Java
# ----------------------------------------------------------------------------------------

# Alternative 1 - Will through an Error
# -------------------------------------
try:
    java_score = marks['Java']
    print(f"Louis scored {java_score} in Java")
except KeyError:
    print("Error: Could not find any subject called Java")

# Alternative 2 preffered approach
# -------------------------------------
java_score = marks.get('Java')
if java_score is None:
    print(f"Louis Does not study Java")
else:
    print(f"Louis scored {java_score} in Java")

# ----------------------------------------------------------------------------------------
# Deleting an element from dictionary
# ----------------------------------------------------------------------------------------

del marks['English']

check_if_passed_in_all_subjects(marks)
