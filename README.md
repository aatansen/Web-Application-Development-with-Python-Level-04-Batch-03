<div align="center">
<h1>Web Application Development with Python Level 04 Batch 03</h1>
</div>

</br>

<details>
<summary>Day-01-Environment & Django Setup (13-03-2024)</summary>
    
## Day 01 Topics:

- Python Install
- Environment Setup
- Install Necessary Packages
- Creating First Project

### Python Install:

[Download](https://www.python.org/downloads/windows/) and install: 

`python 3.11.8`

> Make sure `add to path` is tick while installing or manually need to be added.

### Environment Setup:

Creation

```bash
python -m venv env
```

Activation

```bash
.\env\Scripts\activate
```

Deactivation

```bash
deactivate
```

### Install Necessary Packages:

Installing Django:

```bash
pip install Django
```

### Creating First Project:

Creating first_project:

```bash
django-admin startproject first_project
```

first_project Directory:

```bash
cd first_project
```

Run The Project:

```bash
python manage.py runserver
```
</details>


<details>
<summary>Day-02-Env Setup, Database, Super user & Views (14-03-2024)</summary>
    
## Day 02 Topics:

- Difference between languages
- Different scope of python
- Day 01 recap
- Default database
- Database migrations
- Super user
- Quick Recap
- Coding Editor Setup
- Creating views.py
- Special notes
- Day 02 Recap
- Task

### Difference between languages

- Time of execution
- Low level , High Level

### Different scope of python:

- Machine Learning
- Deep Learning
- Web Development

### Day 01 recap
- Setup environment
- Install django
- Create and run project

### Default database:
- db.sqlite3

### Database migrations

Always perform makemigrations first to initialize the schema (overal database structures initialization)

```bash
py manage.py makemigrations
```

Now do this:
```bash
py manage.py migrate
```
- Download [DB Browser for SQLite](https://sqlitebrowser.org/dl/) and install to see the `db.sqlite3` table or in VSCode install [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer) extension

### Super user:
To create superuser:
```bash
py manage.py createsuperuser
```
This will prompt to enter `Username`,`Email address`,`Password`

### Quick Recap:
- Create environment 
- Activate environtment
- Install django
- Run `django-admin startproject <project_name>`
- Go to project directory by `cd project_name`
- Run `py manage.py runserver` 
- Database migration:
  - `py manage.py makemigrations`
  - `py manage.py migrate`
- For creating superuser :
  - `py manage.py createsuperuser`

### Coding Editor Setup
- Download [VSCode](https://code.visualstudio.com/download) and install
- To open in VSCode run in cmd: `code .`

### Creating views.py:
In project folder create `views.py` and write:
```python
from django.shortcuts import render,redirect,HttpResponse

```
- `render` To show `html`
- `redirect` to redirect Website url 
- `HttpResponse` to show any text or changes on website

Creating a function to show a simple text:
```python
from django.shortcuts import render,redirect,HttpResponse

def homePage():
    return HttpResponse("Hi how are you")
```
A parameter need to be set `request`
```python
from django.shortcuts import render,redirect,HttpResponse

def homePage(request):
    return HttpResponse("Hi how are you")
```
Now in `urls.py` we have to add path of `homePage`
```python
from django.contrib import admin
from django.urls import path
from first_project2.views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage',homePage,name='homePage'),
]
```
here `homePage` function is imported by `from first_project2.views import homePage` and `path('homePage',homePage,name='homePage')` is added in `urlpatterns`.
Similarly more pages can be added

### Special notes
- Variable name can't be same as function,keywords
- While importing writing `*` will import all e.g: `from first_project2.views import *`

### Day 02 Recap
- Create environment 
- Activate environtment
- Install django
- Run `django-admin startproject <project_name>`
- Go to project directory by `cd project_name`
- Run `py manage.py runserver` 
- Migrate Database
- Create Superuser
- Create `views.py` in project directory
- Import neccesary library or modules
- Create function of 5 pages
- Import those fuction in `urls.py` and add 5 pages path in `urlpatterns`
- View those pages in browser

### Task
  - Learn all predefined variables in `settings.py`
  - Learn all predefined variables in `urls.py`
  - Write notes on [commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands) (e.g: `dir`,`cd` etc)
  - Submit a video of today's class

</details>

<details>
<summary>Day-02-Extra & Assignment Notes</summary>

## Day-02-Extra Topics:

- Windows Commands
- Exploring settings.py & urls.py

### Windows Commands

1. `mkdir (Make Directory)`: This command is used to create a new directory or folder.
Example: `mkdir MyFolder`
2. `cd (Change Directory)`: This command is used to change the current directory.
Example: `cd MyFolder`, `cd ..`
3. `dir (Directory Listing)`: This command is used to list the contents of a directory.
Example: `dir`.
Also by passing `/b` parameter output will be simple: `dir /b`
4. `echo`: This command is used to display a line of text/string on the console.
Example: `echo Hello, Tansen!`.
Text can be saved in file also like this: `echo Hello, Tansen! >> textfile.txt`
5. `copy`: This command is used to copy one or more files from one location to another.
Example: `copy file1.txt Destination_Path`
6. `xcopy`: This command is used to copy files and directories, including subdirectories.
Example: `xcopy source_folder destination_folder`
7. `move`: This command is used to move files from one location to another.
Example: `move file1.txt Destination_Path`
8. `ren (Rename)`: This command is used to rename a file or directory.
Example: `ren oldfilename.txt newfilename.txt`
9. `del (Delete)`: This command is used to delete one or more files.
Example: `del file1.txt`
10. `rmdir (Remove Directory)`:This command is used to delete a directory.
Example: `rmdir MyFolder`
11. `type`:This command is used to display the contents of a text file.
Example: `type file.txt`
12. `tree`: This command is used to display the folder structure of a directory and its subdirectories as a tree diagram.
Example: `tree`
13. `find`: This command is used to search for a specific text string in files.
Example: `find "search_term" file.txt`
14. `fc (File Compare)`: This command is used to compare the contents of two files or sets of files.
Example: `fc file1.txt file2.txt`
15. `attrib (Attribute)`: This command is used to display or change file attributes (such as hidden, read-only).
Example: `attrib +h file.txt` Here changing this command with `-h` will do the revert: `attrib -h file.txt`

### Exploring settings.py & urls.py

1. **BASE_DIR**: This variable represents the base directory of Django project.

2. **SECRET_KEY**: This is a secret key used by Django for cryptographic signing and protect user session data.

3. **DEBUG**: This is a boolean that determines whether project is in debug mode or not.Debug mode provides more detailed error pages and enables other debugging tools.

4. **ALLOWED_HOSTS**: This is a list of strings representing the host/domain names that Django site can serve. It's a security measure to prevent HTTP Host header attacks.

5. **INSTALLED_APPS**: This is a list of strings representing the names of all Django applications that are activated in the Django instance.

6. **MIDDLEWARE**: Middleware are hooks into Django's request/response processing. They're executed in the order listed, and they can modify request/response objects, handle exceptions, and perform other operations.

7. **ROOT_URLCONF**: This is the Python path to project's root URL configuration. It's the module that contains URL patterns.

8. **TEMPLATES**: This is a list of dictionaries representing the configuration of Django's template engine. It specifies template directories, template loaders, and context processors.

9. **WSGI_APPLICATION**: This is the Python path to the WSGI application object that Django's built-in server use.

10. **DATABASES**: This is a dictionary containing the configuration of all database connections used by Django project. Default database engine SQLite is used.

11. **AUTH_PASSWORD_VALIDATORS**: This is a list of validators that are used to validate user passwords. These validators enforce various password policies like minimum length, common password checks, etc.

12. **LANGUAGE_CODE**: This is the language code that is used in certain parts of Django's infrastructure.

13. **TIME_ZONE**: This is the time zone used to represent datetimes in the correct time zone.

14. **USE_I18N** and **USE_TZ**: These are boolean flags that control internationalization and time zone support in Django.

15. **STATIC_URL**: This is the URL prefix for static files (CSS, JavaScript, images, etc.) served by Django's static file server.

16. **DEFAULT_AUTO_FIELD**: This is the default primary key field type to use for models that don't have a primary key field explicitly defined. In this case, it's set to use `BigAutoField`, which is a 64-bit integer primary key field that automatically increments.

17. **urlpatterns**: This is a list of URL patterns that Django uses to match incoming browser requests to views within Django application.

</details>