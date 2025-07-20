import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env for API key
load_dotenv()
client = OpenAI()

system_prompt = """
 You are an AI assistant who write code in html,css and js only and you are the pro in it.
 Except html, css, js you can not do other things

 Rule:- 
 1) Write code in html, css, js after understanding user query what project he or she want to do
 2) According to the project name given by user you keep the project name as folder name
 3) Create index.html first write all things and connect the css and js file.
 4) Create style.css and write all the things according to project, so project will look awesome
 5) Create script.js and write all functionailty need for that project

 Your action should be like this:-
 - Understand what user wants to do -> Create a folder with name what user provided when send query. -> Create index.html file and write code for that -> Create style.css and write code  -> Create script.js and write code for that.

 Example :- Create a tik tak toe game using html, css and js 
 Ans:- In index.html :- 
                      <!DOCTYPE html>
                      <html lang="en">
                      <head>
                        <meta charset="UTF-8">
                        <title>Tic Tac Toe Game</title>
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <link rel="stylesheet" href="style.css">
                      </head>
                      <body>
                        <h1>Tic Tac Toe</h1>
                        <div id="status">Player X's turn</div>
                        <div class="board" id="board">
                          <div class="cell" data-index="0"></div>
                          <div class="cell" data-index="1"></div>
                          <div class="cell" data-index="2"></div>
                          <div class="cell" data-index="3"></div>
                          <div class="cell" data-index="4"></div>
                          <div class="cell" data-index="5"></div>
                          <div class="cell" data-index="6"></div>
                          <div class="cell" data-index="7"></div>
                          <div class="cell" data-index="8"></div>
                        </div>
                        <button id="resetBtn">Restart</button>
                        <script src="./script.js"></script>
                      </body>
                      </html>
        In style.css :-
                    body {
                      background: #f4f6ff;
                      color: #1a2329;
                      font-family: 'Segoe UI', Arial, sans-serif;
                      display: flex;
                      flex-direction: column;
                      align-items: center;
                      margin-top: 40px;
                    }
                    h1 {
                      margin-bottom: 0.5em;
                      letter-spacing: 0.04em;
                    }
                    #status {
                      margin-bottom: 18px;
                      font-size: 1.2em;
                      font-weight: bold;
                      min-height: 28px;
                      color: #4f5063;
                    }
                    .board {
                      display: grid;
                      grid-template-columns: repeat(3, 80px);
                      grid-template-rows: repeat(3, 80px);
                      gap: 6px;
                    }
                    .cell {
                      background: #fff;
                      border: 2px solid #a6b5c9;
                      border-radius: 10px;
                      font-size: 2.5em;
                      text-align: center;
                      line-height: 80px;
                      cursor: pointer;
                      transition: background 0.2s;
                      user-select: none;
                      width: 80px;
                      height: 80px;
                      box-shadow: 0 2px 8px #bac6e6a0;
                    }
                    .cell:hover:not(.disabled) {
                      background: #e3eaff;
                    }
                    .cell.disabled {
                      cursor: not-allowed;
                      color: #b5bac9;
                      background: #f5f5fa;
                    }
                    #resetBtn {
                      margin-top: 26px;
                      padding: 10px 30px;
                      font-size: 1.1em;
                      background: #3847a0;
                      color: #fff;
                      border: none;
                      border-radius: 8px;
                      cursor: pointer;
                      letter-spacing: 0.03em;
                      box-shadow: 0 2px 4px #c0ceff70;
                      transition: background 0.2s;
                    }
                    #resetBtn:hover {
                      background: #1b2968;
                    }
        In script.js :-

                    const cells = document.querySelectorAll('.cell');
                    const statusDiv = document.getElementById('status');
                    const resetBtn = document.getElementById('resetBtn');
                    let board = ["", "", "", "", "", "", "", "", ""];
                    let currentPlayer = "X";
                    let isGameActive = true;

                    const winningCombos = [
                      [0,1,2], [3,4,5], [6,7,8], // rows
                      [0,3,6], [1,4,7], [2,5,8], // columns
                      [0,4,8], [2,4,6]           // diagonals
                    ];

                    function checkWinner() {
                      for (const combo of winningCombos) {
                        const [a, b, c] = combo;
                        if (
                          board[a] &&
                          board[a] === board[b] &&
                          board[a] === board[c]
                        ) {
                          return board[a];
                        }
                      }
                      return null;
                    }

                    function handleClick(e) {
                      const idx = e.target.getAttribute('data-index');
                      if (!isGameActive || board[idx]) return;

                      board[idx] = currentPlayer;
                      e.target.textContent = currentPlayer;
                      e.target.classList.add('disabled');

                      const winner = checkWinner();
                      if (winner) {
                        statusDiv.textContent = `Player ${winner} wins!`;
                        isGameActive = false;
                        cells.forEach(cell => cell.classList.add('disabled'));
                        return;
                      }
                      if (!board.includes("")) {
                        statusDiv.textContent = "It's a draw!";
                        isGameActive = false;
                        return;
                      }
                      currentPlayer = currentPlayer === "X" ? "O" : "X";
                      statusDiv.textContent = `Player ${currentPlayer}'s turn`;
                    }

                    function resetGame() {
                      board = ["", "", "", "", "", "", "", "", ""];
                      currentPlayer = "X";
                      isGameActive = true;
                      statusDiv.textContent = "Player X's turn";
                      cells.forEach(cell => {
                        cell.textContent = "";
                        cell.classList.remove('disabled');
                      });
                    }

                    cells.forEach(cell => cell.addEventListener('click', handleClick));
                    resetBtn.addEventListener('click', resetGame);


 Example:-
 User :-  Create a tik tak toe project using html, css and js
 
 System :-{{"step": "analyse", "content":"The user is want a tik tak toe game using html, css and js"}}
          {{"step": "create folder", "content": "create_folder", "input": "project name"}}
          {{"step": "Create html, css and js files", "content": "create_files", "input": "project name"}}
          {{"step" : "write code", "content": "write code", "input": "project name"}}
          {{"step": "complete", "content": "Your project completed successfully run and check"}}

Example 2:-
User :- Create a rock paper scissor game using react

system :- {{"step": "analyse", "content":"The user is want a tik tak toe game using react"}}        
          {{"step": "output", "content" : "Sorry for now i am trained for html,css and js project"}}

"""

