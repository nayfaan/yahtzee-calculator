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
        var new_face = (Math.floor(Math.random() * 6) + 1).toString();
        var dice = $('#'+key);
        dice.attr('src', 'images/dice-'+new_face+'.png');
        dice.attr('data-face', new_face);
    }
}

function lock_change(dice){
    if (dice.src.match(/dice-(\d)/i)[1] != 0){
        var lock = document.getElementById(dice.id.replace("dice", "lock"));
        var is_locked = $(dice).data("locked");
        $(dice).attr("data-locked", $(dice).attr("data-locked") == '0' ? '1' : '0');
        if ($(dice).attr("data-locked") == 1){
            $(lock).css("opacity", 1);
        }else{
            $(lock).css("opacity", 0);
        }
        //stackoverflow.com/questions/3807736
    }
}

var interval;
$('#roll-button').on("mousedown", function () {
    interval = window.setInterval(roll_die, 1);
});
$(document).mouseup(function(){
    window.clearInterval(interval);
});