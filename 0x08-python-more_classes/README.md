<div align=center>

***holbertonschool-higher_level_programming***
<hr />
 <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="Logo Python" style="max-width:80%;">
 <hr />
<a href="https://twitter.com/Jepez90"><img src="https://img.shields.io/twitter/url?label=%40Jepez90&style=social&url=https%3A%2F%2Ftwitter.com%2FJepez90" alt="Logo Twitter">&nbsp;</a>
<a href="https://www.linkedin.com/in/jepez90/"><img src="https://img.shields.io/badge/jepez90-%230077B5.svg?&logo=linkedin&logoColor=white" alt="Logo LinkedIn">&nbsp;</a>
<img src="https://img.shields.io/badge/jepez90-white?style=flat&logo=gmail" alt="Logo Gmail">&nbsp;
<a href="https://twitter.com/HolbertonCOL"><img src="https://img.shields.io/badge/Holberton_School-red" alt="Logo Holberton">&nbsp;</a>

<a href="https://github.com/jepez90"><img src="https://visitor-badge.glitch.me/badge?page_id=jepez90.HigherLevelProgram.0x08&" alt="badget visitors"></a>
</div>

# Project: 0x08. Python - More Classes and Objects

> Excercises about:
class methods and attributes, static methods, magic methods...

## Files in this Folder:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **0-rectangle.py**<br />
Write an empty class ***Rectangle*** that defines a rectangle:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **1-rectangle.py**<br />
Write a class ***Rectangle*** that defines a rectangle by: (based on ***0-rectangle.py***)
* Private instance attribute: ***width***:

    * property ***def width(self):*** to retrieve it
    * property setter ***def width(self, value):*** to set it:
        * ***width*** must be an integer, otherwise raise a ***TypeError*** exception with the message ***width must be an integer***
        * if ***width*** is less than ***0***, raise a ***ValueError*** exception with the message ***width must be >= 0***

* Private instance attribute: ***height***:

    * property def ***height(self):*** to retrieve it
    * property setter ***def height(self, value):*** to set it:
        * ***height*** must be an ***nteger***, otherwise raise a ***TypeError*** exception with the message ***eight must be an integer***
        * if ***height*** is less than ***0***, raise a ***ValueError*** exception with the message ***height must be >= 0***

* Instantiation with optional ***width*** and ***height***: ***def __init__(self, width=0, height=0):***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **2-rectangle.py**<br />
Write a class ***Rectangle*** that defines a rectangle by: (based on ***1-rectangle.py***)
* Public instance method: ***def area(self):*** that returns the rectangle area
* Public instance method: ***def perimeter(self):*** that returns the rectangle perimeter: 
    * if ***width*** or ***height*** is equal to ***0***, perimeter is equal to ***0***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **3-rectangle.py**<br />
Write a class ***Rectangle*** that defines a rectangle by: (based on ***2-rectangle.py***)
* ***print()*** and ***str()*** should print the rectangle with the character ***#***:
    * if width or height is equal to 0, return an empty string

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **4-rectangle.py**<br />
Write a class ***Rectangle*** that defines a rectangle by: (based on ***3-rectangle.py***)
* ***repr()*** should return a string representation of the rectangle to be able to recreate a new instance by using ***eval()***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **5-rectangle.py**<br />
Write a class ***Rectangle*** that defines a rectangle by: (based on ***4-rectangle.py***)
* Print the message ***Bye rectangle...*** (... being 3 dots not ellipsis) when an instance of Rectangle is deleted

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **6-rectangle.py**<br />
Write a class ***Rectangle*** that defines a rectangle by: (based on ***5-rectangle.py***)
* Public class attribute ***number_of_instances***:
    * Initialized to ***0***
    * Incremented during each new instance instantiation
    * Decremented during each instance deletion

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **7-rectangle.py**<br />
Write a class ***Rectangle*** that defines a rectangle by: (based on ***6-rectangle.py***)
* Public class attribute ***print_symbol***:
    * Initialized to ***#***
    * Used as symbol for string representation
    * Can be any type


* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **8-rectangle.py**<br />
Write a class ***Rectangle*** that defines a rectangle by: (based on ***7-rectangle.py***)
* Static method def __bigger_or_equal(rect_1, rect_2):__ that returns the biggest rectangle based on the area
    * ***rect_1*** must be an instance of ***Rectangle***, otherwise raise a ***TypeError*** exception with the message ***rect_1 must be an instance of Rectangle***
    * ***rect_2*** must be an instance of ***Rectangle***, otherwise raise a TypeError exception with the message ***rect_2 must be an instance of Rectangle***
    * Returns ***rect_1*** if both have the same area value


* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **9-rectangle.py**<br />
Write a class ***Rectangle*** that defines a rectangle by: (based on ***8-rectangle.py***)
* Class method ***def square(cls, size=0):*** that returns a new Rectangle instance with ***width == height == size***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **101-nqueens.py**<br />
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.
