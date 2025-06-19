# 🎮 Pygame Obstacle Avoidance Game

This is a simple 2D game made with **Pygame** where a player-controlled square must navigate a maze of moving and stationary obstacles to reach the finish area. The game tracks the time it takes to complete the maze.

## 🧩 Features

- Player movement using arrow keys or `WASD`
- Animated (resizing) walls using a separate thread
- Collision detection with obstacles and boundaries
- Timer display
- Win screen with final time

## 📦 Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/) library

Install Pygame using pip if you haven't:
```bash
pip install pygame
```

## ▶️ How to Play

1. Run the game script:
```bash
python your_script_name.py
```

2. Move the player (green square) using:
   - Arrow keys (`↑ ↓ ← →`) or
   - `W`, `A`, `S`, `D`

3. Avoid all black obstacles and reach the red square (finish).

4. Your time will be shown once you win!

## 📁 File Structure

- `main.py` – the main game file
- `README.md` – this file

## 🧠 How It Works

- A background thread resizes certain walls up and down to make the game dynamic.
- The game checks for collision with all walls and resets movement if a collision is detected.
- Once you reach the finish block, the total time is shown on a win screen.

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

Enjoy dodging obstacles and beating your best time! 🕹️⏱️
