import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

st.set_page_config(
    page_title="MARWAN VS TROLLS",
    page_icon="👨‍🦲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# ARCHIVOS
# ============================================================

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"

MARWAN_FILE = ASSETS_DIR / "marwan.png"
MUSIC_FILE = ASSETS_DIR / "musica.mp3"


# ============================================================
# CONVERTIR ARCHIVOS A BASE64
# Esto permite que funcionen correctamente dentro del juego.
# ============================================================

def file_to_base64(path):

    if not path.exists():
        return ""

    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


marwan_base64 = file_to_base64(MARWAN_FILE)
music_base64 = file_to_base64(MUSIC_FILE)


# ============================================================
# ESTILO STREAMLIT
# ============================================================

st.markdown("""
<style>

.stApp {

    background:
        linear-gradient(
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

    padding-top: 0.5rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;

}

.title {

    text-align: center;

    color: white;

    font-size:
        clamp(25px, 7vw, 45px);

    font-weight: 900;

    text-shadow:
        4px 4px #000;

    margin-bottom: 0;

}

.subtitle {

    text-align: center;

    color: #ffe082;

    font-size:
        clamp(14px, 4vw, 21px);

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


# ============================================================
# IMAGEN
# ============================================================

if marwan_base64:

    marwan_image = (
        "data:image/png;base64,"
        + marwan_base64
    )

else:

    marwan_image = ""


# ============================================================
# MÚSICA
# ============================================================

if music_base64:

    music_source = (
        "data:audio/mpeg;base64,"
        + music_base64
    )

else:

    music_source = ""


# ============================================================
# JUEGO
# ============================================================

game = f"""
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

/* =========================================================
   GENERAL
========================================================= */

* {{

    box-sizing: border-box;

    -webkit-tap-highlight-color:
        transparent;

}}

html,
body {{

    margin: 0;

    padding: 0;

    width: 100%;

    height: 100%;

    overflow: hidden;

    background: #07152b;

    font-family: Arial, sans-serif;

    touch-action: none;

}}


/* =========================================================
   JUEGO
========================================================= */

#game {{

    width: 100%;

    height:
        min(650px, 82vh);

    min-height: 520px;

    position: relative;

    overflow: hidden;

    border:
        4px solid #111;

    border-radius: 18px;

    background:

        linear-gradient(
            #10294b 0%,
            #1c5271 55%,
            #d58a49 56%,
            #f0c078 100%
        );

    touch-action: none;

}}


/* =========================================================
   SOL
========================================================= */

#sun {{

    position: absolute;

    width: 75px;
    height: 75px;

    border-radius: 50%;

    background:
        #ffd54f;

    right: 8%;

    top: 8%;

    box-shadow:
        0 0 35px #ffd54f;

}}


/* =========================================================
   MAR
========================================================= */

#sea {{

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

}}


/* =========================================================
   PUNTAJE
========================================================= */

#score {{

    position: absolute;

    top: 10px;

    left: 10px;

    z-index: 100;

    color: white;

    font-size:
        clamp(15px, 4vw, 22px);

    font-weight: bold;

    background:
        rgba(0,0,0,.60);

    padding:
        8px 12px;

    border-radius: 10px;

}}


/* =========================================================
   VIDAS
========================================================= */

#lives {{

    position: absolute;

    top: 10px;

    right: 10px;

    z-index: 100;

    color: #ff5252;

    font-size:
        clamp(15px, 4vw, 22px);

    font-weight: bold;

    background:
        rgba(0,0,0,.60);

    padding:
        8px 12px;

    border-radius: 10px;

}}


/* =========================================================
   MARWAN
========================================================= */

#marwan {{

    position: absolute;

    width: 80px;

    height: 115px;

    bottom: 88px;

    left: 100px;

    z-index: 20;

}}


/* =========================================================
   CABEZA DE MARWAN
========================================================= */

.head {{

    position: absolute;

    width: 55px;

    height: 55px;

    left: 12px;

    top: 0;

    background:
        #d99a6c;

    border-radius: 50%;

    border:
        3px solid #222;

    overflow: hidden;

}}


/* FOTO DE MARWAN */

.marwan-photo {{

    width: 100%;

    height: 100%;

    object-fit: cover;

    border-radius: 50%;

}}


/* =========================================================
   CUERPO
========================================================= */

.body {{

    position: absolute;

    width: 46px;

    height: 48px;

    left: 16px;

    top: 52px;

    background:
        #263238;

    border-radius:
        12px 12px 5px 5px;

    border:
        3px solid #111;

}}


/* =========================================================
   BRAZOS
========================================================= */

.arm {{

    position: absolute;

    width: 42px;

    height: 10px;

    background:
        #d99a6c;

    top: 62px;

    border-radius: 10px;

}}

.arm.left {{

    left: -12px;

    transform:
        rotate(-25deg);

}}

