# statements.py
# This file contains ONLY text banks (no logic)

opening_phrases = [
    "This year,",
    "This term,",
    "In English,"
]

attitude_bank = {
    90: [
        "brought outstanding enthusiasm and curiosity to learning throughout",
        "showed exceptional drive and independence, always pushing beyond expectations"
    ],
    85: [
        "showed exceptional commitment and rarely needed prompting to engage",
        "worked with real dedication throughout and took pride in every task"
    ],
    80: [
        "demonstrated a confident and positive attitude throughout the year",
        "approached all areas of learning with assurance and a willingness to try"
    ],
    75: [
        "worked reliably and engaged well with tasks across the year",
        "showed consistent effort and could always be counted on to contribute"
    ],
    70: [
        "showed a good attitude and responded well to direction",
        "engaged sensibly with tasks and improved when clear guidance was given"
    ],
    65: [
        "made steady progress and grew in confidence with encouragement",
        "responded positively to support and showed improvement as the year went on"
    ],
    60: [
        "engaged more effectively when tasks were well structured",
        "worked better when given a clear framework and adult support nearby"
    ],
    55: [
        "needed regular support to stay focused but showed effort on familiar tasks",
        "benefited from prompting to stay on task and did best on structured activities"
    ],
    40: [
        "found concentration difficult and required consistent adult support",
        "struggled to sustain focus and needed frequent encouragement to engage"
    ],
    0: [
        "needed significant support to engage with learning",
        "required a high level of adult support to participate across most activities"
    ]
}

reading_bank = {
    90: [
        "read with real insight, analysing language and authorial choices with confidence",
        "demonstrated perceptive reading skills, drawing well-reasoned conclusions from texts"
    ],
    85: [
        "read confidently, making strong inferences across a range of texts",
        "showed excellent comprehension and a clear understanding of how texts are constructed"
    ],
    80: [
        "showed secure understanding and identified how language and structure worked",
        "understood a range of texts well and explained the effect of key features clearly"
    ],
    75: [
        "understood a variety of texts and picked out key features effectively",
        "read a range of texts with good understanding and identified what mattered most"
    ],
    70: [
        "understood the main ideas in familiar texts with some support",
        "grasped key information across familiar text types when supported"
    ],
    65: [
        "identified key information in texts with guidance",
        "located relevant details in texts when given direction and support"
    ],
    60: [
        "understood simple texts and benefited from discussion beforehand",
        "followed straightforward texts with adult support and pre-reading preparation"
    ],
    55: [
        "followed familiar texts with adult support",
        "accessed meaning in short familiar texts with close adult guidance"
    ],
    40: [
        "needed help to access meaning in most texts",
        "found most texts challenging and relied on adult support throughout"
    ],
    0: [
        "is working on early reading skills with adult support",
        "is at an early stage of reading and needs significant adult guidance"
    ]
}

writing_bank = {
    90: [
        "wrote with skill and confidence across all text types studied",
        "produced impressive writing throughout, adapting tone and vocabulary with real control"
    ],
    85: [
        "produced purposeful writing with strong control of structure and vocabulary",
        "wrote effectively across text types, making deliberate and well-judged choices"
    ],
    80: [
        "wrote effectively across text types with appropriate tone and organisation",
        "produced well-structured writing throughout with a clear sense of purpose"
    ],
    75: [
        "organised writing clearly and used vocabulary with care across the year",
        "structured work well and selected language thoughtfully across most tasks"
    ],
    70: [
        "communicated ideas clearly and used familiar text structures consistently",
        "wrote coherently across familiar text types and applied key features reliably"
    ],
    65: [
        "produced organised writing with support across a range of tasks",
        "managed to organise ideas and complete tasks with adult guidance"
    ],
    60: [
        "wrote short structured responses when given a clear model to follow",
        "produced brief written responses with a framework and adult support"
    ],
    55: [
        "completed writing tasks with close guidance; independence was developing",
        "needed support throughout writing tasks but showed emerging independence"
    ],
    40: [
        "produced brief written responses with considerable support",
        "needed significant help at each stage of writing to produce a response"
    ],
    0: [
        "is working on early writing skills with adult support",
        "is at an early stage of writing and requires significant adult guidance"
    ]
}

reading_target_bank = {
    90: [
        "analyse how language and structure create effects in complex texts",
        "explore how writers craft meaning through deliberate language and structural choices"
    ],
    85: [
        "develop inference skills and examine how structure shapes meaning",
        "push beyond surface meaning and consider why writers make specific choices"
    ],
    80: [
        "explore the effect of subtle language choices on the reader",
        "develop sensitivity to connotation and implied meaning across a range of texts"
    ],
    75: [
        "explain why authors use specific features, not just identify them",
        "move from spotting text features to explaining their effect on the reader"
    ],
    70: [
        "build confidence reading longer texts and piece together implied meaning",
        "practise reading less familiar texts and work on understanding implied ideas"
    ],
    65: [
        "read a wider range of text types and identify their key conventions",
        "encounter new text types and develop understanding of their purpose and features"
    ],
    60: [
        "use context clues to work out unfamiliar words while reading",
        "build the habit of checking understanding and tackling new vocabulary independently"
    ],
    55: [
        "build fluency and retell what has been read in own words",
        "read regularly to build confidence and practise explaining what has been understood"
    ],
    40: [
        "read short texts with support and identify the main idea",
        "work with an adult to read accessible texts and pick out the key message"
    ],
    35: [
        "build reading stamina using familiar and accessible texts",
        "spend regular time reading comfortable texts to grow confidence and fluency"
    ]
}

writing_target_bank = {
    90: [
        "manipulate language and structure to achieve deliberate effects",
        "take creative risks with form and language to create sophisticated writing"
    ],
    85: [
        "refine word choices so that every decision serves the writing",
        "focus on precision, ensuring language and structure work purposefully throughout"
    ],
    80: [
        "control pace and rhythm by varying sentence length deliberately",
        "develop greater range in sentence structure and use punctuation as a stylistic tool"
    ],
    75: [
        "use more ambitious vocabulary and varied sentence structures",
        "challenge word choices and experiment with more complex constructions"
    ],
    70: [
        "check that tone and structure match the purpose of each piece",
        "reread writing as a reader would and refine tone to suit the task"
    ],
    65: [
        "plan writing carefully and include key features from the outset",
        "map out the features needed for each text type before starting to write"
    ],
    60: [
        "draft and improve writing by focusing on one feature at a time",
        "practise returning to writing to strengthen a specific element before moving on"
    ],
    55: [
        "use writing frames to include the key features of each text type",
        "follow structured frameworks more independently to organise and complete writing"
    ],
    40: [
        "write in complete sentences and begin to link ideas in paragraphs",
        "focus on forming full sentences and connecting two or three ideas in sequence"
    ],
    35: [
        "build confidence by rehearsing sentences before writing them down",
        "use shared writing with an adult to develop the confidence to write independently"
    ]
}

closer_bank = [
    "A positive year overall with good progress made",
    "A strong year with much to build on going forward",
    "Good foundations laid this year for the year ahead"
]
