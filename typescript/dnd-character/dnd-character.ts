export class DnDCharacter {
	strength: number
	dexterity: number
	constitution: number
	intelligence: number
	wisdom: number
	charisma: number
	hitpoints: number

	constructor() {
		this.strength = DnDCharacter.generateAbilityScore()
		this.dexterity = DnDCharacter.generateAbilityScore()
		this.constitution = DnDCharacter.generateAbilityScore()
		this.intelligence = DnDCharacter.generateAbilityScore()
		this.wisdom = DnDCharacter.generateAbilityScore()
		this.charisma = DnDCharacter.generateAbilityScore()
		this.hitpoints = 10 + DnDCharacter.getModifierFor(this.constitution)
	}

	public static generateAbilityScore(): number {
		const numbers: number[] = getXHighestOfYDiceRolls(3, 4)
		return numbers.reduce((acc, cur) => acc + cur)
	}

	public static getModifierFor(abilityValue: number): number {
		return Math.floor((abilityValue - 10) / 2)
	}
}

function getXHighestOfYDiceRolls(x: number, y: number): number[] {
	return getXDiceThrows(y)
		.sort((a, b) => a - b)
		.slice(0, x)
}

function getXDiceThrows(x: number): number[] {
	let dices: number[] = []
	for (let i = 0; i < x; i++) {
		dices.push(rollDice())
	}
	return dices
}

function rollDice(): number {
	return Math.ceil(Math.random() * 6)
}
