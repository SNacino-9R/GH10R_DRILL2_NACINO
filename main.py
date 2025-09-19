from pyscript import when, display, document

@when("click", "#submit-btn")
def gettinginfo(e):
    name = document.getElementById('name').value
    age = document.getElementById('age').value
    school = document.getElementById('school').value

    note_multilinestring = f'''
   Student Profile
    Name   : {name}
    Age    : {age}
    School : {school}

   Notes:
    {name} is currently {age} years old and studies at {school}.
    This information was gathered through input fields and displayed using
    a multiline string in Python via PyScript.
    '''

    display(note_multilinestring, target="output")

