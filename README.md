*This project has been created as part of the 42 curriculum by brel-bou and zahrabar.*

#  A-Maze-ing

##  Description

**A-Maze-ing** is a Python-based maze generator and solver project.

Its goal is to generate valid mazes from configuration files, encode them efficiently, and compute a valid path from entry to exit.

The project supports:
- Maze generation from configuration input
- Hex-encoded maze representation
- Pathfinding from start to finish
- Visual representation of the maze
- Debugging and validation tools

This project focuses on algorithmic thinking, file parsing, data structures, and pathfinding techniques.

---

##  Instructions

###  Installation
```bash
make install
```

---

###  Run the program

```bash
make run
```

Or manually:

```bash
python3 Amaze/a_maze_ing.py
```

---

###  Debug mode

```bash
make debug
```

Uses Python’s built-in debugger (pdb).

---

###  Clean project

```bash
make clean
```

Removes:
- __pycache__
- .mypy_cache
- .pyc files

---

###  Lint check

```bash
make lint
```

Strict version:

```bash
make lint-strict
```

---

##  Maze Configuration File Format

WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14

Fields:
- WIDTH → maze width (int)
- HEIGHT → maze height (int)
- ENTRY → starting coordinate (x,y)
- EXIT → ending coordinate (x,y)

---

##  Maze Generation Algorithms

This project uses **two different algorithms implemented by team members**:

### 5 brel-bou → Hunt and Kill Algorithm

The Hunt and Kill algorithm works by:
1. Starting from a random cell
2. Walking randomly to unvisited neighbors
3. When stuck, "hunting" for a new unvisited cell adjacent to visited ones
4. Repeating until all cells are visited

###  zahrabar → Depth-First Search (DFS)

The DFS algorithm works by:
1. Starting from the entry cell
2. Exploring as deep as possible into unvisited neighbors
3. Backtracking when reaching dead ends
4. Continuing until the maze is fully generated

---

##  Why these algorithms

- DFS: Simple, reliable, produces perfect mazes
- Hunt & Kill: More randomness, less predictable structure, visually different results
- Combining both improves diversity of generated mazes

---

##  Reusable Components

- Grid system
- Pathfinding logic
- Config parser
- Visualization system

---

## Team & Project Management

###  Team Members
- brel-bou
- zahrabar

###  Planning Evolution
- Started with basic DFS implementation
- Added Hunt & Kill for diversity
- Improved debugging and visualization tools

###  What worked well
- Clean modular design
- Algorithm separation per team member
- Easy debugging with pdb

###  What could be improved
- Performance optimization for large mazes
- Advanced solver (A*)
- GUI visualization

###  Tools used
- Python
- pdb
- flake8
- mypy
- Makefile automation

---

##  AI Usage

AI was used for:
- Debugging type errors (mypy/flake8)
- Improving Makefile structure
- Explaining algorithms
- Fixing lint issues and project structure

AI was used as a **learning and debugging assistant**, not for full project generation.

---

##  Project Structure

Amaze/
├── a_maze_ing.py
├── maze/
│   ├── maze_generator.py
│   ├── maze_solver.py
├── Makefile
├── README.md
└── .gitignore

---

##  Final Note

This project demonstrates:
- Maze generation algorithms
- Software design
- Debugging skills
- Team collaboration
