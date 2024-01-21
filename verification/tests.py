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
            "input": [['m7', 's6', 'p2', 'm9', 's5', 'wn', 's3', 'p4', 's4', 'p3', 's5', 'm8', 's7', 'wn']],
            "answer": ['m789', 'p234', 's345', 's567', 'wnn'],
            "explanation": "pinfu yaku"
        },
        {
            "input": [['s7', 'p4', 's6', 'm8', 'm4', 'm3', 'm8', 'm8', 'm2', 'p6', 'm4', 's5', 'p5', 'm4']],
            "answer": ['m234', 'm44', 'm888', 'p456', 's567'],
            "explanation": "tanyao yaku"
        },
        {
            "input": [['s8', 's7', 'p2', 's4', 's9', 's3', 's5', 's1', 's6', 'm5', 's2', 'p2', 'm3', 'm4']],
            "answer": ['m345', 'p22', 's123', 's456', 's789'],
            "explanation": "izzu yaku"
        },
        {
            "input": [['s8', 's9', 'm1', 'ws', 'dr', 's7', 'dr', 'm9', 'ws', 'm9', 'm2', 'dr', 'm3', 'ws']],
            "answer": ['drrr', 'm123', 'm99', 's789', 'wsss'],
            "explanation": "chanta yaku"
        }
    ],
"Extra": [
        {
            "input": [['p4', 's4', 's5', 'p3', 'm1', 's6', 's7', 's8', 'p2', 'p2', 'p3', 'p4', 'm1', 's6']],
            "answer": ['m11', 'p234', 'p234', 's456', 's678'],
            "explanation": "iipeyko yaku"
        },
        {
            "input": [['m9', 'm2', 'm1', 's7', 's6', 'dg', 'm9', 's2', 'dg', 's5', 'm3', 's2', 's2', 'dg']],
            "answer": ['dggg', 'm123', 'm99', 's222', 's567'],
            "explanation": "yakuhay yaku"
        },
        {
            "input": [['s3', 'p9', 's8', 's9', 'm8', 's2', 'we', 'p7', 's7', 'we', 'p8', 'm7', 's4', 'm9']],
            "answer": ['m789', 'p789', 's234', 's789', 'wee'],
            "explanation": "sanshoku dochzun yaku"
        },
        {
            "input": [['s4', 'm4', 'p4', 's5', 'm4', 's4', 's4', 'p4', 's4', 'p4', 'm4', 's6', 'm1', 'm1']],
            "answer": ['m11', 'm444', 'p444', 's444', 's456'],
            "explanation": "sanshoku doko yaku"
        },
        {
            "input": [['p1', 'p5', 'ws', 's8', 's8', 's9', 's9', 'p1', 'ws', 'p1', 's9', 'p5', 's8', 'p5']],
            "answer": ['p111', 'p555', 's888', 's999', 'wss'],
            "explanation": "toy-toy yaku"
        },
        {
            "input": [['dw', 'we', 'm4', 'dr', 'dg', 'dg', 'dg', 'm3', 'm2', 'we', 'dw', 'dr', 'dw', 'dr']],
            "answer": ['dggg', 'drrr', 'dwww', 'm234', 'wee'],
            "explanation": "daysangen yakuman"
        },
        {
            "input": [['dw', 'm1', 'dw', 'p9', 'm1', 'm5', 'm1', 'm2', 'dw', 'p9', 'm2', 'm4', 'p9', 'm3']],
            "answer": ['dwww', 'm111', 'm22', 'm345', 'p999'],
            "explanation": "daysangen yakuman"
        }
    ]
}
