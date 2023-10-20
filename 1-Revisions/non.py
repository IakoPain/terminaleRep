def calculNote(note) :
    if note>=80:
        return ("A")
    if note>=60:
        return ("B")
    if note>=50:
        return ("C")
    if note>=40:
        return ("D")
    if note<=40:
        return ("F")

print(calculNote(5))