.arm.right {{

    right: -12px;

    transform:
        rotate(25deg);

}}


/* =========================================================
   ARMA
========================================================= */

.gun {{

    position: absolute;

    width: 38px;

    height: 9px;

    background:
        #222;

    right: -34px;

    top: 69px;

    border-radius: 4px;

}}


/* =========================================================
   PIERNAS
========================================================= */

.leg {{

    position: absolute;

    width: 13px;

    height: 38px;

    background: #111;

    top: 95px;

    border-radius: 5px;

}}

.leg.left {{
    left: 23px;
}}

.leg.right {{
    left: 44px;
}}


/* =========================================================
   TROLL
========================================================= */

.troll {{

    position: absolute;

    width: 70px;

    height: 80px;

    z-index: 15;

}}


.troll-head {{

    width: 55px;

    height: 55px;

    background:
        #72a93b;

    border-radius: 50%;

    position: absolute;

    left: 7px;

    top: 5px;

    border:
        3px solid #18230e;

}}


.troll-eye {{

    position: absolute;

    width: 9px;

    height: 9px;

    background: white;

    border-radius: 50%;

    top: 22px;

}}

.eye1 {{
    left: 20px;
}}

.eye2 {{
    left: 39px;
}}


.troll-mouth {{

    position: absolute;

    width: 27px;

    height: 9px;

    background:
        #261414;

    border-radius:
        0 0 15px 15px;

    left: 15px;

    top: 37px;

}}


.troll-body {{

    position: absolute;

    width: 45px;

    height: 35px;

    background:
        #4e682d;

    left: 12px;

    top: 57px;

    border-radius: 12px;

}}


.troll-horn {{

    position: absolute;

    width: 0;

    height: 0;

    border-left:
        13px solid transparent;

    border-right:
        13px solid transparent;

    border-bottom:
        25px solid #6e6e6e;

    top: -15px;

}}

.horn1 {{
    left: 3px;
}}

.horn2 {{
    right: 3px;
}}


/* =========================================================
   BALA
========================================================= */

.bullet {{

    position: absolute;

    width: 14px;

    height: 5px;

    background:
        #ffeb3b;

    border-radius: 5px;

    box-shadow:
        0 0 15px #ff9800;

    z-index: 50;

}}


/* =========================================================
   EXPLOSIÓN
========================================================= */

.explosion {{

    position: absolute;

    font-size: 45px;

    z-index: 80;

    animation:
        boom .4s forwards;

}}


@keyframes boom {{

    from {{

        transform:
            scale(.5);

        opacity: 1;

    }}

    to {{

        transform:
            scale(1.8);

        opacity: 0;

    }}

}}


/* =========================================================
   MENSAJE
========================================================= */

#message {{

    position: absolute;

    top: 43%;

    left: 50%;

    transform:
        translate(-50%, -50%);

    width: 90%;

    color: white;

    text-align: center;

    font-size:
        clamp(23px, 7vw, 34px);

    font-weight: bold;

    z-index: 200;

    text-shadow:
        3px 3px #000;

}}


/* =========================================================
   BOTONES
========================================================= */

#start,
#restart {{

    margin-top: 15px;

    padding:
        14px 28px;

    font-size: 19px;

    font-weight: bold;

    border: none;

    border-radius: 12px;

    background:
        #ffca28;

    cursor: pointer;

}}


/* =========================================================
   CONTROLES CELULAR
========================================================= */

.controls {{

    position: absolute;

    bottom: 10px;

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

}}


.control-group {{

    display: flex;

    gap: 10px;

    pointer-events: auto;

}}


.controls button {{

    width: 65px;

    height: 58px;

    font-size: 25px;

    border:
        2px solid
        rgba(255,255,255,.4);

    border-radius: 15px;

    background:
        rgba(0,0,0,.75);

    color: white;

    cursor: pointer;

    touch-action: manipulation;

    user-select: none;

    box-shadow:
        0 4px 8px
        rgba(0,0,0,.4);

}}


.controls button:active {{

    transform:
        scale(.90);

    background:
        #ff9800;

}}


/* =========================================================
   DISPARO
========================================================= */

#shoot {{

    width: 82px;

    height: 68px;

    font-size: 31px;

    background:
        rgba(180,30,20,.90);

}}


/* =========================================================
   MÚSICA
========================================================= */

#musicButton {{

    position: absolute;

    top: 65px;

    right: 10px;

    z-index: 150;

    width: 45px;

    height: 45px;

    border: none;

    border-radius: 50%;

    background:
        rgba(0,0,0,.65);

    color: white;

    font-size: 21px;

    cursor: pointer;

}}


/* =========================================================
   CELULAR
========================================================= */

@media (max-width: 600px) {{

    #game {{

        height: 620px;

        min-height: 520px;

        border-radius: 12px;

    }}

    #marwan {{

        bottom: 88px;

    }}

}}


