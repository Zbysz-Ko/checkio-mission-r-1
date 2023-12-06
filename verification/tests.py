"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": {'m7', 'm8', 'm9', 'p2', 'p3', 'p4', 's3', 's4', 's5', 's5', 's6', 's7', 'wn', 'wn'},
            "answer": {'m789', 'p234', 's345', 's567', 'wnn'}
            "explanation": "pinfu yaku"
        },
        {
            "input": {'', '', '', '', '', '', '', '', '', '', '', '', '', ''},
            "answer": {'', '', '', '', ''}
            "explanation": "yaku"
        }
    ],
    "Extra": [
        {
            "input": {'', '', '', '', '', '', '', '', '', '', '', '', '', ''},
            "answer": {'', '', '', '', ''}
            "explanation": "yaku"
        },
        {
            "input": {'', '', '', '', '', '', '', '', '', '', '', '', '', ''},
            "answer": {'', '', '', '', ''}
            "explanation": "yaku"
        }
    ]
}
