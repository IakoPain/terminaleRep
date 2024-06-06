#Exo 9.2
"""
def effectif_notes(notes_eval):
    tab = [0]*11
    for note in notes_eval:
        tab[note] += 1
    return tab

def notes_triees(eff):
    triees = []
    for i in range(11):
        if eff[i] != 0:
            for _ in range(eff[i]):
                triees.append(i)
    return triees

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
print(notes_eval)
eff = effectif_notes(notes_eval)
"""
#Exo 9.2

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == '0':
            return 0
        else:
            return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

print(dec_to_bin(25))