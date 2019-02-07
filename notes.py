# note

import os
import json

the_notes = []

#get the list of notes
def get_notes():
    global the_notes
    if os.path.exists("notes.json"):
        with open("notes.json","r") as f:
            the_notes = json.load(f)
    return the_notes

# add a note to the list of notes
def add_note(note):
    global the_notes
    if os.path.exists("notes.json"):
        with open("notes.json","r") as f:
            the_notes = json.load(f)
    print("the initial notes")
    print("the notes")
    the_notes.append(note)
    print("the notes")
    print(the_notes)
    with open("notes.json","w") as f:
        json.dump(the_notes, f)

