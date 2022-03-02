export class Matrix {
	public readonly rows: number[][]
	public readonly columns: number[][]

	constructor(readonly inputMatrix: string) {
		// convert input matrix (string) into array of arrays rows and columns matrixes
		this.rows = inputMatrix.split('\n').map(row => row.split(' ').map(x => +x))
		// one-time transposition of matrix
		this.columns = this.transpose(this.rows)
	}

	private transpose(rows: number[][]): number[][] {
		return rows
			.map((_, i) => this.rows.map((_, j) => this.rows[j][i]).filter(x => x))
			.filter(x => x.length)
	}
}
