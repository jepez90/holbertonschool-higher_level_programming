<div align=center>

***holbertonschool-higher_level_programming***
<hr />
 <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="Logo Python" style="max-width:80%;">
 <hr />
<a href="https://twitter.com/Jepez90"><img src="https://img.shields.io/twitter/url?label=%40Jepez90&style=social&url=https%3A%2F%2Ftwitter.com%2FJepez90" alt="Logo Twitter">&nbsp;</a>
<a href="https://www.linkedin.com/in/jepez90/"><img src="https://img.shields.io/badge/jepez90-%230077B5.svg?&logo=linkedin&logoColor=white" alt="Logo LinkedIn">&nbsp;</a>
<img src="https://img.shields.io/badge/jepez90-white?style=flat&logo=gmail" alt="Logo Gmail">&nbsp;
<a href="https://twitter.com/HolbertonCOL"><img src="https://img.shields.io/badge/Holberton_School-red" alt="Logo Holberton">&nbsp;</a>

<a href="https://github.com/jepez90"><img src="https://visitor-badge.glitch.me/badge?page_id=jepez90.HigherLevelProgram.0x0B&" alt="badget visitors"></a>
</div>

# Project: 0x0B. Python - Input/Output

> Excercises about:
open, read and write in text files. JSON serialization

## Files in this Folder:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_folder.svg" alt="Logo Folder" height="15"> **tests**<br />
Files for test all functions

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **0-read_file.py**<br />
Function that reads a text file (***UTF8***) and prints it to stdout:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **1-write_file.py**<br />
Function that writes a string to a text file (***UTF8***) and returns the number of characters written:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **2-append_write.py**<br />
Function that appends a string at the end of a text file (***UTF8***) and returns the number of characters added:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **3-to_json_string.py**<br />
Function that returns the JSON representation of an object (string):

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **4-from_json_string.py**<br />
Function that returns an object (Python data structure) represented by a JSON string:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **5-save_to_json_file.py**<br />
Function that writes an Object to a text file, using a JSON representation:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **6-load_from_json_file.py**<br />
Function that creates an Object from a &ldquo;JSON file&rdquo;:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **7-add_item.py**<br />
Write a script that adds all arguments to a Python list, and then save them to a file:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **8-class_to_json.py**<br />
Function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **9-student.py**<br />
Write a class ***Student*** that defines a student by:
    * Public instance attributes:
        * ***first_name***
        * ***last_name***
        * ***age***
    * Instantiation with ***first_name***, ***last_name*** and ***age***: ***def __init__(self, first_name, last_name, age):***
    * Public method ***def to_json(self):*** that retrieves a dictionary representation of a ***Student*** instance (same as ***8-class_to_json.py***)
    * You are not allowed to import any module


* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **10-student.py**<br />
Write a class ***Student*** that defines a student by: (based on ***9-student.py***)
    * Public method ***def to_json(self, attrs=None):*** that retrieves a dictionary representation of a ***Student*** instance (same as ***8-class_to_json.py***):
        * If ***attrs*** is a list of strings, only attribute names contained in this list must be retrieved.
        * Otherwise, all attributes must be retrieved

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **11-student.py**<br />
Write a class ***Student*** that defines a student by: (based on ***10-student.py***)
    * Public method ***def reload_from_json(self, json):*** that replaces all attributes of the ***Student*** instance:
        * You can assume ***json*** will always be a dictionary
        * A dictionary key will be the public attribute name
        * A dictionary value will be the value of the public attribute

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **12-pascal_triangle.py**<br />
Create a function ***def pascal_triangle(n):*** that returns a list of lists of integers representing the Pascal’s triangle of ***n***:

    * Returns an empty list if ***n <= 0***
    * You can assume ***n*** will be always an integer
    * You are not allowed to import any module


* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **100-append_after.py**<br />
Function that inserts a line of text to a file, after each line containing a specific string (see example):

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="15"> **101-stats.py**<br />
Write a script that reads ***stdin*** line by line and computes metrics:
