var score_list = {
    "score-tu": null,
    "score-1": null,
    "score-2": null,
    "score-3": null,
    "score-4": null,
    "score-5": null,
    "score-6": null,
    "score-st": null,
    "score-bo": null,
    "score-ch": null,
    "score-4k": null,
    "score-fh": null,
    "score-ss": null,
    "score-bs": null,
    "score-ya": null,
    "score-to": null
};
var temp = 0;

function fill_score(){
    for(var key in score_list) {
        var value = score_list[key];
        document.getElementById(key).innerHTML = temp;
    }
    temp += 1;
}

var dice_list = {
    "dice-1": null,
    "dice-2": null,
    "dice-3": null,
    "dice-4": null,
    "dice-5": null
};
function roll_die(){
    for(var key in dice_list) {
        var value = dice_list[key];
        document.getElementById(key).innerHTML = '<img src="images/dice-'+(Math.floor(Math.random() * 6) + 1).toString()+'.png" class="dice"/>';
    }
}