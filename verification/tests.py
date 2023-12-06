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
            "input": {'m2', 'm3', 'm4', 'm4', 'm4', 'm8', 'm8', 'm8', 'p4', 'p5', 'p6', 's5', 's6', 's7'},
            "answer": {'m234', 'm44', 'm888', 'p456', 's567'}
            "explanation": "tanyao yaku"
        },
        {
            "input": {'m3', 'm4', 'm5', 'p2', 'p2', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9'},
            "answer": {'m345', 'p22', 's123', 's456', 's789'}
            "explanation": "izzu yaku"
        },
        {
            "input": {'m1', 'm2', 'm3', 'm9', 'm9', 's7', 's8', 's9', 'ws', 'ws', 'ws', 'dr', 'dr', 'dr'},
            "answer": {'m123', 'm99', 's789', 'wss', 'drrr'}
            "explanation": "chanta yaku"
        }
    ],
    "Extra": [
        {
            "input": {'m1', 'm1', 'p2', 'p2', 'p3', 'p3', 'p4', 'p4', 's4', 's5', 's6', 's6', 's7', 's8'},
            "answer": {'m11', 'm234', 'm234', 's456', 's678'}
            "explanation": "iipeyko yaku"
        },
        {
            "input": {'m1', 'm2', 'm3', 'm9', 'm9', 's2', 's2', 's2', 's5', 's6', 's7', 'dg', 'dg', 'dg'},
            "answer": {'m123', 'm99', 's222', 's567', 'dggg'}
            "explanation": "yakuhay yaku"
        },
        {
            "input": {'m7', 'm8', 'm9', 'p7', 'p8', 'p9', 's2', 's3', 's4', 's7', 's8', 's9', 'we', 'we'},
            "answer": {'m789', 'p789', 's234', 's789', 'wee'}
            "explanation": "sanshoku dochzun yaku"
        },
        {
            "input": {'', '', '', '', '', '', '', '', '', '', '', '', '', ''},
            "answer": {'m11', 'm444', 'p444', 's444', 's456'}
            "explanation": "sanshoku doko yaku"
        },
        {
            "input": {'', '', '', '', '', '', '', '', '', '', '', '', '', ''},
            "answer": {'p111', 'p555', 's888', 's999', 'wss'}
            "explanation": "toy-toy yaku"
        },
        {
            "input": {'', '', '', '', '', '', '', '', '', '', '', '', '', ''},
            "answer": {'m234', 'wee', 'drrr', 'dwww', 'dggg'}
            "explanation": "daysangen yakuman"
        }
    ]
}
