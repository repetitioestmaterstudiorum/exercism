enum ColorEncoding {
	black = 0,
	brown = 1,
	red = 2,
	orange = 3,
	yellow = 4,
	green = 5,
	blue = 6,
	violet = 7,
	grey = 8,
	white = 9,
}

type ColorEncodingStrings = keyof typeof ColorEncoding

export function decodedValue([firstColor, secondColor]: ColorEncodingStrings[]): number {
	return +`${ColorEncoding[firstColor]}${ColorEncoding[secondColor]}`
}

// version with object rather than enum

// export function decodedValue(colors: string[]): number {
// 	interface ColorEncoding {
// 		[key: string]: number
// 	}

// 	const colorEncoding: ColorEncoding = {
// 		black: 0,
// 		brown: 1,
// 		red: 2,
// 		orange: 3,
// 		yellow: 4,
// 		green: 5,
// 		blue: 6,
// 		violet: 7,
// 		grey: 8,
// 		white: 9,
// 	}

// 	return +colors
// 		.map((color, i) => (i < 2 ? colorEncoding[color] : null))
// 		.filter(x => x !== null)
// 		.join('')
// }
