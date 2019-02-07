import notes

def test_get_notes():
    n = notes.get_notes()
    print(n)
    notes.add_note("hello there")
    n = notes.get_notes()
    print(n)


if __name__ == "__main__":
    test_get_notes()

