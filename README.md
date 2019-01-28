Programming exercises - tutorial materials for work with a beginner. I am searching for exercises that can be solved with a simple code and give properly impressive results. Results that may be
shown to friend/mother/brother/daughter and will impress them.

Code in this repository is a mix of notes, used ideas and materials left as a feedback for the future.

# Exercises

All images below were created using code from this repository.

![mandelbrot_-_zoomed.png](mandelbrot_-_zoomed.png)

## Hello world
Standard hello world example.

## Mandelbrot visualisation

Generation of beautiful Mandelbrot fractal. Demonstrates one of cases where vast computing power of a computer allows to achieve results unfeasible with human computing power due to a cost differences alone.

![mandelbrot.png](mandelbrot.png)

## Image generation

Making image out of simple shapes. For example group of dwarves in from of their home. Excellent situation to demonstarte why code reuse using functions is useful.

![dwarves.png](dwarves.png)

## Text statistics

## Sierpiński's carpet

![Sierpiński's_carpet.gif](Sierpiński's_carpet.gif)

# Bonus

Materials showing interesting cases where programming is necessary:

* [7 Minutes of Terror: Curiosity Rover's Risky Mars Landing](https://www.youtube.com/watch?v=h2I8AoB1xgU) (bonus: [landing video](https://www.youtube.com/watch?v=svUJdzMHwmM) + [Curiosity rover descending on parachute, photo made by Mars Reconnaissance Orbiter](https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA15978))

# Maintenance commands

## Reformat code to follow Python coding stadards

`autopep8 --in-place --recursive .`

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Detect code style issues

`pylint **/*.py --include-naming-hint=y --variable-rgx=^[a-z][a-z0-9]*((_[a-z0-9]+)*)?$ --argument-rgx=^[a-z][a-z0-9]*((_[a-z0-9]+)*)?$ --disable=C0103,R0801`

It includes workaround for bug [#2018](https://github.com/PyCQA/pylint/issues/2018) and disables rule `C0103` with many false positives (too eager to convert variables into constants).

Rule `R0801` is also disabled as it is not working properly due to specific repository format (many versions of the same code).

### Version without minor complaints

`pylint **/*.py --include-naming-hint=y --variable-rgx=^[a-z][a-z0-9]*((_[a-z0-9]+)*)?$ --argument-rgx=^[a-z][a-z0-9]*((_[a-z0-9]+)*)?$ --disable=C0103,R0801,C0111,W0621`

Rule `C0111` requesting docstrings is disabled, the same with `W0621` complaining about defining some varaibles not within functions.

## Run all Python scripts in one folder

`find . -maxdepth 1 -type f -name "*.py" -exec python3 {} \;`

Command based on one by [Jim Lewis](https://stackoverflow.com/a/10523492/4130619)

# Similar projects

There are some similar projects with materials and ideas on topic of teaching programming to beginners with interesting miniprojects.

Some of them have extensive explanations making the useful on their own for the beginner.

Note that it is not list of tutorials - I am rather looking for lists of interesting project ideas. I is necessary that this projects are doable by a beginners (with a help from a tutor or on their own) and give impressive results.

It may be in any programming, not only Python (though I think that Python is a great first programing language).

* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
* [Let's Learn Python!](http://www.letslearnpython.com/)
* [Making Games with Python & Pygame](http://inventwithpython.com/pygame/)

If something is missing on this list, [let me know](https://github.com/matkoniecz/quick-beautiful/issues/new).
