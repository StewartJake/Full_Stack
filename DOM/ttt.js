var cells=document.querySelectorAll(".cell");
for (var i=0; i<cells.length; i++){
	cells[i].addEventListener("click", changeCell);
}
var resetButton=document.querySelector("#resetBtn");
resetButton.addEventListener("click", resetBoard);

function resetBoard(){
	for (var i=0; i<cells.length; i++)
		cells[i].textContent=" ";
};

function changeCell(){
	if (this.textContent === " ")
		this.textContent = "X";
	else if (this.textContent === "X")
		this.textContent = "O";
	else
		this.textContent = " ";
};
