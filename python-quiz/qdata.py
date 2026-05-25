questions = (
    "How many parameters does a print statement have?",
    "Which functions returns the ASCII number associated with a char?",
    "What does the method dict.keys() return?",
    "What is the  difference between a list and a tuple?",
    "What is the full form of json?",
    "What does the function json.dumps() does?",
    "What does the function json.loads() does?",
    "In a dictionary, what does (dict_name['key']) this syntax return?",
    "Methods and functions are the same.",
    "What type of datatype does the input() function return?",
)

answers = (
    "3",
    "ord()",
    "view object",
    "A list can be modified but a tuple cannot be modified",
    "Javascript Object Notation",
    "Converts dictionary to a str",
    "Converts str to a dictionary",
    "Returns the value associated with the given key",
    "False",
    "str",
)

qna = {}
for i in range(len(questions)):
    qna[questions[i]] = answers[i]

options = [
    ["1", "2", "3", "4"],
    ["list()", "chr()", "ord()", "int()"],
    ["tuple of keys", "list of keys", "view object", "object"],
    ["They are both the same", "A list can be modified but a tuple cannot be modified", "A tuple can be modified but a list cannot be modified", "We can access an element in lists but not in tuples"],
    ["Java Subject Object Notes", "Javascript Object Notation", "Jackle and Son Oxygen Needs", "Java SON"],
    ["Closes the file", "Converts str to a dictionary", "Converts dictionary to a str", "Clears the file"],
    ["Creates a new file", "Converts dictionary to a str", "Converts str to a dictionary", "Opens the file"],
    ["Returns the key", "Returns the value associated with the given key", "Returns all the keys", "Returns the dictionary name"],
    ["True", "False", "Both True and False", "None of the above"],
    ["float", "integer", "character", "str"]
]

markers = ["A", "B", "C", "D"]