# === Step 1: Helper Functions ===

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

def create_files(folder_name):
    files = ["index.html", "style.css", "script.js"]
    for file in files:
        path = os.path.join(folder_name, file)
        with open(path, "w") as f:
            f.write("") 

def write_code(folder_name, user_prompt):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert frontend developer. Generate clean and working HTML, CSS, and JS code for the user's request. "
                "Respond ONLY in JSON with keys: html, css, js."
            )
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        response_format= {"type": "json_object"}
    )

    code_parts = json.loads(response.choices[0].message.content)

    files = {
        "index.html": code_parts.get("html", ""),
        "style.css": code_parts.get("css", ""),
        "script.js": code_parts.get("js", "")
    }

    for filename, code in files.items():
        with open(os.path.join(folder_name, filename), "w") as f:
            f.write(code)

# === Step 2: Main Workflow ===

def handle_project(user_query):
    print(json.dumps({"step": "analyse", "content": f"User asked: '{user_query}'"}))

    project_name = (
        user_query.lower()
        .replace("create", "")
        .replace("using html, css, and js", "")
        .strip()
        .replace(" ", "-")
    )

    print(json.dumps({"step": "think", "content": f"Project name will be '{project_name}'"}))
    print(json.dumps({"step": "action", "function": "create_folder", "input": project_name}))
    create_folder(project_name)

    print(json.dumps({"step": "action", "function": "create_files", "input": project_name}))
    create_files(project_name)

    print(json.dumps({"step": "action", "function": "write_code", "input": project_name}))
    write_code(project_name, user_query)

    print(json.dumps({"step": "done", "content": f"Web project '{project_name}' has been created successfully!"}))

if __name__ == "__main__":
    user_input = input("Enter your web project idea (using HTML, CSS, JS only):\n> ")
    handle_project(user_input)

