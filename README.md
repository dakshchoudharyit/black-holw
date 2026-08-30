# 🕳️ Black Hole Simulation

An interactive **Black Hole Simulation** built with Python and Pygame. The simulation visualizes stars moving under the gravitational pull of a black hole, allowing them to orbit, escape, or get captured by the event horizon.

## ✨ Features

* 🕳️ Black hole with an event horizon
* ⭐ Multiple moving stars
* 🌀 Gravitational force simulation
* 📍 Star trajectory trails
* 🔥 Animated accretion disk
* ⏸️ Pause and resume simulation
* 🔄 Reset simulation
* 🖱️ Click to add new stars
* ⚙️ Adjust black hole mass using the mouse wheel
* 🌌 Animated space background

## 🖼️ Simulation

The stars are affected by a simplified Newtonian gravity model:

```text
F = G × M × m / r²
```

Where:

* `G` = gravitational constant used in the simulation
* `M` = mass of the black hole
* `m` = mass of the star
* `r` = distance between the star and the black hole

As stars move closer to the black hole, the gravitational force increases.

If a star crosses the **event horizon**, it is captured by the black hole.

## 🛠️ Technologies Used

* Python
* Pygame Community Edition (`pygame-ce`)

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
```

Go inside the project:

```bash
cd YOUR_REPOSITORY_NAME
```

Install the required dependency:

```bash
py -m pip install pygame-ce
```

## ▶️ Run the Simulation

```bash
py blackhole.py
```

## 🎮 Controls

| Control          | Action                    |
| ---------------- | ------------------------- |
| `SPACE`          | Pause / Resume simulation |
| `R`              | Reset simulation          |
| Left Mouse Click | Add a new star            |
| Mouse Wheel Up   | Increase black hole mass  |
| Mouse Wheel Down | Decrease black hole mass  |

## 📁 Project Structure

```text
BlackHoleSimulation/
│
├── blackhole.py
└── README.md
```

## ⚠️ Physics Note

This project uses a **simplified Newtonian gravity model** for visualization purposes.

It is **not a full general relativity simulation** and does not accurately simulate effects such as:

* Gravitational time dilation
* Real gravitational lensing
* Spacetime curvature
* Schwarzschild geometry

The goal of the project is to create an interactive and visually interesting simulation while demonstrating gravitational motion and orbital mechanics.

## 🚀 Future Improvements

* [ ] Realistic orbital velocity calculation
* [ ] Gravitational lensing effects
* [ ] Better particle-based accretion disk
* [ ] Adjustable simulation speed
* [ ] Interactive control panel
* [ ] Star collisions
* [ ] Save and load simulations
* [ ] 3D visualization
* [ ] General relativity-based physics

## 🤝 Contributing

Contributions, ideas, and improvements are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📜 License

This project is open-source and available for learning and experimentation.

---

⭐ If you like this project, consider giving the repository a star!
