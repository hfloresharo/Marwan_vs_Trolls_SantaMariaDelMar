import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MARWAN VS TROLLS",
    page_icon="👨‍🦲",
    layout="wide",
    initial_sidebar_state="collapsed"
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

.block-container {
    padding: 0.5rem;
}

.title {
    text-align: center;
    color: white;
    font-size: clamp(25px, 6vw, 42px);
    font-weight: 900;
    text-shadow: 4px 4px #000;
    margin-bottom: 0;
}

.subtitle {
    text-align: center;
    color: #ffe082;
    font-size: clamp(14px, 4vw, 20px);
    font-weight: bold;
    margin-bottom: 5px;
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


game = r"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width,
initial-scale=1.0,
maximum-scale=1.0,
user-scalable=no">


<style>

/* =========================
   CONFIGURACIÓN GENERAL
========================= */

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

    background: #07152b;

    font-family: Arial, sans-serif;

    touch-action: none;
}


/* =========================
   JUEGO
========================= */

#game {

    width: 100%;
    height: min(650px, 82vh);

    min-height: 520px;

    position: relative;

    overflow: hidden;

    border: 4px solid #111;

    border-radius: 18px;

    background:
        linear-gradient(
            #10294b 0%,
            #1c5271 55%,
            #d58a49 56%,
            #f0c078 100%
        );

    touch-action: none;
}


/* =========================
   SOL
========================= */

#sun {

    position: absolute;

    width: 70px;
    height: 70px;

    border-radius: 50%;

    background: #ffd54f;

    right: 8%;

    top: 8%;

    box-shadow:
        0 0 30px #ffd54f;
}


/* =========================
   MAR
========================= */

#sea {

    position: absolute;

    bottom: 0;
    left: 0;

    width: 100%;
    height: 42%;

    background:
        repeating-linear-gradient(
            0deg,
            #155d78 0px,
            #155d78 12px,
            #207a91 13px,
            #207a91 20px
        );
}


/* =========================
   PUNTAJE
========================= */

#score {

    position: absolute;

    top: 10px;
    left: 10px;

    z-index: 100;

    color: white;

    font-size: clamp(15px, 4vw, 22px);

    font-weight: bold;

    background: rgba(0,0,0,.55);

    padding: 7px 12px;

    border-radius: 10px;
}


/* =========================
   VIDAS
========================= */

#lives {

    position: absolute;

    top: 10px;
    right: 10px;

    z-index: 100;

    color: #ff5252;

    font-size: clamp(15px, 4vw, 22px);

    font-weight: bold;

    background: rgba(0,0,0,.55);

    padding: 7px 12px;

    border-radius: 10px;
}


/* =========================
   MARWAN
========================= */

#marwan {

    position: absolute;

    width: 75px;
    height: 110px;

    bottom: 85px;

    left: 100px;

    z-index: 20;

    transform-origin: bottom center;
}


/* CABEZA */

.head {

    position: absolute;

    width: 50px;
    height: 50px;

    left: 13px;
    top: 0;

    background: #d99a6c;

    border-radius: 50%;

    border: 3px solid #222;
}


/* CARA */

.face {

    position: absolute;

    left: 9px;
    top: 19px;

    font-size: 22px;
}


/* CUERPO */

.body {

    position: absolute;

    width: 45px;
    height: 48px;

    left: 15px;
    top: 50px;

    background: #263238;

    border-radius: 12px 12px 5px 5px;

    border: 3px solid #111;
}


/* BRAZOS */

.arm {

    position: absolute;

    width: 42px;
    height: 10px;

    background: #d99a6c;

    top: 60px;

    border-radius: 10px;
}

.arm.left {

    left: -13px;

    transform:
        rotate(-25deg);
}

.arm.right {

    right: -13px;

    transform:
        rotate(25deg);
}


/* ARMA */

.gun {

    position: absolute;

    width: 35px;
    height: 9px;

    background: #222;

    right: -32px;

    top: 67px;

    border-radius: 4px;
}


/* PIERNAS */

.leg {

    position: absolute;

    width: 13px;
    height: 38px;

    background: #111;

    top: 94px;

    border-radius: 5px;
}

.leg.left {
    left: 22px;
}

.leg.right {
    left: 43px;
}


/* =========================
   TROLL
========================= */

.troll {

    position: absolute;

    width: 70px;
    height: 80px;

    z-index: 15;
}


.troll-head {

    width: 55px;
    height: 55px;

    background: #72a93b;

    border-radius: 50%;

    position: absolute;

    left: 7px;
    top: 5px;

    border: 3px solid #18230e;
}


.troll-eye {

    position: absolute;

    width: 9px;
    height: 9px;

    background: white;

    border-radius: 50%;

    top: 22px;
}


.eye1 {
    left: 20px;
}

.eye2 {
    left: 39px;
}


.troll-mouth {

    position: absolute;

    width: 27px;
    height: 9px;

    background: #261414;

    border-radius:
        0 0 15px 15px;

    left: 15px;
    top: 37px;
}


.troll-body {

    position: absolute;

    width: 45px;
    height: 35px;

    background: #4e682d;

    left: 12px;
    top: 57px;

    border-radius: 12px;
}


.troll-horn {

    position: absolute;

    width: 0;
    height: 0;

    border-left: 13px solid transparent;
    border-right: 13px solid transparent;

    border-bottom:
        25px solid #6e6e6e;

    top: -15px;
}


.horn1 {
    left: 3px;
}

.horn2 {
    right: 3px;
}


/* =========================
   BALAS
========================= */

.bullet {

    position: absolute;

    width: 13px;
    height: 5px;

    background: #ffeb3b;

    border-radius: 5px;

    box-shadow:
        0 0 15px #ff9800;

    z-index: 50;
}


/* =========================
   EXPLOSIÓN
========================= */

.explosion {

    position: absolute;

    font-size: 45px;

    z-index: 80;

    animation:
        boom .4s forwards;
}


@keyframes boom {

    from {

        transform:
            scale(.5);

        opacity: 1;
    }

    to {

        transform:
            scale(1.8);

        opacity: 0;
    }
}


/* =========================
   MENSAJE INICIAL
========================= */

#message {

    position: absolute;

    top: 43%;
    left: 50%;

    transform:
        translate(-50%, -50%);

    width: 90%;

    color: white;

    text-align: center;

    font-size:
        clamp(23px, 7vw, 32px);

    font-weight: bold;

    z-index: 200;

    text-shadow:
        3px 3px #000;
}


#start,
#restart {

    margin-top: 15px;

    padding:
        14px 28px;

    font-size: 19px;

    font-weight: bold;

    border: none;

    border-radius: 12px;

    background: #ffca28;

    cursor: pointer;

    touch-action: manipulation;
}


/* =========================
   CONTROLES CELULAR
========================= */

.controls {

    position: absolute;

    bottom: 12px;

    left: 50%;

    transform:
        translateX(-50%);

    z-index: 200;

    width: 95%;

    display: flex;

    justify-content:
        space-between;

    align-items: center;

    pointer-events: none;
}


.control-group {

    display: flex;

    gap: 12px;

    pointer-events: auto;
}


.controls button {

    width: 70px;
    height: 60px;

    font-size: 27px;

    border: 2px solid
        rgba(255,255,255,.4);

    border-radius: 15px;

    background:
        rgba(0,0,0,.70);

    color: white;

    cursor: pointer;

    touch-action: manipulation;

    user-select: none;

    -webkit-user-select: none;

    box-shadow:
        0 4px 8px
        rgba(0,0,0,.4);
}


.controls button:active {

    transform:
        scale(.90);

    background:
        #ff9800;
}


/* BOTÓN DISPARO MÁS GRANDE */

#shoot {

    width: 85px;
    height: 70px;

    font-size: 32px;

    background:
        rgba(180,30,20,.85);
}


/* =========================
   CELULAR VERTICAL
========================= */

@media (max-width: 600px) {

    #game {

        height: 620px;

        min-height: 520px;

        border-radius: 12px;

        border-width: 3px;
    }


    #marwan {

        bottom: 90px;

    }


    .controls {

        bottom: 10px;

        width: 94%;
    }


    .controls button {

        width: 62px;
        height: 58px;

        font-size: 25px;
    }


    #shoot {

        width: 78px;
        height: 65px;

        font-size: 29px;
    }

}


/* =========================
   CELULAR PEQUEÑO
========================= */

@media (max-width: 380px) {

    #game {

        height: 560px;

        min-height: 500px;
    }


    .controls button {

        width: 55px;
        height: 52px;

        font-size: 22px;
    }


    #shoot {

        width: 68px;
        height: 58px;
    }

}

</style>

</head>


<body>


<div id="game">


    <div id="sun"></div>


    <div id="sea"></div>


    <div id="score">

        ⭐ PUNTOS: 0

    </div>


    <div id="lives">

        ❤️❤️❤️

    </div>


    <!-- MENSAJE -->

    <div id="message">

        👨‍🦲 MARWAN VS TROLLS

        <br>

        <span
        style="font-size:18px">

            Santa María del Mar 🇵🇪

        </span>

        <br>

        <button id="start">

            🚀 COMENZAR

        </button>

    </div>


    <!-- MARWAN -->

    <div id="marwan">

        <div class="head">

            <div class="face">

                😠

            </div>

        </div>


        <div class="body"></div>


        <div class="arm left"></div>


        <div class="arm right"></div>


        <div class="gun"></div>


        <div class="leg left"></div>


        <div class="leg right"></div>

    </div>


    <!-- CONTROLES PARA CELULAR -->

    <div class="controls">


        <div class="control-group">

            <button id="left">

                ⬅️

            </button>


            <button id="right">

                ➡️

            </button>

        </div>


        <div class="control-group">

            <button id="shoot">

                🔫

            </button>

        </div>


    </div>


</div>


<script>

/* ==========================
   VARIABLES
========================== */


const game =
    document.getElementById(
        "game"
    );


const marwan =
    document.getElementById(
        "marwan"
    );


const scoreText =
    document.getElementById(
        "score"
    );


const livesText =
    document.getElementById(
        "lives"
    );


const message =
    document.getElementById(
        "message"
    );


const startButton =
    document.getElementById(
        "start"
    );


let playerX = 100;

let score = 0;

let lives = 3;

let playing = false;


/*
================================
VELOCIDAD LENTA
================================
*/

let speed = 0.55;


/*
================================
APARICIÓN DE TROLLS
3 segundos
================================
*/

const spawnRate = 3000;


let trolls = [];

let bullets = [];


/*
================================
CONTROL DE TECLADO
================================
*/

let keys = {

    left: false,

    right: false

};


/*
================================
ACTUALIZAR MARWAN
================================
*/

function updatePlayer() {

    playerX =
        Math.max(
            5,
            Math.min(
                game.clientWidth - 90,
                playerX
            )
        );


    marwan.style.left =
        playerX + "px";

}


/*
================================
CREAR TROLL
================================
*/

function createTroll() {

    if (!playing) {

        return;

    }


    const troll =
        document.createElement(
            "div"
        );


    troll.className =
        "troll";


    troll.innerHTML = `

        <div class="troll-head">

            <div
            class="troll-horn horn1">
            </div>

            <div
            class="troll-horn horn2">
            </div>

            <div
            class="troll-eye eye1">
            </div>

            <div
            class="troll-eye eye2">
            </div>

            <div
            class="troll-mouth">
            </div>

        </div>

        <div
        class="troll-body">
        </div>

    `;


    const x =
        Math.random() *
        (
            game.clientWidth - 90
        );


    troll.style.left =
        x + "px";


    troll.style.top =
        "-90px";


    game.appendChild(
        troll
    );


    trolls.push({

        element: troll,

        x: x,

        y: -90

    });

}


/*
================================
DISPARAR
================================
*/

