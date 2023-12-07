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
            "input": ['m7', 's6', 'p2', 'm9', 's5', 'wn', 's3', 'p4', 's4', 'p3', 's5', 'm8', 's7', 'wn'],
            "answer": ['m789', 'p234', 's345', 's567', 'wnn'],
            "explanation": "pinfu yaku"
        },
        {
            "input": ['s7', 'p4', 's6', 'm8', 'm4', 'm3', 'm8', 'm8', 'm2', 'p6', 'm4', 's5', 'p5', 'm4'],
            "answer": ['m234', 'm44', 'm888', 'p456', 's567'],
            "explanation": "tanyao yaku"
        },
        {
            "input": ['s8', 's7', 'p2', 's4', 's9', 's3', 's5', 's1', 's6', 'm5', 's2', 'p2', 'm3', 'm4'],
            "answer": ['m345', 'p22', 's123', 's456', 's789'],
            "explanation": "izzu yaku"
        },
        {
            "input": ['s8', 's9', 'm1', 'ws', 'dr', 's7', 'dr', 'm9', 'ws', 'm9', 'm2', 'dr', 'm3', 'ws'],
            "answer": ['m123', 'm99', 's789', 'wss', 'drrr'],
            "explanation": "chanta yaku"
        }
    ]
}
