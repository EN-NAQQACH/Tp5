

from main import greet

def test_greet(capsys):
    greet("Mohssine")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Bonjour, Mohssine!"
