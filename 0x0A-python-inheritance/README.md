<div align=center>

***holbertonschool-higher_level_programming***
<hr />
 <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="Logo Python" style="max-width:80%;">
 <hr />
<a href="https://twitter.com/Jepez90"><img src="https://img.shields.io/twitter/url?label=%40Jepez90&style=social&url=https%3A%2F%2Ftwitter.com%2FJepez90" alt="Logo Twitter">&nbsp;</a>
<a href="https://www.linkedin.com/in/jepez90/"><img src="https://img.shields.io/badge/jepez90-%230077B5.svg?&logo=linkedin&logoColor=white" alt="Logo LinkedIn">&nbsp;</a>
<img src="https://img.shields.io/badge/jepez90-white?style=flat&logo=gmail" alt="Logo Gmail">&nbsp;
<a href="https://twitter.com/HolbertonCOL"><img src="https://img.shields.io/badge/Holberton_School-red" alt="Logo Holberton">&nbsp;</a>

<a href="https://github.com/jepez90"><img src="https://visitor-badge.glitch.me/badge?page_id=jepez90.HigherLevelProgram.0x0A&" alt="badget visitors"></a>
</div>

# Project: 0x0A. Python - Inheritance

> Excercises about:
inheritance

## Files in this Folder:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_folder.svg" alt="Logo Folder" height="15"> **tests**<br />
Files for test all functions

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **0-lookup.py**<br />
Function that returns the list of available attributes and methods of an object:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **1-my_list.py, tests/1-my_list.txt**<br />
Class ***MyList*** that inherits from ***list***, and implements an instance method ***def print_sorted(self):*** that prints the list, but sorted (ascending sort)

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **2-is_same_class.py**<br />
Function that returns ***True*** if the object is <em>exactly</em> an instance of the specified class ; otherwise ***False***.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **3-is_kind_of_class.py**<br />
Function that returns ***True*** if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise ***False***.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **4-inherits_from.py**<br />
Function that returns ***True*** if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise ***False***.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **5-base_geometry.py**<br />
Write an empty class ***BaseGeometry***.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **6-base_geometry.py**<br />
Write a class ***BaseGeometry*** (based on ***5-base_geometry.py***) with a public instance method: ***def area(self):*** that raises an ***Exception*** with the message ***area() is not implemented***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **7-base_geometry.py, tests/7-base_geometry.txt**<br />
Write a class ***BaseGeometry*** (based on ***6-base_geometry.py***) with a public instance method: ***def integer_validator(self, name, value):*** that validates ***value***:
    * if ***value*** is not an integer: raise a ***TypeError*** exception, with the message ***<name> must be an integer***
    * if ***value*** is less or equal to 0: raise a ***ValueError*** exception with the message ***<name> must be greater than 0***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **8-rectangle.py**<br />
Write a class ***Rectangle*** that inherits from ***BaseGeometry*** (***7-base_geometry.py***) instantiation with width and height: def __init__(self, width, height):
    * ***width*** and ***height*** must be private. No getter or setter
    * ***width*** and ***height*** must be positive integers, validated by ***integer_validator***


* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **9-rectangle.py**<br />
Write a class ***Rectangle*** that inherits from ***BaseGeometry*** (***7-base_geometry.py***).
    * the ***area()*** method must be implemented
    * ***print()*** should print, and ***str()*** should return, the following rectangle description: ***[Rectangle] <width>/<height>***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **10-square.py**<br />
Write a class ***Square*** that inherits from ***Rectangle*** (***9-rectangle.py***):

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **11-square.py**<br />
Write a class ***Square*** that inherits from ***Rectangle*** (***9-rectangle.py***).

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **100-my_int.py**<br />
Write a class ***MyInt*** that inherits from ***int***:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **101-add_attribute.py**<br />
Function that adds a new attribute to an object if it&rsquo;s possible:
