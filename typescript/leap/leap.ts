export function isLeap(year: number = new Date().getFullYear()): boolean {
	const isYearDivisibleBy = (number: number) => year % number === 0
	return (isYearDivisibleBy(4) && !isYearDivisibleBy(100)) || isYearDivisibleBy(400)
}
