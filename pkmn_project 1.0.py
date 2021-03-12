class Pokemon:
    def __init__(self, name, type1, type2=None, levitate=False):
        type1 = type1.lower()
        supereffective = []
        notvery = []
        immunity = []
        types = [type1]
        if type2 is not None:
            type2 = type2.lower()
            types.append(type2)
        if levitate is not False:
            immunity.append("ground")
        for i in range(len(types)):
            # by the time i realized that a dictionary would be better it was too late
            # don't do this, just use a fucking dictionary like a smart coder
            if types[i] == "normal":
                supereffective.append("fighting")
                immunity.append("ghost")
            elif types[i] == "fire":
                supereffective.append("water")
                supereffective.append("ground")
                supereffective.append("rock")
                notvery.append("fire")
                notvery.append("grass")
                notvery.append("ice")
                notvery.append("steel")
                notvery.append("fairy")
                notvery.append("bug")
            elif types[i] == "water":
                supereffective.append("electric")
                supereffective.append("grass")
                notvery.append("fire")
                notvery.append("water")
                notvery.append("steel")
            elif types[i] == "electric":
                supereffective.append("ground")
                notvery.append("electric")
                notvery.append("flying")
                notvery.append("steel")
            elif types[i] == "grass":
                supereffective.append("fire")
                supereffective.append("ice")
                supereffective.append("poison")
                supereffective.append("flying")
                supereffective.append("bug")
                notvery.append("water")
                notvery.append("electric")
                notvery.append("grass")
                notvery.append("ground")
            elif types[i] == "ice":
                supereffective.append("fire")
                supereffective.append("fighting")
                supereffective.append("rock")
                supereffective.append("steel")
                notvery.append("ice")
            elif types[i] == "fighting":
                supereffective.append("flying")
                supereffective.append("psychic")
                supereffective.append("fairy")
                notvery.append("bug")
                notvery.append("rock")
                notvery.append("dark")
            elif types[i] == "poison":
                supereffective.append("ground")
                supereffective.append("psychic")
                notvery.append("grass")
                notvery.append("fighting")
                notvery.append("poison")
                notvery.append("bug")
                notvery.append("fairy")
            elif types[i] == "ground":
                supereffective.append("water")
                supereffective.append("grass")
                supereffective.append("ice")
                notvery.append("poison")
                notvery.append("rock")
                immunity.append("electric")
            elif types[i] == "flying":
                supereffective.append("electric")
                supereffective.append("rock")
                supereffective.append("ice")
                notvery.append("grass")
                notvery.append("fighting")
                notvery.append("bug")
                immunity.append("ground")
            elif types[i] == "psychic":
                supereffective.append("bug")
                supereffective.append("ghost")
                supereffective.append("dark")
                notvery.append("fighting")
                notvery.append("psychic")
            elif types[i] == "bug":
                supereffective.append("flying")
                supereffective.append("fire")
                supereffective.append("rock")
                notvery.append("grass")
                notvery.append("fighting")
                notvery.append("ground")
            elif types[i] == "rock":
                supereffective.append("water")
                supereffective.append("grass")
                supereffective.append("fighting")
                supereffective.append("ground")
                supereffective.append("steel")
                notvery.append("normal")
                notvery.append("fire")
                notvery.append("poison")
                notvery.append("flying")
            elif types[i] == "ghost":
                supereffective.append("ghost")
                supereffective.append("dark")
                immunity.append("normal")
                immunity.append("fighting")
                notvery.append("poison")
                notvery.append("bug")

            elif types[i] == "dragon":
                supereffective.append("ice")
                supereffective.append("dragon")
                supereffective.append("fairy")
                notvery.append("fire")
                notvery.append("water")
                notvery.append("electric")
                notvery.append("grass")
            elif types[i] == "dark":
                supereffective.append("fighting")
                supereffective.append("bug")
                supereffective.append("fairy")
                notvery.append("ghost")
                notvery.append("dark")
                immunity.append("psychic")
            elif types[i] == "steel":
                supereffective.append("fire")
                supereffective.append("fighting")
                supereffective.append("ground")
                notvery.append("normal")
                notvery.append("grass")
                notvery.append("ice")
                notvery.append("flying")
                notvery.append("psychic")
                notvery.append("bug")
                notvery.append("rock")
                notvery.append("dragon")
                notvery.append("steel")
                notvery.append("fairy")
            elif types[i] == "fairy":
                supereffective.append("poison")
                supereffective.append("steel")
                immunity.append("dragon")
                notvery.append("fighting")
                notvery.append("bug")
                notvery.append("dark")
            else:
                raise NameError("invalid pokemon type")
        supereffective.sort()
        notvery.sort()
        immunity.sort()
        length = len(supereffective)
        for i in range(0, len(immunity)):
            s_length = len(supereffective) - 1
            n_length = len(notvery) - 1 
            for j in range(0, s_length):
                if j >= s_length:
                    break
                if immunity[i] == supereffective[j]:
                    del supereffective[j]
            for j in range(0, n_length):
                if immunity[i] == notvery[j]:
                    n_length -= 1
                    del notvery[j]
        for i in range(0, length): # Fix this method
            length = len(supereffective)
            if i >= length:
                break # i have to add this for some reason
            for j in range(0, length):
                length = len(supereffective)
                if j >= length:
                    break
                if i == j:
                    continue
                if supereffective[i] == supereffective[j]:
                    temp = supereffective[j] + " (4x)"
                    supereffective[j] = temp
                    del supereffective[i]
        length = len(notvery)

        for i in range(0, length):
            length = len(notvery)
            if i >= length:
                break
            for j in range(0, length):
                length = len(notvery)
                if j >= length:
                    break
                if i == j:
                    continue
                if notvery[i] == notvery[j]:
                    temp = notvery[j] + " (1/4x)"
                    notvery[j] = temp
                    del notvery[i]
        for i in immunity:
            for j in notvery:
                if i == j:
                    notvery.remove(j)
            for j in supereffective:
                if i == j:
                    supereffective.remove(j)
        self.name = name
        self.type1 = type1[0].upper() + type1[1:]
        if type2 is not None:
            self.type2 = type2[0].upper() + type2[1:]
        else:
            self.type2 = None
        self.immunities = self.__fixCase(immunity)
        self.supereffective = self.__fixCase(supereffective)
        self.resistances = self.__fixCase(notvery)
    def __fixCase(self, x):
        for i in range(0, len(x)):
            uppercase = x[i]
            x[i] = uppercase[0].upper() + uppercase[1:]
        return x        
    def __str__(self):
        retString = ""
        dashes = ""
        for i in range(0, 75):
            dashes += "-"
        s_length = len(self.supereffective)
        r_length = len(self.resistances)
        i_length = len(self.immunities)
        length = 0
        if s_length >= r_length:
            length = s_length
        elif r_length >= i_length:
            length = r_length
        else:
            length = i_length
        if length == 1:
            length += 1

        if self.type2 == None:
            retString += "{:} ({:})\n".format(self.name, self.type1)
            retString += dashes
            retString += "\n"
            retString += "{:^25}{:^25}{:^25}\n".format("Weaknesses", "Resistances", "Immunities")
        else:
            retString += "{:} ({:} & {:})\n".format(self.name, self.type1, self.type2)
            retString += dashes
            retString += "\n"
            retString += " {:^25}{:^25}{:^25}\n".format("Weaknesses", "Resistances", "Immunities")
        retString += dashes + "\n"
        for i in range(0, length - 1):
            try:
                retString += "{:^25}".format(self.supereffective[i])
            except:
                retString += "{:^25}".format("")
            try:
                retString += "{:^25}".format(self.resistances[i])
            except:
                retString += "{:^25}".format("")
            try:
                retString += "{:^25}".format(self.immunities[i])
            except:
                retString += "{:^25}".format("")

            retString += "\n"
        return retString