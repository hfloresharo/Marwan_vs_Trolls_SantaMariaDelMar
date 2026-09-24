import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MARWAN VS TROLLS",
    page_icon="👨‍🦲",
    layout="wide"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(
            180deg,
            #07152b 0%,
            #0b2d4d 45%,
            #d88b45 100%
        );
    }

    header {
        visibility: hidden;
    }

    .title {
        text-align: center;
        color: white;
        font-size: 42px;
        font-weight: 900;
        text-shadow: 4px 4px #000;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #ffe082;
        font-size: 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">👨‍🦲 MARWAN VS TROLLS 👹</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">VERSIÓN SANTA MARÍA DEL MAR, PERÚ 🇵🇪</div>',
    unsafe_allow_html=True
)

game = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>

body {
    margin: 0;
    overflow: hidden;
    background: #07152b;
    font-family: Arial;
}

#game {
    width: 100%;
    height: 650px;
    position: relative;
    overflow: hidden;
    border: 5px solid #111;
    border-radius: 18px;
    background:
        linear-gradient(
            #10294b 0%,
            #1c5271 55%,
            #d58a49 56%,
            #f0c078 100%
        );
}

#sun {
    position:absolute;
    width:90px;
    height:90px;
    border-radius:50%;
    background:#ffd54f;
    right:80px;
    top:50px;
    box-shadow:0 0 40px #ffd54f;
}

#sea {
    position:absolute;
    bottom:0;
    left:0;
    width:100%;
    height:42%;
    background:
        repeating-linear-gradient(
            0deg,
            #155d78 0px,
            #155d78 12px,
            #207a91 13px,
            #207a91 20px
        );
}

#score {
    position:absolute;
    top:15px;
    left:20px;
    z-index:100;
    color:white;
    font-size:22px;
    font-weight:bold;
    background:rgba(0,0,0,.55);
    padding:10px 18px;
    border-radius:12px;
}

#lives {
    position:absolute;
    top:15px;
    right:20px;
    z-index:100;
    color:#ff5252;
    font-size:22px;
    font-weight:bold;
    background:rgba(0,0,0,.55);
    padding:10px 18px;
    border-radius:12px;
}

#marwan {
    position:absolute;
    width:75px;
    height:110px;
    bottom:45px;
    left:100px;
    z-index:20;
}

.head {
    position:absolute;
    width:50px;
    height:50px;
    left:13px;
    top:0;
    background:#d99a6c;
    border-radius:50%;
    border:3px solid #222;
}

.face {
    position:absolute;
    left:9px;
    top:19px;
    font-size:22px;
}

.body {
    position:absolute;
    width:45px;
    height:48px;
    left:15px;
    top:50px;
    background:#263238;
    border-radius:12px 12px 5px 5px;
    border:3px solid #111;
}

.arm {
    position:absolute;
    width:42px;
    height:10px;
    background:#d99a6c;
    top:60px;
    border-radius:10px;
}

.arm.left {
    left:-13px;
    transform:rotate(-25deg);
}

.arm.right {
    right:-13px;
    transform:rotate(25deg);
}

.gun {
    position:absolute;
    width:35px;
    height:9px;
    background:#222;
    right:-32px;
    top:67px;
    border-radius:4px;
}

.leg {
    position:absolute;
    width:13px;
    height:38px;
    background:#111;
    top:94px;
    border-radius:5px;
}

.leg.left {
    left:22px;
}

.leg.right {
    left:43px;
}

.troll {
    position:absolute;
    width:70px;
    height:80px;
    z-index:15;
}

.troll-head {
    width:55px;
    height:55px;
    background:#72a93b;
    border-radius:50%;
    position:absolute;
    left:7px;
    top:5px;
    border:3px solid #18230e;
}

.troll-eye {
    position:absolute;
    width:9px;
    height:9px;
    background:white;
    border-radius:50%;
    top:22px;
}

.eye1 { left:20px; }
.eye2 { left:39px; }

.troll-mouth {
    position:absolute;
    width:27px;
    height:9px;
    background:#261414;
    border-radius:0 0 15px 15px;
    left:15px;
    top:37px;
}

.troll-body {
    position:absolute;
    width:45px;
    height:35px;
    background:#4e682d;
    left:12px;
    top:57px;
    border-radius:12px;
}

