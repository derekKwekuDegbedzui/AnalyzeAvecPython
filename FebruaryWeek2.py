## 2025 February Week 2

# Sunday February 09, 2025
# Pushing from local repository to Git automatically

## Python Basics
# https://youtube.com/playlist?list=PL30AETbxgR-cvGNPAWsocLfEnlCK3c6Pw&si=FOniZ4SdOSv5bmBn
# using dir to get applicable functions
curString = 'Mawunyo'
print(dir(curString))

curAge = 18
print(dir(curAge))

curList = [curAge, curString]
print(dir(curList))

## Monday, February 10, 2025.
# Preferred Installer Program
# pip --version
# pip install
# pip list
# pip uninstall

# x = 5
try:
    print(x)
except NameError:
    print('Error')
else:
    print('No Error Detected')
finally:
    print('Always executed')

## OOP


class Student:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f'{first.lower()}.{last.lower()}@mail.com'

    def initials(self):
        """A method within the class Student"""
        first_initial = self.first[0]
        last_initial = self.last[0]
        return f"{first_initial} {last_initial}"


cur_student = Student('Bob', 'Griffin')

print(cur_student.email)
print(cur_student.initials())
