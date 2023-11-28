from random import randint
class File:
    def __init__(self):
        self.file = []

    def __len__(self):
        return len(self.file)

    def __repr__(self):
        return ' '.join([str(i) for i in self.file])

    def enfiler(self, element):
        self.file.append(element)

    def defiler(self):
        return self.file.pop(0)

    def estVide(self):
        vide=False
        if self.file==[]:
            vide=True
        return vide

    def sommet(self):
        if not self.estVide():
            return self.file[0]

def extractionPaire(fileIn):
    fileOut=File()
    for n in range (0,len(fileIn)):
        temp=fileIn.defiler()
        if temp%2==0:
            fileOut.enfiler(temp)



    return fileOut

f=File()
for n in range(0,20):
    f.enfiler(randint(10,50))

print(f)
print(extractionPaire(f))