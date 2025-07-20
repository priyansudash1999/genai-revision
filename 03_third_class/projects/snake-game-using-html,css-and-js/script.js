const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const box = 20;
const canvasSize = 400;
let snake = [{ x: 200, y: 200 }, { x: 200, y: 220 }];
let food = { x: 0, y: 0 };
let dx = 0;
let dy = -20;

function drawSnake(){
    ctx.fillStyle = 'green';
    snake.forEach(segment => {
        ctx.fillRect(segment.x, segment.y, box, box);
    });
}

function drawFood(){
    ctx.fillStyle = 'red';
    ctx.fillRect(food.x, food.y, box, box);
}

function randomFood(){
    food.x = Math.floor(Math.random() * 20) * box;
    food.y = Math.floor(Math.random() * 20) * box;
}

function gameLoop(){
    ctx.clearRect(0, 0, canvasSize, canvasSize);
    drawSnake();
    drawFood();
    moveSnake();
}

function moveSnake(){
    const head = { x: snake[0].x + dx, y: snake[0].y + dy };
    snake.unshift(head);
    if (head.x === food.x && head.y === food.y){
        randomFood();
    } else {
        snake.pop();
    }
}

randomFood();
setInterval(gameLoop, 100);