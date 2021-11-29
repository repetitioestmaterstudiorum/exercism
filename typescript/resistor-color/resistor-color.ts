export function colorCode(color: COLORSString): number {
	return COLORS.indexOf(color)
}

type COLORSString = typeof COLORS[number]

export const COLORS = [
	'black',
	'brown',
	'red',
	'orange',
	'yellow',
	'green',
	'blue',
	'violet',
	'grey',
	'white',
]

// IMO this is a poor exercise. It forces the use of an array for COLORS, which is a bad choice for key value pairs. An object would be much more expressive.