/* =========================================================
   CELULAR PEQUEÑO
========================================================= */

@media (max-width: 380px) {{

    #game {{

        height: 560px;

        min-height: 500px;

    }}

    .controls button {{

        width: 56px;

        height: 52px;

        font-size: 22px;

    }}

    #shoot {{

        width: 70px;

        height: 58px;

    }}

}}

</style>

</head>


<body>


<div id="game">


    <div id="sun"></div>


    <div id="sea"></div>


    <!-- PUNTAJE -->

    <div id="score">

        ⭐ PUNTOS: 0

    </div>


    <!-- VIDAS -->

    <div id="lives">

        ❤️❤️❤️

    </div>


    <!-- BOTÓN MÚSICA -->

    <button id="musicButton">

        🔇

    </button>


    <!-- AUDIO -->

    {
        '<audio id="music" loop>'
        '<source src="' + music_source + '" type="audio/mpeg">'
        '</audio>'
        if music_source
        else ''
    }


    <!-- MENSAJE -->

    <div id="message">

        👨‍🦲 MARWAN VS TROLLS

        <br>

        <span style="font-size:18px">

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

            {
                '<img class="marwan-photo" src="' +
                marwan_image +
                '">'
                if marwan_image
                else
                '<div style="font-size:28px;text-align:center;padding-top:10px;">👨‍🦲</div>'
            }

        </div>


        <div class="body"></div>


        <div class="arm left"></div>


        <div class="arm right"></div>


        <div class="gun"></div>


        <div class="leg left"></div>


        <div class="leg right"></div>

    </div>


    <!-- CONTROLES -->

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

/* =========================================================
   VARIABLES
========================================================= */

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


const music =
    document.getElementById(
        "music"
    );

const musicButton =
    document.getElementById(
        "musicButton"
    );


let playerX = 100;

let score = 0;

let lives = 3;

let playing = false;


/* =========================================================
   VELOCIDAD MUY LENTA
========================================================= */

let speed = 0.55;


/* =========================================================
   APARICIÓN DE TROLLS
3 segundos
========================================================= */

const spawnRate = 3000;


let trolls = [];

let bullets = [];


let keys = {

    left: false,

    right: false

};


let trollTimer = null;

let musicOn = false;


/* =========================================================
   ACTUALIZAR JUGADOR
========================================================= */

function updatePlayer() {{

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

}}


/* =========================================================
   CREAR TROLL
========================================================= */

function createTroll() {{

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

}}


/* =========================================================
   DISPARAR
========================================================= */

function shoot() {{

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

}}


/* =========================================================
   EXPLOSIÓN
========================================================= */

function explosion(x, y) {{

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

}}


/* =========================================================
   GAME LOOP
========================================================= */

function gameLoop() {{

    if (!playing) {

        return;

    }


    /* TROLLS */

    trolls.forEach(
        (
            troll,
            ti
        ) => {{

            troll.y += speed;


            troll.element.style.top =
                troll.y + "px";


            if (
                troll.y >
                game.clientHeight - 170
            ) {{

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
                ) {{

                    gameOver();

                }}

            }}

        }}
    );


    /* BALAS */

    bullets.forEach(
        (
            bullet,
            bi
        ) => {{

            bullet.y -= 9;


            bullet.element.style.top =
                bullet.y + "px";


            if (
                bullet.y < -20
            ) {{

                bullet.element.remove();


                bullets.splice(
                    bi,
                    1
                );


                return;

            }}


            trolls.forEach(
                (
                    troll,
                    ti
                ) => {{

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
                    ) {{

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
                        AUMENTO MUY SUAVE
                        */

                        if (
                            score % 100 === 0
                        ) {{

                            speed += 0.05;

                        }}

                    }}

                }}
            );

        }}
    );


    /* MOVIMIENTO */

    if (keys.left) {{

        playerX -= 4;

        updatePlayer();

    }}


    if (keys.right) {{

        playerX += 4;

        updatePlayer();

    }}


    requestAnimationFrame(
        gameLoop
    );

}}


/* =========================================================
   GAME OVER
========================================================= */

function gameOver() {{

    playing = false;


    message.style.display =
        "block";


    message.innerHTML = `

        💀 GAME OVER

        <br>

        <span
        style="font-size:20px">

            Marwan consiguió
            ${{score}}
            puntos

        </span>

        <br>

        <button id="restart">

            🔄 JUGAR DE NUEVO

        </button>

    `;


    document
        .getElementById(
            "restart"
        )
        .onclick =
        startGame;

}}


/* =========================================================
   MÚSICA
========================================================= */

function startMusic() {{

    if (!music) {{

        return;

    }}


    music.volume = 0.35;


    music.play()
        .then(() => {{

            musicOn = true;

            musicButton.innerHTML =
                "🔊";

        }})
        .catch(() => {{

            musicOn = false;

        }});

}}