.troll-horn {
    position:absolute;
    width:0;
    height:0;
    border-left:13px solid transparent;
    border-right:13px solid transparent;
    border-bottom:25px solid #6e6e6e;
    top:-15px;
}

.horn1 { left:3px; }
.horn2 { right:3px; }

.bullet {
    position:absolute;
    width:13px;
    height:5px;
    background:#ffeb3b;
    border-radius:5px;
    box-shadow:0 0 15px #ff9800;
    z-index:50;
}

.explosion {
    position:absolute;
    font-size:45px;
    z-index:80;
    animation: boom .4s forwards;
}

@keyframes boom {
    from {
        transform:scale(.5);
        opacity:1;
    }

    to {
        transform:scale(1.8);
        opacity:0;
    }
}

#message {
    position:absolute;
    top:45%;
    left:50%;
    transform:translate(-50%,-50%);
    color:white;
    text-align:center;
    font-size:32px;
    font-weight:bold;
    z-index:200;
    text-shadow:3px 3px #000;
}

#start {
    margin-top:15px;
    padding:15px 35px;
    font-size:20px;
    font-weight:bold;
    border:none;
    border-radius:12px;
    background:#ffca28;
    cursor:pointer;
}

.controls {
    position:absolute;
    bottom:15px;
    left:50%;
    transform:translateX(-50%);
    z-index:200;
    display:flex;
    gap:12px;
}

.controls button {
    width:65px;
    height:55px;
    font-size:25px;
    border:none;
    border-radius:12px;
    background:rgba(0,0,0,.7);
    color:white;
    cursor:pointer;
}

.controls button:active {
    background:#ff9800;
}

</style>
</head>

<body>

<div id="game">

<div id="sun"></div>
<div id="sea"></div>

<div id="score">⭐ PUNTOS: 0</div>
<div id="lives">❤️❤️❤️</div>

<div id="message">
    MARWAN VS TROLLS
    <br>
    <span style="font-size:18px">
        Santa María del Mar
    </span>
    <br>
    <button id="start">🚀 COMENZAR</button>
</div>

<div id="marwan">

    <div class="head">
        <div class="face">😠</div>
    </div>

    <div class="body"></div>

    <div class="arm left"></div>
    <div class="arm right"></div>

    <div class="gun"></div>

    <div class="leg left"></div>
    <div class="leg right"></div>

</div>

<div class="controls">
    <button id="left">⬅️</button>
    <button id="shoot">🔫</button>
    <button id="right">➡️</button>
</div>

</div>

<script>

const game = document.getElementById("game");
const marwan = document.getElementById("marwan");
const scoreText = document.getElementById("score");
const livesText = document.getElementById("lives");
const message = document.getElementById("message");
const startButton = document.getElementById("start");

let playerX = 100;
let score = 0;
let lives = 3;
let playing = false;
let speed = 2.0;
let spawnRate = 1500;

let trolls = [];
let bullets = [];

function updatePlayer() {
    playerX = Math.max(
        10,
        Math.min(
            game.clientWidth - 90,
            playerX
        )
    );

    marwan.style.left = playerX + "px";
}

function createTroll() {

    if (!playing) return;

    const troll = document.createElement("div");
    troll.className = "troll";

    troll.innerHTML = `
        <div class="troll-head">
            <div class="troll-horn horn1"></div>
            <div class="troll-horn horn2"></div>
            <div class="troll-eye eye1"></div>
            <div class="troll-eye eye2"></div>
            <div class="troll-mouth"></div>
        </div>
        <div class="troll-body"></div>
    `;

    const x = Math.random() * (game.clientWidth - 90);

    troll.style.left = x + "px";
    troll.style.top = "-90px";

    game.appendChild(troll);

    trolls.push({
        element: troll,
        x: x,
        y: -90
    });
}

function shoot() {

    if (!playing) return;

    const bullet = document.createElement("div");

    bullet.className = "bullet";

    bullet.style.left = (playerX + 80) + "px";
    bullet.style.top =
        (game.clientHeight - 120) + "px";

    game.appendChild(bullet);

    bullets.push({
        element: bullet,
        x: playerX + 80,
        y: game.clientHeight - 120
    });
}

