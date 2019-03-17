# Quick & Beautiful

Programming exercises for beginners that I collected and prepared.

Repository contains overview readme file that you are reading and folders with materials for each exercise. Each folder contains code in stages from simplest one to a finished project. Some folder contain also additional data like example data ready for processing.

Tutorial materials for work with a beginner, mostly code in stages from scratch to a completed work.

I am searching for exercises that can be solved with a simple code and give properly impressive results. Results that may be
shown to friend/mother/brother/daughter and will impress them.

Code in this repository is a mix of material already used and tested, ideas for a future, work in progress and notes.

![mandelbrot_-_zoomed.png](mandelbrot_-_zoomed.png)

# Exercises

All images below were created using code from this repository.

## Hello world

Standard hello world example.

## Mandelbrot visualisation

Generation of beautiful Mandelbrot fractal. Demonstrates one of cases where vast computing power of a computer allows to achieve results unfeasible with human computing power due to cost differences alone.

![mandelbrot.png](mandelbrot.png)

## Image generator

Making an image out of simple shapes. For example group of dwarves in from of their home. Excellent situation to demonstrate why code reuse using functions is useful.

![dwarves.png](dwarves.png)

## Lists and simple statistics

Introduction to lists - very basic level (showing list, looping through a list).

## Splitting text into words

Building function that will split text into words.

## Book statistics

Loading entire book and outputting statistics. Doing in minutes what before computers needed [years](https://en.wikipedia.org/wiki/Concordance_(publishing)).

Book texts are in public domain and were obtained from:

[Project Gutenberg](http://www.gutenberg.org/)

* A Christmas Carol in Prose; Being a Ghost Story of Christmas by Charles Dickens
* Moby Dick; or The Whale, by Herman Melville

[Wikiźródła](https://pl.wikisource.org/)

* Ania z Wyspy, Lucy Maud Montgomery, przełożył Andrzej Magórski

[Wolne Lektury](https://wolnelektury.pl/)

* Anhelli, Juliusz Słowacki

Short texts covered by fair use:

* "Torched the haystack. Found the needle." by Newtonswig
* "Voyager still transmitted, but Earth didn’t." by ErasedCitizen

## Sierpiński's carpet

More complicated case of recursion.

![Sierpiński's_carpet.gif](Sierpiński's_carpet.gif)

# Beyond simple programs

Note that simple programs like listed here are a great first step. But to really learn programing one needs also to be able to dive in large programs made by other people, to properly document changes. Basic skills like Git were not even mentioned here and are absolute necessity even for a hobbyist.

# Bonus

Materials showing interesting cases where programming is necessary:

* [7 Minutes of Terror: Curiosity Rover's Risky Mars Landing](https://www.youtube.com/watch?v=h2I8AoB1xgU) (bonus: [landing video](https://www.youtube.com/watch?v=svUJdzMHwmM) + [Curiosity rover descending on a parachute, photo made by Mars Reconnaissance Orbiter](https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA15978))

# Maintenance commands

## Reformat code to follow Python coding standards

`autopep8 --in-place --recursive .`

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Detect code style issues

`pylint **/*.py --include-naming-hint=y --variable-rgx=^[a-z][a-z0-9]*((_[a-z0-9]+)*)?$ --argument-rgx=^[a-z][a-z0-9]*((_[a-z0-9]+)*)?$ --disable=C0103,R0801`

It includes a workaround for bug [#2018](https://github.com/PyCQA/pylint/issues/2018) and disables rule `C0103` with many false positives (too eager to convert variables into constants).

Rule `R0801` is also disabled as it is not working properly due to specific repository format (many versions of the same code).

### Version without minor complaints

`pylint **/*.py --include-naming-hint=y --variable-rgx=^[a-z][a-z0-9]*((_[a-z0-9]+)*)?$ --argument-rgx=^[a-z][a-z0-9]*((_[a-z0-9]+)*)?$ --disable=C0103,R0801,C0111,W0621`

Rule `C0111` requesting docstrings is disabled, the same with `W0621` complaining about defining some variables not within functions.

## Run all Python scripts in one folder

`find . -maxdepth 1 -type f -name "*.py" -exec python3 {} \;`

Command based on one by [Jim Lewis](https://stackoverflow.com/a/10523492/4130619)

# Similar projects

There are some similar projects with materials and ideas on the topic of teaching programming to beginners with interesting miniprojects.

Some of them have extensive explanations making the useful on their own for the beginner.

Note that it is not a list of tutorials - I am rather looking for lists of interesting project ideas. It is necessary that these projects are doable by beginners (with a help from a tutor or on their own) and give impressive results.

It may be in any programming, not only Python (though I think that Python is a great first programing language).

* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
* [Let's Learn Python!](http://www.letslearnpython.com/)
* [Making Games with Python & Pygame](http://inventwithpython.com/pygame/)

If something is missing on this list, [let me know](https://github.com/matkoniecz/quick-beautiful/issues/new).
