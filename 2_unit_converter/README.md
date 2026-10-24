# Hayun's Ultimte Unit Converter

**Level:** 2D  ·  **Language:** Python

## Pitch  (CP1)
- **The problem:** Converting measurements from one unit to another manually can be slow and tedious.
- **The user:** Anyone who needs to convert measurements quickly and accurately.
- **What it does:** This program is a unit converter built entirely in Python and used Tkinter for its gui. Users enter a number, select a starting unit and a target unit, and receive the converted result.
- **Done looks like:** The program successfully converts supported units, displays accurate results, and the user can properly interact with the gui.

## Plan  (CP1)

### Pseudocode
**run_this.py**
- imports tkinter for gui stuff and creates the main application window
- Starts the tkinter loop
**gui.py**
- sets the application window dimensions and layout
- a textbox for number input
- drop down menus for selecting units
- a "convert" button that runs the coversion
- an output box for displaying the result
**converter.py**
- store units and conversion factors
- organize the units by what they measure (distance, temperature, etc)
- convert the value that's in the starting unit the user put in into the base unit of its category (temperature, distance, etc) and then convert into the target unit
- return the converted result


## Test Plan  (CP2 → CP3)
| # | What I'm testing | Input | Expected | Actual | Pass? |
|---|---|---|---|---|---|
| 1 |  |  |  |  |  |

## Debugger Walkthrough
*Screenshot of a breakpoint, what the variables showed, what you learned.*

## Mentoring Log

## How to Run
Run "run_this.py" to start the program

## Changes Along the Way
*What changed from your plan, and why.*

## AI Collaboration
| What I asked | What came back | What I kept / changed, and why |
|Asked it to create a dictionary with different units and the conversion factors based on the base unit of that category (length, mass, temperature, volume, time)|a dictionary called "UNITS" containing exactly what i asked|kept the entire dictionary with the units and conversion factors|
