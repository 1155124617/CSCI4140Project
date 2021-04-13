
// JavaScript source code
var number = 4;
var hash = new Array();
for (var i = 0; i < 4; i++) {
    hash[i] = 0;
}
var Game = {
    UID: "test1",
    physical_health: 50,
    mental_health: 50,
    money: 50,
    academic: 50,
    question_ID: 0,
    round: 0,
    flag: true,
    ask_question: function (number) {
        var id = Math.round(Math.random() * (number-1));
        this.question_ID = id;
    },
    update_physical: function (point) {
        this.physical_health += point;
        if (this.physical_health >= 100) {
            this.physical_health = 100;
        }
        if (this.physical_health >= 66) {
            document.getElementById("physical").style.color = "green";
            document.getElementById("physical1").style.color = "green";
        }
        if (this.physical_health < 66 && this.physical_health > 33) {
            document.getElementById("physical").style.color = "goldenrod";
            document.getElementById("physical1").style.color = "goldenrod";
        }
        if (this.physical_health <= 33 && this.physical_health > 0) {
            document.getElementById("physical").style.color = "red";
            document.getElementById("physical1").style.color = "red";
        }
        if (this.physical_health <= 0) {
            document.getElementById("physical").style.color = "black";
            document.getElementById("physical1").style.color = "black";
        }
    },
    update_mental: function (point) {
        this.mental_health += point;
        if (this.mental_health >= 100) {
            this.mental_health = 100;
        }
        if (this.mental_health >= 66) {
            document.getElementById("mental").style.color = "green";
            document.getElementById("mental1").style.color = "green";
        }
        if (this.mental_health < 66 && this.mental_health > 33) {
            document.getElementById("mental").style.color = "goldenrod";
            document.getElementById("mental1").style.color = "goldenrod";
        }
        if (this.mental_health <= 33 && this.mental_health > 0) {
            document.getElementById("mental").style.color = "red";
            document.getElementById("mental1").style.color = "red";
        }
        if (this.mental_health <= 0) {
            document.getElementById("mental").style.color = "black";
            document.getElementById("mental1").style.color = "black";
        }
    },
    update_money: function (point) {
        this.money += point;
        if (this.money >= 100) {
            this.money = 100;
        }
        if (this.money >= 66) {
            document.getElementById("money").style.color = "green";
            document.getElementById("money1").style.color = "green";
        }
        if (this.money < 66 && this.money > 33) {
            document.getElementById("money").style.color = "goldenrod";
            document.getElementById("money1").style.color = "goldenrod";
        }
        if (this.money <= 33 && this.money > 0) {
            document.getElementById("money").style.color = "red";
            document.getElementById("money1").style.color = "red";
        }
        if (this.money <= 0) {
            document.getElementById("money").style.color = "black";
            document.getElementById("money1").style.color = "black";
        }
    },
    update_academic: function (point) {
        this.academic += point;
        if (this.academic >= 100) {
            this.academic = 100;
        }
        if (this.academic >= 66) {
            document.getElementById("academic").style.color = "green";
            document.getElementById("academic1").style.color = "green";
        }
        if (this.academic < 66 && this.academic > 33) {
            document.getElementById("academic").style.color = "goldenrod";
            document.getElementById("academic1").style.color = "goldenrod";
        }
        if (this.academic <= 33 && this.academic > 0) {
            document.getElementById("academic").style.color = "red";
            document.getElementById("academic1").style.color = "red";
        }
        if (this.academic <= 0) {
            document.getElementById("academic").style.color = "black";
            document.getElementById("academic1").style.color = "black";
        }
    },
    game_over: function () {
        if (this.physical_health <= 0 || this.mental_health <= 0 || this.money <= 0 || this.academic <= 0 || this.round > 3) {
            alert("Game over!");
            this.reset();
            return 1;
        }
        return 0;
    },
    load_save: function () {

    },
    upload_save: function () {

    },
    reset: function () {
        location.reload(true);
    }
};
var Event1 = {
    question_ID: 0,
    title: "Your Best Friend",
    content: "Do you wanna go for a gym?",
    img: "images/1.jpg",
    physical_1: 30,
    physical_2: -27,
    mental_1: 15,
    mental_2: 0,
    money_1: -14,
    money_2: 0,
    academic_1: -10,
    academic_2: 10

}
var Event2 = {
    question_ID: 1,
    title: "Your Target",
    content: "Let's go for a date tonight.",
    img: "images/2.jpg",
    physical_1: -25,
    physical_2: 0,
    mental_1: 35,
    mental_2: 0,
    money_1: -30,
    money_2: 0,
    academic_1: -10,
    academic_2: 10
}
var Event3 = {
    question_ID: 2,
    title: "Your Professor" ,
    content: "Do you wanna have a lunch talk with me?",
    img: "images/3.jpg",
    physical_1: 30,
    physical_2: -27,
    mental_1: 15,
    mental_2: 0,
    money_1: -14,
    money_2: 0,
    academic_1: -10,
    academic_2: 10
}
var Event4 = {
    question_ID: 3,
    title: "The Final Exam is comming!",
    content: "You have just downloaded the newest 'Monster hunter' Game and you have to struggle to choose whether playing the game or reviewing for the exam. Do you wanna play the game?",
    img: "images/4.jpg",
    physical_1: 30,
    physical_2: -27,
    mental_1: 15,
    mental_2: 0,
    money_1: -14,
    money_2: 0,
    academic_1: -10,
    academic_2: 10
}
var question = [Event1, Event2, Event3, Event4];
$(document).ready(function () {
    $("img.page1").attr('src', question[Game.question_ID].img);
    $("h1.page1").html(question[Game.question_ID].title);
    $("p.page1").html(question[Game.question_ID].content);
    $(".disagree").click(function () {
        Game.round++;
        hash[Game.question_ID] = 1;
        Game.update_physical(question[Game.question_ID].physical_2);
        Game.update_mental(question[Game.question_ID].mental_2);
        Game.update_money(question[Game.question_ID].money_2);
        Game.update_academic(question[Game.question_ID].academic_2);
        if (Game.game_over() == 0) {
            while (hash[Game.question_ID] == 1) {
                Game.ask_question(number);
                console.log(Game.question_ID);
            }
            if (Game.flag == true) {
                $("img.page2").attr('src', question[Game.question_ID].img);
                $("h1.page2").html(question[Game.question_ID].title);
                $("p.page2").html(question[Game.question_ID].content);
            } else {
                $("img.page1").attr('src', question[Game.question_ID].img);
                $("h1.page1").html(question[Game.question_ID].title);
                $("p.page1").html(question[Game.question_ID].content);
            }
            Game.flag = !Game.flag;
        }
    });
    $(".agree").click(function () {
        Game.round++;
        hash[Game.question_ID] = 1;
        Game.update_physical(question[Game.question_ID].physical_1);
        Game.update_mental(question[Game.question_ID].mental_1);
        Game.update_money(question[Game.question_ID].money_1);
        Game.update_academic(question[Game.question_ID].academic_1);
        if (Game.game_over() == 0) {
            while (hash[Game.question_ID] == 1) {
                Game.ask_question(number);
                console.log(Game.question_ID);
            }
            if (Game.flag == true) {
                $("img.page2").attr('src', question[Game.question_ID].img);
                $("h1.page2").html(question[Game.question_ID].title);
                $("p.page2").html(question[Game.question_ID].content);
            } else {
                $("img.page1").attr('src', question[Game.question_ID].img);
                $("h1.page1").html(question[Game.question_ID].title);
                $("p.page1").html(question[Game.question_ID].content);
            }
            Game.flag = !Game.flag;
        }
    });
});

