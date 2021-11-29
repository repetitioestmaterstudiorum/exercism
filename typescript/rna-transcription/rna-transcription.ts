export function toRna(dna: string): string {
	type DnaNucleotides = 'G' | 'C' | 'T' | 'A'
	type RnaNucleotides = 'C' | 'G' | 'A' | 'U'

	const dnaToRna: Record<DnaNucleotides, RnaNucleotides> = {
		'G': 'C',
		'C': 'G',
		'T': 'A',
		'A': 'U',
	}

	return dna
		.split('')
		.map(n => {
			if (!(n in dnaToRna)) throw new Error('Invalid input DNA.')
			return dnaToRna[n as DnaNucleotides]
		})
		.join('')
}
