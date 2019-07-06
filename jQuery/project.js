var player1Name = prompt("Player1, please enter your name. You'll be blue.");
var p1Color = "rgb(86, 151, 255)";
var player2Name= prompt("Player2, please enter your name. You'll be red.");
var p2Color = "rgb(237, 45, 73)";
player1 = {"name": player1Name,
	"color": p1Color,
	"colorStr":"blue"};
player2 = {"name": player2Name,
	"color": p2Color,
	"colorStr": "red"};
var tbl = $("#board");

function dropChip(col, color){
	//Fn: changes the lowest gray row to current players color
	//Arg: column as integer and color as string
	//Ret: null
	for (var row=5; row>=0; row--){
		var cell=tbl.find("tr").eq(row).find("td").eq(col).find("button");
		if (cell.css("background-color") === "rgb(128, 128, 128)"){
			cell.css("background-color",color);
			break;
		}
	}
}


function changeMessage(player, color){
	//Fn: changes the message to let players know whose turn it is
	//Arg: player name, color as string
	//Ret: null
	var msg = player + ": it is your turn. Place your " + color + " chip.";
	$("#message").text(msg);
}


function checkWinner(color){
	coords = []
	var li = tbl.find("button").filter(function() {
		return $(this).css("background-color") === color;
	});
	for (var i=0; i<li.length; i++){
		var winner = checkWinConds(li.eq(i));
		return winner;
	};
}


function checkWinConds(btn){
	var row = btn.closest("tr").index();
	var col = btn.closest("td").index();
	var color = btn.css("background-color");
	var count = 1;
	var won = false;
	//Horizontal
	//Right
	for (var i=1; i<4 && col+i <= 6; i++){
		if (tbl.find("tr").eq(row).find("td").eq(col + i).find("button").css("background-color") === color){
		count += 1;}
		else
			break
	}
	//Left
	for (i = 1; i<4 && col-i >= 0; i++){
		if (tbl.find("tr").eq(row).find("td").eq(col - i).find("button").css("background-color") === color){
			count += 1;}
		else
			break
	}
	if (count === 4)
		won = true;
	//Vertical
	count = 1;
	//Up
	for (var i=1; i<4 && row+i <= 5; i++){
		if (tbl.find("tr").eq(row + 1).find("td").eq(col).find("button").css("background-color") === color){
		count += 1;}
		else
			break
	}
	if (count ===4)
		won = true;

	//Diagonal
	count = 1;
	//N-W
	for (var i=1; i<4 && col+i <= 6 && row+i <=5; i++){
		if (tbl.find("tr").eq(row + i).find("td").eq(col + i).find("button").css("background-color") === color){
		count += 1;}
		else
			break
	}
	if (count === 4)
		won = true;
	count = 1;
	//N-E
	for (i = 1; i<4 && col-i >= 0 && row+i <= 5; i++){
		if (tbl.find("tr").eq(row + i).find("td").eq(col - i).find("button").css("background-color") === color){
			count += 1;}
		else
			break
	}
	if (count === 4)
		won = true;

	return won;
}


var player = 1;
gameOver = false;
$("#board button").on("click", function(){
	var col=$(this).closest("td").index();
	var row=$(this).closest("tr").index();
	if (player === 1){
		var currPlayer = player1;
		var otherPlayer = player2;
	}
	else{
		var currPlayer = player2;
		var otherPlayer = player1;
	}
	dropChip(col, currPlayer.color);
	changeMessage(otherPlayer.name, otherPlayer.colorStr);
	gameOver = checkWinner(currPlayer.color);
	if (player === 1)
		player = 2;
	else
		player = 1;
	if (gameOver){
		$("#message").text(currPlayer.name + " has won. Refresh the browser to play again!");
}
});
