# 🪨 Rock Paper Scissors (Python)

A simple command-line **Rock Paper Scissors** game built with Python.  
The user plays against the computer, which randomly selects its move.

---

## 📌 Features

- Interactive command-line gameplay
- ASCII art for Rock, Paper, and Scissors
- Random computer choice using Python's `random` module
- Input validation for incorrect entries
- Win/Lose/Draw result logic

---

## 🛠 Requirements

- Python 3.x

No external libraries are required. The game only uses built-in Python modules:
- `random`
- `sys`

---

## ▶️ How to Run

1. Make sure Python is installed on your system.
2. Save the script as:

```bash
rock_paper_scissors.py
```

3. Run the program:

```bash
python rock_paper_scissors.py
```

---

## 🎮 How to Play

When prompted, enter:

- `0` → Rock  
- `1` → Paper  
- `2` → Scissors  

Example:

```
Enter your choice: 0
```

The computer will randomly choose its move, and the result will be displayed:

- **You win!**
- **You lose!**
- **It's a draw!**

If you enter an invalid value (anything other than 0, 1, or 2), the program will exit.

---

## 🧠 Game Logic

- Rock beats Scissors
- Scissors beat Paper
- Paper beats Rock
- Same choices result in a draw

The computer’s move is generated using:

```python
random.randint(0, 2)
```

---

Enjoy the game! 🎉
