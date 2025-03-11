from itertools import permutations
from functools import reduce

allNotes = [ 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B' ]

minorNotes = ['Db', 'Eb', 'Gb', 'Ab', 'Bb']

tempo = { 't': 2, 'ht': 1 }

naturalMajorTempoSeq = [
	tempo['t'],
	tempo['t'],
	tempo['ht'],
	tempo['t'],
	tempo['t'],
	tempo['t'],
	tempo['ht'],
]

naturalMinorTempoSeq = [
	tempo['t'],
	tempo['ht'],
	tempo['t'],
	tempo['t'],
	tempo['ht'],
	tempo['t'],
	tempo['t'],
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
	majorNotes = [note for note in notes if 'm' not in note]
	minorNotes = [note.replace('m', '') for note in notes if 'm' in note]

	majorScales = [generateScale(note, naturalMajorTempoSeq)[0] for note in majorNotes]
	minorScales = [generateScale(note, naturalMinorTempoSeq)[0] for note in minorNotes]

	relationScales = {}

	allNotes = intersecNotesScales(majorScales + minorScales) if len(majorNotes + minorNotes) > 1 else (majorScales + minorScales)[0]

	for note in notes:
		currentScale = None
		if 'm' in note:
			currentScale = list(filter(lambda n: n[0] == note.replace('m', ''), minorScales))[0]
		else:
			currentScale = list(filter(lambda n: n[0] == note, majorScales))[0]

		relationScales[note.replace('m', '')] = currentScale
		
	result = {
		'allNotesInterserct': allNotes,
		'relationScales': relationScales
	}

	return result


def convertionNote(note, toMajor=True):
	if toMajor: 
		return notesMinor[note] if note in notesMinor else note
	else:
		return notesMajor[note] if note in notesMajor else note

def __calc__(arr):
    return reduce(lambda a, b: a+b, arr[:2])

def getScales(note, isMajor=True):
	convertedNote = convertionNote(note) if note in minorNotes else note
	isMajorSeq = lambda seq: __calc__(seq) == 4
	isMinorSeq = lambda seq: __calc__(seq) == 3
	seqs = list(filter(isMajorSeq if isMajor else isMinorSeq, seqTempo))
	scales = [generateScale(convertedNote, seq)[0] for seq in seqs]

	convertedScales = []
	for scale in scales:
		convertedScales.append(list(map(lambda n: convertionNote(n, isMajor), scale)))
	return convertedScales

permutations = permutations(naturalMajorTempoSeq)
seqTempo = list(set(filter(lambda permutation: vefirySeqTempo('C', permutation), permutations)))


if __name__ == '__main__':
	print(findScale(['B', 'C', 'E', 'F'])[0])

	print(len(seqTempo))
	for scale in seqTempo:
		print(generateScale('C', scale)[0])

	for scale in getScales('Db', False):
		print(scale)