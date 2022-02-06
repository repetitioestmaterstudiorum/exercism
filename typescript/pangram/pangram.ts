export function isPangram(sentence: string) {
	// assuming each letter is used only once:

	// if (sentence.length === 0) return false

	// const sanitizedSentence: string = sentence.replace(/ |\.|"/g, '').toLowerCase()

	// const letters = new Set<string>()
	// for (let i: number = 0; i < sanitizedSentence.length; i++) {
	// 	const nextLetter: string = sanitizedSentence[i]
	// 	if (letters.has(nextLetter)) {
	// 		return false
	// 	} else {
	// 		letters.add(nextLetter)
	// 	}
	// }

	// return true

	// assuming each letter can be used more than once:
	const alphabetsLetters: string[] = 'abcdefghijklmnopqrstuvwxyz'.split('')
	const loweredSentence: string = sentence.toLowerCase()
	return alphabetsLetters.every(l => loweredSentence.includes(l))
}
