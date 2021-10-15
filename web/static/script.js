var score_list = {
    "score_tu": null,
    "score_1": null,
    "score_2": null,
    "score_3": null,
    "score_4": null,
    "score_5": null,
    "score_6": null,
    "score_st": null,
    "score_bo": null,
    "score_ch": null,
    "score_4k": null,
    "score_fh": null,
    "score_ss": null,
    "score_bs": null,
    "score_ya": null,
    "score_to": null
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