"""
Tuple
-----
Time for Louis to go to school, and its time for him to
choose subjcts, School doesn't want students to change
subjects after they are chosen, so the use a Tuple.

Tuple is like a stricker brother of List. Once a Tuple is
created, it cannot be edited.

Info:
-----
Tuple also start from index 0.
"""
from typing import Final

subjects: tuple[str, str, str] = ("Math", "Science", "History")

# ---------------------------------------------------
# Louis wants to count his number of subjects
# ---------------------------------------------------

len_subjects = len(subjects)
print(f"Number of subjects: {len(subjects)}")


# ---------------------------------------------------
# Louis needs to sihnup for all the subjects
# ---------------------------------------------------

for subject in subjects:
    print(f"Louis is signing up for: {subject}")


# ---------------------------------------------------
# Louis want to check which is his second subject
# ---------------------------------------------------

print(subjects[1])

# ---------------------------------------------------
# LSchool wants Louis to take another 3 subjects to get full credits
# ---------------------------------------------------

# subject.append('Physics') # not possible

add_subject = ('English', "Physics", "Python",)
total_subjects = subjects + add_subject
print(f"All Subjects: {total_subjects}")


# ---------------------------------------------------
# Louis loves Python, and want to see if it's there in his subjects
# ---------------------------------------------------

if 'Python' in subjects:
    print("Yeahhh!! I've got python on my list of subjects")
else:
    print("Oh no, No python for Louis.")