/* =========================================================
   ACTIVAR / DESACTIVAR MÚSICA
========================================================= */

musicButton.onclick =
    function() {{

        if (!music) {{

            alert(
                "No se encontró musica.mp3"
            );

            return;

        }}


        if (music.paused) {{

            music.play();

            musicOn = true;

            musicButton.innerHTML =
                "🔊";

        }}
        else {{

            music.pause();

            musicOn = false;

            musicButton.innerHTML =
                "🔇";

        }}

    }};


/* =========================================================
   INICIAR JUEGO
========================================================= */

function startGame() {{

    trolls.forEach(
        troll =>
        troll.element.remove()
    );


    bullets.forEach(
        bullet =>
        bullet.element.remove()
    );


    trolls = [];

    bullets = [];


    score = 0;

    lives = 3;


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


    /*
    MÚSICA
    */

    startMusic();


    gameLoop();

}}


/* =========================================================
   GENERADOR DE TROLLS
========================================================= */

function startTrollSpawner() {{

    if (
        trollTimer !== null
    ) {{

        clearInterval(
            trollTimer
        );

    }}


    trollTimer =
        setInterval(
            () => {{

                if (playing) {{

                    createTroll();

                }}

            }},
            spawnRate
        );

}}


/* =========================================================
   BOTÓN COMENZAR
========================================================= */

startButton.onclick =
    function() {{

        startGame();

        startTrollSpawner();

    }};


/* =========================================================
   BOTÓN IZQUIERDA
========================================================= */

const leftButton =
    document.getElementById(
        "left"
    );


leftButton.addEventListener(
    "touchstart",
    function(e) {{

        e.preventDefault();

        keys.left = true;

    }},
    {{
        passive: false
    }}
);


leftButton.addEventListener(
    "touchend",
    function(e) {{

        e.preventDefault();

        keys.left = false;

    }},
    {{
        passive: false
    }}
);


leftButton.addEventListener(
    "mousedown",
    function() {{

        keys.left = true;

    }}
);


leftButton.addEventListener(
    "mouseup",
    function() {{

        keys.left = false;

    }}
);


/* =========================================================
   BOTÓN DERECHA
========================================================= */

const rightButton =
    document.getElementById(
        "right"
    );


rightButton.addEventListener(
    "touchstart",
    function(e) {{

        e.preventDefault();

        keys.right = true;

    }},
    {{
        passive: false
    }}
);


rightButton.addEventListener(
    "touchend",
    function(e) {{

        e.preventDefault();

        keys.right = false;

    }},
    {{
        passive: false
    }}
);


rightButton.addEventListener(
    "mousedown",
    function() {{

        keys.right = true;

    }}
);


rightButton.addEventListener(
    "mouseup",
    function() {{

        keys.right = false;

    }}
);


/* =========================================================
   BOTÓN DISPARO
========================================================= */

const shootButton =
    document.getElementById(
        "shoot"
    );


shootButton.addEventListener(
    "touchstart",
    function(e) {{

        e.preventDefault();

        shoot();

    }},
    {{
        passive: false
    }}
);


shootButton.addEventListener(
    "click",
    function() {{

        shoot();

    }}
);


/* =========================================================
   TECLADO PC
========================================================= */

document.addEventListener(
    "keydown",
    function(e) {{

        if (!playing) {{

            return;

        }}


        if (
            e.key === "ArrowLeft" ||
            e.key.toLowerCase() === "a"
        ) {{

            keys.left = true;

        }}


        if (
            e.key === "ArrowRight" ||
            e.key.toLowerCase() === "d"
        ) {{

            keys.right = true;

        }}


        if (
            e.key === " " ||
            e.key === "Enter"
        ) {{

            shoot();

        }}

    }}
);


document.addEventListener(
    "keyup",
    function(e) {{

        if (
            e.key === "ArrowLeft" ||
            e.key.toLowerCase() === "a"
        ) {{

            keys.left = false;

        }}


        if (
            e.key === "ArrowRight" ||
            e.key.toLowerCase() === "d"
        ) {{

            keys.right = false;

        }}

    }}
);


/* =========================================================
   POSICIÓN INICIAL
========================================================= */

updatePlayer();

</script>

</body>

</html>
"""


# ============================================================
# MOSTRAR JUEGO
# ============================================================

components.html(
    game,
    height=720,
    scrolling=False
)


# ============================================================
# INSTRUCCIONES
# ============================================================

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
🔫 disparar |
🎵 música

<br>

💻 PC:
⬅️ ➡️ mover |
ESPACIO disparar

<br><br>

🇵🇪 MARWAN VS TROLLS
— SANTA MARÍA DEL MAR

</div>
""", unsafe_allow_html=True)