function explosion(x,y) {

    const boom = document.createElement("div");

    boom.className = "explosion";
    boom.innerHTML = "💥";

    boom.style.left = x + "px";
    boom.style.top = y + "px";

    game.appendChild(boom);

    setTimeout(() => boom.remove(), 400);
}

function gameLoop() {

    if (!playing) return;

    trolls.forEach((troll, ti) => {

        troll.y += speed;

        troll.element.style.top =
            troll.y + "px";

        // troll llegó a Marwan

        if (
            troll.y >
            game.clientHeight - 140
        ) {

            troll.element.remove();

            trolls.splice(ti,1);

            lives--;

            livesText.innerHTML =
                "❤️".repeat(Math.max(0,lives));

            if (lives <= 0) {
                gameOver();
            }
        }

    });

    bullets.forEach((bullet, bi) => {

        bullet.y -= 9;

        bullet.element.style.top =
            bullet.y + "px";

        if (bullet.y < -20) {

            bullet.element.remove();
            bullets.splice(bi,1);
            return;
        }

        trolls.forEach((troll, ti) => {

            const distanceX =
                Math.abs(
                    bullet.x - troll.x
                );

            const distanceY =
                Math.abs(
                    bullet.y - troll.y
                );

            if (
                distanceX < 65 &&
                distanceY < 65
            ) {

                explosion(
                    troll.x,
                    troll.y
                );

                troll.element.remove();
                bullet.element.remove();

                trolls.splice(ti,1);
                bullets.splice(bi,1);

                score += 10;

                scoreText.innerHTML =
                    "⭐ PUNTOS: " + score;

                if (score % 100 === 0) {
                    speed += .25;
                }

            }

        });

    });

    requestAnimationFrame(gameLoop);
}

function gameOver() {

    playing = false;

    message.style.display = "block";

    message.innerHTML = `
        💀 GAME OVER
        <br>
        <span style="font-size:20px">
        Marwan consiguió ${score} puntos
        </span>
        <br>
        <button id="restart"
        style="
        margin-top:15px;
        padding:15px 30px;
        font-size:20px;
        border:0;
        border-radius:12px;
        background:#ffca28;
        ">
        🔄 JUGAR DE NUEVO
        </button>
    `;

    document
        .getElementById("restart")
        .onclick = startGame;
}

function startGame() {

    trolls.forEach(t =>
        t.element.remove()
    );

    bullets.forEach(b =>
        b.element.remove()
    );

    trolls = [];
    bullets = [];

    score = 0;
    lives = 3;
    speed = 2.0;

    scoreText.innerHTML =
        "⭐ PUNTOS: 0";

    livesText.innerHTML =
        "❤️❤️❤️";

    playerX = 100;

    updatePlayer();

    playing = true;

    message.style.display = "none";

    gameLoop();

    setInterval(() => {

        if (playing) {
            createTroll();
        }

    }, spawnRate);
}

startButton.onclick = startGame;

document.addEventListener(
    "keydown",
    function(e) {

        if (!playing) return;

        if (
            e.key === "ArrowLeft" ||
            e.key.toLowerCase() === "a"
        ) {
            playerX -= 20;
            updatePlayer();
        }

        if (
            e.key === "ArrowRight" ||
            e.key.toLowerCase() === "d"
        ) {
            playerX += 20;
            updatePlayer();
        }

        if (
            e.key === " " ||
            e.key === "Enter"
        ) {
            shoot();
        }

    }
);

document.getElementById("left")
.onclick = () => {
    playerX -= 30;
    updatePlayer();
};

document.getElementById("right")
.onclick = () => {
    playerX += 30;
    updatePlayer();
};

document.getElementById("shoot")
.onclick = shoot;

updatePlayer();

</script>

</body>
</html>
"""

components.html(
    game,
    height=700,
    scrolling=False
)

st.markdown("""
<div style="
text-align:center;
color:white;
font-weight:bold;
padding:15px;
">
🎮 CONTROLES: ⬅️ ➡️ para moverse | ESPACIO para disparar
<br>
🇵🇪 MARWAN VS TROLLS — SANTA MARÍA DEL MAR
</div>
""", unsafe_allow_html=True)
