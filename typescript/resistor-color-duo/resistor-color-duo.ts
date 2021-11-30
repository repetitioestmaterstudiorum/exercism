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

// version with an object as dictionary rather than enum
// export function decodedValue([firstColor, secondColor]: string[]): number {
// 	const colorEncoding: { [color: string]: number } = {
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

// 	return +`${colorEncoding[firstColor]}${colorEncoding[secondColor]}`
// }
