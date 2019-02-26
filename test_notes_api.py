import notes_api

def test_get_notes():
    n = notes_api.get_notes()
    notes_api.add_note("aaa")
    n = notes_api.get_notes("aaa")
    assert len(n) > 0
    assert "aaa" in n
    print(n)


if __name__ == "__main__":
    test_get_notes()

