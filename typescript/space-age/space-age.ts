export function age(planet: string, seconds: number): number {
	const earthYears: number = secondsToYears(seconds)

	const planetYears: number = earthYears / planetToEarthYears[planet]

	return Math.round((planetYears + Number.EPSILON) * 100) / 100
}

function secondsToYears(seconds: number): number {
	return seconds / 31557600
}

const planetToEarthYears: { [planet: string]: number } = {
	'mercury': 0.2408467,
	'venus': 0.61519726,
	'earth': 1,
	'mars': 1.8808158,
	'jupiter': 11.862615,
	'saturn': 29.447498,
	'uranus': 84.016846,
	'neptune': 164.79132,
}
