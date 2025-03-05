import itertools
allNotes = [ 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B' ]

tempo = { 't': 2, 'ht': 1 }

naturalTempoSeq = [
	tempo['t'],
	tempo['t'],
	tempo['ht'],
	tempo['t'],
	tempo['t'],
	tempo['t'],
	tempo['ht'],
]

def convertTempo(value):
	names = ['half tone', 'tone']
	return names[value-1]

def generateScale(allNotes, firstNote, seq):
	index = allNotes.index(firstNote)
	currentNote = allNotes[index]
	notes = []
	for tmp in seq:
		notes.append(currentNote)
		index = index + tmp if index + tmp < len(allNotes) else (index + tmp) - len(allNotes)
		currentNote = allNotes[index]
	return notes, currentNote

def vefirySeqTempo(allNotes, firstNote, seq):
	notes, currentNote = generateScale(allNotes, firstNote, seq)
	return notes[0] == currentNote

def intersecNotesScales(listNotesScales):
	listSameNotes = []
	for i in range(len(listNotesScales)):
		for j in range(len(listNotesScales)):
			if listNotesScales[i] == listNotesScales[j]:
				continue
			listSameNotes += list(filter(lambda note: note in listNotesScales[i], listNotesScales[j]))
	noRepeatedScale = list(set(listSameNotes))
	return [note for note in allNotes if note in noRepeatedScale]

def verifyScaleContainNotes(scale, notes):
	for note in notes:
		if not note in scale:
			return False
	return True

def findScale(seqTempo, allNotes, notes):
	matrix = []
	matrixSeq = []
	for seq in seqTempo:
		for note in allNotes:
			scale = generateScale(allNotes, note, seq)[0]
			if verifyScaleContainNotes(scale, notes):
				matrix.append(scale)
				matrixSeq.append(seq)
	
	finalScale = []
	for scale in matrix:
		finalScale += scale

	return list(set(finalScale)), matrixSeq


permutations = itertools.permutations(naturalTempoSeq)
seqTempo = list(set(filter(lambda permutation: vefirySeqTempo(allNotes, 'C', permutation), permutations)))

# print(findScale(seqTempo, allNotes, ['B', 'C', 'E', 'F'])[0])

# print(len(seqTempo))
# for scale in seqTempo:
# 	print(generateScale(allNotes, 'C', scale)[0])

