<div align=center>

***holbertonschool-higher_level_programming***
<hr />
 <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="Logo Python" style="max-width:80%;">
<a href="https://twitter.com/Jepez90"><img src="https://img.shields.io/twitter/url?label=%40Jepez90&style=social&url=https%3A%2F%2Ftwitter.com%2FJepez90" alt="Logo Twitter">&nbsp;</a>
<a href="https://www.linkedin.com/in/jepez90/"><img src="https://img.shields.io/badge/jepez90-%230077B5.svg?&logo=linkedin&logoColor=white" alt="Logo LinkedIn">&nbsp;</a>
<img src="https://img.shields.io/badge/jepez90-white?style=flat&logo=gmail" alt="Logo Gmail">&nbsp;
<a href="https://twitter.com/HolbertonCOL"><img src="https://img.shields.io/badge/Holberton_School-red" alt="Logo Holberton">&nbsp;</a>

<a href="https://github.com/jepez90"><img src="https://visitor-badge.glitch.me/badge?page_id=jepez90.HigherLevelProgram.0x0F" alt="badget visitors"></a>
</div>

# Project: 0x0F. Python - Object-relational mapping

> In the first part, we will use the module MySQLdb to connect to a MySQL database and execute your SQL queries. In the second part, we will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).  
 * Why Python programming is awesome
 * How to connect to a MySQL database from a Python script
 * How to SELECT rows in a MySQL table from a Python script
 * How to INSERT rows in a MySQL table from a Python script
 * What ORM means
 * How to map a Python Class to a MySQL table


## Files in this Folder:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **0-select_states.py**<br />
Script that lists all ***states*** from the database ***hbtn_0e_0_usa***:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **1-filter_states.py**<br />
Script that lists all ***states*** with a ***name*** starting with ***N*** (upper N) from the database <code>hbtn_0e_0_usa</code>:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **2-my_filter_states.py**<br />
Script that takes in an argument and displays all values in the ***states*** table of ***hbtn_0e_0_usa*** where ***name*** matches the argument.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **3-my_safe_filter_states.py**<br />
Wait, do you remember the previous task? Did you test ***&quot;Arizona&#39;; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = &#39;&quot;*** as an input?

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **4-cities_by_state.py**<br />
Script that lists all ***cities*** from the database ***hbtn_0e_4_usa***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **5-filter_cities.py**<br />
Script that takes in the name of a state as an argument and lists all ***cities*** of that state, using the database ***hbtn_0e_4_usa***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **model_state.py**<br />
Python file that contains the class definition of a ***State*** and an instance ***Base = declarative_base()***:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **7-model_state_fetch_all.py**<br />
Script that lists all ***State*** objects from the database ***hbtn_0e_6_usa***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **8-model_state_fetch_first.py**<br />
Script that prints the first ***State*** object from the database ***hbtn_0e_6_usa***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **9-model_state_filter_a.py**<br />
Script that lists all ***State*** objects that contain the letter ***a*** from the database ***hbtn_0e_6_usa***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **10-model_state_my_get.py**<br />
Script that prints the ***State*** object with the ***name*** passed as argument from the database ***hbtn_0e_6_usa***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **11-model_state_insert.py**<br />
Script that adds the ***State*** object &ldquo;Louisiana&rdquo; to the database ***hbtn_0e_6_usa***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **12-model_state_update_id_2.py**<br />
Script that changes the name of a ***State*** object from the database ***hbtn_0e_6_usa***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **13-model_state_delete_a.py**<br />
Script that deletes all ***State*** objects with a name containing the letter ***a*** from the database ***hbtn_0e_6_usa***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **model_city.py**,<img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20"> **14-model_city_fetch_by_state.py**<br />
Write a Python file similar to ***model_state.py*** named ***model_city.py*** that contains the class definition of a ***City***.
