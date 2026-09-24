import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

# ---------------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------------
st.set_page_config(
    page_title="MARWAN VS TROLLS",
    page_icon="🏍️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# ARCHIVOS
# ---------------------------------------------------------
BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"

MARWAN_FILE = ASSETS_DIR / "marwan.png"
MUSIC_FILE = ASSETS_DIR / "musica.mp3"


# ---------------------------------------------------------
# CONVERTIR ARCHIVOS A BASE64
# ---------------------------------------------------------
def file_to_base64(file_path):
    if file_path.exists():
        with open(file_path, "rb") as file:
            return base64.b64encode(file.read()).decode()
    return ""


# Imagen
marwan_base64 = file_to_base64(MARWAN_FILE)

if marwan_base64:
    marwan_image = "data:image/png;base64," + marwan_base64
else:
    marwan_image = ""


# Música
music_base64 = file_to_base64(MUSIC_FILE)

if music_base64:
    music_source = "data:audio/mpeg;base64," + music_base64
else:
    music_source = ""


# ---------------------------------------------------------
# HTML DEL JUEGO
# ---------------------------------------------------------
game = """
<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width,
               initial-scale=1.0,
               maximum-scale=1.0,
               user-scalable=no">

<style>

* {
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}

html,
body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #111;
    font-family: Arial, sans-serif;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
}

#gameContainer {
    width: 100%;
    max-width: 900px;
    height: 720px;
    position: relative;
    overflow: hidden;
    background:
        linear-gradient(
            to bottom,
            #67c8ff 0%,
            #bdefff 55%,
            #f5d28b 56%,
            #d7a75c 100%
        );
    border-radius: 15px;
    border: 4px solid #222;
}

/* ----------------------------------------------------
   SOL
---------------------------------------------------- */

.sun {
    position: absolute;
    width: 90px;
    height: 90px;
    background: #ffd43b;
    border-radius: 50%;
    right: 35px;
    top: 25px;
    box-shadow: 0 0 35px #ffd43b;
}

/* ----------------------------------------------------
   MARWAN
---------------------------------------------------- */

#player {
    position: absolute;
    width: 90px;
    height: 120px;
    bottom: 75px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 20;
}

.player-body {
    position: absolute;
    width: 45px;
    height: 55px;
    background: #1769aa;
    border-radius: 15px 15px 8px 8px;
    left: 23px;
    top: 48px;
}

.player-head {
    position: absolute;
    width: 58px;
    height: 58px;
    background: #e5a16f;
    border-radius: 50%;
    left: 16px;
    top: 0;
    overflow: hidden;
}

.player-head img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
}

.player-face {
    position: absolute;
    width: 58px;
    height: 58px;
    left: 16px;
    top: 0;
    border-radius: 50%;
    background: #e5a16f;
}

.eye {
    position: absolute;
    width: 6px;
    height: 6px;
    background: #222;
    border-radius: 50%;
    top: 22px;
}

.eye.left {
    left: 17px;
}

.eye.right {
    right: 17px;
}

.mouth {
    position: absolute;
    width: 20px;
    height: 7px;
    border-bottom: 3px solid #222;
    border-radius: 50%;
    left: 19px;
    top: 37px;
}

.arm {
    position: absolute;
    width: 13px;
    height: 42px;
    background: #e5a16f;
    border-radius: 10px;
    top: 53px;
}

.arm.left {
    left: 9px;
    transform: rotate(20deg);
}

.arm.right {
    right: 9px;
    transform: rotate(-20deg);
}

.leg {
    position: absolute;
    width: 15px;
    height: 35px;
    background: #333;
    border-radius: 8px;
    top: 98px;
}

.leg.left {
    left: 24px;
}

.leg.right {
    right: 24px;
}

.gun {
    position: absolute;
    width: 48px;
    height: 12px;
    background: #222;
    right: -12px;
    top: 63px;
    border-radius: 5px;
}

/* ----------------------------------------------------
   TROLL
---------------------------------------------------- */

.troll {
    position: absolute;
    width: 62px;
    height: 70px;
    z-index: 10;
}

.troll-head {
    position: absolute;
    width: 52px;
    height: 52px;
    background: #6b38a8;
    border-radius: 50%;
    left: 5px;
    top: 5px;
}

.troll-eye {
    position: absolute;
    width: 10px;
    height: 10px;
    background: white;
    border-radius: 50%;
    top: 18px;
}

.troll-eye::after {
    content: "";
    position: absolute;
    width: 5px;
    height: 5px;
    background: black;
    border-radius: 50%;
    left: 2px;
    top: 2px;
}

.troll-eye.left {
    left: 14px;
}

.troll-eye.right {
    right: 14px;
}

.troll-mouth {
    position: absolute;
    width: 27px;
    height: 12px;
    background: #222;
    border-radius: 0 0 20px 20px;
    left: 13px;
    top: 33px;
}

.troll-horn {
    position: absolute;
    width: 15px;
    height: 22px;
    background: #e8e8e8;
    top: -13px;
    border-radius: 50% 50% 20% 20%;
}

.troll-horn.left {
    left: 4px;
    transform: rotate(-20deg);
}

.troll-horn.right {
    right: 4px;
    transform: rotate(20deg);
}

/* ----------------------------------------------------
   DISPARO
---------------------------------------------------- */

.bullet {
    position: absolute;
    width: 9px;
    height: 20px;
    background: #ffe600;
    border-radius: 5px;
    z-index: 15;
    box-shadow: 0 0 10px #ffae00;
}

/* ----------------------------------------------------
   INFORMACIÓN
---------------------------------------------------- */

#hud {
    position: absolute;
    left: 12px;
    top: 12px;
    z-index: 100;
    background: rgba(0,0,0,0.65);
    color: white;
    padding: 10px 14px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

#title {
    position: absolute;
    top: 10px;
    left: 50%;
    transform: translateX(-50%);
    color: white;
    font-size: 24px;
    font-weight: bold;
    text-shadow: 3px 3px 4px #000;
    z-index: 90;
    text-align: center;
    white-space: nowrap;
}

#message {
    position: absolute;
    top: 45%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: rgba(0,0,0,0.82);
    color: white;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    z-index: 200;
    min-width: 280px;
}

#message h2 {
    margin-top: 0;
}

button {
    border: none;
    border-radius: 15px;
    padding: 13px 20px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
}

/* ----------------------------------------------------
   CONTROLES MÓVILES
---------------------------------------------------- */

#mobileControls {
    position: absolute;
    bottom: 12px;
    left: 0;
    width: 100%;
    z-index: 150;
    display: flex;
    justify-content: space-between;
    padding: 0 15px;
    pointer-events: none;
}

.controlGroup {
    display: flex;
    gap: 12px;
    pointer-events: auto;
}

.controlButton {
    width: 72px;
    height: 60px;
    border-radius: 18px;
    background: rgba(0,0,0,0.72);
    color: white;
    font-size: 28px;
    user-select: none;
    touch-action: none;
}

.shootButton {
    width: 90px;
    background: rgba(200,30,30,0.85);
    font-size: 20px;
}

#musicButton {
    position: absolute;
    top: 12px;
    right: 12px;
    z-index: 110;
    width: 48px;
    height: 48px;
    padding: 0;
    background: rgba(0,0,0,0.65);
    color: white;
    border-radius: 50%;
    font-size: 22px;
}

/* ----------------------------------------------------
   RESPONSIVE
---------------------------------------------------- */

@media (max-width: 600px) {

    #gameContainer {
        height: 700px;
        border-radius: 8px;
        border-width: 2px;
    }

    #title {
        font-size: 18px;
        top: 10px;
    }

    #hud {
        font-size: 15px;
        padding: 8px 10px;
    }

    .controlButton {
        width: 65px;
        height: 58px;
    }

    .shootButton {
        width: 82px;
    }

}

</style>

</head>

<body>

<div id="gameContainer">

    <div class="sun"></div>

    <div id="title">
        🏍️ MARWAN VS TROLLS
    </div>

    <div id="hud">
        Puntos: <span id="score">0</span>
        &nbsp;&nbsp;
        ❤️ <span id="lives">3</span>
    </div>

    <button id="musicButton">🔇</button>

    <div id="player">

        <div class="player-head" id="playerHead"></div>

        <div class="player-body"></div>

        <div class="arm left"></div>
        <div class="arm right"></div>

        <div class="leg left"></div>
        <div class="leg right"></div>

        <div class="gun"></div>

    </div>

    <div id="mobileControls">

        <div class="controlGroup">

            <button
                class="controlButton"
                id="leftButton">
                ◀
            </button>

            <button
                class="controlButton"
                id="rightButton">
                ▶
            </button>

        </div>

        <div class="controlGroup">

            <button
                class="controlButton shootButton"
                id="shootButton">
                🔫
            </button>

        </div>

    </div>

    <div id="message">

        <h2>🏖️ SANTA MARÍA DEL MAR</h2>

        <p>
            MARWAN VS TROLLS
        </p>

        <p>
            🎯 ¡Dispara a los trolls!
        </p>

        <button id="startButton">
            ▶ EMPEZAR
        </button>

    </div>

    <audio id="music" loop></audio>

</div>


<script>

/* =====================================================
   VARIABLES
===================================================== */

const game = document.getElementById("gameContainer");

const player = document.getElementById("player");

const scoreElement = document.getElementById("score");

const livesElement = document.getElementById("lives");

const message = document.getElementById("message");

const startButton = document.getElementById("startButton");

const musicButton = document.getElementById("musicButton");

const music = document.getElementById("music");

const playerHead = document.getElementById("playerHead");

const leftButton = document.getElementById("leftButton");

const rightButton = document.getElementById("rightButton");

const shootButton = document.getElementById("shootButton");


let score = 0;

let lives = 3;

let gameRunning = false;

let playerX = 50;

let keys = {};

let trollTimer = null;

let animationFrame = null;

let musicPlaying = false;


/* =====================================================
   IMAGEN DE MARWAN
===================================================== */

const marwanImage = "__MARWAN_IMAGE__";

if (marwanImage !== "") {

    playerHead.innerHTML =
        '<img src="' +
        marwanImage +
        '" alt="Marwan">';

}


/* =====================================================
   MÚSICA
===================================================== */

const musicSource = "__MUSIC_SOURCE__";

if (musicSource !== "") {

    music.src = musicSource;

}


/* =====================================================
   MÚSICA
===================================================== */

function startMusic() {

    if (musicSource === "") {
        return;
    }

    music.volume = 0.35;

    music.play()
        .then(function() {

            musicPlaying = true;
            musicButton.textContent = "🔊";

        })
        .catch(function() {

            musicPlaying = false;

        });

}


musicButton.addEventListener(
    "click",
    function() {

        if (musicSource === "") {

            alert(
                "Coloca el archivo musica.mp3 dentro de la carpeta assets."
            );

            return;

        }

        if (musicPlaying) {

            music.pause();

            musicPlaying = false;

            musicButton.textContent = "🔇";

        } else {

            music.play()
                .then(function() {

                    musicPlaying = true;
                    musicButton.textContent = "🔊";

                });

        }

    }
);


/* =====================================================
   INICIAR JUEGO
===================================================== */

startButton.addEventListener(
    "click",
    startGame
);


function startGame() {

    score = 0;

    lives = 3;

    playerX = 50;

    gameRunning = true;

    scoreElement.textContent = score;

    livesElement.textContent = lives;

    player.style.left = playerX + "%";

    message.style.display = "none";

    document
        .querySelectorAll(".troll")
        .forEach(function(troll) {

            troll.remove();

        });

    document
        .querySelectorAll(".bullet")
        .forEach(function(bullet) {

            bullet.remove();

        });

    startMusic();

    startTrollSpawner();

    gameLoop();

}


/* =====================================================
   CONTROLES DE TECLADO
===================================================== */

document.addEventListener(
    "keydown",
    function(event) {

        keys[event.key.toLowerCase()] = true;

        if (
            event.key === " " ||
            event.key === "Enter"
        ) {

            event.preventDefault();

            if (gameRunning) {
                shoot();
            }

        }

    }
);


document.addEventListener(
    "keyup",
    function(event) {

        keys[event.key.toLowerCase()] = false;

    }
);


/* =====================================================
   BOTONES MÓVILES
===================================================== */

function setupMoveButton(button, direction) {

    button.addEventListener(
        "pointerdown",
        function(event) {

            event.preventDefault();

            keys[direction] = true;

        }
    );

    button.addEventListener(
        "pointerup",
        function(event) {

            event.preventDefault();

            keys[direction] = false;

        }
    );

    button.addEventListener(
        "pointercancel",
        function() {

            keys[direction] = false;

        }
    );

    button.addEventListener(
        "pointerleave",
        function() {

            keys[direction] = false;

        }
    );

}


setupMoveButton(
    leftButton,
    "arrowleft"
);


setupMoveButton(
    rightButton,
    "arrowright"
);


shootButton.addEventListener(
    "pointerdown",
    function(event) {

        event.preventDefault();

        if (gameRunning) {
            shoot();
        }

    }
);


/* =====================================================
   MOVIMIENTO
===================================================== */

function movePlayer() {

    if (!gameRunning) {
        return;
    }

    const gameWidth =
        game.clientWidth;

    const playerWidth =
        player.offsetWidth;

    const speed = 0.8;

    if (
        keys["arrowleft"] ||
        keys["a"]
    ) {

        playerX -= speed;

    }

    if (
        keys["arrowright"] ||
        keys["d"]
    ) {

        playerX += speed;

    }

    if (playerX < 7) {
        playerX = 7;
    }

    if (playerX > 93) {
        playerX = 93;
    }

    player.style.left =
        playerX + "%";

}


/* =====================================================
   DISPARAR
===================================================== */

function shoot() {

    if (!gameRunning) {
        return;
    }

    const bullet =
        document.createElement("div");

    bullet.className = "bullet";

    const playerRect =
        player.getBoundingClientRect();

    const gameRect =
        game.getBoundingClientRect();

    const bulletX =
        playerRect.left -
        gameRect.left +
        playerRect.width / 2;

    const bulletY =
        playerRect.top -
        gameRect.top -
        20;

    bullet.style.left =
        bulletX + "px";

    bullet.style.top =
        bulletY + "px";

    game.appendChild(bullet);

    moveBullet(bullet);

}


/* =====================================================
   MOVIMIENTO DE BALA
===================================================== */

function moveBullet(bullet) {

    let y =
        parseFloat(bullet.style.top);

    const speed = 8;

    function animateBullet() {

        if (!bullet.parentElement) {
            return;
        }

        y -= speed;

        bullet.style.top =
            y + "px";

        if (y < -30) {

            bullet.remove();

            return;

        }

        checkBulletCollision(bullet);

        if (bullet.parentElement) {

            requestAnimationFrame(
                animateBullet
            );

        }

    }

    requestAnimationFrame(
        animateBullet
    );

}


/* =====================================================
   COLISIÓN
===================================================== */

function checkBulletCollision(bullet) {

    const bulletRect =
        bullet.getBoundingClientRect();

    const trolls =
        document.querySelectorAll(".troll");

    trolls.forEach(
        function(troll) {

            const trollRect =
                troll.getBoundingClientRect();

            if (
                bulletRect.left <
                    trollRect.right &&
                bulletRect.right >
                    trollRect.left &&
                bulletRect.top <
                    trollRect.bottom &&
                bulletRect.bottom >
                    trollRect.top
            ) {

                troll.remove();

                bullet.remove();

                score += 10;

                scoreElement.textContent =
                    score;

            }

        }
    );

}


/* =====================================================
   CREAR TROLL
===================================================== */

function createTroll() {

    if (!gameRunning) {
        return;
    }

    const troll =
        document.createElement("div");

    troll.className = "troll";

    troll.innerHTML = `

        <div class="troll-head">

            <div class="troll-horn left"></div>

            <div class="troll-horn right"></div>

            <div class="troll-eye left"></div>

            <div class="troll-eye right"></div>

            <div class="troll-mouth"></div>

        </div>

    `;

    const maxX =
        game.clientWidth - 70;

    const x =
        Math.random() * maxX;

    troll.style.left =
        x + "px";

    troll.style.top =
        "-80px";

    game.appendChild(troll);

    moveTroll(troll);

}


/* =====================================================
   MOVIMIENTO DE TROLL
===================================================== */

function moveTroll(troll) {

    let y =
        parseFloat(troll.style.top);

    /*
       VELOCIDAD LENTA
    */

    let speed = 0.55;

    /*
       Aumenta muy poco
       conforme sube el puntaje
    */

    speed +=
        Math.floor(score / 100) * 0.05;


    function animateTroll() {

        if (!troll.parentElement) {
            return;
        }

        y += speed;

        troll.style.top =
            y + "px";


        const playerRect =
            player.getBoundingClientRect();

        const trollRect =
            troll.getBoundingClientRect();


        /* ---------------------------------------------
           TROLL TOCA AL JUGADOR
        --------------------------------------------- */

        if (
            trollRect.bottom >=
                playerRect.top &&
            trollRect.left <
                playerRect.right &&
            trollRect.right >
                playerRect.left
        ) {

            troll.remove();

            loseLife();

            return;

        }


        /* ---------------------------------------------
           TROLL LLEGA AL SUELO
        --------------------------------------------- */

        if (
            y >
            game.clientHeight - 110
        ) {

            troll.remove();

            loseLife();

            return;

        }


        requestAnimationFrame(
            animateTroll
        );

    }

    requestAnimationFrame(
        animateTroll
    );

}


/* =====================================================
   PERDER VIDA
===================================================== */

function loseLife() {

    if (!gameRunning) {
        return;
    }

    lives--;

    livesElement.textContent =
        lives;

    if (lives <= 0) {

        gameOver();

    }

}


/* =====================================================
   GAME OVER
===================================================== */

function gameOver() {

    gameRunning = false;

    if (trollTimer) {

        clearInterval(
            trollTimer
        );

        trollTimer = null;

    }

    if (animationFrame) {

        cancelAnimationFrame(
            animationFrame
        );

    }

    message.innerHTML = `

        <h2>💥 GAME OVER</h2>

        <p>
            Puntuación:
            <strong>${score}</strong>
        </p>

        <p>
            🏖️ Santa María del Mar
        </p>

        <button id="restartButton">
            🔄 JUGAR DE NUEVO
        </button>

    `;

    message.style.display =
        "block";


    document
        .getElementById("restartButton")
        .addEventListener(
            "click",
            startGame
        );

}


/* =====================================================
   GENERADOR DE TROLLS
===================================================== */

function startTrollSpawner() {

    if (trollTimer) {

        clearInterval(
            trollTimer
        );

    }

    trollTimer =
        setInterval(
            function() {

                createTroll();

            },
            3000
        );

}


/* =====================================================
   LOOP DEL JUEGO
===================================================== */

function gameLoop() {

    if (!gameRunning) {
        return;
    }

    movePlayer();

    animationFrame =
        requestAnimationFrame(
            gameLoop
        );

}

</script>

</body>
</html>
"""


# ---------------------------------------------------------
# INSERTAR IMAGEN Y MÚSICA
# ---------------------------------------------------------

game = game.replace(
    "__MARWAN_IMAGE__",
    marwan_image
)

game = game.replace(
    "__MUSIC_SOURCE__",
    music_source
)


# ---------------------------------------------------------
# MOSTRAR JUEGO
# ---------------------------------------------------------

components.html(
    game,
    height=730,
    scrolling=False
)
