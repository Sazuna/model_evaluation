#!/bin/python3
# -*- coding: utf-8 -*-

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

table = []
with open (input_file, "r") as f:
	for line in f:
		line = line.split('\t')
		table.append(line)

# parcours de la table et calcul pour chaque ligne:

resultats = [("label", "Rappel", "Précision", "F-mesure", "Jaccard", "Diversité", "Exactitude", "Spécificité", "Dice", "SokalSneath")]

MacroRappel = 0
MacroPrécision = 0
SommeVP = 0
SommeFN = 0
SommeFP = 0

for i in range(1, len(table)):
	line = table[i]
	etq = line[0]
	VP = int(line[1])
	FP = int(line[2])
	FN = int(line[3])
	VN = int(line[4])
	
	# Rappel:
	Rappel = VP / (VP + FN)

	# Précision:
	Précision = VP / (VP + FP)

	# F-mesure:
	Beta = 1
	FMesure = (1+Beta*Beta) * (Rappel * Précision) / (Beta*Beta * Précision + Rappel)

	# Jaccard:
	Jaccard = VP / (VP + FP + FN)

	# Diversité:
	Diversité = 1 - Jaccard
	
	# Exactitude:
	Exactitude = (VP + VN) / (VP + VN + FP + FN)

	# Spécificité:
	Spécificité = VN / (VN + FP)

	# Dice:
	Dice = 2 * VP / (2 * VP + FP + FN)

	# Sokal et Sneath:
	SokalSneath = VP / (VP + 2 * FP + 2 * FN)

	resultats.append((etq, str(Rappel), str(Précision), str(FMesure), str(Jaccard), str(Diversité), str(Exactitude), str(Spécificité), str(Dice), str(SokalSneath)))

	# Macro Rappel
	MacroRappel += Rappel
	# Macro Précision
	MacroPrécision += Précision

	# Pour les Micro Rappel et Micro Précision:
	SommeVP += VP
	SommeFN += FN
	SommeFP += FP

MacroRappel /= (len(table)-1)
MacroPrécision /= (len(table)-1)

MicroRappel = SommeVP / (SommeVP + SommeFN)
MicroPrécision = SommeVP / (SommeVP + SommeFP)

print("Macro rappel =", MacroRappel)
print("Macro précision =", MacroPrécision)
print("Micro rappel =", MicroRappel)
print("Micro précision =", MicroPrécision)

with open (output_file, "w") as f:
	f.write("Macro rappel = " + str(MacroRappel) + '\n')
	f.write("Macro précision =" + str(MacroPrécision) + '\n')
	f.write("Micro rappel ="+ str(MicroRappel) + '\n')
	f.write("Micro précision =" + str(MicroPrécision) + '\n\n')
	for line in resultats:
		f.write('\t'.join(line) + '\n')

