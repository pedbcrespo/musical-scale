import itertools
from functools import reduce

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

notesMinor = {
	'Db': 'C#',
	'Eb': 'D#',
	'Gb': 'F#',
	'Ab': 'G#',
	'Bd': 'A#',
}

notesMajor = {
	'C#': 'Db',
	'D#': 'Eb',
	'F#': 'Gb',
	'G#': 'Ab',
	'A#': 'Bd'
}

def convertTempo(value):
	names = ['half tone', 'tone']
	return names[value-1]

def generateScale(firstNote, seq):
	index = allNotes.index(firstNote)
	currentNote = allNotes[index]
	notes = []
	for tmp in seq:
		notes.append(currentNote)
		index = index + tmp if index + tmp < len(allNotes) else (index + tmp) - len(allNotes)
		currentNote = allNotes[index]
	return notes, currentNote

def vefirySeqTempo(firstNote, seq):
	notes, currentNote = generateScale(firstNote, seq)
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

def findScale(notes):
	matrix = []
	matrixSeq = []
	for seq in seqTempo:
		for note in allNotes:
			scale = generateScale(note, seq)[0]
			if verifyScaleContainNotes(scale, notes):
				matrix.append(scale)
				matrixSeq.append(seq)
	
	finalScale = []
	for scale in matrix:
		finalScale += scale

	return list(set(finalScale)), matrixSeq



def convertionNote(note, toMajor=True):
	if toMajor: 
		return notesMinor[note] if note in notesMinor else note
	else:
		return notesMajor[note] if note in notesMajor else note

def __calc__(arr):
    return reduce(lambda a, b: a+b, arr[:2])

def getScales(note, isMajor=True):
	note = convertionNote(note)
	isMajorSeq = lambda seq: __calc__(seq) == 4
	isMinorSeq = lambda seq: __calc__(seq) == 3
	seqs = list(filter(isMajorSeq if isMajor else isMinorSeq, seqTempo))
	scales = [generateScale(note, seq)[0] for seq in seqs]

	convertedScales = []
	for scale in scales:
		convertedScales.append(list(map(lambda n: convertionNote(n, isMajor), scale)))
	return convertedScales

permutations = itertools.permutations(naturalTempoSeq)
seqTempo = list(set(filter(lambda permutation: vefirySeqTempo('C', permutation), permutations)))


if __name__ == '__main__':
	# print(findScale(seqTempo, allNotes, ['B', 'C', 'E', 'F'])[0])

	# print(len(seqTempo))
	# for scale in seqTempo:
	# 	print(generateScale('C', scale)[0])

	print(getScales('Db', False))