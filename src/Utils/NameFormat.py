class NameFormat:

    def AddSpace(self, name):

        NewName = ""

        for character in name:
            if character.isupper() and len(NewName) > 0:
                NewName += " " + character
            else:
                NewName += character
 
        return NewName

