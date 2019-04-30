all:
	time python sudoku2.py input.txt output.txt a,Easy-NYTimes
	time python sudoku2.py input.txt output.txt a,Medium-NYTimes
	time python sudoku2.py input.txt output.txt a,Hard-NYTimes
	time python sudoku2.py input.txt output.txt a,WebSudoku-Hard
	time python sudoku2.py input.txt output.txt a,WebSudoku-Evil
	time python sudoku2.py input.txt output.txt a,hardest-sudoku-telegraph
	time python sudoku2.py input.txt output.txt a,sudokugarden.de/files/100sudoku2-en.pdf-Nr-100
	time python sudoku2.py input.txt output.txt a,sudokugarden.de/files/100sudoku2-en.pdf-Nr-50
	time python sudoku.py input.txt output.txt a,Easy-NYTimes
	time python sudoku.py input.txt output.txt a,Medium-NYTimes
	time python sudoku.py input.txt output.txt a,Hard-NYTimes
	time python sudoku.py input.txt output.txt a,WebSudoku-Hard
	time python sudoku.py input.txt output.txt a,WebSudoku-Evil
	time python sudoku.py input.txt output.txt a,hardest-sudoku-telegraph
	time python sudoku.py input.txt output.txt a,sudokugarden.de/files/100sudoku2-en.pdf-Nr-100
	time python sudoku.py input.txt output.txt a,sudokugarden.de/files/100sudoku2-en.pdf-Nr-50
	time python sudokunaive.py input.txt output.txt a,Easy-NYTimes
	time python sudokunaive.py input.txt output.txt a,Medium-NYTimes
	time python sudokunaive.py input.txt output.txt a,Hard-NYTimes
	time python sudokunaive.py input.txt output.txt a,WebSudoku-Hard
	time python sudokunaive.py input.txt output.txt a,WebSudoku-Evil
	time python sudokunaive.py input.txt output.txt a,hardest-sudoku-telegraph
	time python sudokunaive.py input.txt output.txt a,sudokugarden.de/files/100sudoku2-en.pdf-Nr-100
	time python sudokunaive.py input.txt output.txt a,sudokugarden.de/files/100sudoku2-en.pdf-Nr-50
