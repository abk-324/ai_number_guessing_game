# ai_number_guessing_game

# 🎯 AI Number Guessing Game

An interactive web-based game where **AI guesses the number** you're thinking of (between 1 and 100) using your feedback. Built with Flask (Python backend) and HTML/CSS/JavaScript (frontend).

---

## 🤖 What's "AI" About It?

This project uses a **Binary Search algorithm**, a classic problem-solving strategy that mimics how AI would optimize decision-making. Based on your feedback (`Too High`, `Too Low`, or `Correct`), the AI narrows its guess efficiently, ideally finding the correct number in 7 or fewer steps.

---

## 🔧 Features

- AI guesses your number from 1 to 100
- Web UI with buttons for feedback
- AI adapts to your responses and guesses smarter each time
- Game resets on page refresh

---

## 🧠 Concepts Used

- **Binary Search** (algorithm to narrow down the number)
- **Session Management** using `Flask-Session`
- **Client-Server Communication** with `fetch()` and JSON
- Simple use of AI logic in an intuitive and fun interface

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask, Flask-Session
- **Session Store**: Filesystem-based

---

## 📁 Project Structure

