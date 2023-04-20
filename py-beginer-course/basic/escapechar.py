# (splitting new line) backslash- \n :-
splitString = " string \n splitting \n in several \n lines"
print(splitString)
# (space tab line) backslash- \t :-
tabbedString = "1\t2\t3\t4"
print(tabbedString)
# e.g- single string in a \single string\ is escaped :-
print('The pet shop owner said "No, no, \'lucy\'s uh,....she\'s resting".')
# or- double string in a \double string\ is  escaped:-
print("The pet shop owner said \"No, no , 'lucy's uh,....she's resting\".")
# """ No need to escape in triple strings""" :-
print("""The pet shop owner said "No, no , 'lucy's uh,....she's resting" .""")
anotherSplitString = """This string is 
splitting over 
several
lines"""
print(anotherSplitString)
# escaping end of a line by \ :-
anotherSplitString = """This string is \
splitting over \
several \
lines """
print(anotherSplitString)
# escaping \single  with \\ double slash ..will take as 1 row, prefer 1.
print("C:\\ Users\\Manisha\\notes.txt")
# r for row - escaping \ with \\.
print(r"C:\\ Users\\Manisha\\notes.txt")
