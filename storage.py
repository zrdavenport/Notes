# storage.py

import os
import json
import re
from tinydb import TinyDB, Query, where

notes_db = TinyDB("notes_tinydb.json")
profile_table = notes_db.table("profile")
note_table = notes_db.table("note")
session_table = notes_db.table("session")

# Manage user profiles

def add_profile(profile):
    assert type(profile) is dict
    assert 'user' in profile
    assert type(profile['user']) is str
    profile_table.insert(profile)

def get_profile(user):
    profile = profile_table.get(where('user') == user)
    if profile:
        return dict(profile)
    return None

def delete_profile(user):
    profile_table.remove(where('user') == user)

# Manage sessions

def add_session(session):
    assert type(session) is dict
    assert 'key' in session
    assert type(session['key']) is str
    session_table.insert(session)

def get_session(key):
    session = session_table.get(where('key') == key)
    if session:
        return dict(session)
    return None

def update_session(key, updates):
    assert type(updates) is dict
    session_table.update(updates, where('key') == key)

def delete_session(key):
    session_table.remove(where('key') == key)

# Manage notes

def get_notes(search = None):
    query = Query()
    if search:
        notes = note_table.search(query.text.matches(".*"+search+".*", flags=re.IGNORECASE))
    else:
        notes = note_table.all()
    for note in notes:
        note['id'] = note.doc_id
    return [dict(n) for n in notes]

def add_note(note):
    assert type(note) is dict
    assert 'text' in note
    assert type(note['text']) is str
    id = note_table.insert(note)
    return id

def delete_note(id):
    try:
        note_table.remove(doc_ids = [id])
    except KeyError:
        pass