function shoot() {

    if (!playing) {

        return;

    }


    const bullet =
        document.createElement(
            "div"
        );


    bullet.className =
        "bullet";


    bullet.style.left =
        (
            playerX + 80
        ) + "px";


    bullet.style.top =
        (
            game.clientHeight - 165
        ) + "px";


    game.appendChild(
        bullet
    );


    bullets.push({

        element: bullet,

        x: playerX + 80,

        y:
            game.clientHeight - 165

    });

}


/*
================================
EXPLOSIÓN
================================
*/

function explosion(
    x,
    y
) {

    const boom =
        document.createElement(
            "div"
        );


    boom.className =
        "explosion";


    boom.innerHTML =
        "💥";


    boom.style.left =
        x + "px";


    boom.style.top =
        y + "px";


    game.appendChild(
        boom
    );


    setTimeout(
        () => {

            boom.remove();

        },
        400
    );

}


/*
================================
GAME LOOP
================================
*/

function gameLoop() {

    if (!playing) {

        return;

    }


    /*
    MOVIMIENTO DE TROLLS
    */

    trolls.forEach(
        (
            troll,
            ti
        ) => {

            troll.y += speed;


            troll.element.style.top =
                troll.y + "px";


            /*
            SI LLEGA ABAJO
            */

            if (
                troll.y >
                game.clientHeight - 170
            ) {

                troll.element.remove();


                trolls.splice(
                    ti,
                    1
                );


                lives--;


                livesText.innerHTML =
                    "❤️".repeat(
                        Math.max(
                            0,
                            lives
                        )
                    );


                if (
                    lives <= 0
                ) {

                    gameOver();

                }

            }

        }
    );


    /*
    MOVIMIENTO BALAS
    */

    bullets.forEach(
        (
            bullet,
            bi
        ) => {

            bullet.y -= 9;


            bullet.element.style.top =
                bullet.y + "px";


            /*
            BALAS FUERA
            */

            if (
                bullet.y < -20
            ) {

                bullet.element.remove();


                bullets.splice(
                    bi,
                    1
                );


                return;

            }


            /*
            COLISIÓN
            */

            trolls.forEach(
                (
                    troll,
                    ti
                ) => {

                    const distanceX =
                        Math.abs(
                            bullet.x -
                            troll.x
                        );


                    const distanceY =
                        Math.abs(
                            bullet.y -
                            troll.y
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


                        trolls.splice(
                            ti,
                            1
                        );


                        bullets.splice(
                            bi,
                            1
                        );


                        score += 10;


                        scoreText.innerHTML =
                            "⭐ PUNTOS: " +
                            score;


                        /*
                        AUMENTO MUY LENTO
                        */

                        if (
                            score % 100 === 0
                        ) {

                            speed += 0.05;

                        }

                    }

                }
            );

        }
    );


    /*
    CONTROLES DE MOVIMIENTO
    */

    if (
        keys.left
    ) {

        playerX -= 4;

        updatePlayer();

    }


    if (
        keys.right
    ) {

        playerX += 4;

        updatePlayer();

    }


    requestAnimationFrame(
        gameLoop
    );

}


/*
================================
GAME OVER
================================
*/

function gameOver() {

    playing = false;


    message.style.display =
        "block";


    message.innerHTML = `

        💀 GAME OVER

        <br>

        <span
        style="font-size:20px">

            Marwan consiguió
            ${score}
            puntos

        </span>

        <br>

        <button
        id="restart">

            🔄 JUGAR DE NUEVO

        </button>

    `;


    document
        .getElementById(
            "restart"
        )
        .onclick =
        startGame;

}


/*
================================
INICIAR JUEGO
================================
*/

function startGame() {


    /*
    LIMPIAR TROLLS
    */

    trolls.forEach(
        troll =>
        troll.element.remove()
    );


    /*
    LIMPIAR BALAS
    */

    bullets.forEach(
        bullet =>
        bullet.element.remove()
    );


    trolls = [];

    bullets = [];


    score = 0;

    lives = 3;


    /*
    VELOCIDAD INICIAL
    MUY LENTA
    */

    speed = 0.55;


    scoreText.innerHTML =
        "⭐ PUNTOS: 0";


    livesText.innerHTML =
        "❤️❤️❤️";


    playerX = 100;


    updatePlayer();


    playing = true;


    message.style.display =
        "none";


    gameLoop();

}


