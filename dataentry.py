import pandas as pd 
dataset = pd.read_csv("pokemon.csv")
print(dataset)
actualdata = dataset.iloc[:, 3:7]

print(actualdata)
csvStr = actualdata.to_csv(index=False)
testFile = open("pokemontest.csv", "w")
testFile.write(csvStr)
