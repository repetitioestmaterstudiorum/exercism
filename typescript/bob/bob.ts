export function hey(message: string): string {
	// remove new lines, tabs, and spaces
	const cleanMsg: string = message.trim().replace(/\t|\n|\r/g, '')

	// get message properties
	const messageLen: number = cleanMsg.length
	const isAllCaps: boolean =
		// message is same if transformed to uppercase and contains at least one character
		cleanMsg.toUpperCase() === cleanMsg && cleanMsg.match(/[a-zA-Z]/) !== null
	const isQuestion: boolean = cleanMsg.slice(messageLen - 1, messageLen) == '?'

	// return appropriate message
	if (isQuestion && isAllCaps) {
		return "Calm down, I know what I'm doing!"
	} else if (isAllCaps) {
		return 'Whoa, chill out!'
	} else if (isQuestion) {
		return 'Sure.'
	} else if (cleanMsg === '') {
		return 'Fine. Be that way!'
	} else {
		return 'Whatever.'
	}
}