/*
================================
GENERADOR DE TROLLS
================================

Usamos un único intervalo.
================================
*/

let trollTimer = null;


function startTrollSpawner() {

    if (trollTimer !== null) {

        clearInterval(
            trollTimer
        );

    }


    trollTimer =
        setInterval(
            () => {

                if (playing) {

                    createTroll();

                }

            },
            spawnRate
        );

}


/*
================================
BOTÓN COMENZAR
================================
*/

startButton.onclick =
    function() {

        startGame();

        startTrollSpawner();

    };


/*
================================
BOTÓN IZQUIERDA
================================
*/

const leftButton =
    document.getElementById(
        "left"
    );


/*
TOUCH START
*/

leftButton.addEventListener(
    "touchstart",
    function(e) {

        e.preventDefault();

        keys.left = true;

    },
    {
        passive: false
    }
);


/*
TOUCH END
*/

leftButton.addEventListener(
    "touchend",
    function(e) {

        e.preventDefault();

        keys.left = false;

    },
    {
        passive: false
    }
);


/*
MOUSE
*/

leftButton.addEventListener(
    "mousedown",
    function() {

        keys.left = true;

    }
);


leftButton.addEventListener(
    "mouseup",
    function() {

        keys.left = false;

    }
);


/*
================================
BOTÓN DERECHA
================================
*/

const rightButton =
    document.getElementById(
        "right"
    );


rightButton.addEventListener(
    "touchstart",
    function(e) {

        e.preventDefault();

        keys.right = true;

    },
    {
        passive: false
    }
);


rightButton.addEventListener(
    "touchend",
    function(e) {

        e.preventDefault();

        keys.right = false;

    },
    {
        passive: false
    }
);


rightButton.addEventListener(
    "mousedown",
    function() {

        keys.right = true;

    }
);


rightButton.addEventListener(
    "mouseup",
    function() {

        keys.right = false;

    }
);


/*
================================
BOTÓN DISPARAR
================================
*/

const shootButton =
    document.getElementById(
        "shoot"
    );


shootButton.addEventListener(
    "touchstart",
    function(e) {

        e.preventDefault();

        shoot();

    },
    {
        passive: false
    }
);


shootButton.addEventListener(
    "click",
    function() {

        shoot();

    }
);


/*
================================
TECLADO PC
================================
*/

document.addEventListener(
    "keydown",
    function(e) {

        if (!playing) {

            return;

        }


        if (
            e.key === "ArrowLeft" ||
            e.key.toLowerCase() === "a"
        ) {

            keys.left = true;

        }


        if (
            e.key === "ArrowRight" ||
            e.key.toLowerCase() === "d"
        ) {

            keys.right = true;

        }


        if (
            e.key === " " ||
            e.key === "Enter"
        ) {

            shoot();

        }

    }
);


document.addEventListener(
    "keyup",
    function(e) {

        if (
            e.key === "ArrowLeft" ||
            e.key.toLowerCase() === "a"
        ) {

            keys.left = false;

        }


        if (
            e.key === "ArrowRight" ||
            e.key.toLowerCase() === "d"
        ) {

            keys.right = false;

        }

    }
);


/*
================================
POSICIÓN INICIAL
================================
*/

updatePlayer();

</script>

</body>

</html>
"""


components.html(
    game,
    height=720,
    scrolling=False
)


st.markdown("""
<div style="
text-align:center;
color:white;
font-weight:bold;
padding:10px;
font-size:14px;
">

📱 CELULAR:
⬅️ ➡️ mover |
🔫 disparar

<br>

💻 PC:
⬅️ ➡️ mover |
ESPACIO disparar

<br><br>

🇵🇪 MARWAN VS TROLLS
— SANTA MARÍA DEL MAR

</div>
""", unsafe_allow_html=True)
