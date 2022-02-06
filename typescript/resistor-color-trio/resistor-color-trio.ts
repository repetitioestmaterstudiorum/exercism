export function decodedResistorValue([colorOne, colorTwo, colorThree]: string[]): string {
	const ohms: number =
		+`${colorEncoding[colorOne]}${colorEncoding[colorTwo]}` *
		Math.pow(10, colorEncoding[colorThree])

	return ohms > 1000 ? `${ohms / 1000} kiloohms` : `${ohms} ohms`
}

const colorEncoding: { [color: string]: number } = {
	black: 0,
	brown: 1,
	red: 2,
	orange: 3,
	yellow: 4,
	green: 5,
	blue: 6,
	violet: 7,
	grey: 8,
	white: 9,
}
