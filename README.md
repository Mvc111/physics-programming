# Physics & Computational Simulation

### 1. Physics & Path Integration 🚀

* **Ellipse Path Integrator** (`opgave42023.py`): A numerical solver that calculates the circumference of an ellipse by summing discrete time-steps (`dt`) using Pythagoras. This bypasses the need for complex elliptic integrals by modeling the path iteratively.
* **Monte Carlo Distance Solver** (`afstand.py`): Simulates millions of random points in a 2D square to statistically determine the "Average Distance" between two points—a classic probability density problem solved via brute-force simulation.
* **Area & Volume Estimation** (`montecarlo.py`, `riemann.py`): Uses random sampling and Riemann sums to calculate the area under complex, non-linear curves where standard integration is difficult.

### 2. Stochastic Simulations (Probability & Games) 🎲
Modeling randomness, "finding the odds," and game theory.
* **Monopoly Simulation Engine** (`monopoly_realistisch.py`): A full game engine that simulates 10,000+ turns of Monopoly.
    * *Goal:* Determine the statistical advantage of the starting player.
    * *Feature:* Includes an algorithm to calculate the exact "equilibrium start money" required to make the game fair (50/50 win rate).
* **Central Limit Visualizer** (`histogram.py`): Generates distributions of random sums to visualize the Central Limit Theorem in action, exporting results to histograms.
* **Probability Density Logic** (`test.py`): Solves complex probability ratios (e.g., "Ratio of points close together vs. far apart") using optimized counting algorithms to handle edge cases.

### 3. Algorithmic Number Theory 🧮
High-performance scripts for integer analysis.
* **Project Euler Suite** (`projecteuler.py`): A library of highly optimized scripts for solving constraint problems.
    * *Includes:* Largest Prime Factors, Palindrome Products, and Even Fibonacci Sums.
    * *Optimization:* Uses mathematical pruning (e.g., symmetry checks) to reduce complexity from $O(N^2)$ to $O(N)$ or $O(1)$.
* **Series Approximation** (`opgave22023.py`): Compares the convergence speed of Leibniz vs. Euler infinite series for approximating $\pi$.

---

### 💻 Technologies Used
* **Languages:** Python 3
* **Libraries:** `NumPy` (Vectorization), `Matplotlib` (Data Viz), `Math`, `Random`
* **Techniques:** Monte Carlo Simulation, Discrete Time-Stepping, Numerical Integration, Search Space Pruning.

---
*(If you have questions about the logic or the math behind the simulations, feel free to reach out.)*
