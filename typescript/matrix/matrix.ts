export class Matrix {
	private matrix: number[][] = new Array()

	constructor(inputMatrix: string) {
		// convert input matrix (string) into array of arrays matrix
		this.matrix = inputMatrix.split('\n').map(row => row.split(' ').map(x => +x))
	}

	get rows() {
		return this.matrix
	}

	get columns() {
		return this.matrix
			.map((_, i) => this.matrix.map((_, j) => this.matrix[j][i]).filter(x => x))
			.filter(x => x.length)
	}
}
