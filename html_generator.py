Notes_from_Stage_2 = [["""Introduction to serious programming:""",
 [["""Computer Science: Computers and Programming""","""Computer science is about how to solve 
    problems breaking them into smaller pieces and then precisely and 
    mechanically describe a sequence of steps to solve each piece that can be executed by a computer. 
    A computer is an universal machine, we can program it to do any computation. 
    Programming is the core of Computer Science. A program needs to be a precise sequence of steps. 
    The power of the Computer is that it can execute these steps super fast"""],
    ["""Programming Language""","""Why do we need to invent new languages to program computers, rather than using natural languages? 
    Ambiguity, Verbosity. A programming language is what programmers use to tell a computer what to do"""],
    ["""Grammar""","""Backus-Naur Form purpose is to describe precisely language in a simple and concise way: non-terminal - replacement. 
    Terminals are never on the left side of the rule. Replacing you get derivations"""],
    ["""Other Takeaways""","""For a recursive definition (non circular) we need two rules: one with the same thing on the left and the right side
    and one where we can stop. High level language, instead of running in the computer is an interpreter which translates to the language 
    of the computer A compiler is a program that produces other programs. 
    It does all the work at once and then runs the program, an interpreter does everything at the same time"""]]],
 ["""Variables and strings:""",
    [["""What are variables?""","""Variables is a way to give names to values. Variables (obviously) can vary. 
    They improve code readability by giving meaningful names, they allow us to store important data."""],
    ["""Assigning a value to a variable""","""To assign a value to a variable, simply input in Python the following assignment statement: Name = Expression"""],
    ["""Other Takeaways""","""Python evaluates first the right side. Indexing: string -expression- - 
    one-character string (expression should evaluate to a number)"""]]],
 ["""Input - Function - Output""",
    [["""What is a function (procedure)?""","""Functions take input, do something with it, and then produce output."""],
    ["""Phyton syntax to create functions""","""procedure (input,input,...). Inputs also called operands, arguments. 
    Inputs must match the ones used in the procedure."""],
    ["""Return is the output""","""First line of a function: you must begin the line with def (lowercase). 
    After def you must give a function name. Next, you must have a set of parentheses with the required parameters inside. 
    The line must end with : colon. In the body of the function: every line in the function must be indented. 
    If you want your function to produce output, it must end with a return statement."""],
    ["""Using functions""","""Once created, you can use the function by writings its name followed by () with the required inputs. 
    This helps avoid repetition, as instead of writing the definition everytime we need it we just define it once and then use it 
    by simply writing its name and inputs."""]]],
 ["""Decisions and Repetition: If and While""",
    [["""Making decisions:""","""Number Operator Number - Boolean (True or False). If - if TestExpression: Code Block. 
    Or: Expression or Expression. only evaluates what it needs to, once an expression is TRUE it stops. 
    If statements match a decision flowchart. The indentations in the code correspond to branches in the flow chart. 
    With arithmetic, comparisons, procedures and if to make decisions you know enough to write every possible computer program (as proved by Alan Turing)"""],
    ["""Repetitions:""","""Loops: while TestExpression: Code Block. If executes 0 or 1 times (depending if it's True). 
    while executes n times, as long as it's True. How to break a loop: Break: While TextExpression: Code. if BreakTest: break. More Code after While"""]]],
 ["""Structured Data: Lists and For Loops""",
     [["""Lists""","""Lists can contain strings, numbers, even other lists, it's a sequence of anything (strings are only of characters). 
     list - [Expression,Expression,...]. An advantage of structured data is that you can look through the elements (for loop)"""],
     ["""Mutation and aliasing:""","""Mutation: we can change values of a list after is created. Strings are immutable. 
     We can change elements of the list without creating a new list. Aliasing: two different ways to refer to the same object. 
     If the element changes, all variables values change too"""],
     ["""List operations:""","""list.append(element) - it mutates the list. list + list - produces a new list. len(list) - length of the list. 
     For loops (each element of the list): for name in list: block. Index: list.index(value). 
     If value is in the list, returns the first position where value is found in list. Otherwise, produces an error. value in list, value not in list"""]]]]
     
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
        <div class="concept">
            <div class="concept-title">
                ''' + concept_title
    html_text_2 = '''
            </div>
            <div class="concept-description">
                <p>
                    ''' + concept_description
    html_text_3 = '''
                </p>
            </div>
        </div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)


def make_HTML_for_many_concepts(list_of_concepts):
    html = ""
    for session in list_of_concepts:
        session_title = session[0]
        html_session_title = '''
<div class="lesson">
    <h2>''' + session_title +'''</h2>
    <div class="notes">'''
        html = html + html_session_title
        for concept in session[1]:
            concept_html = make_HTML(concept)
            html = html + concept_html
        html_session_ending = '''
    </div>
</div>'''
        html = html + html_session_ending
    return html

print make_HTML_for_many_concepts(Notes_from_Stage_2)