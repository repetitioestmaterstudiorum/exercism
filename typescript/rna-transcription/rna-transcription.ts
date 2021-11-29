export function toRna(dna: string): string {
	const nucleotides: string[] = dna.split('')

	// throw error if input data invalid (=not all values in dnaRnaTranscription dict)
	if (!nucleotides.every(n => Object.keys(dnaRnaTranscription).includes(n))) {
		throw new Error('Invalid input DNA.')
	}

	return nucleotides.map(n => dnaRnaTranscription[n]).join('')
}

const dnaRnaTranscription: DnaRnaTranscription = {
	'G': 'C',
	'C': 'G',
	'T': 'A',
	'A': 'U',
}

type DnaRnaTranscription = {
	[key: string]: string
}
