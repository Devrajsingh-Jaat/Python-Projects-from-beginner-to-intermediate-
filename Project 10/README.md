# 🏆 Auction Project (Python)

A simple command-line auction program written in Python. This project allows multiple users to place bids, stores them, and determines the highest bidder at the end.

---

## 📌 Features

* Accepts multiple bidders
* Stores bids using a Python dictionary
* Clears the screen between bidders for privacy
* Determines and displays the highest bidder
* Beginner-friendly and easy to understand

---

## 🛠️ How It Works

1. The program displays a logo (from the `art` module).
2. Users enter their **name** and **bid amount**.
3. The program asks if there are more bidders:

   * If **yes**, the screen clears and the next user can bid.
   * If **no**, the auction ends.
4. The program compares all bids and prints the winner.

---

## 📂 Code Overview

* `auction_people` → Dictionary storing `{name: bid}`
* `auction_running` → Controls the input loop
* `highest_bid` → Tracks the highest bid value
* `highest_bidder_name` → Stores the winner’s name

---

## 🧾 Example Usage

```
Welcome to the Auction Project!
Enter your name: Alice
Enter your bid: $100
Are there any other bidders? Yes or No: yes

Enter your name: Bob
Enter your bid: $150
Are there any other bidders? Yes or No: no
```

**Output:**

```
The winner is Bob with a bid of $150!
```

---

## ⚠️ Notes

* Input for bids must be a number (integer).
* The program does not handle invalid numeric input (e.g., letters instead of numbers).
* The screen clearing method (`print("\n" * 100)`) is a simple workaround and may not behave exactly like a real terminal clear command.

---
