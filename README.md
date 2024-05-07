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

<details>
<summary>Day-03-Render Template, Dictionary DS , Template Language (16-03-2024)</summary>

## Day 03 Topics:

- Day 2 recap
- Render template
- Show table data dinamically using dictionary
- Notes on dictionary
- Now Recap

### Render template
Create a folders `static`, `Template` in project directory where `manage.py` is present.
Now in `settings.py` add `STATICFILES_DIRS`:
```python
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]
```
Now in `TEMPLATES`'s `DIRS` list add these:
```python
'DIRS': [BASE_DIR, "Template"],
```
Now similarly in `views.py` file `return render(request,'homePage.html')` will be added as below:
```python
from django.shortcuts import render,redirect,HttpResponse

def homePage(request):
    return render(request,'homePage.html')
```
Now in `urls.py` this will be added:
```python
from first_project.views import homePage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/',homePage,name='homePage'),
]
```
### Show table data dynamically using dictionary
In `views.py` file:
```python
from django.shortcuts import render,redirect,HttpResponse

def tableData(request):
    myDict={
        'name':'Tansen',
        'department':'CSE',
        'city':'Dhaka',
        'name2':'Shakil',
        'department2':'EEE',
        'city2':'Barisal',
    }

    return render(request,'tableData.html',myDict)
```
In `urls.py` file:
```python
from django.contrib import admin
from django.urls import path
from first_project.views import homePage,contactPage,orderPage,paymentPage,productPage,navBar,tableData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tableData',tableData,name='tableData'),

]
```
In `tableData.html` file:
```html
<table id="info">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
  </tr>
  <tr>
    <td>{{name}}</td>
    <td>{{department}}</td>
    <td>{{city}}</td>
  </tr>
  <tr>
    <td>{{name2}}</td>
    <td>{{department2}}</td>
    <td>{{city2}}</td>
  </tr>

</table>
```
### Notes on dictionary
- Dictionary is `key - value` pair

### Day 03 Recap:
- Day 02 recap
  - Create environment
  - Activate environment
  - Install necessary package (django)
  - Create a project
  - Run the project and view in browser
  - Now migrate database
  - View the database
  - Create super user
  - Now Create function of 5 pages in `views.py`
  - Import those fuction in `urls.py` and add 5 pages path in `urlpatterns`
  - View those pages in browser
- Render template (`HTML` files)
- Create a table and view it
- Get a table from external source [Fancy HTML CSS table](https://www.w3schools.com/css/tryit.asp?filename=trycss_table_fancy) and create 5 html pages
- Dynamically change table data from backend using dictionary data structure & template laguage
</details>

<details>
<summary>Day-04-Template Mastering, Navigation, url,include,block,extends (18-03-2024)</summary>

## Day 04 Topics:

- Day 3 recap
- Template mastering
- Organize reuse code
- Day 04 Recap

### Template mastering
- clicking on navbar any section change other element of the page
- In template mastering we reuse same element again and again. e.g: navbar

Create a navbar (get it from [external source](https://www.w3schools.com/css/tryit.asp?filename=trycss_navbar_horizontal_black_right))

Now in created `home.html`:
```html
<ul>
  <li><a href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li style="float:right"><a class="active" href="#about">About</a></li>
</ul>
```

Now in `urls.py` file there is `path('home/', home,name='home')` where `name='home'` needs to be added in `href` like this: `href="{% url 'home' %}"`:
```html
<ul>
  <li><a href="{% url 'home' %}">Home</a></li>
  <li><a href="{% url 'news' %}">News</a></li>
  <li><a href="{% url 'contact' %}">Contact</a></li>
  <li style="float:right"><a class="active" href="{% url 'about' %}">About</a></li>
</ul>
```
### Organize reuse code

create a new `navbar.html` and add:
```html
<ul>
  <li><a href="{% url 'home' %}">Home</a></li>
  <li><a href="{% url 'news' %}">News</a></li>
  <li><a href="{% url 'contact' %}">Contact</a></li>
  <li style="float:right"><a class="active" href="{% url 'about' %}">About</a></li>
</ul>
```

now include it in `home.html`:
```html
</head>
<body>

{% include 'navbar.html' %}

</body>
</html>
```

Now to use it in every page , block content need to be added in `home.html`:
```html
<body>

{% include 'navbar.html' %}

{% block content %}
<h1>This is home page</h1>
{% endblock content %}
</body>
```
now let's add in `about.html`:
first `home.html` need to be extend then all content need to be in `block` content:
```html
{% extends 'home.html' %}
{% block content %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This about page</h1>
</body>
</html>
{% endblock content %}
``` 

### Day 04 Recap:
- Day 03 recap
- In Virtual environment Start Django Project with DB migrate & superuser
- Initialize Django static file
- Get a navbar from [external source](https://www.w3schools.com/css/tryit.asp?filename=trycss_navbar_horizontal_black_right)
- Create a `template` folder `manage.py` file location
- Create a `index.html` file  inside `template` folder and view the navbar
- Template mastering
  - Now create individual other 3 pages (news,contact,about)
  - Make those navbar navigation working (hypertext reference `href`)
  - Stick navbar on each page (Organize reused code)
    - url
    - Include
    - block
    - Extend

### Task
- Upload today's recap video 
- Django Models

</details>

<details>
<summary>Day-05-App,Models,Entity & Attribute (19-03-2024)</summary>
    
## Day 05 Topics:
- Day 4 recap
- Create Django app
- Install app
- Models
- Database note
- Configure admin
- Make created object table name more identical

### Create Django app
for creating django app:
```bash
py manage.py startapp myapp
```
This command will create myapp project with additional files
### Install app
inside settings.py there is `INSTALLED_APPS` where we have to add our `myapp`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
```
### Models
Now in created `myapp` there is `models.py` file where we will create models (database data/table) :
```python
from django.db import models

# Create your models here.
class studentModel(models.Model):
    name=models.CharField(max_length=100)
    roll=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
```
### Database note
`Entity` - Table initial column names (e.g.: name,roll,department,city)

`Attribute` - values of entities (Tansen,05,CSE,Dhaka)

**Whenever we change anything in models we must perform:**
```bash
py manage.py makemigrations
```
```bash
py manage.py migrate
```
### Configure admin
Now in `admin.py` which is in `myapp` we need to import the created model and register it.
```python
from django.contrib import admin

from myapp.models import studentModel

# Register your models here.

admin.site.register(studentModel)
```
### Make created object table name more identical
In `models.py` file inside `myapp` we need to add `__str__` functions:
```python
from django.db import models

# Create your models here.
class studentModel(models.Model):
    name=models.CharField(max_length=100)
    roll=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    # this will make the table name more identical:
    def __str__(self):
        return f"{self.name}-{self.department}-{self.roll}"
```
### Quick Recap:
- App
- Model
- Site Register
- Create

### Day 05 Recap:
- Create Django project in virtual environment
- Initialize database (migrate)
- Create superuser (admin)
- Models
    - Create Django app
    - Install app (`in settings.py`)
    - Create some models
    - Configure admin (`site register`)
    - Migrate database (`Whenever changes in models`)
    - View and add data in created models

### Task
- Create 5 apps, 5 models, each model with 3 entity
- Submit video

</details>

<details>
<summary>Day-05-Extra & Assignment Notes</summary>

## Notes on creating 5 apps, 5 models & 3 entity for each

### blogapp

- BlogModel
    - blog_title
    - blog_date
    - blog_category

- NewsModel
    - news_headings
    - news_date
    - news_category

- CommentModel
    - comment_text
    - comment_date
    - commenter_name

- AuthorModel
    - author_name
    - author_bio
    - author_email

- TagModel
    - tag_name
    - tag_description
    - tagged_items


### kidsapp

- KidModel
    - kid_name
    - kid_age
    - kid_gender

- ToyModel
    - toy_name
    - toy_category
    - toy_price

- RatingModel
    - rating_value
    - rating_date
    - reviewer_name

- ManufacturerModel
    - manufacturer_name
    - manufacturer_location
    - manufacturer_contact
- LocationModel
    - location_name
    - location_description
    - location_address

### portfolioapp

- PortfolioModel
    - project_title
    - project_description
    - project_date

- ExperienceModel
    - company_name
    - job_title
    - employment_duration

- SkillModel
    - skill_name
    - skill_category
    - skill_proficiency

- EducationModel
    - institution_name
    - degree_obtained
    - graduation_year

- ProjectCategoryModel
    - category_name
    - category_description
    - categorized_projects


### ecommerceapp

- ProductModel
    - product_name
    - product_price
    - product_quantity

- OrderModel
    - order_number
    - order_date
    - customer_name


- ReviewModel
    - review_text
    - review_date
    - product_id

- SellerModel
    - seller_name
    - seller_email
    - seller_location

- PaymentModel
    - payment_method
    - payment_date
    - payment_amount


### aiapp

- aiModel
    - ai_name
    - ai_usages
    - ai_category

- TaskModel
    - task_name
    - task_deadline
    - task_priority

- DatasetModel
    - dataset_name
    - dataset_format
    - dataset_size

- ExperimentModel
    - experiment_name
    - experiment_date
    - experiment_results

- UserModel
    - user_name
    - user_email
    - user_role

</details>

<details>
<summary>Day-06-Reading Data from Database and Displaying it in Frontend (20-03-2024)</summary>

## Day 06 Topics:

- Day 5 recap
- Render html recap
- Navbar recap
- Read database data and show in frontend
- Common errors
- Task

### Read database data and show in frontend
Create a model in `models.py`:
```python
class BlogModel(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_author = models.CharField(max_length=100)
    blog_date = models.CharField(max_length=100)
    
    def __str__(self):
        return self.blog_title
```
Now register `BlogModel` in `admin.py`:
```python
from blogapp.models import BlogModel,AuthorModel,CommentModel,ReviewModel,TagModel
# Register your models here.

admin.site.register(BlogModel)
```
Now perform database migrations:
```bash
py manage.py makemigrations
py manage.py migrate
```
Now Let's enter some data from admin site and prepare to show it in frontend:
create a `template` folder in `manage.py` directory and create `index.html` get a navbar from [external source](https://www.w3schools.com/css/tryit.asp?filename=trycss_navbar_horizontal_black_right) , make sure to add `template` dir in `settings.py` file: `'DIRS': [BASE_DIR, 'templates']`:
```html
<!DOCTYPE html>
<html>
<head>
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #04AA6D;
}
</style>
</head>
<body>

<ul>
  <li><a href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li style="float:right"><a class="active" href="#about">About</a></li>
</ul>
<h1>This is home page</h1>
</body>
</html>
```
Now create separate `navbar.html` and only cut `ul` there:
```html
<ul>
  <li><a href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li style="float:right"><a class="active" href="#about">About</a></li>
</ul>
```
Now in `index.html` do the template mastering using `include` and `block`:
```html
{% include 'navbar.html' %}
{% block content %}
<h1>This is home page</h1>
{% endblock content %}
```
Now when creating others page we just need to `extends` `index.html` and `block content` will be that page content. e.g:
```html
{% extends 'index.html' %}
{% block content %}
<h1>This is news page</h1>
{% endblock content %}
```
Now lets add it in `views.py`
```python
from django.shortcuts import render,redirect,HttpResponse
from blogapp.models import BlogModel,AuthorModel,CommentModel,ReviewModel,TagModel

def home(request):
    blog=BlogModel.objects.all()
    myDict={
        'blog':blog
    }
    return render(request,'index.html',myDict)
```
here `blog=BlogModel.objects.all()` to read `blogModel` data from database. now set `url.py`'s `urlpatterns`:
```python
path('home/',home,name='home'),
```
Now let's add a table from [external source](https://www.w3schools.com/css/tryit.asp?filename=trycss_table_fancy):
```html
<!DOCTYPE html>
<html>
<head>
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #04AA6D;
}
</style>
</head>
<body>

{% include 'navbar.html' %}

{% block content %}
<h1>This is blog page</h1>
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>A Fancy Table</h1>

<table id="customers">
  <tr>
    <th>Blog Title</th>
    <th>Blog Author</th>
    <th>Blog Date</th>
  </tr>

  {% for i in blog %}
  <tr>
    <td>{{i.blog_title}}</td>
    <td>{{i.blog_author}}</td>
    <td>{{i.blog_date}}</td>
  </tr>
  {% endfor %}

</table>

</body>
</html>

{% endblock content %}
    
</body>
</html>

```
Here `{% for i in blog %}`is used to loop through the `blog`. Similarly other model will be created and read the data from database to show it in frontend.
###  Common errors
- `OperationalError`: When `makemigrations` / `migrate` not performed and try to access database data, it will give `OperationalError`
- `Value not Assign`: This error occurs sometimes, to solve this error inside `app`'s `models.py` file set `null=True` e.g: `author_name=models.CharField(max_length=100, null=True)`

### Day 06 Recap:
- Create project & app under virtual environment
- Migrate db & create superuser
- Create 5 models, 5 navbar for each model
- Read the database data
- Show the data in frontend

### Task
- Presentation from day 1 to day 6
- submit video (youtube)
- 1 app, 5 model, 5 navbar

</details>

<details>
<summary>Day-06-A Quick Recap from Day 01 to Day 06</summary>

1. Create and active environment
    - `py -m venv env`
    - `./env/Scripts/activate`
2. Create django project
    - `django-admin startproject my_project`
    - `cd my_project`
    - `py manage.py runserver`
3. Migrate database
    - `py manage.py makemigrations`
    - `py manage.py migrate`
4. Create superuser
    - `py manage.py createsuperuser`
5. Show simple text on website
    - Create a `views.py` within prject directory
    - Use `HttpResponse` to view a simple `Text/String`
    - import created function in `urls.py` file and add `urlpatterns` path
6. Render a simple html page
    - First add django static file path setting in `settings.py` file
    - Create `template` folder in `manage.py` directory
    - Now create a `html` file within `template` folder
    - Go to project directory and create a function to render the created `html` file.
7. Show a simple table in html page
    - After doing `6th` step, create a simple table with html `table tag`
8. Get a table from external source and view it
    - Get a `fancy table` from `w3school`
9. Now send table data from backend
    - In `views.py` where `function` is defined add a `dictionary` there and `return` it
10. Get a navbar from external source
    - Get a horizontal `navbar` from `w3school`
11. By template mastering separate navbar and use on other pages
    - Create a `navbar.html` file
    - Now use `include` in `index.html` page to show the navbar in index page
    - Use `block content` to show the content
    - For other pages use `extends`
12. Now Create a app and model
    - `py manage.py startapp blogapp`
    - Add this app name in `settings.py` file within `INSTALLED_APPS`
    - Now in created `blogapp` there is `models.py`
    - Create a `Model` and register it in `admin.py`
    - Each time changes in `models.py` do `py manage.py makemigrations` and `py manage.py migrate`
13. Now show the created model data in frontend
    - Create a `blog.html` put table data here using `block content` and `extends` `index.html` at first line which will include the `navbar`
    - In views.py import the created `model`. Create a function and get the model data in a `varible` using `objects.all()`. Now create a `dictionary` and assign it with the `variable` of `model data`. return the dictionary.
    - Now add `path` in `urls.py` file
    - Go to `navber.html` and add `url` with created `path name`
    - In `blog.html` create a for `loop` to show the model data

</details>

<details>
<summary>Day-07-Exam Day 01 Practical Exam (23-03-2024)</summary>

## Exam Day 01 on Day-06 task (Practical Exam)
### Question:
- Create a studentModel with all the functionality you have learned from day 01 to day 06:
  - Create a folder as 'your_name'
  - Create Django project within virtual environment
  - Create a app for model creation
  - Include a navbar for navigation
  - Do template mastering
  - Fetch the data from database to frontend
  - Show the student model data in frontend

</details>

<details>
<summary>Day-08-Exam Day 02 Written Exam (24-03-2024)</summary>

## Exam Day 02 on Day-06 task (Written Exam)
### Question:
- 5 MCQ Question
- 8 Short Question
- 2 Practical Question

### MCQ Question
Which of the following is not a component of a Django project?
  - [ ] Views
  - [ ] Models
  - [ ] Controllers
  - [ ] Templates

What is the purpose of the urls.py file in Django?
  - [ ] To define the structure of the database
  - [ ] To specify the URL patterns of the routing
  - [ ] To configure project-wide settings
  - [ ] To define HTML templates

What command is used to create a new Django project?
  - [ ] django new
  - [ ] django startproject
  - [ ] django create
  - [ ] django init

In Django, which file is used to define database models?
  - [ ] views.py
  - [ ] models.py
  - [ ] settings.py
  - [ ] admin.py

What command is used to apply database migrations in Django?
  - [ ] manage.py apply
  - [ ] manage.py migrate
  - [ ] manage.py update
  - [ ] manage.py deploy

### Short Question
1. Describe the purpose of urls.py, models.py, admin.py
2. Which files is responsible for defining the database settings for a Django project?
3. What are migrations in Django? Explain the purpose of the `manage.py makemigrations` and `manage.py migrate` commands.
4. How do you define URL patterns in Django's `urls.py`
5. What is the purpose of the `settings.py` file in Django?
6. What is the purpose of Django's template language?
7. What is the default database used by Django and how do you configure it?
8. Explain the concept of the middleware in Django

### Practical Question
- Create a Django project named "myproject" and an app named "myapp". Define a model in "myapp" with fields: name (CharField) and age (IntegerField)
- Write a function-based view in Django to render a simple HTML template that displays "Hello, World!"
### Task : 
- Poster presentation based on Day 01 to Day 06 (27-03-2024)
- Oral test tomorrow (25-03-2024)

</details>

<details>
<summary>Day-09-Django CRUD Add Operation From Frontend (25-03-2024)</summary>

## Day 09 Topics:
- Day 01 - 06 recap
- Oral test
- Model add operation from frontend
- null = True explained
- An error after modifying previous saved model (null return typeError)
- Day 09 Recap
- Task

### Model add operation from frontend
Create a form page `addstudent.html`
```html
{% extends 'base.html' %}

{% block content %}
<!DOCTYPE html>
<html>
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>
<body>

<h3>Using CSS to style an HTML Form</h3>

<div>
  <form action="{% url 'addstudent' %}" method="POST">
    {% csrf_token %}
    <label for="fname">Name</label>
    <input type="text" id="fname" name="name" placeholder="Your name..">

    <label for="lname">Department</label>
    <input type="text" id="lname" name="department" placeholder="Your Department">
    <label for="lname">City</label>
    <input type="text" id="lname" name="city" placeholder="Your City">
  
    <input type="submit" value="Submit">
  </form>
</div>

</body>
</html>
{% endblock content %}
    
```
- Here method will be always `POST`
- Here action url will be the name value from `urls.py` file of `addstudent`
- `csrf_token` is used for security
- Here `name="department"` is important as we will get the form value by this

Now add a function in `views.py` as below:
```python
def addstudent(request):
    if request.method=='POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        
        student=studentModel(
            Name=name,
            Department=department,
            City=city,
        )
        
        student.save()
        return redirect('student')
    return render(request,'addstudent.html')
```
- Here if `request.method=='POST'` is true then we will get the value from form by `POST` method 
- Then we will add those value in our previously created model which is `studentModel`
- After that save the model and in frontend user will be redirected to `student.html` page

### null = True explained
Sometimes we get error while migrating a model. a common solution is adding `null=True`:
```python
class studentModel(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Department=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
```
For example let's assume we created a model with 3 entity and work with that but after sometimes when we add a new entity to that model an error will occur as empty value is being assign to the model. so to add that new entity we have to explicitly add `null=True` to add that new entity as empty null value.

### An error after modifying previous saved model (null return typeError)
This error occur as below:
```python
class studentModel(models.Model):
    Name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
```
In this code when we have modified our studentModel entity `return self.Name` will throw an error of type error. commenting this will solved it.
### Day 09 Recap:
- Create Django Models with 5 add operation in frontend
  - Create django project & app in virtual environment
  - Setup app, static, template files
  - Create 5 navigation pages in navbar with table to show the added data
    - Student Table
    - Mark Table
    - Teacher Table
    - Subject Table
    - University Table
  - Create 5 more navigation pages in navbar to add data from frontend
    - Add Student
    - Add Mark
    - Add Teacher
    - Add Subject
    - Add University
  - Create form for each 5 add operation pages

### Task
- Create 5 add operation pages and show the data in table


</details>

<details>
<summary>Day-10-Django CRUD Delete Operation From Frontend (27-03-2024)</summary>

## Day 10 Topics
- Day 09 recap
- Oral test
- Two annoying error (comma method in form, model return type error)
- Delete operation
- Special notes (return , redirect error)
- Exam Result
- Task

### Oral test:
- Explain urlpatterns (It define to specific path route to handle the request)
- How navigation route is working explain (from urls.py to views.py there request handle the request and fetch the required data to show in the defined html page)
- Explain models.Model and what will happened if we don't use it (in models.Model module SQL is defined)
- Explain Database concept (Entity,attribute,default value,primary key, etc.....)
- How database is configure by settings.py and not models.py (initially everything is configure in settings.py file)
- What we will find if we break database (answer: table)

### Two annoying error
The first one is form submit stay in the same page after submitting
```html
<div>
  <form action="{% url 'addstudent' %}" method="POST">
    {% csrf_token %}
    <label for="fname">Name</label>
    <input type="text" id="fname" name="name" placeholder="Your name..">

    <label for="lname">Department</label>
    <input type="text" id="lname" name="department" placeholder="Your Department">
    <label for="lname">City</label>
    <input type="text" id="lname" name="city" placeholder="Your City">
  
    <input type="submit" value="Submit">
  </form>
</div>
```
- `<form action="{% url 'addstudent' %}" method="POST">` if this line is include comma between `{% url 'addstudent' %}",method="POST"` this cause the page stay in the same page even after submit.

Second one is model return type error
```python
 class studentModel(models.Model):
    Name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
```
- In here `self.Name` return will give error when there is `max_length=100,null=True` it is because when explicitly adding new entity we have to make it `null=True` but by doing this when `return` is trying to access `Name` it get `None` so that causes error. Deleting the value will solved it.

### Delete operation
Go to table html page and add as below `Action column` and Delete url with id:
```html
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
        </td>
    </tr>

  {% endfor %}
    
</table>
```
Now in `views.py` file add a function named `deleteStudent`
```python
def deleteStudent(request,myid):
    student=studentModel.objects.get(id=myid)
    student.delete()
    return redirect('student')
```
In `urls.py` file add as below:
```python
from django.contrib import admin
from django.urls import path
from d10_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteStudent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
]
```
### Special notes
- When a function is defined but not return or redirect to anything than an error will occur
  ```python
  def deleteStudent(request,myid):
      student=studentModel.objects.get(id=myid)
      student.delete()
  ```
- This will do the delete but after that will show an error page with `deleteStudent didn't return an HttpResponse object it returned None Instead`

## Exam Result
- **Practical** --> 25/25 (Completed the task in 17 minutes ; time limit was 30 minutes)
- **Written** --> 21/25 (Short question database configure answer was `settings.py`, Others question need to be answer in more detail way)
- **Oral** --> 7/10 (Was confuse on database and how navigation works in backend question)
- **Total** --> `53 marks`

### Task:
- Create 5 models & perform delete operation from frontend
    - Create 5 model:
        - StudentModel
        - MarkModel
        - TeacherModel
        - SubjectModel
        - UniversityModel
    - Create 5 page in drop down navbar with table to show the added data
        - Student Table
        - Mark Table
        - Teacher Table
        - Subject Table
        - University Table
    - Create 5 form page for each table pages
        - Add Student
        - Add Mark
        - Add Teacher
        - Add Subject
        - Add University
    - Add an action on each table column to delete data


</details>

<details>
<summary>Day-11-Django CRUD Edit Update & View Operation (28-03-2024)</summary>

## Day 11 Topics:
- Day 10 Recap
- Edit operation
- Add view action
- Get vs Filter QuerySet
- Task

## Edit operation
In table page `student.html` add a href link for edit action:
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>A Fancy Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
          <a href="">Edit</a>
        </td>
    </tr>

  {% endfor %}
    
</table>

</body>
</html>



{% endblock content %}
    
```
- Here href is empty so let's add a page for editing then link that page in this `href`

Create `editstudent.html` file and add as below:
```html
{% extends 'base.html' %}


{% block content %}
<h1> edit page </h1>
{% endblock content %}
    
```
Now create a function in `views.py` file to view this page:
```python
def editstudent(request,myid):
    student=studentModel.objects.filter(id=myid)
    myDict={
        'student':student
    }
    return render(request,'editstudent.html',myDict)
```
- Here we have `myid` which is needed to specific data and using `filter QuerySet` as it is iterable. 

Now import this in `urls.py` file and create the route path
```python
from django.contrib import admin
from django.urls import path
from d11_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,editstudent,
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('editstudent/<int:myid>',editstudent,name='editstudent'),
]

```
- Here `<int:myid>` to get the id in path route

Finally add this url `name` in `student table` page with for loop to iterate the data
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>A Fancy Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
          <a href="{% url 'editstudent' i.id %}">Edit</a>
        </td>
    </tr>

  {% endfor %}
    
</table>

</body>
</html>

{% endblock content %}
    
```
Now we will be able to see the data in `edit page` as below:
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}


</style>
<body>

<h3>Using CSS to style an HTML Form</h3>

<div>
  <form action="" method="POST">
    {% csrf_token %}
    
    {% for i in student %}
    <label for="fname">ID</label>
    <input type="text" id="fname" value={{i.id}} name="myid" placeholder="Your ID.." readonly>
    <label for="fname">Name</label>
    <input type="text" id="fname" value={{i.Name}} name="name" placeholder="Your name..">

    <label for="lname">Department</label>
    <input type="text" id="lname" value={{i.Department}} name="department" placeholder="Your Department">
    <label for="lname">City</label>
    <input type="text" id="lname" value={{i.City}} name="city" placeholder="Your City">
    {% endfor %}
        

  
    <input type="submit" value="Submit">
  </form>
</div>

</body>
</html>
{% endblock content %}
    
```
As we are able to see the data which we can edit but we need to implement the submit to work with update functionalities. For that we will create a update function in `views.py`
```python
def updatestudent(request):
    if request.method=="POST":
        myid=request.POST.get('myid')
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        
        student=studentModel(
            id=myid, # this need to be done otherwise new value will be added rather than update
            Name=name,
            Department=department,
            City=city,
        )
        student.save()
        return redirect('student')
```
- This is similar as add function only deference is editing it by specific `ID`

Now import and create the path in `urls.py`
```python
from django.contrib import admin
from django.urls import path
from d11_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,editstudent,updatestudent,viewstudent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('editstudent/<int:myid>',editstudent,name='editstudent'),
    path('updatestudent',updatestudent,name='updatestudent'),
    
]

```
Now the `name` value `'updatestudent'` will be in the action url of the edit page form as: `<form action="{% url 'updatestudent' %}" method="POST">`


### Add view action:
Create a view page `viewstudent.html`:
```html
{% extends 'base.html' %}


{% block content %}

<h1>View student page</h1>

{% endblock content %}
    
```
It is similar as editing function; add view function in `views.py`:
```python
def viewstudent(request,myid):
    student=studentModel.objects.filter(id=myid)
    myDict={
        'student':student
    }
    return render(request,'viewstudent.html',myDict)
```

Add path in `urls.py`:
```python
from django.contrib import admin
from django.urls import path
from d11_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,editstudent,updatestudent,viewstudent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('editstudent/<int:myid>',editstudent,name='editstudent'),
    path('updatestudent',updatestudent,name='updatestudent'),
    path('viewstudent/<int:myid>',viewstudent,name='viewstudent'),
    
]

```
Add `viewstudent` in `href` of `student table` view action:
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>A Fancy Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
          <a href="{% url 'editstudent' i.id %}">Edit</a>
          <a href="{% url 'viewstudent' i.id %}">View</a>
        </td>
    </tr>

  {% endfor %}
    
</table>

</body>
</html>
{% endblock content %}

```
Now after clicking on `View` it will go to `viewstudent.html` page , Let's add a `CSS card` and loop throw the value we will get to show it in user info format:
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 40%;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.container {
  padding: 2px 16px;
}
</style>
</head>
<body>

<h2>Card</h2>

<div class="card">
  <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="width:100%">
  <div class="container">
    
    {% for i in student %}
    <h4><b>{{i.Name}}</b></h4> 
    <p>{{i.Department}}</p> 
    <p>{{i.City}}</p> 
    {% endfor %}
        

  </div>
</div>

</body>
</html> 

{% endblock content %}
    
```

### Get vs Filter QuerySet
- Get is not iterable
- Filter is iterable

While trying to get user data a problem was faced and this [Stack Overflow](https://stackoverflow.com/questions/56374741/django-model-object-is-not-iterable) answer helped.

### Task:
- Create Edit Update & View action in table data
- Saturday (30-03-2024) Exam based on Day 1 to 11 task

</details>

<details>
<summary>Day-11-Django CRUD Quick recap</summary>

## Django CRUD Quick recap:
1. setup virtual env and django project
    - `.\env\Scripts\activate`
    - `django-admin startproject d11_practise`
2. Migrate database and create superuser
    - `py manage.py makemigrations`
    - `py manage.py migrate`
    - `py manage.py createsuperuser`
3. Create an app
    - `py manage.py startapp studentapp`
4. Add the app name in `settings.py` file `INSTALLED_APPS`
    - `'studentapp'`
5. Add Django static file & template path
    - Static file (at the end):
        ```python
        STATICFILES_DIRS = [
        BASE_DIR / "static",
        "/var/www/static/",
        ]
        ```
    - Template path in TEMPLATES:
        `'DIRS': [BASE_DIR,'template'],`
6. Create a `template` folder in `manage.py` directory and create some initial pages like `base.html`, `navbar.html` etc.
7. Get a navbar code from external site and paste it in `base.html`
8. For template mastering separate navbar from the `base.html` and paste it in `navbar.html` file
    ```html
    <ul>
    <li><a href="#student">Student</a></li>
    </ul>
    ```
9. Now in `base.html` `include` it and create a empty `block content` inside body tag
    ```html
    <body>

    {% include 'navbar.html' %}


    {% block content %}
        
    {% endblock content %}

    </body>
    ```
10. Now create a `student.html` page and `extends` the `base.html` with its own `block content`
    ```html
    {% extends 'base.html' %}

    {% block content %}
        <h1>Student page</h1>
    {% endblock content %}
    ```
11. Now to view the `student.html` page we need to create `views.py` file in project directory where `settings.py` exits. In `views.py` we need to define a function where we will render our created `student.html` file
    ```python
    from django.shortcuts import render,redirect

    def student(request):
    return render(request,'student.html')
    ```
12. Now in` urls.py` file we have to import our created `student` function set the route
    ```python
    from django.contrib import admin
    from django.urls import path
    from d11_practise.views import student

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('student/',student,name='student'),
    ]
    ```
13. Now we have to add the `name` value in `navbar.html` file `href`
    ```html
    <ul>
        <li><a href="{% url 'student' %}">Student</a></li>
    </ul>
    ```
14. Now in `http://127.0.0.1:8000/student/` link we can view our created `student.html` page
15. Let's add a table in our student page. a table from w3school (fancy table)
    ```html
    {% extends 'base.html' %}


    {% block content %}
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    #customers {
    font-family: Arial, Helvetica, sans-serif;
    border-collapse: collapse;
    width: 100%;
    }

    #customers td, #customers th {
    border: 1px solid #ddd;
    padding: 8px;
    }

    #customers tr:nth-child(even){background-color: #f2f2f2;}

    #customers tr:hover {background-color: #ddd;}

    #customers th {
    padding-top: 12px;
    padding-bottom: 12px;
    text-align: left;
    background-color: #04AA6D;
    color: white;
    }
    </style>
    </head>
    <body>

    <h1>A Fancy Table</h1>

    <table id="customers">
    <tr>
        <th>Name</th>
        <th>Department</th>
        <th>City</th>
    </tr>
    </table>

    </body>
    </html>
    {% endblock content %}
    ```
16. To add table let's create model in our app `models.py` file
    ```python
    from django.db import models

    # Create your models here.
    class studentModel(models.Model):
        Name=models.CharField(max_length=100)
        Department=models.CharField(max_length=100)
        City=models.CharField(max_length=100)
        
        def __str__(self):
            return self.Name
    ```
17. Register this model in `admin.py`
    ```python
    from django.contrib import admin
    from studentapp.models import studentModel

    # Register your models here.
    admin.site.register(studentModel)
    ```
18. Now we have to migrate it
    - `py manage.py makemigrations`
    - `py manage.py migrate`
19. Now go to admin page `http://127.0.0.1:8000/admin/` and add data in student model
20. To see the data in frontend we have to `READ` it. let's import our model in `views.py` and return the data as `dictionary` in frontend
    ```python
    from django.shortcuts import render,redirect
    from studentapp.models import studentModel

    def student(request):
        student=studentModel.objects.all()
        myDict={
            'student':student
        }
        return render(request,'student.html',myDict)
    ```
21. Now in our `student.html` file we have to iterate the student data using loop
    ```python
    <table id="customers">
    <tr>
        <th>Name</th>
        <th>Department</th>
        <th>City</th>
    </tr>
    
    {% for i in student %}
        <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        </tr>
    {% endfor %}
        
    </table>
    ```
    Here `i.Name`, `i.Department`, `i.City` will be same as defined in `models.py` file. Now we can see the data in frontend at `http://127.0.0.1:8000/student/` route.
22. Now let's add data from frontend not from admin page, to do that we will create a form page named `addstudent.html`
    ```html
    {% extends 'base.html' %}

    {% block content %}
    <!DOCTYPE html>
    <html>
    <style>
    input[type=text], select {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    }

    input[type=submit] {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    }

    input[type=submit]:hover {
    background-color: #45a049;
    }
    </style>
    <body>

    <h3>Using CSS to style an HTML Form</h3>

    <div>
    <form action="" method="">
        {% csrf_token %}
        <label for="fname">Name</label>
        <input type="text" id="fname" name="name" placeholder="Your name..">

        <label for="lname">Department</label>
        <input type="text" id="lname" name="department" placeholder="Your Department">
        <label for="lname">City</label>
        <input type="text" id="lname" name="city" placeholder="Your City">
    
        <input type="submit" value="Submit">
    </form>
    </div>

    </body>
    </html>
    {% endblock content %}
    ```
    Here `action`, `method`, `name` attribute is important
23. To view `addstudent` form page we will similarly create a function in `views.py` to render it
    ```python
    def addstudent(request):
        return render(request,'addstudent.html')
    ```
    Add the path in `urls.py` file for routing
    ```python
    from django.contrib import admin
    from django.urls import path
    from d11_practise.views import student,addstudent

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('student/',student,name='student'),
        path('addstudent/',addstudent,name='addstudent'),
    ]
    ```
    To see it in frontend let's add the `name` in `navbar.html` file
    ```html
    <ul>
        <li><a href="{% url 'student' %}">Student</a></li>
        <li><a href="{% url 'addstudent' %}">Add Student</a></li>
    </ul>
    ```
24. Now to get the data from frontend to backend we will assign the `action`
    - `action="{% url 'addstudent' %}"` and set the method as POST `method="POST"`
    - Set the `name` attribute, will be used to get the value
25. In `views.py` `addstudent` function we will get the value and assign it in our model
    ```python
    def addstudent(request):
        if request.method=='POST':
            name=request.POST.get('name')
            department=request.POST.get('department')
            city=request.POST.get('city')
            
            student=studentModel(
                Name=name,
                Department=department,
                City=city,
            )
            student.save()
            return redirect('student')
        return render(request,'addstudent.html')
    ```
    Here we have get the values by `name attribute` then assign those value in our `model` after that we save it and `redirect` to the `student` page. Now in our `http://127.0.0.1:8000/addstudent/` route we can add data in our form and after submitting the data will be shown in `http://127.0.0.1:8000/student/` route
26. Now Let's create a action for deleting the data, In `student.html` page create a table column `Action` and create a `href link` as `Delete`
    ```html
    <table id="customers">
    <tr>
        <th>Name</th>
        <th>Department</th>
        <th>City</th>
        <th>Action</th>
    </tr>
    
    {% for i in student %}
        <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td><a href="">Delete</a></td>
        </tr>
    {% endfor %}
        
    </table>
    ```
27. Now we have to create a functions in `views.py` with id so that we can `filter` the specific id to delete
    ```python
    def deletestudent(request,myid):
        student=studentModel.objects.filter(id=myid)
        student.delete()
        return redirect('student')
    ```
    In `urls.py` we have to specify the id also
    ```python
    from django.contrib import admin
    from django.urls import path
    from d11_practise.views import student,addstudent,deletestudent

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('student/',student,name='student'),
        path('addstudent/',addstudent,name='addstudent'),
        path('deletestudent/<int:myid>',deletestudent,name='deletestudent'),
    ]
    ```
    Now we have to add the `href` url in` Delete`:

    `<td><a href="{% url 'deletestudent' i.id %}">Delete</a></td>`

    Now the `Delete action` will work in our student table
28. Now let's Edit the table value, add a new Action in table as `Edit`
    ```html
      <td>
        <a href="{% url 'deletestudent' i.id %}">Delete</a>
        <a href="">Edit</a>
      </td>
    ```
    Create the same form page of add student but as `editstudent.html`
    ```html
    {% extends 'base.html' %}

    {% block content %}
    <!DOCTYPE html>
    <html>
    <style>
    input[type=text], select {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    }

    input[type=submit] {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    }

    input[type=submit]:hover {
    background-color: #45a049;
    }
    </style>
    <body>

    <h3>Using CSS to style an HTML Form</h3>

    <div>
    <form action="" method="POST">
        {% csrf_token %}
        <label for="fname">Name</label>
        <input type="text" id="fname" name="name" placeholder="Your name..">

        <label for="lname">Department</label>
        <input type="text" id="lname" name="department" placeholder="Your Department">
        <label for="lname">City</label>
        <input type="text" id="lname" name="city" placeholder="Your City">
    
        <input type="submit" value="Submit">
    </form>
    </div>

    </body>
    </html>
    {% endblock content %}
    ```
    Create a function in `views.py`
    ```python
    def editstudent(request,myid):
        student=studentModel.objects.filter(id=myid)
        myDict={
            'student':student
        }
        return render(request,'editstudent.html',myDict)
    ``` 
    Here we are reading the data from our model and sending it to form of `editstudent.html` file.

    Add the path in `urls.py`
    ```python
    from django.contrib import admin
    from django.urls import path
    from d11_practise.views import student,addstudent,deletestudent,editstudent

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('student/',student,name='student'),
        path('addstudent/',addstudent,name='addstudent'),
        path('deletestudent/<int:myid>',deletestudent,name='deletestudent'),
        path('editstudent/<int:myid>',editstudent,name='editstudent'),
    ]
    ```
    Now add this `name` value in `Edit` action `href`

    `<a href="{% url 'editstudent' i.id %}">Edit</a>`

    Now after clicking on edit it wil show the form of `editstudent.html` file. Let's iterate using loop to show the value also for editing with `value` attribute
    ```html
    <form action="" method="POST">
        {% csrf_token %}
        
        {% for i in student %}
        <label for="fname">ID</label>
        <input type="text" id="fname" value={{i.id}} name="myid" placeholder="Your id.." readonly>
        <label for="fname">Name</label>
        <input type="text" id="fname" value={{i.Name}} name="name" placeholder="Your name..">

        <label for="lname">Department</label>
        <input type="text" id="lname" value={{i.Department}} name="department" placeholder="Your Department">
        <label for="lname">City</label>
        <input type="text" id="lname" value={{i.City}} name="city" placeholder="Your City">
        {% endfor %}
        <input type="submit" value="Submit">
    </form>
    ```
    Here a new attribute added which is `value` also `id` viewing as `readonly`

29. Now to make the edit work we will define a function `views.py` as `updatestudent`
    ```python
    def updatestudent(request):
        if request.method=='POST':
            myid=request.POST.get('myid')
            name=request.POST.get('name')
            department=request.POST.get('department')
            city=request.POST.get('city')
            
            student=studentModel(
                id=myid,
                Name=name,
                Department=department,
                City=city,
            )
            student.save()
            return redirect('student')
    ```
    Now add the path in `urls.py` 
    ```python
    from django.contrib import admin
    from django.urls import path
    from d11_practise.views import student,addstudent,deletestudent,editstudent,updatestudent

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('student/',student,name='student'),
        path('addstudent/',addstudent,name='addstudent'),
        path('deletestudent/<int:myid>',deletestudent,name='deletestudent'),
        path('editstudent/<int:myid>',editstudent,name='editstudent'),
        path('updatestudent',updatestudent,name='updatestudent'),
    ]
    ```
    Now update the `action` in `editstudent.html` file as `action="{% url 'updatestudent' %}"`

    This will make the submit work after editing.
30. To add `View action` we can do the same as where we define our function with id to view the specific table data.

</details>

<details>
<summary>Day-12-Assessment-02 (30-03-2024)</summary>

## Day 12 Assessment-02

Question: As a job recruiter, you are tasked with hiring a Django developer for a project that involves managing user data. You need to create a model to store information about potential candidates. Define the fields for this model, keeping in mind the CRUD (Create, Read, Update, Delete) operations you may need to perform.

> Define the following fields for the candidate model, using only CharField type:

`full_name`: A CharField to store the full name of the candidate.

`email`: A CharField to store the email address of the candidate.

`phone_number`: A CharField to store the phone number of the candidate.

`address`: A CharField to store the address of the candidate.

`job_title`: A CharField to store the job title or desired position of the candidate.

`linkedin_profile`: A CharField to store the Linkedin profile URL of the candidate.

`university`: A CharField to store the university or educational institution of the candidate.

`degree`: A CharField to store the degree attained by the candidate.

`languages`: A CharField to store the languages known by the candidate.

`years_of_experience`: A CharField to store the years of professional experience of the candidate.

> Total time took for me --> 43 Minutes

</details>

<details>
<summary>Day-13-Python Basic Day 01, View Action & All Model Table Data in Single Page (31-03-2024)</summary>

## Day 13 Topics:-
- Security & code editor
- Python Basic Day 01
- Variable
- View Action 
- Task

### Security & code editor
Compiler / Interpreter -->Translator (Python has both)

- Interpreter--> (line by line)
- Compiler--> (Run at once)
- Security (csrf,session-hijack,man in the middle attack,vulnerability)
- Authentication

### Python Basic
- Variable
- Operator
- Condition (increment / decrement)
    - Nested condition
- Loop
    - Nested loop
- Array (1d,2d,3d)
    - List
    - Set
    - Tuple
    - Dictionary
- Function
    - Recurssion (self call)
- OOP 
    - Inheritance
    - Incapsulation
    - Polymorphism
    - Class / Object
### Variable
- Changeable (able to vary)
- It is volatile
- Assign sign (`=`)
- Comparison / equal (`==`)

### View Action

To add view action go to the table page `student.html` file and add view action:
```html
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
          <a href="">View</a>
        </td>
    </tr>

  {% endfor %}
    
</table>
```
Now create a page `viewstudent.html` page and use the css card html code there:
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>
</head>
<body>

<h2 style="text-align:center">User Profile Card</h2>


{% for i in student %}
<div class="card">
    <img src="/w3images/team2.jpg" alt="John" style="width:100%">
    <h1>{{i.Name}}</h1>
    <p class="title">{{i.Department}}, {{i.City}}</p>
  </div>
{% endfor %}
    


</body>
</html>

{% endblock content %}
    
```
Now Create function in `views.py` file:
```python
def viewstudent(request,myid):
    student=studentModel.objects.filter(id=myid)
    myDict={
        'student':student
    }
    return render(request,'viewstudent.html',myDict)
```
Add the url path in `urls.py` file
```python
from django.contrib import admin
from django.urls import path
from d13_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,viewstudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('viewstudent/<int:myid>',viewstudent,name='viewstudent'),
]
```
Now add url in student page view action `<a href="{% url 'viewstudent' i.id %}">View</a>` with id.

Similarly it is done with other pages too.

For viewing all model table in single page. Just create a new page and add a function in `views.py` that return all table data from models  and link the url path 

`alltable.html`:
```html
{% extends 'base.html' %}

{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>Student Table</h1>
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
    </tr>
  {% endfor %}
    
</table>
<h1>Mark Table</h1>
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Roll</th>
    <th>Mark</th>
  </tr>
  
  {% for i in mark %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Roll}}</td>
        <td>{{i.Mark}}</td>
    </tr>
  {% endfor %}
    
</table>
<h1>Teacher Table</h1>
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
  </tr>
  
  {% for i in teacher %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
    </tr>
  {% endfor %}
    
</table>
<h1>Subject Table</h1>
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Category</th>
    <th>Mark</th>
  </tr>
  
  {% for i in subject %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Category}}</td>
        <td>{{i.Mark}}</td>
    </tr>
  {% endfor %}
    
</table>
<h1>University Table</h1>
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Rank</th>
    <th>Location</th>
  </tr>
  
  {% for i in university %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Rank}}</td>
        <td>{{i.Location}}</td>
    </tr>
  {% endfor %}
    
</table>

</body>
</html>

{% endblock content %}
    
```

`views.py`:
```python
def alltable(request):
    student=studentModel.objects.all()
    mark=markModel.objects.all()
    teacher=teacherModel.objects.all()
    subject=subjectModel.objects.all()
    university=universityModel.objects.all()
    myDict={
        'student':student,
        'mark':mark,
        'teacher':teacher,
        'subject':subject,
        'university':university,
    }
    return render(request,'alltable.html',myDict)
```

`urls.py`:
```python
from django.contrib import admin
from django.urls import path
from d13_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,viewstudent,viewteacher,viewmark,viewsubject,viewuniversity,alltable
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('viewstudent/<int:myid>',viewstudent,name='viewstudent'),
    path('viewteacher/<int:myid>',viewteacher,name='viewteacher'),
    path('viewmark/<int:myid>',viewmark,name='viewmark'),
    path('viewsubject/<int:myid>',viewsubject,name='viewsubject'),
    path('viewuniversity/<int:myid>',viewuniversity,name='viewuniversity'),
    path('alltable/',alltable,name='alltable'),
    
]
```
Now link the `alltable.html` page in navbar:
```html
<div class="navbar">
    <div class="dropdown">
      <button class="dropbtn">Add Tables 
        <i class="fa fa-caret-down"></i>
      </button>
      <div class="dropdown-content">
        <a href="{% url 'addstudent' %}">Add Student</a>
        <a href="{% url 'addmark' %}">Add Mark</a>
        <a href="{% url 'addteacher' %}">Add Teacher</a>
        <a href="{% url 'addsubject' %}">Add Subject</a>
        <a href="{% url 'adduniversity' %}">Add University</a>
      </div>
    </div> 
    <div class="dropdown">
      <button class="dropbtn">View Tables 
        <i class="fa fa-caret-down"></i>
      </button>
      <div class="dropdown-content">
        <a href="{% url 'student' %}">Student Table</a>
        <a href="{% url 'mark' %}">Mark Table</a>
        <a href="{% url 'teacher' %}">Teacher Table</a>
        <a href="{% url 'subject' %}">Subject Table</a>
        <a href="{% url 'university' %}">University Table</a>
        <a href="{% url 'alltable' %}">All Table</a>
      </div>
    </div> 
  </div>
```
### Task:
- Practice variable task
- Add view action
- Show all model data in single page

</details>

<details>
<summary>Day-14-Add Image Option with Delete, Edit, View Action (01-04-2024)</summary>

## Day 14 Topics
- Day 13 recap
- Add Image
- Disscussion on previous batch final assessment
- Task

### Add Image
For adding image , first we have to add image field in our model
```python
class studentModel(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Department=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
    StudentImage=models.ImageField(upload_to='media/StudentImages',null=True)
    
    def __str__(self):
        return self.Name
```
- Here `StudentImage` is added with `ImageField` which include path `media/StudentImages`
- Setting `null=True` either an error will occur

After changes in model we have to use migrations command: `py manage.py makemigrations` then `py manage.py migrate`

Now we can add image from admin site : `http://127.0.0.1:8000/admin/`

After adding image to view it in frontend table, we have to edit our `student.html` page table 
```html
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Image</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <img src="/{{i.StudentImage}}" alt="" width="50">
        </td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
          <a href="{% url 'viewstudent' i.id %}">View</a>
        </td>
    </tr>

  {% endfor %}
    
</table>
```
- Here `<img src="/{{i.StudentImage}}" alt="" width="50">` is added ad source of the image. This line can be written like this also: `<img src="{{i.StudentImage.url}}" alt="" width="50">`
- Now another important things to do otherwise image won't show. which is adding `static media url` in `urls.py` file
    ```python
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        # ... the rest of URLconf goes here ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
- Now we can see the image in table

Now Let's add the image from frontend, modify the `addstudent.html` file as below:
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}


</style>
<body>

<h3>Using CSS to style an HTML Form</h3>

<div>
  <form action="{% url 'addstudent' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    <label for="fname">Name</label>
    <input type="text" id="fname" name="name" placeholder="Your name..">

    <label for="lname">Department</label>
    <input type="text" id="lname" name="department" placeholder="Your Department">
    <label for="lname">City</label>
    <input type="text" id="lname" name="city" placeholder="Your City">
    <label for="lname">Image</label>
    <input type="file" id="lname" name="studentImage" placeholder="Your City">
  
    <input type="submit" value="Submit">
  </form>
</div>

</body>
</html>

{% endblock content %}
    
```
- Here Image type is file which is written as `type="file"`
- `enctype="multipart/form-data"` is important otherwise image won't be added

Now we have to edit our `addstudent` function in `views.py`
```python
def addstudent(request):
    if request.method=='POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        studentImage=request.FILES.get('studentImage')
        
        student=studentModel(
            Name=name,
            Department=department,
            City=city,
            StudentImage=studentImage,
        )
        
        student.save()
        return redirect('student')
    return render(request,'addstudent.html')
```
- Here `studentImage` is getting the image by `request.FILES.get('studentImage')`
- After that including it in model `StudentImage=studentImage,` then save and redirected to student table page

Now to make the image to view in `viewstudent.html` page
```html
{% extends 'base.html' %}


{% block content %}
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>
</head>
<body>

<h2 style="text-align:center">User Profile Card</h2>


{% for i in student %}
<div class="card">
    <img src="/{{i.StudentImage}}" alt="" style="width:100%">
    <h1>{{i.Name}}</h1>
    <p class="title">{{i.Department}}, {{i.City}}</p>
  </div>
{% endfor %}
    


</body>
</html>

{% endblock content %}
    
```
- Here same as the way we show the image source in table `<img src="/{{i.StudentImage}}" alt="" style="width:100%">`

Now let's do the edi part, we need the same form as `addstudent.html` page form in `editstudent.html`
```html
{% extends 'base.html' %}

{% block content %}
<!DOCTYPE html>
<html>
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

</style>
<body>

<h3>Using CSS to style an HTML Form</h3>

<div>
  <form action="{% url 'updatestudent' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}

    
    {% for i in student %}
               
    <label for="fname">ID</label>
    <input type="text" id="fname" value={{i.id}} name="myid" placeholder="Your id.." readonly>
    <label for="fname">Name</label>
    <input type="text" id="fname" value={{i.Name}} name="name" placeholder="Your name..">

    <label for="lname">Department</label>
    <input type="text" id="lname" value={{i.Department}} name="department" placeholder="Your Department">
    <label for="lname">City</label>
    <input type="text" id="lname" value={{i.City}} name="city" placeholder="Your City">
    <label for="lname">Current Image:</label><br>
    <img src="/{{i.StudentImage}}" alt="" width="50"> <br>
    
    <label for="lname">Image</label>
    <input type="file" id="lname" name="studentImage" placeholder="Your City"> 
    {% endfor %}

  
    <input type="submit" value="Update">
  </form>
</div>

</body>
</html>

{% endblock content %}
    
```
- Here for loop is added
- `value` attribute added
- To show the current image , image source is added
- To make the update work the function `updatestudent` is created in `views.py`
```python
def updatestudent(request):
    if request.method=='POST':
        myid=request.POST.get('myid')
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        studentImage=request.FILES.get('studentImage')
        
        student=studentModel(
            id=myid,
            Name=name,
            Department=department,
            City=city,
            StudentImage=studentImage,
        )
        student.save()
        return redirect('student')
```
- All are similar but image is getting by `FILES`

Finally add the url path in `urls.py`
```python
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from d14_project.views import student,addstudent,mark,addmark,teacher,addteacher,subject,addsubject,university,adduniversity,deleteMark,deleteStudent,deleteSubject,deleteTeacher,deleteUniversity,viewstudent,viewteacher,viewmark,viewsubject,viewuniversity,alltable,editstudent,updatestudent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('mark/',mark,name='mark'),
    path('addmark/',addmark,name='addmark'),
    path('teacher/',teacher,name='teacher'),
    path('addteacher/',addteacher,name='addteacher'),
    path('subject/',subject,name='subject'),
    path('addsubject/',addsubject,name='addsubject'),
    path('university/',university,name='university'),
    path('adduniversity/',adduniversity,name='adduniversity'),
    path('deleteMark/<str:myid>',deleteMark,name='deleteMark'),
    path('deleteStudent/<str:myid>',deleteStudent,name='deleteStudent'),
    path('deleteSubject/<str:myid>',deleteSubject,name='deleteSubject'),
    path('deleteTeacher/<str:myid>',deleteTeacher,name='deleteTeacher'),
    path('deleteUniversity/<str:myid>',deleteUniversity,name='deleteUniversity'),
    path('viewstudent/<int:myid>',viewstudent,name='viewstudent'),
    path('viewteacher/<int:myid>',viewteacher,name='viewteacher'),
    path('viewmark/<int:myid>',viewmark,name='viewmark'),
    path('viewsubject/<int:myid>',viewsubject,name='viewsubject'),
    path('viewuniversity/<int:myid>',viewuniversity,name='viewuniversity'),
    path('alltable/',alltable,name='alltable'),
    path('editstudent/<int:myid>',editstudent,name='editstudent'),
    path('updatestudent',updatestudent,name='updatestudent'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
Now add this `name` in table edit action
```html
<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Image</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
        <td>{{i.Name}}</td>
        <td>{{i.Department}}</td>
        <td>{{i.City}}</td>
        <td>
          <img src="/{{i.StudentImage}}" alt="" width="50">
        </td>
        <td>
          <a href="{% url 'deleteStudent' i.id %}">Delete</a>
          <a href="{% url 'viewstudent' i.id %}">View</a>
          <a href="{% url 'editstudent' i.id %}">Edit</a>
        </td>
    </tr>

  {% endfor %}
    
</table>
```
- Here `<a href="{% url 'editstudent' i.id %}">Edit</a>` is added with specific id to view in editpage for editing.

Now the update will work.

### Disscussion on previous batch final assessment
- Portfolio Project

### Task:
- Add image in form
- Delete, Edit, View action with image 

</details>

<details>
<summary>Day-15-Image update (02-04-2024)</summary>

## Day 15 Topics
- Recap old days work
- Image add problem
- Two ways to write object class
- Edit Image
- Task

### Image add problem
When User don't update image while editing there will be no image to get and error will occur.To handle this we need to implement condition in update function
```python
def updatestudent(request):
    if request.method=='POST':
        myid=request.POST.get('myid')
        name=request.POST.get('name')
        department=request.POST.get('department')
        city=request.POST.get('city')
        studentImage=request.FILES.get('studentImage')
        print(f"This is image: {studentImage}")
        if studentImage:
            student=studentModel(
                id=myid,
                Name=name,
                Department=department,
                City=city,
                StudentImage=studentImage,
            )
        else:
            studentbyid=studentModel.objects.get(id=myid)
            student=studentModel(
                id=myid,
                Name=name,
                Department=department,
                City=city,
                StudentImage=studentbyid.StudentImage
            )
        student.save()
        return redirect('student')
```
- Here If-Else condition is applied to check if we are getting the image from frontend or not
- When we don't get the image we will give the model the old image by id `studentbyid=studentModel.objects.get(id=myid)`
- To handle this properly , after learning user authentication this will be implement in good way.

### Two ways to write object class
- We can use `.` with model to inherit the class like this: `student.id`, `student.Name`...

### Edit image
Similar task is repeated for student who failed to complete it. In Day 14 full details is already covered.

### Task
- No task assigned 
- Tomorrow (03-04-2024) exam on Django CRUD

</details>

<details>
<summary>Day-16-Python Basics Day 02 & PDF Download Test (03-04-2024)</summary>

## Day 16 Topics
- Previous days recap
- Python basics day 2
- PDF Download

### Python basics day 2
- Variable recap 
- Code editor
- first code run
- sum operation
- Symbol - Character - Sign - Letters
    - A - Z
    - 0 - 9
    - Special Character

### PDF Download
- Tested few packages for pdf output of a profile page.
- [pyhtml2pdf](https://pypi.org/project/pyhtml2pdf/) give good output
- Need to implement it in future

</details>

<details>
<summary>Day-17-Python Day 03 & Custom Template Setup (04-04-2024)</summary>

## Day 17 Topics
- Django Framework Disscussion
- Custom template setup / Customize UI
- Python Day 03
- Task

### Custom template setup / Customize UI
- Download site: [Bootstrapmade](https://bootstrapmade.com/iportfolio-bootstrap-portfolio-websites-template/)

- Custom Template setup guide : [Youtube](https://www.youtube.com/watch?v=bFsIXYygsg4)

To setup custom template we have to add the js,images,css files in static folder and in `settings.py` include the static path & template folder path also in template DIR:
```python
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]
```
Now add all the html files in our template folder and set the `index.html` as base html and do the template mastering.
```html
  <main id="main">

{% include 'about.html' %}

{% include 'facts.html' %}

{% include 'skills.html' %}

{% include 'resume.html' %}

{% include 'portfolio.html' %}

{% include 'services.html' %}

{% include 'testomonial.html' %}

{% include 'contact.html' %}

  </main><!-- End #main -->

{% include 'footer.html' %}
```
To make the static files work, we have to load the static and add the static in each files url with static:
```html
<!-- load static at the top line of the base html -->
{% load static %}
  <!-- Vendor JS Files -->
  <script src="{% static 'assets/vendor/purecounter/purecounter_vanilla.js' %}"></script>
  <script src="{% static 'assets/vendor/aos/aos.js' %}"></script>
  <script src="{% static 'assets/vendor/bootstrap/js/bootstrap.bundle.min.js' %}"></script>
  <script src="{% static 'assets/vendor/glightbox/js/glightbox.min.js' %}"></script>
  <script src="{% static 'assets/vendor/isotope-layout/isotope.pkgd.min.js' %}"></script>
  <script src="{% static 'assets/vendor/swiper/swiper-bundle.min.js' %}"></script>
  <script src="{% static 'assets/vendor/typed.js/typed.umd.js' %}"></script>
  <script src="{% static 'assets/vendor/waypoints/noframework.waypoints.js' %}"></script>
  <script src="{% static 'assets/vendor/php-email-form/validate.js' %}"></script>
```
Now create a function in `views.py`
```python
def portfolio(request):
    return render(request,'index.html')
```
Add the path route in `urls.py`
```python
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from d17_project.views import student,addstudent,viewstudent,portfolio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',student,name='student'),
    path('addstudent/',addstudent,name='addstudent'),
    path('viewstudent/<int:myid>',viewstudent,name='viewstudent'),
    path('portfolio/',portfolio,name='portfolio')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
Now we will be able to see our custom website is working.

To include a model table in this custom template we will create our model as usual and add it in here using block content
```html
      <nav id="navbar" class="nav-menu navbar">
        <ul>
          <li><a href="#hero" class="nav-link scrollto active"><i class="bx bx-home"></i> <span>Home</span></a></li>
          <li><a href="#about" class="nav-link scrollto"><i class="bx bx-user"></i> <span>About</span></a></li>
          <li><a href="{% url 'student' %}" class="nav-link scrollto"><i class="bx bx-envelope"></i> <span>Student Table</span></a></li>
          <li><a href="#resume" class="nav-link scrollto"><i class="bx bx-file-blank"></i> <span>Resume</span></a></li>
          <li><a href="#portfolio" class="nav-link scrollto"><i class="bx bx-book-content"></i> <span>Portfolio</span></a></li>
          <li><a href="#services" class="nav-link scrollto"><i class="bx bx-server"></i> <span>Services</span></a></li>
          <li><a href="#contact" class="nav-link scrollto"><i class="bx bx-envelope"></i> <span>Contact</span></a></li>
        </ul>
      </nav><!-- .nav-menu -->
```
- Here we added the `{% url 'student' %}` student table. to show it in page:
```html
{% extends 'index.html' %}

{% block content %}

<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>Student Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Department</th>
    <th>City</th>
    <th>Image</th>
    <th>Action</th>
  </tr>
  
  {% for i in student %}
    <tr>
      <td>{{i.Name}}</td>
      <td>{{i.Department}}</td>
      <td>{{i.City}}</td>
      <td>
        <img src="/{{i.Image}}" alt="" width="50">
      </td>
      <td>
        <a href="{% url 'viewstudent' i.id %}">View</a>
      </td>
    </tr>
  {% endfor %}
</table>

</body>
</html>

{% endblock content %}
```
- We have extends the base html which is `index.html` then our content is in block
- Now let's add this after about section just like we did in navbar
```html
{% include 'about.html' %}

{% block content %}
  
{% endblock content %}

{% include 'facts.html' %}

{% include 'skills.html' %}

{% include 'resume.html' %}

{% include 'portfolio.html' %}

{% include 'services.html' %}

{% include 'testomonial.html' %}

{% include 'contact.html' %}

  </main><!-- End #main -->

{% include 'footer.html' %}
```
- Here after about section we added the block content.
- Now we will be able to see our student table.

### Python Day 03
- Discussion on `Operator` & `Operand`

### Contingency management
- Doing same task in variety of way
- Environment management

### Expression evaluation
- [Operator Precedence](https://www.google.com/search?q=operator+precedence)

### Task
- Setup full portfolio custom template in django

</details>

<details>
<summary>Day-17-Portfolio Project</summary>

## Day-17-Portfolio Project
- Created a portfolio project based on this [template](https://bootstrapmade.com/iportfolio-bootstrap-portfolio-websites-template/)
- Most of the task followed by creating models and showing the data in frontend
    - First create a project: `django-admin startproject portfolio`
    - Now create app:
        - `cd portfolio`
        - `py manage.py startapp portfolioapp`
    - Add the app in `INSTALLED_APPS` list
        ```python
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'portfolioapp',
        ]
        ```
    - Add static directory `STATICFILES_DIRS` at the end of `settings.py` file
        ```python
        STATICFILES_DIRS = [
            BASE_DIR / "static",
        ]
        ```
    - Add `DIRS` of tamplates folder directory in `TEMPLATES`
        > 'DIRS': [BASE_DIR, 'templates']
    - Add downloaded `.html` content file in `templates` folder which will be created in `manage.py` directory
        ```python 
        project_name/ # Which is portfolio
        │
        ├── manage.py
        ├── project_name/ # portfolio
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── asgi.py
        │   ├── urls.py
        │   └── wsgi.py
        │   └── views.py # This is created manually
        │
        └── templates # This folder is created manually
        │
        └── static # This folder is created manually
        │
        └── app_name/ # Which is portfolioapp
            ├── migrations/
            │   └── __init__.py
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── models.py
            ├── tests.py
            └── views.py
        ```
    - Now Create static folder and paste all the static files here from the downloaded template
    - Now create `views.py` in project directory and create a function to render it:
        ```python
        from django.shortcuts import redirect,render

        def portfolio(request):

            return render(request,'index.html',myDict)
        ```
    - Now add url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from portfolio.views import portfolio

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',portfolio,name='portfolio'),
        ]
        ```
    - Now if we visit `http://127.0.0.1:8000/admin/` we won't see any static file effect on our html page.
    - We have to load the static file in html to see the effect.
    - Add `{% load static %}` at the top in `index.html` file
    - And change each `src` & `href` that include files from `assets/static` like this: `  <link href="{% static 'assets/img/favicon.png' %}" rel="icon">`
    - If everything done correctly we will be able to see the html page with all the static files loaded perfectly.
    - Now let's make the `index.html` base html and separate other section.
    - Now include those separated section:
        ```html
        <main id="main">

        {% include 'about.html' %}

        {% include 'facts.html' %}

        {% include 'skills.html' %}

        {% include 'resume.html' %}

        {% include 'portfolio.html' %}

        {% include 'services.html' %}

        {% include 'testimonials.html' %}

        {% include 'contact.html' %}

        </main><!-- End #main -->
        ```
    - Now let's create necessary models 
        ```python
        from django.db import models

        # Create your models here.
        class SocialMediaModel(models.Model):
            twitter=models.CharField(max_length=100)
            facebook=models.CharField(max_length=100)
            Instagram=models.CharField(max_length=100)
            skype=models.CharField(max_length=100)
            linkedin=models.CharField(max_length=100)

            def __str__(self):
                return self.twitter

        class AboutModel(models.Model):
            Profile_img = models.ImageField(upload_to='media/ProfileImg')
            Name=models.CharField(max_length=100)
            Profession1=models.CharField(max_length=100)
            Profession2=models.CharField(max_length=100)
            Profession3=models.CharField(max_length=100)
            About_details=models.CharField(max_length=500)
            Profession_title1=models.CharField(max_length=100)
            Profession_title2=models.CharField(max_length=100)
            Profession_details=models.CharField(max_length=500)
            Profession_para=models.CharField(max_length=500)
            Birthday=models.CharField(max_length=100)
            Website=models.CharField(max_length=100)
            Phone=models.CharField(max_length=100)
            City=models.CharField(max_length=100)
            Age=models.CharField(max_length=100)
            Email=models.CharField(max_length=100)
            Freelance_status=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Name
            
        class factModel(models.Model):
            Fact_para=models.CharField(max_length=500)
            Happy_clients=models.CharField(max_length=100)
            Projects=models.CharField(max_length=100)
            Hours_of_support=models.CharField(max_length=100)
            Hard_workers=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Happy_clients
            
        class SkillsModel(models.Model):
            Skill_para=models.CharField(max_length=500)
            
            def __str__(self):
                return self.Skill_para
            
        class SkillMatricesModel(models.Model):
            Skill_name=models.CharField(max_length=100)
            Skill_progressbar=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Skill_name
            
        class ResumeModel(models.Model):
            Resume_para=models.CharField(max_length=500)
            Name=models.CharField(max_length=100)
            About=models.CharField(max_length=100)
            Address=models.CharField(max_length=100)
            Mobile=models.CharField(max_length=100)
            Email=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Name  

        class ResumeEducationModel(models.Model):
            Education_name=models.CharField(max_length=100)
            Education_year=models.CharField(max_length=100)
            Education_institute=models.CharField(max_length=100)
            Education_details=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Education_name
            
        class ResumeProfessionalModel(models.Model):
            Professional_experience=models.CharField(max_length=100)
            Professional_experience_year=models.CharField(max_length=100)
            Professional_experience_location=models.CharField(max_length=100)
            Professional_responsibilities=models.CharField(max_length=100)

            def __str__(self):
                return self.Professional_experience

        class PortfolioModel(models.Model):
            Portfolio_para=models.CharField(max_length=500)
            
            def __str__(self):
                return self.Portfolio_para
            
        class ServicesModel(models.Model):
            Services_para=models.CharField(max_length=500)

            def __str__(self):
                return self.Services_para

        class ServicesSectionModel(models.Model):
            Service_icon=models.CharField(max_length=100)
            Service_name=models.CharField(max_length=100)
            Service_details=models.CharField(max_length=500)
            
            def __str__(self):
                return self.Service_name
            
        class TestimonialModel(models.Model):
            Testimonial_para=models.CharField(max_length=500)
            
            def __str__(self):
                return self.Testimonial_para

        class ClientTestimonialModel(models.Model):
            Client_name=models.CharField(max_length=100)
            Client_img=models.ImageField(upload_to='media/ClientImg')
            Client_profession=models.CharField(max_length=100)
            Client_quote=models.CharField(max_length=500)

            def __str__(self):
                return self.Client_name

        class ContactModel(models.Model):
            Contact_para=models.CharField(max_length=500)
            Contact_location=models.CharField(max_length=100)
            Contact_Email=models.CharField(max_length=100)
            Contact_Call=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Contact_para
        ```
    - Register it in `admin.py`
        ```python
        from django.contrib import admin
        from portfolioapp.models import SocialMediaModel,AboutModel,factModel,SkillsModel,SkillMatricesModel,ResumeModel,ResumeEducationModel,ResumeProfessionalModel,PortfolioModel,ServicesModel,ServicesSectionModel,TestimonialModel,ContactModel,ClientTestimonialModel
        # Register your models here.
        admin.site.register(SocialMediaModel)
        admin.site.register(AboutModel)
        admin.site.register(factModel)
        admin.site.register(SkillsModel)
        admin.site.register(SkillMatricesModel)
        admin.site.register(ResumeModel)
        admin.site.register(ResumeEducationModel)
        admin.site.register(ResumeProfessionalModel)
        admin.site.register(PortfolioModel)
        admin.site.register(ServicesModel)
        admin.site.register(ServicesSectionModel)
        admin.site.register(TestimonialModel)
        admin.site.register(ClientTestimonialModel)
        admin.site.register(ContactModel)
        ```
    - As we can see there will be image too. In order to show the image we have to set the media static:
        ```python 
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from portfolio.views import portfolio

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',portfolio,name='portfolio'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Now let's migrate and create our superuser to input data in our model:
        - `py manage.py makemigrations`
        - `py manage.py migrate`
        - `py manage.py createsuperuser`
    - Now to show those data , we have to import it in our `views.py` and return it in `dictionary`
        ```python
        from django.shortcuts import redirect,render
        from portfolioapp.models import SocialMediaModel,AboutModel,factModel,SkillsModel,SkillMatricesModel,ResumeModel,ResumeEducationModel,ResumeProfessionalModel,PortfolioModel,ServicesModel,ServicesSectionModel,TestimonialModel,ClientTestimonialModel,ContactModel

        def portfolio(request):
            socialmedia = SocialMediaModel.objects.get()
            about = AboutModel.objects.get()
            fact = factModel.objects.get()
            skills = SkillsModel.objects.get()
            skills_matrices = SkillMatricesModel.objects.all()
            resume = ResumeModel.objects.get()
            resume_edu = ResumeEducationModel.objects.all()
            resume_pro = ResumeProfessionalModel.objects.all()
            portfolio_des = PortfolioModel.objects.get()
            services_des = ServicesModel.objects.get()
            services_section = ServicesSectionModel.objects.all()
            testimonial_des = TestimonialModel.objects.get()
            client_testimonial = ClientTestimonialModel.objects.all()
            contact = ContactModel.objects.get()
            myDict={
                'socialmedia':socialmedia,
                'about':about,
                'fact':fact,
                'skills':skills,
                'skills_matrices':skills_matrices,
                'resume':resume,
                'resume_edu':resume_edu,
                'resume_pro':resume_pro,
                'portfolio_des':portfolio_des,
                'services_des':services_des,
                'services_section':services_section,
                'testimonial_des':testimonial_des,
                'client_testimonial':client_testimonial,
                'contact':contact,
                
            }
            return render(request,'index.html',myDict)
        ```
    - Everything is set , now all we have to do is to view the models in html file iterate in for loop for those model which are `.objects.all()` and for others which are `.objects.get()` can be directly accessible.

</details>

<details>
<summary>Day-18-Custom Template CRUD Update Operation (16-04-2024)</summary>

## Day 18 Topic
- Custom template setup recap
- CRUD Operation on Custom Template
- Task

  > Note:- The update option should be on separated admin page but as a practise I did it on the same page. Which will be changed in future.

### CRUD Operation on Custom Template
- It follow up the Day-17 portfolio project
- Today added the `edit option` in about section
    - Get a bootstrap form from [bootstrap site](https://getbootstrap.com/docs/4.0/components/forms/#:~:text=%3Cform%3E%0A%20%20%3Cdiv%20class%3D%22form%2Dgroup,primary%22%3ESubmit%3C/button%3E%0A%3C/form%3E)
    - Create `editabout.html`
        ```html
        {% extends 'index.html' %}

        {% block content %}
        <div class="container mt-5">
            <form action="{% url 'updateabout' %}" method="POST" enctype="multipart/form-data">
                {% csrf_token %}
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">ID</label>
                    <input type="text" class="form-control" name= "myid" value="{{about.id}}" id="exampleInput" aria-describedby="emailHelp" readonly>
                </div>
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Current Image</label><br>
                    <img src="/{{about.Profile_img}}" alt="" width="50"><br>
                </div>
                <div class="form-group">
                    <label for="exampleFormControlFile1">Update Image</label>
                    <input type="file" name="profile_img" class="form-control-file" id="exampleFormControlFile1">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Name</label>
                <input type="text" class="form-control" name= "name" value="{{about.Name}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession 1</label>
                <input type="text" class="form-control" name="profession1" value="{{about.Profession1}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession 2</label>
                <input type="text" class="form-control" name="profession2" value="{{about.Profession2}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession 3</label>
                <input type="text" class="form-control" name="profession3" value="{{about.Profession3}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">About details</label>
                <textarea class="form-control" name="about_details" name="about_details" id="exampleFormControlTextarea1" rows="3">{{about.About_details}}</textarea>
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession title 1</label>
                <input type="text" class="form-control" name="profession_title1" value="{{about.Profession_title1}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession title 2</label>
                <input type="text" class="form-control" name="profession_title2" value="{{about.Profession_title2}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession details</label>
                <textarea class="form-control" name="profession_details" name="profession_details" id="exampleFormControlTextarea1" rows="3">{{about.Profession_details}}</textarea>
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profession Paragraph</label>
                <textarea class="form-control" name="profession_para"  id="exampleFormControlTextarea1" rows="3">{{about.Profession_para}}</textarea>
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Birthday</label>
                <input type="text" class="form-control" name="birthday" value="{{about.Birthday}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Website</label>
                <input type="text" class="form-control" name="website" value="{{about.Website}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Phone</label>
                <input type="text" class="form-control" name="phone" value="{{about.Phone}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">City</label>
                <input type="text" class="form-control" name="city" value="{{about.City}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Age</label>
                <input type="text" class="form-control" name="age" value="{{about.Age}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email</label>
                <input type="email" class="form-control" name="email" value="{{about.Email}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Freelance status</label>
                <input type="text" class="form-control" name="freelance_status" value="{{about.Freelance_status}}" id="exampleInput" aria-describedby="emailHelp">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
        {% endblock content %}
        ```
        - Here `action`, `method`, `enctype`, `name` & `value` must be included
    - Now render this html page in `views.py`
        ```python
        def editabout(request, myid):
            about = AboutModel.objects.get(id=myid)
            myDict={
                'about':about
            }
            return render(request,'editabout.html',myDict)
        ```
    - Set the path url in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from portfolio.views import portfolio,editabout,updateabout

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',portfolio,name='portfolio'),
            path('editabout/<str:myid>',editabout,name='editabout'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Now to make it work create a button under edit section of html page so after clicking it the form will be open
        ```html
        <a href="{% url 'editabout' about.id %}" type="button" class="btn mt-2" style="background-color: #173b6c; color: #fff;">Edit About</a>
        ```
    - Create a `updateabout` function in `views.py`
        ```python
        def updateabout(request):
            if request.method=="POST":
                myid = request.POST.get('myid')
                profile_img = request.FILES.get('profile_img')
                name=request.POST.get('name')
                profession1=request.POST.get('profession1')
                profession2=request.POST.get('profession2')
                profession3=request.POST.get('profession3')
                about_details=request.POST.get('about_details')
                profession_title1=request.POST.get('profession_title1')
                profession_title2=request.POST.get('profession_title2')
                profession_details=request.POST.get('profession_details')
                profession_para=request.POST.get('profession_para')
                birthday=request.POST.get('birthday')
                website=request.POST.get('website')
                phone=request.POST.get('phone')
                city=request.POST.get('city')
                age=request.POST.get('age')
                email=request.POST.get('email')
                freelance_status=request.POST.get('freelance_status')
                if profile_img:  
                    about = AboutModel(
                        id = myid,
                        Profile_img = profile_img,
                        Name=name,
                        Profession1=profession1,
                        Profession2=profession2,
                        Profession3=profession3,
                        About_details=about_details,
                        Profession_title1=profession_title1,
                        Profession_title2=profession_title2,
                        Profession_details=profession_details,
                        Profession_para=profession_para,
                        Birthday=birthday,
                        Website=website,
                        Phone=phone,
                        City=city,
                        Age=age,
                        Email=email,
                        Freelance_status=freelance_status,
                    )
                else:
                    aboutbyid=AboutModel.objects.get(id=myid)
                    about = AboutModel(
                        id = myid,
                        Profile_img = aboutbyid.Profile_img,
                        Name=name,
                        Profession1=profession1,
                        Profession2=profession2,
                        Profession3=profession3,
                        About_details=about_details,
                        Profession_title1=profession_title1,
                        Profession_title2=profession_title2,
                        Profession_details=profession_details,
                        Profession_para=profession_para,
                        Birthday=birthday,
                        Website=website,
                        Phone=phone,
                        City=city,
                        Age=age,
                        Email=email,
                        Freelance_status=freelance_status,
                    )
                about.save()
                return redirect('/')
        ```
        - Here image also handle when user don't update image
        - after updating it will redirect to homepage
        - This function will be trigger after clicking on submit button which is in form page action
### Task
- Complete remaining CRUD operation in Custom Template

</details>

<details>
<summary>Day-19-Lab Exam 03 (18-04-2024)</summary>

## Day 19 Topics
- Lab Exam 03
- PDF download using js (Test code)
- Bonus task: PDF download implementation

### Lab Exam 03
> Question: Building a Resume Builder Web Application with Django You are tasked with creating a simple Resume Builder web application using Django.The application should allow users to cease, view, update, and delete their resumes, Including various fields such as profile picture, address, phone number, career objective, and others. Your task is to Implement the CRUD (Create, Read, Update, Delete) operations for managing resumes.

Resume Creation:
- Profile picture
- Full name
- Address
- Phone number
- Email address
- Career objective
- Education history (e.g., degree, Institution, graduation year)
- Work experience (e.g., company, position, start and end dates)
- Skills (Hard Skills, Soft Skills)
- Certifications
- Projects
- References, etc.

Listing Resumes:
- Display a list of all resumes

Viewing and Editing Resumes:
- View the details of a specific resume.
Provide options to edit and update the information within the resume.

Deleting Resumes:
- Implement functionality to delete resumes when required.

Bonus (optional):
- Add the ability for users to upload and manage multiple profile pictures.
- Implement search and filtering functionality for resumes.
- Allow users to download their resumes in PDF format.
- Implement rich text editors for fields like career objective and project descriptions. 

Requirements: 
- Use Django models to define the resume structure.
- Create clean and responsive templates for the user Interface.

Submission: 
- Submit the project as a zip file or provide a link to a version control repository GitHub. Include a README file with instructions and any necessary dependencies. 

> Total time took by me 1 Hour 40 Minutes.

### PDF download using js (Test code)
- Below code was done to test how to generate pdf with js
    ```html
    <!--CDN:--> 
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.3.2/jspdf.debug.js"></script>

    <script>
        document.getElementById("downloadPDF").addEventListener("click", function() {
            // Create a new instance of jsPDF
            const doc = new jsPDF();
        
            // Add profile section
            doc.text("Profile", 10, 10);
            doc.text("Name: " + "{{ resume.Full_name }}", 10, 20);
            doc.text("Address: " + "{{ resume.Address }}", 10, 30);
            doc.text("Phone: " + "{{ resume.Phone_number }}", 10, 40);
            doc.text("Email: " + "{{ resume.Email_address }}", 10, 50);
        
            // Add career objective section
            doc.text("Career Objective", 10, 70);
            doc.text("{{ resume.Career_objective }}", 10, 80);
            
            // Add education section
            doc.text("Education", 10, 100);
            doc.text("{{ education.Degree }} - {{ education.Institution }}, {{ education.Graduation_year }}", 10, 110);
            
            // Add work experience section
            doc.text("Work Experience", 10, 130);
            doc.text("{{ work.Position }} at {{ work.Company }}, {{ work.Start_date }} - {{ work.End_date }}", 10, 140);
            
            // Add skills section
            doc.text("Skills", 10, 160);
            doc.text("Hard Skills: {{ resume.Hard_skills }}", 10, 170);
            doc.text("Soft Skills: {{ resume.Soft_skills }}", 10, 180);
            
            // Add certifications section
            doc.text("Certifications", 10, 200);
            doc.text("{{ resume.Certifications }}", 10, 210);
            
            // Add projects section
            doc.text("Projects", 10, 230);
            doc.text("{{ resume.Projects }}", 10, 240);
            
            // Add references section
            doc.text("References", 10, 260);
            doc.text("{{ resume.References }}", 10, 270);
        
            // Save the PDF
            doc.save("resume.pdf");
        });
    </script>
    ```

### Bonus task: PDF download implementation
- I found a package in python which is `pyhtml2pdf` which i used to convert the created resume in pdf. Below function was implemented to download the generated pdf file:
    ```python
    def downloadresume(request, myid):
        # Run the converter function to generate/update the PDF file
        username=ResumeModel.objects.get(id=myid)
        print(username.Full_name)
        pdf_file = converter.convert(f'http://127.0.0.1:8000/viewresume/{myid}', 'resume.pdf')
        print(f"PDF file path from converter: {pdf_file}")

        # Get the root path of the project
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        print(f"Project root path: {project_root}")

        # If the converter returns a valid file path, use it
        if pdf_file:
            pdf_file_path = pdf_file
        else:
            # Otherwise, construct the file path relative to the project root
            pdf_file_path = os.path.join(project_root, 'resume.pdf')
            print(f"PDF file path: {pdf_file_path}")

        if not os.path.exists(pdf_file_path):
            # Handle the case where the file doesn't exist
            print("Error: PDF file not found.")
            return HttpResponse("Error: Unable to find PDF file.")

        try:
            with open(pdf_file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type='application/pdf')
                # response['Content-Disposition'] = 'attachment; filename=resume.pdf'
                response['Content-Disposition'] = f'attachment; filename={username}-Resume.pdf'
        except Exception as e:
            print(f"Error opening PDF file: {e}")
            return HttpResponse("Error: Unable to open PDF file.")

        return response
    ```

</details>

<details>
<summary>Day-20-Python Basic Day 04 & Lab Exam 03 Portfolio Project Recap (20-04-2024)</summary>

## Day 20 Topics

- Arithmetic operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Conditions and If statements
- Lab exam 03 portfolio project recap
- Task

### Arithmetic operators

|Operator|	Name|	Example|
|-       | -    |      -   |
|+	|Addition	| $x + y$ |	
|-	|Subtraction|	$x - y$ |	
|*	|Multiplication	| $x * y$ |	
|/	|Division|	$x / y$ |	
|%	|Modulus	| $x % y$	|
|**	|Exponentiation|	$x ** y$ |	
|//	|Floor division|	$x // y$ |


### Assignment Operators
- Task
    - $a/=10$
        > $a=a/10$
    - $a+=b+10$
        > $a=a/10$
    - $a**=3+c$
        > $a=a**(3+c)$
    - $a//=x+y**4$
        > $a=a//(x+(y**4))$
    - $b-=x**y$
        > $b=b-(x**y)$

### Comparison Operators

|Operator	|Name|	Example|
|    -      |  - |     -    |        
|==	|Equal|	 $x == y$ |	
|!=	|Not equal	| $x != y$	|
|>	|Greater than|	$x > y$ |	
|<	|Less than	| $x < y$ |	
|>=	|Greater than or equal to|	$x >= y$ |	
|<=	|Less than or equal to	| $x <= y$ |

- Task
    - x= 5
    - y = 3
    - print(x==y)
        > z =(x==y)
        
        > print(z)

### Logical Operators

|Operator	|Description	|Example|
|-|-|-|
|and 	|Returns True if both statements are true	|x < 5 and  x < 10	|
|or	|Returns True if one of the statements is true|	x < 5 or x < 4	|
|not	|Reverse the result, returns False if the result is true	|not(x < 5 and x < 10)|

### Conditions and If statements

- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

### Lab exam 03 portfolio project recap
> Question: Building a Resume Builder Web Application with Django You are tasked with creating a simple Resume Builder web application using Django.The application should allow users to cease, view, update, and delete their resumes, Including various fields such as profile picture, address, phone number, career objective, and others. Your task is to Implement the CRUD (Create, Read, Update, Delete) operations for managing resumes.

Resume Creation:
- Profile picture
- Full name
- Address
- Phone number
- Email address
- Career objective
- Education history (e.g., degree, Institution, graduation year)
- Work experience (e.g., company, position, start and end dates)
- Skills (Hard Skills, Soft Skills)
- Certifications
- Projects
- References, etc.

Listing Resumes:
- Display a list of all resumes

Viewing and Editing Resumes:
- View the details of a specific resume.
Provide options to edit and update the information within the resume.

Deleting Resumes:
- Implement functionality to delete resumes when required.

Bonus (optional):
- Add the ability for users to upload and manage multiple profile pictures.
- Implement search and filtering functionality for resumes.
- Allow users to download their resumes in PDF format.
- Implement rich text editors for fields like career objective and project descriptions. 

Requirements: 
- Use Django models to define the resume structure.
- Create clean and responsive templates for the user Interface.

Submission: 
- Submit the project as a zip file or provide a link to a version control repository GitHub. Include a README file with instructions and any necessary dependencies.

### Solution
- Initial setup:
    - Create Project : `django-admin startproject resumeProject`
    - Create App: `py manage.py startapp resumeApp`
    - Migrate Database: `py manage.py migrate`
    - Modification in `settings.py`:
        - Add app name `resumeApp` in `settings.py`'s `INSTALLED_APPS`:
            ```python
            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'resumeApp',
            ]
            ```
        - Add static file path at the end of the `settings.py` file:
            ```python
            STATICFILES_DIRS = [
                BASE_DIR / "static",
            ]
            ```
        - Add template path in `TEMPLATES`
            ```python
            'DIRS': [BASE_DIR,'templates'],
            ```
    - Now create a folder and name it exactly as added in `TEMPLATES`'s `DIRS` which is `templates` In project directory:
        ```text
        project_name/ # Which is resumeProject
        │
        ├── manage.py
        ├── project_name/ # resumeProject
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── asgi.py
        │   ├── urls.py
        │   └── wsgi.py
        │   └── views.py # This is created manually
        │
        ├── templates # This folder is created manually
        │
        ├── static # This folder is created manually
        │
        └── app_name/ # Which is resumeApp
            ├── migrations/
            │   └── __init__.py
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── models.py
            ├── tests.py
            └── views.py
        ```
- Now let's begin with first task which is **Listing Resumes**
    - To do this let's create our `base.html`, `navbar.html`, `home.html`,  files. 
    - Here: 
        - `base.html` :- For our base structure of the template 
        - `navbar.html` :- This will be included in `base.html`
        - `home.html` :-  Now this will extends `base.html` and show it's own content in block; As per requirement we will list all the resume in table data list in the block content of `home.html`
    - Let's create the required models in our app directory `models.py`
        ```python
        from django.db import models

        # Create your models here.
        class ResumeModel(models.Model):
            Profile_picture=models.ImageField(upload_to='media/ProfilePic')
            Full_name=models.CharField(max_length=100)
            Address=models.CharField(max_length=100)
            Phone_number=models.CharField(max_length=100)
            Email_address=models.CharField(max_length=100)
            Career_objective=models.TextField()
            Hard_Skills=models.CharField(max_length=100)
            Soft_Skills=models.CharField(max_length=100)
            Certifications=models.CharField(max_length=100)
            Projects=models.CharField(max_length=100)
            References=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Full_name
            
        class ResumeEducationModel(models.Model):
            Degree=models.CharField(max_length=100)
            Institution=models.CharField(max_length=100)
            Graduation_year=models.CharField(max_length=100)
            
            def __str__(self):
                return self.Institution
            
        class ResumeWorkModel(models.Model):
            Company=models.CharField(max_length=100)
            Position=models.CharField(max_length=100)
            Start_dates=models.CharField(max_length=100)
            End_dates =models.CharField(max_length=100)
            
            def __str__(self):
                return self.Company
        ```
    - In `admin.py` we have to register it
        ```python
        from django.contrib import admin
        from resumeApp.models import ResumeModel,ResumeEducationModel,ResumeWorkModel
        # Register your models here.

        admin.site.register(ResumeModel)
        admin.site.register(ResumeEducationModel)
        admin.site.register(ResumeWorkModel)
        ```
    - Now as we have done changes in model so we have to migrate it;
        - `py manage.py makemigrations`
        - `py manage.py migrate`
    - Run the server `py manage.py runserver`
    - Now add some data from admin page so that we can show it in frontend
    -  Let's setup our template pages
    - `base.html`:
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Resume Builder</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        <body>
            {% include 'navbar.html' %}
            
            {% block content %}
                
            {% endblock content %}
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </body>
        </html>
        ```
        - Here we can see we have also added bootstrap cdn as we are using bootstrap to build our project.
    - `navbar.html`:
        ```html
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
            <a class="navbar-brand" href="{% url 'home' %}">Resume Builder</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="{% url 'home' %}">All Resume</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="{% url 'addresume' %}">Add Resume</a>
                </li>
                </ul>
            </div>
            </div>
        </nav>
        ```
        - Here we have two navigation `All Resume`,  `Add Resume` & a default one which is navigating to home page `Resume Builder`.
    - Now the page we are going to show the list of all resumes which is `home.html`
        ```html
        {% extends 'base.html' %}

        {% block content %}
            <table class="table">
                <thead>
                <tr>
                    <th scope="col">Profile picture</th>
                    <th scope="col">Full name</th>
                    <th scope="col">Address</th>
                    <th scope="col">Phone number</th>
                    <th scope="col">Action</th>
                </tr>
                </thead>
                
                {% for i in resumedata %}
                <tbody>
                <tr>
                    <td>
                    <img src="/{{i.Profile_picture}}" width="50px" alt="">
                    </td>
                    <td>{{i.Full_name}}</td>
                    <td>{{i.Address}}</td>
                    <td>{{i.Phone_number}}</td>
                    <td>
                    <a href="{% url 'deleteresume' i.id %}">Delete</a>
                    <a href="{% url 'editresume' i.id %}">Edit</a>
                    <a href="{% url 'viewresume' i.id %}">View</a>
                    </td>
                </tr>
                </tbody>
                {% endfor %}
                
            </table>
        {% endblock content %}
        ```
        - We can see there is a for loop, which is working because we have done some work in `views.py` which we have to create in project directory manually:
            ```python
            from django.shortcuts import render,redirect
            from resumeApp.models import ResumeModel,ResumeEducationModel,ResumeWorkModel

            def home(request):
                resumedata=ResumeModel.objects.all()
                educationdata=ResumeEducationModel.objects.all()
                workdata=ResumeWorkModel.objects.all()
                
                resume={
                    'resumedata':resumedata,
                    'educationdata':educationdata,
                    'workdata':workdata,
                }
                return render(request,'home.html',resume)
            ```
        - In `urls.py` we have to add the path route
            ```python
            from django.contrib import admin
            from django.urls import path
            from resumeProject.views import home,addresume,deleteresume,editresume,updateresume,viewresume

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('',home,name='home'),
            ]
            ```
- We added the data from django admin page , So now let's add it from frontend
    - First create a html page `addresume.html` and add bootstrap form 
        ```html
        {% extends 'base.html' %}


        {% block content %}
        <div class="container">
            <form action="{% url 'addresume' %}" method="POST" enctype="multipart/form-data">
                {% csrf_token %}
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Profile Picture</label>
                <input type="file" class="form-control" id="exampleInputEmail1" name="profile_picture" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Full name</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="full_name" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Address</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="address" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Phone number</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="phone_number" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="email_address" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Career objective</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="career_objective" aria-describedby="emailHelp">
                </div>
                <h4>Education history:</h4>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Degree</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="degree" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Institution</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="institution" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Graduation_year</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="graduation_year" aria-describedby="emailHelp">
                </div>
                <h4>Work experience:</h4>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Company</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="company" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Position</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="position" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Start dates</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="start_dates" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">End dates</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="end_dates" aria-describedby="emailHelp">
                </div>
                <h4>Skills:</h4>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Hard Skills</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="hard_Skills" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Soft Skills</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="soft_Skills" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Certifications</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="certifications" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Projects</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="projects" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">References</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="references" aria-describedby="emailHelp">
                </div>

                <button type="submit" class="btn btn-primary">Submit</button>
            </form>

        </div>
        {% endblock content %}
        ```
        - Here `action`,`method`,`enctype` and the html `name` attribute is important
    - Now create a function which we included in action
        ```python
        def addresume(request):
            if request.method=="POST":
                profile_picture=request.FILES.get('profile_picture')
                full_name=request.POST.get('full_name')
                address=request.POST.get('address')
                phone_number=request.POST.get('phone_number')
                email_address=request.POST.get('email_address')
                career_objective=request.POST.get('career_objective')
                hard_Skills=request.POST.get('hard_Skills')
                soft_Skills=request.POST.get('soft_Skills')
                certifications=request.POST.get('certifications')
                projects=request.POST.get('projects')
                references=request.POST.get('references')
                degree=request.POST.get('degree')
                institution=request.POST.get('institution')
                graduation_year=request.POST.get('graduation_year')
                company=request.POST.get('company')
                position=request.POST.get('position')
                start_dates=request.POST.get('start_dates')
                end_dates=request.POST.get('end_dates')
                
                resume=ResumeModel(
                    Profile_picture=profile_picture,
                    Full_name=full_name,
                    Address=address,
                    Phone_number=phone_number,
                    Email_address=email_address,
                    Career_objective=career_objective,
                    Hard_Skills=hard_Skills,
                    Soft_Skills=soft_Skills,
                    Certifications=certifications,
                    Projects=projects,
                    References=references,
                )
                education=ResumeEducationModel(
                    Degree=degree,
                    Institution=institution,
                    Graduation_year=graduation_year,
                )
                work=ResumeWorkModel(
                    Company=company,
                    Position=position,
                    Start_dates=start_dates,
                    End_dates=end_dates,
                    
                )
                resume.save()
                education.save()
                work.save()
                
                return redirect('home')
                
            return render(request,'addresume.html')
        ```
    - Now add the url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from resumeProject.views import home,addresume,deleteresume,editresume,updateresume,viewresume

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',home,name='home'),
            path('addresume/',addresume,name='addresume'),
            
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
        - Here MEDIA static url added so that image related task work properly
    - Now in `navbar.html` url will be added in `href`
        ```html
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'addresume' %}">Add Resume</a>
          </li>
        ```
- Now let's do the delete action
    - First create a function with id in parameter as we need specific id to delete it
        ```python
        def deleteresume(request,myid):
            resumedata=ResumeModel.objects.get(id=myid)
            educationdata=ResumeEducationModel.objects.get(id=myid)
            workdata=ResumeWorkModel.objects.get(id=myid)
            
            resumedata.delete()
            educationdata.delete()
            workdata.delete()
            return redirect('home')
        ```
    - Create url route path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from resumeProject.views import home,addresume,deleteresume,editresume,updateresume,viewresume

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',home,name='home'),
            path('addresume/',addresume,name='addresume'),
            path('deleteresume/<str:myid>',deleteresume,name='deleteresume'),
            
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Now in table :
        ```html
            <td>
              <a href="{% url 'deleteresume' i.id %}">Delete</a>
            </td>
        ```
- Now let's edit and update the data
    - first create a form as same as `addresume.html` page which is `editresume.html`
        ```html
        {% extends 'base.html' %}


        {% block content %}
        <div class="container">
            <form action="{% url 'updateresume' %}" method="POST" enctype="multipart/form-data">
                {% csrf_token %}
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">ID</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.id}}" name="myid" aria-describedby="emailHelp" readonly>
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Current Profile Picture:</label> <br>
                <img src="/{{resumedata.Profile_picture}}" width="50px" alt=""><br>
                <input type="file" class="form-control" id="exampleInputEmail1" name="profile_picture" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Full name</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Full_name}}" name="full_name" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Address</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Address}}" name="address" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Phone number</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Phone_number}}" name="phone_number" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Email_address}}" name="email_address" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Career objective</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Career_objective}}" name="career_objective" aria-describedby="emailHelp">
                </div>
                <h4>Education history:</h4>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Degree</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{educationdata.Degree}}" name="degree" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Institution</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{educationdata.Institution}}" name="institution" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Graduation_year</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{educationdata.Graduation_year}}" name="graduation_year" aria-describedby="emailHelp">
                </div>
                <h4>Work experience:</h4>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Company</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{workdata.Company}}" name="company" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Position</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{workdata.Position}}" name="position" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Start dates</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{workdata.Start_dates}}" name="start_dates" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">End dates</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{workdata.End_dates}}" name="end_dates" aria-describedby="emailHelp">
                </div>
                <h4>Skills:</h4>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Hard Skills</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Hard_Skills}}" name="hard_Skills" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Soft Skills</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Soft_Skills}}" name="soft_Skills" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Certifications</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Certifications}}" name="certifications" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Projects</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.Projects}}" name="projects" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">References</label>
                <input type="text" class="form-control" id="exampleInputEmail1" value="{{resumedata.References}}" name="references" aria-describedby="emailHelp">
                </div>

                <button type="submit" class="btn btn-primary">Update</button>
            </form>

        </div>
        {% endblock content %}
        ```
        - Here difference between add page is the action which is for updating after clicking on update.
        - Value attribute for seeing the current data 
    - Now create a function for this page to show
        ```python
        def editresume(request,myid):
            resumedata=ResumeModel.objects.get(id=myid)
            educationdata=ResumeEducationModel.objects.get(id=myid)
            workdata=ResumeWorkModel.objects.get(id=myid)
            
            resume={
                'resumedata':resumedata,
                'educationdata':educationdata,
                'workdata':workdata,
            }
            return render(request,'editresume.html',resume)
        ```
        - Here we first the created `editresume.html` page 
        - As we need id so that we can show the current data of that specific person
        - and finally we return the model data as dictionary
    - Now in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from resumeProject.views import home,addresume,deleteresume,editresume,updateresume,viewresume

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',home,name='home'),
            path('addresume/',addresume,name='addresume'),
            path('deleteresume/<str:myid>',deleteresume,name='deleteresume'),
            path('editresume/<str:myid>',editresume,name='editresume'),
            
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
        - As we can see there is the id 
    - Now in action 
        ```html
            <td>
              <a href="{% url 'editresume' i.id %}">Edit</a>
            </td>
        ```
        - So after clicking on it it will open that specific id's data for editing
    - Now to make the update button work we have to create a update function as below:
        ```python
        def updateresume(request):
            if request.method=="POST":
                myid=request.POST.get('myid')
                profile_picture=request.FILES.get('profile_picture')
                full_name=request.POST.get('full_name')
                address=request.POST.get('address')
                phone_number=request.POST.get('phone_number')
                email_address=request.POST.get('email_address')
                career_objective=request.POST.get('career_objective')
                hard_Skills=request.POST.get('hard_Skills')
                soft_Skills=request.POST.get('soft_Skills')
                certifications=request.POST.get('certifications')
                projects=request.POST.get('projects')
                references=request.POST.get('references')
                degree=request.POST.get('degree')
                institution=request.POST.get('institution')
                graduation_year=request.POST.get('graduation_year')
                company=request.POST.get('company')
                position=request.POST.get('position')
                start_dates=request.POST.get('start_dates')
                end_dates=request.POST.get('end_dates')
                
                if profile_picture:
                    resume=ResumeModel(
                        id=myid,
                        Profile_picture=profile_picture,
                        Full_name=full_name,
                        Address=address,
                        Phone_number=phone_number,
                        Email_address=email_address,
                        Career_objective=career_objective,
                        Hard_Skills=hard_Skills,
                        Soft_Skills=soft_Skills,
                        Certifications=certifications,
                        Projects=projects,
                        References=references,
                    )
                    education=ResumeEducationModel(
                        id=myid,
                        Degree=degree,
                        Institution=institution,
                        Graduation_year=graduation_year,
                    )
                    work=ResumeWorkModel(
                        id=myid,
                        Company=company,
                        Position=position,
                        Start_dates=start_dates,
                        End_dates=end_dates,
                        
                    )
                else:
                    resumebyid=ResumeModel.objects.get(id=myid)
                    resume=ResumeModel(
                        id=myid,
                        Profile_picture=resumebyid.Profile_picture,
                        Full_name=full_name,
                        Address=address,
                        Phone_number=phone_number,
                        Email_address=email_address,
                        Career_objective=career_objective,
                        Hard_Skills=hard_Skills,
                        Soft_Skills=soft_Skills,
                        Certifications=certifications,
                        Projects=projects,
                        References=references,
                    )
                    education=ResumeEducationModel(
                        id=myid,
                        Degree=degree,
                        Institution=institution,
                        Graduation_year=graduation_year,
                    )
                    work=ResumeWorkModel(
                        id=myid,
                        Company=company,
                        Position=position,
                        Start_dates=start_dates,
                        End_dates=end_dates,
                        
                    )
                resume.save()
                education.save()
                work.save()
            return redirect('home')
        ```
        - This function also handle the `None` image 
        - As we are updating the values withing a model so id is playing very important role here, if we don't do that we will create a new table data rather than updating.
        - finally we save it and redirect to home page.
    - Add the url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from resumeProject.views import home,addresume,deleteresume,editresume,updateresume,viewresume

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',home,name='home'),
            path('addresume/',addresume,name='addresume'),
            path('deleteresume/<str:myid>',deleteresume,name='deleteresume'),
            path('editresume/<str:myid>',editresume,name='editresume'),
            path('updateresume/',updateresume,name='updateresume'),
            
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
- Now let's view the resume we created 
    - We will need a good template for that , gpt will be very helpful in this part. Create a `viewresume.html`
        ```html
        {% extends 'base.html' %}

        {% block content %}
        <style>
            /* Custom styles */
            body {
                background-color: #f8f9fa;
                color: #343a40;
            }
            .section-title {
                color: #007bff;
            }
            .section-heading {
                color: #28a745;
            }
            .profile-picture {
                border-radius: 50%;
                border: 5px solid #17a2b8;
                max-width: 200px;
                height: auto;
            }
            .list-group-item {
                background-color: #f1f1f1;
                border-color: #dee2e6;
            }
        </style>
        <div class="container mt-5">
            <div class="row">
                <div class="col-md-4">
                    <img src="/{{ resumedata.Profile_picture }}" class="img-fluid profile-picture" alt="Profile Picture">
                </div>
                <div class="col-md-8">
                    <h1 class="section-heading">{{ resumedata.Full_name }}</h1>
                    <p><strong>Address:</strong> {{ resumedata.Address }}</p>
                    <p><strong>Phone:</strong> {{ resumedata.Phone_number }}</p>
                    <p><strong>Email:</strong> {{ resumedata.Email_address }}</p>
                    <hr>
                    <h3 class="section-title">Career Objective</h3>
                    <p>{{ resumedata.Career_objective }}</p>
                </div>
            </div>
            <hr>
            <div class="row mt-4">
                <div class="col-md-6">
                    <h3 class="section-title">Education</h3>
                    <ul class="list-group">
                        <li class="list-group-item">{{ educationdata.Degree }} - {{ educationdata.Institution }} ({{ educationdata.Graduation_year }})</li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <h3 class="section-title">Work Experience</h3>
                    <ul class="list-group">
                        <li class="list-group-item">{{ workdata.Position }} at {{ workdata.Company }} ({{ workdata.Start_dates }} - {{ workdata.End_dates }})</li>
                    </ul>
                </div>
            </div>
            <hr>
            <div class="row mt-4">
                <div class="col-md-6">
                    <h3 class="section-title">Hard Skills</h3>
                    <p>{{ resumedata.Hard_Skills }}</p>
                </div>
                <div class="col-md-6">
                    <h3 class="section-title">Soft Skills</h3>
                    <p>{{ resumedata.Soft_Skills }}</p>
                </div>
            </div>
            <hr>
            <div class="row mt-4">
                <div class="col-md-6">
                    <h3 class="section-title">Certifications</h3>
                    <p>{{ resumedata.Certifications }}</p>
                </div>
                <div class="col-md-6">
                    <h3 class="section-title">Projects</h3>
                    <p>{{ resumedata.Projects }}</p>
                </div>
            </div>
            <hr>
            <div class="row mt-4">
                <div class="col-md-12">
                    <h3 class="section-title">References</h3>
                    <p>{{ resumedata.References }}</p>
                </div>
            </div>
        </div>
        {% endblock content %}
        ```
    - Now create a function for this html page to view
        ```python
        def viewresume(request,myid):
            resumedata=ResumeModel.objects.get(id=myid)
            educationdata=ResumeEducationModel.objects.get(id=myid)
            workdata=ResumeWorkModel.objects.get(id=myid)
            
            resume={
                'resumedata':resumedata,
                'educationdata':educationdata,
                'workdata':workdata,
            }
            return render(request,'viewresume.html',resume)
        ```
    - Create url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from resumeProject.views import home,addresume,deleteresume,editresume,updateresume,viewresume

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',home,name='home'),
            path('addresume/',addresume,name='addresume'),
            path('deleteresume/<str:myid>',deleteresume,name='deleteresume'),
            path('editresume/<str:myid>',editresume,name='editresume'),
            path('updateresume/',updateresume,name='updateresume'),
            path('viewresume/<str:myid>',viewresume,name='viewresume'),
            
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Now in action 
        ```html
            <td>
              <a href="{% url 'viewresume' i.id %}">View</a>
            </td>
        ```
- We have done all the required CRUD operation in this Portfolio project

> Bonus Task solution not included here
### Task
- Do full lab-3 project video and submit

</details>

<details>
<summary>Day-21-Python Basic Day 05 & Job Portal Project Part 01 (21-04-2024)</summary>
    
## Day 21 Topics
- Python Basics Day 04 recap
- Nested If else
- Simple problem solving using only if..else
- Job Portal Project Part 01 (Using AbstractUser)

### Simple problem solving using only if..else
> Problem-01: x,y,z who is greater
```python
x=10
y=20
z=30

if x>y:
    if x>z:
        print("x is greater")
    else:
        print("z is greater")
else:
    if y>x:
        if y>z:
            print("y is greater")
        else:
            print("z is greater")
```
> Problem-02: w,x,y,z who is greater
```python
w=10
x=20
y=30
z=40

if w>x:
    if w>y:
        if w>z:
            print("w is greater")
        else:
            print("z is greater")
    else:
        if y>z:
            print("y is greater")
        else:
            print("z is greater")
else:
    if x>y:
        if x>z:
            print("x is greater")
        else:
            print("z is greater")
    else:
        if y>z:
            print("y is greater")
        else:
            print("z is greater")
```
> Problem-03: write the output of below code
```python
a=100
b=300
c=0
c=a
a=b
b=c
c=0
if c:
    print("Hello")
else:
    print(f"Value of a = {a} and value of b = {b}")
```

### Job Portal Project Part 01 (Using AbstractUser)
- Create project and app as usual way
- Create a signup page `signuppage.html`:
    ```html
    {% extends 'base.html' %}
    {% block content %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Signup Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            
            .container {
                max-width: 400px;
                margin: 50px auto;
                background-color: #fff;
                border-radius: 5px;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            
            h2 {
                text-align: center;
            }
            
            label {
                display: block;
                margin-bottom: 5px;
            }
            
            input[type="text"],
            input[type="password"],
            input[type="email"],
            select {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
            }
            
            input[type="submit"] {
                width: 100%;
                background-color: #4caf50;
                color: #fff;
                padding: 10px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            
            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Signup</h2>
            <form action="#" method="POST">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" placeholder="Enter your username" required>
                
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
                
                <label for="confirm_password">Confirm Password:</label>
                <input type="password" id="confirm_password" name="confirm_password" placeholder="Confirm your password" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" placeholder="Enter your email" required>
                
                <label for="user_type">User Type:</label>
                <select id="user_type" name="user_type" required>
                    <option value="" disabled selected>Select User Type</option>
                    <option value="job_seeker">Job Seeker</option>
                    <option value="job_recruiter">Job Recruiter</option>
                </select>
                
                <input type="submit" value="Sign Up">
            </br>
            </br>
                <a href="{% url 'signinpage' %}">Already have an account?</a>
            </form>
        </div>
    </body>
    </html>
    {% endblock content %}
    ```
    - Create function for signin:
        ```python
        from django.shortcuts import render, redirect

        def signuppage(request):
            return render(request,'signuppage.html')

        ```
    - Create url path
        ```python
        from django.contrib import admin
        from django.urls import path
        from jobportalProject.views import signuppage

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('signuppage/',signuppage,name='signuppage'),
        ]
        ```
- Now create a signin page `signinpage.html`
    ```html
    {% extends 'base.html' %}
    {% block content %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Signup Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            
            .container {
                max-width: 400px;
                margin: 50px auto;
                background-color: #fff;
                border-radius: 5px;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            
            h2 {
                text-align: center;
            }
            
            label {
                display: block;
                margin-bottom: 5px;
            }
            
            input[type="text"],
            input[type="password"],
            input[type="email"],
            select {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
            }
            
            input[type="submit"] {
                width: 100%;
                background-color: #4caf50;
                color: #fff;
                padding: 10px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            
            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Signup</h2>
            <form action="#" method="POST">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" placeholder="Enter your username" required>
                
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
                <input type="submit" value="Sign In">
            </br>
            </br>
                <a href="{% url 'signuppage' %}">Don't have an account?</a>
            </form>
        </div>
    </body>
    </html>
    {% endblock content %}

    ```
    - Create function for the singinpage
        ```python
        from django.shortcuts import render, redirect

        def signinpage(request):
            return render(request,'signinpage.html')
        ```
    - Add url path:
        ```python
        from django.contrib import admin
        from django.urls import path
        from jobportalProject.views import signuppage,signinpage

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('signuppage/',signuppage,name='signuppage'),
            path('',signinpage,name='signinpage'),
        ]
        ```
- Now new changes:
    - Create class of `AbstractUser` in `models.py`
        ```python
        from django.db import models
        from django.contrib.auth.models import AbstractUser

        # Create your models here.
        class CustomUserModel(AbstractUser):
            USER=[
                ('recruiter','Recruiter'),
                ('jobseeker','JobSeeker'),
            ]
            user_type=models.CharField(choices=USER,max_length=100)
            user_name = models.CharField(max_length=100)
            display_name=models.CharField(max_length=100)
            email=models.CharField(max_length=100)
            password=models.EmailField(max_length=100)
            confirm_password=models.CharField(max_length=100)

            def __str__(self):
                return self.user_name
        ```
        - Here `CustomUserModel(AbstractUser)` is new, where we created the model.
    - In `admin.py`
        ```python
        from django.contrib import admin
        from jobportalApp.models import CustomUserModel

        # Register your models here.
        class Custom_User_Display(admin.ModelAdmin):
            list_display=['display_name','user_name','email']

        admin.site.register(CustomUserModel,Custom_User_Display)
        ```
        - Here we did some modification before registering the model.
        - The modification is done to display the model data properly in custom way
    - Changes in `settings.py` where we have to include the Auth user model in end line
        ```python
        AUTH_USER_MODEL='jobportalApp.CustomUserModel' # here appname.created_model_name
        ```
    - Now we will migrate our database and create the sueruser:
        - `py manage.py makemigrations jobportalApp`
        - `py manage.py migrate jobportalApp`
        - `py manage.py migrate`
        - `py manage.py makemigrations`
        - `py manage.py createsuperuser`
    - Now we will be able to add new data in our created model

</details>

<details>
<summary>Day-22-Job Portal Project Part 02 (22-04-2024)</summary>

## Day 22 Topics
- Day 21 recap
- Job Portal Project Part 02 (Signup)

### Job Portal Project Part 02 (Signup)
- Modify in `settings.py`
    - Add app in installed app
    - Add template path
    - Add static path
    - Add `AUTH_USER_MODEL`
- Creating model:
    - As we are creating custom model from AbstractUser where many common thing already defined, So we will add only things that are uncommon are not include in AbstractUser:
        ```python
        from django.db import models
        from django.contrib.auth.models import AbstractUser
        # Create your models here.
        class CustomUserModel(AbstractUser):
            USER=[
                ('recruiter','Recruiter'),
                ('seeker','Seeker'),
            ]
            BLOOD_GROUP=[
                ('A+', 'A positive'),
                ('A-', 'A negative'),
                ('B+', 'B positive'),
                ('B-', 'B negative'),
                ('AB+', 'AB positive'),
                ('AB-', 'AB negative'),
                ('O+', 'O positive'),
                ('O-', 'O negative'),
            ]

            fname=models.CharField(max_length=100)
            lname=models.CharField(max_length=100)
            profile_picture=models.ImageField(upload_to='media/profilePic')
            # date_of_birth=models.DateField(auto_now=True)
            date_of_birth=models.DateField(auto_now_add=True)
            address=models.CharField(max_length=100)
            blood_group=models.CharField(choices=BLOOD_GROUP,max_length=100)
            usertype=models.CharField(choices=USER,max_length=100)

            def __str__(self):
                return self.fname
        ```
        - Here `DateField` field is `auto_now_add=True` which will take the date and save it, if it is set as `auto_now=True` then it will save the current date
    - Register the Model
        ```python
        from django.contrib import admin
        from jobportalApp.models import CustomUserModel
        # Register your models here.

        class Custom_User_Display(admin.ModelAdmin):
            list_display=['fname','usertype','blood_group','date_of_birth']

        admin.site.register(CustomUserModel,Custom_User_Display)
        ```
        - Here `Custom_User_Display` class is used to show some of the selected column in admin page in table structure
    - Now let's do the database migrate
        > Execute below command one by one
        - `py manage.py makemigrations jobportalApp`
        - `py manage.py migrate jobportalApp`
        - `py manage.py migrate`
        - `py manage.py makemigrations`
        - `py manage.py createsuperuser`
    - Now we can add model data 
- To add it from frontend page we will create a `signup.html` page
    ```html
    {% extends 'base.html' %}


    {% block content %}
    <form action="{% url 'signup' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
        <label for="name">First Name:</label><br>
        <input type="text" id="name" name="fname" required><br><br>
        <label for="name">Last Name:</label><br>
        <input type="text" id="name" name="lname" required><br><br>
        <label for="name">User Name:</label><br>
        <input type="text" id="name" name="username" required><br><br>
    
        <label for="username">Profile Picture:</label><br>
        <input type="file" id="username" name="profile_picture" required><br><br>
        <label for="date_of_birth">Date of Birth:</label><br>
        <input type="date" id="date_of_birth" name="date_of_birth" required><br><br>
        

        <label for="usertype">Blood Group:</label><br>
        <select id="usertype" name="blood_group" required>
        <option value="" disabled selected>Please select an option</option>
        <option value="A+">A+</option>
        <option value="A-">A-</option>
        <option value="B+">B+</option>
        <option value="B-">B-</option>
        <option value="AB+">AB+</option>
        <option value="AB-">AB-</option>
        <option value="O+">O+</option>
        <option value="O-">O-</option>
    </select><br><br>
    
        <label for="email">Address:</label><br>
        <input type="text" id="email" name="address" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
    
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>
    
        <label for="confirm_password">Confirm Password:</label><br>
        <input type="password" id="confirm_password" name="confirm_password" required><br><br>
    
        <label for="usertype">User Type:</label><br>
        <select id="usertype" name="usertype" required>
            <option value="" disabled selected>Please select an option</option>
        <option value="seeker">Job Seeker</option>
        <option value="recruiter">Job Recruiter</option>
        </select><br><br>
    
        <input type="submit" value="Sign Up">
    </form>
    
    {% endblock content %}
    ```
    - Create a function to render it
        ```python
        from django.shortcuts import render,redirect
        from jobportalApp.models import CustomUserModel

        def signup(request):
            if request.method=="POST":
                fname=request.POST.get('fname')
                lname=request.POST.get('lname')
                profile_picture=request.FILES.get('profile_picture')
                date_of_birth=request.POST.get('date_of_birth')
                blood_group=request.POST.get('blood_group')
                address=request.POST.get('address')
                username=request.POST.get('username')
                email=request.POST.get('email')
                password=request.POST.get('password')
                confirm_password=request.POST.get('confirm_password')
                usertype=request.POST.get('usertype')

                if password==confirm_password:
                    user=CustomUserModel.objects.create_user(
                        username=username,
                        password=confirm_password,
                    )
                    user.fname=fname
                    user.lname=lname
                    user.profile_picture=profile_picture
                    user.date_of_birth=date_of_birth
                    user.blood_group=blood_group
                    user.address=address
                    user.email=email
                    user.usertype=usertype
                    user.save()
                    return redirect('signin')

                else:
                    return redirect('signup')

            return render(request,'signup.html')
        ```
    - Add url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from jobportalProject.views import signin,signup

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('signup/',signup,name='signup'),
        ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Now we will be able to add it from this frontend form

</details>

<details>
<summary>Day-23-Job Portal Project Part 01 to 03 (23-04-2024)</summary>

## Day 23 Topics

- Day 22 recap
- Job Portal Part 03 (Sign-In Authentication)
- Task

### Job Portal Part 03 (Sign-In Authentication)
- For authenticate user login `authenticate`,`login` is used 
    ```python 
    from django.contrib.auth import authenticate,login,logout
    def signin(request):
        if request.method=="POST":
            uname=request.POST.get('uname')
            password=request.POST.get('password')
            
            user = authenticate(
                username=uname,
                password=password,
            )
            print(f'Logged in user: {user}')
            if user:
                login(request,user)
                return redirect('dashboard')
            else:
                return redirect('signin')
        return render(request,'signin.html')
    ```
    - For log out
        ```python
        def logoutpage(request):
            logout(request)
            return redirect('signin')
        ```
- Other task are similar to previous CRUD operation
### Task
- Job Portal Project Part 01 - 03
    - Create user model using `AbstractUser` Model
    - Create `SignUp` / `SignIn` page using below field
        - **First Name**
        - **Last name**
        - **Username**
        - **Email**
        - **Password**
        - **Confirm Password**
        - **Profile Picture**
        - **Date of Birth**
        - **Address**
        - **Blood Group**
        - **User Type** 
    - After Login user will be in a `Dashboard` with `navbar` where:
        - **Dashboard**
        - **View Job**
        - **Add Job**
        - **Applied Job**
        - **Recent Job**
        - **Profile**
        - **Log out**

            - If user is `Job Recruiter` below navigation will be present
                - **Dashboard**
                - **View Job**
                - **Add Job**
                - **Profile**
                - **Log out**
            - If user is `Job Seeker` below navigation will be present
                - **Dashboard**
                - **View Job**
                - **Applied Job**
                - **Recent Job**
                - **Profile**
                - **Log out**
            > Create all those above mentioned individual navigation pages including CRUD Operation
        - `Add Job` page will have these field:
            - **Job title**
            - **Company name**
            - **Address**
            - **Company description**
            - **Job description**
            - **Qualification**
            - **Salary information**
            - **Deadline**
            - **Designation**
            - **Experience**

</details>

<details>
<summary>Day-24-Job Portal Project Part 04 (24-04-2024)</summary>

## Day 24 Topics
- Day 23 recap
- Job Portal Project Part 04
    - Organize Templates
    - Login Required
    - In Dashboard/view job page Only Recruiter can edit/update, delete job post where seeker can only view
    - Recruiter can see their post only which they posted but Job seeker will be able to see all the job

### Organize Templates
- Create individual folder in template folder
    ```text
    |----templates
         |
         |--recruiter
             |
             |--addjob.html
    ```
- Now edit the edit the path in `views.py` function `'recruiter/addjob.html'`

### Login Required
- It is used to restrict an user from access some pages which required login
    ```python
    from django.contrib.auth.decorators import login_required
    @login_required
    def dashboard(request):
        job=JobModel.objects.all()
        jobDict={
            'job':job
        }
        return render(request,'dashboard.html',jobDict)
    ```
    - Now in `settings.py` we have to include the `LOGIN_URL`
        ```python
        LOGIN_URL='signin'
        ```
    - Now the `dashboard.html` is being restricted from accessing without login

- Now what if according to our project there is two type of person can login `recruiter` and `seeker` where `seeker` want to access `addjob` page, so we can restrict it by using below method:
    ```python
    @login_required
    def addjob(request):
        if request.user.user_type == 'recruiter':
            if request.method=="POST":
                Job_title=request.POST.get('Job_title')
                Company_name=request.POST.get('Company_name')
                Address=request.POST.get('Address')
                Company_description=request.POST.get('Company_description')
                Job_description=request.POST.get('Job_description')
                Qualification=request.POST.get('Qualification')
                Salary_information=request.POST.get('Salary_information')
                Deadline=request.POST.get('Deadline')
                Designation=request.POST.get('Designation')
                Experience=request.POST.get('Experience')
                
                job=JobModel(
                    Recruiter=request.user.username,
                    Job_title=Job_title,
                    Company_name=Company_name,
                    Address=Address,
                    Company_description=Company_description,
                    Job_description=Job_description,
                    Qualification=Qualification,
                    Salary_information=Salary_information,
                    Deadline=Deadline,
                    Designation=Designation,
                    Experience=Experience,
                )
                job.save()
                return redirect('viewjob')
            return render(request,'recruiter/addjob.html')
        else:
            logout(request)
            return redirect('signin')
    ```
    > Also we can use is_authenticated to authenticate an user before accessing

### In Dashboard/view job page Only Recruiter can edit/update, delete job post where seeker can only view
- To do this we will use condition
    ```python
    @login_required
    def dashboard(request):
        job=JobModel.objects.all()
        jobDict={
            'job':job
        }
        return render(request,'dashboard.html',jobDict)
    ```
- Now `dashboard.html` page
    ```html
    <table id="customers">
    <tr>
        <th>Recruiter</th>
        <th>Job title</th>
        <th>Company name</th>
        <th>Address</th>
        <th>Company description</th>
        <th>Job description</th>
        <th>Qualification</th>
        <th>Salary information</th>
        <th>Deadline</th>
        <th>Designation</th>
        <th>Experience</th>
        <th>Action</th>
    </tr>
    {% for i in job %}
    {% if user.username == i.Recruiter %}
        <tr>
            <td>{{i.Recruiter}}</td>
            <td>{{i.Job_title}}</td>
            <td>{{i.Company_name}}</td>
            <td>{{i.Address}}</td>
            <td>{{i.Company_description}}</td>
            <td>{{i.Job_description}}</td>
            <td>{{i.Qualification}}</td>
            <td>{{i.Salary_information}}</td>
            <td>{{i.Deadline}}</td>
            <td>{{i.Designation}}</td>
            <td>{{i.Experience}}</td>
            <td>
            
            {% if user.user_type == 'recruiter' %}
            <a href="{% url 'editjob' i.id %}">Edit</a>
            <a href="{% url 'deletejob' i.id %}">Delete</a>
            {% endif %}
            <a href="{% url 'viewjob' %}">View</a>

            </td>
        </tr>
        {% elif user.user_type == 'seeker' %}
        <tr>
        <td>{{i.Recruiter}}</td>
        <td>{{i.Job_title}}</td>
        <td>{{i.Company_name}}</td>
        <td>{{i.Address}}</td>
        <td>{{i.Company_description}}</td>
        <td>{{i.Job_description}}</td>
        <td>{{i.Qualification}}</td>
        <td>{{i.Salary_information}}</td>
        <td>{{i.Deadline}}</td>
        <td>{{i.Designation}}</td>
        <td>{{i.Experience}}</td>
        <td>
            
            {% if user.user_type == 'recruiter' %}
            <a href="{% url 'editjob' i.id %}">Edit</a>
            <a href="{% url 'deletejob' i.id %}">Delete</a>
            {% endif %}
            <a href="{% url 'viewjob' %}">View</a>

        </td>
        {% endif %}
    {% endfor %}
        
    </table>
    ```
### Recruiter can see their post only which they posted but Job seeker will be able to see all the job
- To do this we can use condition 
    ```python
    @login_required
    def viewjob(request):
        job=JobModel.objects.all()
        jobDict={
            'jobs':job
        }
        return render(request,'viewjob.html',jobDict)
    ```
- Now the `viewjob.html` page
    ```html
    <body>
        <h1>Job Listings</h1>
        <div class="job-listings">
            
            {% for job in jobs %}
            
            {% if user.username == job.Recruiter %}
            <div class="job">
                <h2>{{ job.Job_title }}</h2>
                <p><strong>Company:</strong> {{ job.Company_name }}</p>
                <p><strong>Location:</strong> {{ job.Address }}</p>
                <p><strong>Company Description:</strong> {{ job.Company_description }}</p>
                <p><strong>Job Description:</strong> {{ job.Job_description }}</p>
                <p><strong>Qualification:</strong> {{ job.Qualification }}</p>
                <p><strong>Salary Information:</strong> {{ job.Salary_information }}</p>
                <p><strong>Deadline:</strong> {{ job.Deadline }}</p>
                <p><strong>Designation:</strong> {{ job.Designation }}</p>
                <p><strong>Experience:</strong> {{ job.Experience }}</p>
                <div class="actions">
                    {% if user.user_type == 'recruiter' %}
                    <button class="update"> <a href="{% url 'editjob' job.id %}" >Update</a></button>
                    <button class="delete"><a href="{% url 'deletejob' job.id %}" >Delete</a></button> 
                    {% endif %}
                </div>
            </div>
            {% elif user.user_type == 'seeker' %}
            <div class="job">
                <h2>{{ job.Job_title }}</h2>
                <p><strong>Recruiter:</strong> {{ job.Recruiter }}</p>
                <p><strong>Company:</strong> {{ job.Company_name }}</p>
                <p><strong>Location:</strong> {{ job.Address }}</p>
                <p><strong>Company Description:</strong> {{ job.Company_description }}</p>
                <p><strong>Job Description:</strong> {{ job.Job_description }}</p>
                <p><strong>Qualification:</strong> {{ job.Qualification }}</p>
                <p><strong>Salary Information:</strong> {{ job.Salary_information }}</p>
                <p><strong>Deadline:</strong> {{ job.Deadline }}</p>
                <p><strong>Designation:</strong> {{ job.Designation }}</p>
                <p><strong>Experience:</strong> {{ job.Experience }}</p>
                <div class="actions">
                    {% if user.user_type == 'recruiter' %}
                    <button class="update"> <a href="{% url 'editjob' job.id %}" >Update</a></button>
                    <button class="delete"><a href="{% url 'deletejob' job.id %}" >Delete</a></button> 
                    {% endif %}
                </div>
            </div>
            {% endif %}
        {% endfor %}
        </div>
    </body>
    {% endblock content %}
    ```
    - Here `username` of the recruiter is checked to show their posting job only
    - As job seeker can view all jobs so only the type is checked which showed all the job

</details>

<details>
<summary>Day-25-Job Portal Project (ForeignKey) (25-04-2024)</summary>

## Day 25 Topics
- Job Portal Project Day 01 to 04 Recap
- Using ForeignKey

### Using ForeignKey
- To make sure the recruiter who posted the job we can use `ForeignKey` in `JobModel` to make a relationship with `CustomUserModel`
    ```python
    from django.db import models
    from django.contrib.auth.models import AbstractUser

    # Create your models here.

    class CustomUserModel(AbstractUser):
        fname=models.CharField(max_length=100)
        lname=models.CharField(max_length=100)
        profile_picture=models.ImageField(upload_to='media/profile_pic')
        date_of_birth=models.DateField(auto_now_add=True)
        address=models.CharField(max_length=100)
        BLOOD_GROUP=[
            ('a+','A Positive'),
            ('a-','A Negative'),
            ('b+','B Positive'),
            ('b-','B Negative'),
            ('ab+','AB Positive'),
            ('ab-','AB Negative'),
            ('o+','O Positive'),
            ('o-','O Negative'),
        ]
        blood_group=models.CharField(choices=BLOOD_GROUP,max_length=100)
        USER_TYPE=[
            ('recruiter','Job Recruiter'),
            ('seeker','Job Seeker'),
        ]
        user_type=models.CharField(choices=USER_TYPE,max_length=100)
        
        def __str__(self):
            return self.fname
        
    class JobModel(models.Model):
        Job_title=models.CharField(max_length=100)
        Company_name=models.CharField(max_length=100)
        Address=models.CharField(max_length=100)
        Company_description=models.TextField()
        Job_description=models.TextField()
        Qualification=models.CharField(max_length=100)
        Salary_information=models.CharField(max_length=100)
        Deadline=models.DateField(auto_now_add=True)
        Designation=models.CharField(max_length=100)
        Experience=models.CharField(max_length=100)
        Recruiter=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
        
        def __str__(self):
            return self.Job_title
    ```
    - Here in `JobModel` we used `Recruiter=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)` 
    - Now the argument we are passing are:
        - First one is our `CustomUserModel`
        - Second one is `on_delete=models.CASCADE`
        > First one is used for creating the relationship and the Second one is used when we gonna delete a recruiter it will also delete the jobs created by that user
</details>

<details>
<summary>Day-26-Job Portal Project Part 01 to 04 Recap (27-04-2024)</summary>

## Job portal Part 01 to 04 recap
1. Create project: `django-admin startproject jobportalProject`
2. Create app: 
    - `cd jobportalProject`
    - `py manage.py startapp jobportalApp`
3. Initial modification in `settings.py`
    - Add app name in `INSTALLED_APPS`
        ```python
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'jobportalApp',
        ]
        ```
    - Static file directory
        ```python
        STATICFILES_DIRS = [
            BASE_DIR / "static",
        ]
        ```
    - Add the value of `'DIRS'` in `TEMPLATES` for templates directory path
        ```python
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [BASE_DIR, 'templates'],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]
        ```
4. Now Create a folder `templates` which we have added in `TEMPLATES`'s in `'DIRS'` project directory where `manage.py` present
    ```text
    jobportalProject/ # this is project name
    │
    ├── manage.py
    ├── jobportalProject/ # this is project name
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├─── jobportalApp/ # this is app name
    │    ├── migrations/
    │    ├── __init__.py
    │    ├── admin.py
    │    ├── apps.py
    │    ├── models.py
    │    ├── tests.py
    │    └── views.py
    │
    └──── templates/  # this is created manually
    ```
5. Create a `signup.html` in `templates` directory
    - Get a simple `css form` from [w3school](https://www.w3schools.com/css/css_form.asp)
    - Now let's render it; Create a file `views.py` in project directory
        ```text
        jobportalProject/ # this is project name
        │
        └── jobportalProject/ # this is project name
            ├── __init__.py
            ├── settings.py
            ├── urls.py
            ├── wsgi.py
            └── views.py # manually created
        ```
    - Create a function in `views.py`
        ```python
        from django.shortcuts import render,redirect

        def signup(request):
            return render(request,'signup.html')
        ```
    - Add url path in url pattern 
        ```python
        from django.contrib import admin
        from django.urls import path
        from jobportalProject.views import signup

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('signup/',signup,name='signup'),
        ]
        ```
    - Now we can view the page in `http://127.0.0.1:8000/signup/` path
    - Modify the `signup.html` page with those below field
        - **First Name**
        - **Last name**
        - **Username**
        - **Email**
        - **Password**
        - **Confirm Password**
        - **Profile Picture**
        - **Date of Birth**
        - **Address**
        - **Blood Group**
        - **User Type**
    - As there is image in `signup`, So we need to add the media url in our `urls.py`
        ```python
        from django.conf import settings
        from django.conf.urls.static import static

        urlpatterns = [
            # ... the rest of your URLconf goes here ...
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Now create `AbstractUser` model in `models.py` which is in app directory
        ```python
        from django.db import models
        from django.contrib.auth.models import AbstractUser
        # Create your models here.
        class CustomUserModel(AbstractUser):
            picture=models.ImageField(upload_to='static/profilepics')
            dob=models.DateField(auto_now_add=True)
            address=models.TextField()
            BLOOD_GROUP=[
                ('a+','A Positive'),
                ('a-','A Negative'),
                ('b+','B Positive'),
                ('b-','B Negative'),
                ('ab+','AB Positive'),
                ('ab-','AB Negative'),
                ('o+','O Positive'),
                ('o-','O Negative'),
            ]
            blood_group=models.CharField(choices=BLOOD_GROUP,max_length=100)
            USER_TYPE=[
                ('recruiter','Job Recruiter'),
                ('seeker','Job Seeker'),
            ]
            user_type=models.CharField(choices=USER_TYPE,max_length=100)
            
            def __str__(self):
                return self.username
        ````
        - Here missing `first_name`,`last_name`,`username`,`email`,`password` are already defined in `AbstractUser`
    - Now register the model in `admin.py`
        ```python
        from django.contrib import admin
        from jobportalApp.models import CustomUserModel

        # Register your models here.

        class CustomUserModelDisplay(admin.ModelAdmin):
            list_display=['username','blood_group','user_type']

        admin.site.register(CustomUserModel)
        ```
        - Here `CustomUserModelDisplay` is created to display the model data in admin page in more detailed.
    - Add `CustomUserModel` in `settings.py` 
        ```python
        AUTH_USER_MODEL='jobportalApp.CustomUserModel'
        ```
    - Run those command in order
        ```bash
        py manage.py makemigrations jobportalApp
        py manage.py migrate jobportalApp
        py manage.py makemigrations
        py manage.py migrate
        ```
    - Now let's modify our `signup` function in `views.py`
        ```python
        from django.shortcuts import render,redirect
        from jobportalApp.models import CustomUserModel
        def signup(request):
            if request.method=="POST":
                fname=request.POST.get('fname')
                lname=request.POST.get('lname')
                uname=request.POST.get('uname')
                email=request.POST.get('email')
                password=request.POST.get('password')
                cpassword=request.POST.get('cpassword')
                picture=request.FILES.get('picture')
                dob=request.POST.get('dob')
                address=request.POST.get('address')
                blood_group=request.POST.get('blood_group')
                user_type=request.POST.get('user_type')
                
                if password==cpassword:
                    
                    user = CustomUserModel.objects.create_user(
                        first_name=fname,
                        last_name=lname,
                        username=uname,
                        email=email,
                        password=password,
                        picture=picture,
                        dob=dob,
                        address=address,
                        blood_group=blood_group,
                        user_type=user_type,
                    )
                    user.save()
                    return redirect('signin')
                else:
                    return redirect('signup')
                
            return render(request,'signup.html')

        def signin(request):
            return render(request,'signin.html')
        ```
        - Here after we get the data from form we checked if password and confirm password is same or not
        - We created another page in `templates` which is `signin.html` so that after signup user will be redirected to `signin.html` page
6. Now let's modify `signin.html`
    - `signin.html` page will have those field
        - **Username**
        - **Password**
    - Modify `signin` function
        ```python
        def signin(request):
            if request.method=="POST":
                uname=request.POST.get('uname')
                password=request.POST.get('password')
                
                user=authenticate(
                    username=uname,
                    password=password,
                )
                if user:
                    login(request,user)
                    return redirect('dashboard')
                else:
                    return redirect('signin')
            return render(request,'signin.html')

        def dashboard(request):
            return render(request,'dashboard.html')
        ```
        - Here we have imported `from django.contrib.auth import authenticate,login,logout` where 
            - `authenticate` is used to authenticate an user
            - `login` is used to login an user with session
            - `logout` which will be used in separate function to logout an user
        - After authentication is successful user will be redirected to `dashboard.html` page
7. Now we have to do the template mastering while creating `dashboard.html`
    - Get a navbar from [w3school](https://www.w3schools.com/css/css_navbar_horizontal.asp)
    - Create `base.html`, `navbar.html`, `dashboard.html`
        - `base.html` - This is the base structure of the page
        - `navbar.html` - This will only contain the navbar content and include it in `base.html`
        - `dashboard.html` - This will extends the `base.html` and it's content will be inside block content
8. Let's implement logout function
    - Create a `logoutpage` function in `views.py` 
        ```python
        def logoutpage(request):
            logout(request)
            return redirect('signin')
        ```
    - Add url path in `urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path
        from django.conf import settings
        from django.conf.urls.static import static
        from jobportalProject.views import signup,signin,dashboard,logoutpage

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('signup/',signup,name='signup'),
            path('',signin,name='signin'),
            path('dashboard/',dashboard,name='dashboard'),
            path('logoutpage/',logoutpage,name='logoutpage'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Add the `logoutpage` name in navbar url 
        ```html
        <ul>
            <li><a href="{% url 'dashboard' %}">Dashboard</a></li>
            <li style="float:right"><a class="active" href="{% url 'logoutpage' %}">Log Out</a></li>
        </ul>
        ```
9. Now after logout we can still visit the dashboard url which should not.
    - Let's add login required functionality
        ```python
        from django.contrib.auth.decorators import login_required
        @login_required
        def dashboard(request):
            return render(request,'dashboard.html')
        ```
        Now we have to add `LOGIN_URL` in `settings.py`
        ```python
        LOGIN_URL='signin'
        ```
        - Now without login dashboard can't be access
        - As we have added `LOGIN_URL` so whenever user try to access dashboard page without login , user will be redirected in login page
10. Now we have to add those pages in our `navbar.html` where we already created `dashboard` and `logout`
    - **Dashboard**
    - **View Job**
    - **Add Job**
    - **Applied Job**
    - **Recent Job**
    - **Profile**
    - **Log out**
        - First let's create add job page; In `addjob.html` form page below field will be present and the template file will be in `recuiter/addjob.html` of templates directory
            - **Job title**
            - **Company name**
            - **Address**
            - **Company description**
            - **Job description**
            - **Qualification**
            - **Salary information**
            - **Deadline**
            - **Designation**
            - **Experience**
        - After creating form we will create the `addjob` function 
            ```python
            def addjob(request):
                return render(request,'addjob.html')
            ```
        - Add this in `urls.py` and `navbar` and proceed to create the model in `models.py`
            ```python
            class JobModel(models.Model):
                Job_title=models.CharField(max_length=100)
                Company_name=models.CharField(max_length=100)
                Address=models.CharField(max_length=100)
                Company_description=models.TextField()
                Job_description=models.TextField()
                Qualification=models.CharField(max_length=100)
                Salary_information=models.CharField(max_length=100)
                Deadline=models.DateField(auto_now_add=True)
                Designation=models.CharField(max_length=100)
                Experience=models.CharField(max_length=100)
                Created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
                
                def __str__(self):
                    return f"{self.Job_title} created by {self.Created_by}"
            ```
            - Here `Created_by` is creating a relationship with our `CustomUserModel` model and when a user is deleted it will delete all the job created by that user too which is done by using `on_delete=models.CASCADE`
        - Register the model in `admin.py`
            ```python
            admin.site.register(JobModel)
            ```
        - Now we can modify our `addjob` function to get the user input and save it in our `JobModel`
            ```python
            @login_required
            def addjob(request):
                if request.method=="POST":
                    Job_title=request.POST.get('Job_title')
                    Company_name=request.POST.get('Company_name')
                    Address=request.POST.get('Address')
                    Company_description=request.POST.get('Company_description')
                    Job_description=request.POST.get('Job_description')
                    Qualification=request.POST.get('Qualification')
                    Salary_information=request.POST.get('Salary_information')
                    Deadline=request.POST.get('Deadline')
                    Designation=request.POST.get('Designation')
                    Experience=request.POST.get('Experience')
                    
                    job=JobModel(
                        Job_title=Job_title,
                        Company_name=Company_name,
                        Address=Address,
                        Company_description=Company_description,
                        Job_description=Job_description,
                        Qualification=Qualification,
                        Salary_information=Salary_information,
                        Deadline=Deadline,
                        Designation=Designation,
                        Experience=Experience,
                        Created_by=request.user
                    )
                    job.save()
                    return redirect('dashboard')
                return render(request,'addjob.html')
            ```
        - Now let's create `viewjob.html` page to view the job which we have added; where below function will pass all the job data
            ```python
            @login_required
            def viewjob(request):
                jobs=JobModel.objects.all()
                jobDict={
                    'jobs':jobs
                }
                return render(request,'viewjob.html',jobDict)
            ```
        - Now let's create the dashboard where all the job will be present in table with three action: `edit`,`delete`,`view`; get the table from [w3school](https://www.w3schools.com/css/tryit.asp?filename=trycss_table_fancy)
            ```python
            @login_required
            def dashboard(request):
                jobs=JobModel.objects.all()
                jobDict={
                    'jobs':jobs
                }
                return render(request,'dashboard.html',jobDict)
            ```
            Where the table will be as below
            ```html
            <table id="customers">
            <tr>
                <th>Job title</th>
                <th>Company name</th>
                <th>Address</th>
                <th>Action</th>
            </tr>

            {% for i in jobs %}
                <tr>
                    <td>{{i.Job_title}}</td>
                    <td>{{i.Company_name}}</td>
                    <td>{{i.Address}}</td>
                    <td>
                        <a href="">View</a>
                        <a href="">Edit</a>
                        <a href="">Delete</a>
                    </td>
                </tr>
            {% endfor %}
                
            </table>
            ```
            - Here we will implement the delete action first
                ```python
                @login_required
                def deletejob(request,myid):
                    job=JobModel.objects.get(id=myid)
                    job.delete()
                    return redirect('dashboard')
                ```
                Now add the function in `urls.py` pattern and add the name in dashboard delete action url
            - Now let's implement the edit action; Where we will create the `editjob.html` page same as `addjob.html` in recruiter directory of our templates folder with different action function; Below we implement the `editjob function`
                ```python
                @login_required
                def editjob(request,myid):
                    job=JobModel.objects.get(id=myid)
                    jodDict={
                        'job':job
                    }
                    return render(request,'recruiter/editjob.html',jodDict)
                ```
                Now the update function which will be the action of the `editjob.html` page
                ```python
                @login_required
                def updatejob(request):
                    if request.method=="POST":
                        myid=request.POST.get('myid')
                        Job_title=request.POST.get('Job_title')
                        Company_name=request.POST.get('Company_name')
                        Address=request.POST.get('Address')
                        Company_description=request.POST.get('Company_description')
                        Job_description=request.POST.get('Job_description')
                        Qualification=request.POST.get('Qualification')
                        Salary_information=request.POST.get('Salary_information')
                        Deadline=request.POST.get('Deadline')
                        Designation=request.POST.get('Designation')
                        Experience=request.POST.get('Experience')
                        
                        if Deadline:
                            job=JobModel(
                                id=myid,
                                Job_title=Job_title,
                                Company_name=Company_name,
                                Address=Address,
                                Company_description=Company_description,
                                Job_description=Job_description,
                                Qualification=Qualification,
                                Salary_information=Salary_information,
                                Deadline=Deadline,
                                Designation=Designation,
                                Experience=Experience,
                                Created_by=request.user
                            )
                        else:
                            jobbyid=JobModel.objects.get(id=myid)
                            job=JobModel(
                            id=myid,
                            Job_title=Job_title,
                            Company_name=Company_name,
                            Address=Address,
                            Company_description=Company_description,
                            Job_description=Job_description,
                            Qualification=Qualification,
                            Salary_information=Salary_information,
                            Deadline=jobbyid.Deadline,
                            Designation=Designation,
                            Experience=Experience,
                            Created_by=request.user
                            )
                        job.save()
                        return redirect('dashboard')
                ```
                - Here `Deadline` is checked if it is not updated by user it will take the currently available deadline from the model
            - Now we will implement the `viewsinglejob.html` page where user will view the specific single job from dashboard
                ```python
                @login_required
                def viewsinglejob(request,myid):
                    job=JobModel.objects.get(id=myid)
                    jodDict={
                        'job':job
                    }
                    return render(request,'viewsinglejob.html',jodDict)
                ```
        - As we haven't complete the profile page yet, so let's do it by adding a `profile.html` in templates directory and implement the below function
            ```python
            @login_required
            def profile(request):
                return render(request,'profile.html')
            ```
            Now the `profile.html` page which already have the `user` data after login, so we can access the model data using `{{user.variable_name_in_model}}`
            ```html
            <div class="user-info">
                <label>First Name:</label>
                <p>{{ user.first_name }}</p>

                <label>Last Name:</label>
                <p>{{ user.last_name }}</p>

                <label>Username:</label>
                <p>{{ user.username }}</p>

                <label>Email:</label>
                <p>{{ user.email }}</p>

                <label>Date of Birth:</label>
                <p>{{ user.dob }}</p>

                <label>Address:</label>
                <p>{{ user.address }}</p>

                <label>Blood Group:</label>
                <p>{{ user.blood_group }}</p>

                <label>User Type:</label>
                <p>{{ user.user_type }}</p>
            </div>
            ```
11. Now we have completed the project but there is something which we can notice, like Job seeker can 
    - Add job
    - Delete job
    - Edit job
    
    To solve this we have to use condition to verify the `usertype`
    - First we will solve the add job where only recruiter can add job; For now we can simply check it in frontend if usertype is recruiter or not. Let's edit the `navbar.html`
        ```html
        <ul>
            <li><a href="{% url 'dashboard' %}">Dashboard</a></li>
            
            {% if user.user_type == 'recruiter' %}
            <li><a href="{% url 'addjob' %}">Add Job</a></li>
            {% endif %}
            <li><a href="{% url 'viewjob' %}">View Job</a></li>
            <li style="float:right"><a class="active" href="{% url 'logoutpage' %}">Log Out</a></li>
            <li style="float:right"><a href="{% url 'profile' %}">Profile</a></li>
        </ul>
        ```
        - Here we checked the user type `user.user_type == 'recruiter'`
    - Now the delete and edit action in `dashboard.html` page; Here similarly we will checked the user type
        ```html
        {% for i in jobs %}
            <tr>
                <td>{{i.Job_title}}</td>
                <td>{{i.Company_name}}</td>
                <td>{{i.Address}}</td>
                <td>
                {% if user.user_type == 'recruiter' %}
                <a href="{% url 'editjob' i.id %}">Edit</a>
                <a href="{% url 'deletejob' i.id %}">Delete</a>
                {% endif %}
                <a href="{% url 'viewsinglejob' i.id %}">View</a>
                </td>
            </tr>
        {% endfor %}
        ```
        - Here we also checked the user type `user.user_type == 'recruiter'`
12. Now a recruiter can only see their posted job and edit those only not the others 
    - To do this we have to modify our `viewjob` function
        ```python
        @login_required
        def viewjob(request):
            current_user=request.user
            if current_user.user_type == 'recruiter':
                jobs=JobModel.objects.filter(Created_by=request.user)
            else:
                jobs=JobModel.objects.all()
            jobDict={
                'jobs':jobs
            }
            return render(request,'viewjob.html',jobDict)
        ```
    - Now let's fix the `dashboard.html` page also by modifying the dashboard function
        ```python
        @login_required
        def dashboard(request):
            current_user=request.user
            if current_user.user_type == 'recruiter':
                jobs=JobModel.objects.filter(Created_by=request.user)
            else:
                jobs=JobModel.objects.all()
            jobDict={
                'jobs':jobs
            }
            return render(request,'dashboard.html',jobDict)
        ```
        ```diff
        - The old viewjob & dashboard function was passing the whole job model data in dictionary
        + We changes that by checking the user type if it is recruiter then who created that job by filtering that we pass the data in dictionary otherwise if user type is job seeker we pass whole job model data
        ```
</details>

<details>
<summary>Day-27-Lab Exam 04 (28-04-2024)</summary>

## Lab Exam 04 Recipe Manager Project

> Recipe Manager Project Overview: The Recipe Manager is a web application built with using Django. allowing users to manage their recipes. It provides features for user authentication, recipe management. The application utilizes Django's built-in authentication system, SQLite for the database, and Django templates for rendering HTML pages. Two types of users: chef (or owners) who can create, edit, delete, and update recipes. and viewers who can only view recipes.

User Authentication: 
- **Sign up**: Users can create a new account by providing a Username, E-mail. and Password, Gender, Age, City, Country. **(15 Marks)**
- **Log in**: Registered users can log in using their Username and Password. **(10 Marks)**
- **Log out**: Users can log out of their accounts. **(5 Marks)**
- **Recipe**: Recipe Title, Ingredients, Instructions, Preparation Time, Cooking Time, Total Time. Difficulty Level, Nutritional Information, Sample Recipe image, Recipe Category, Tags (vegetarian, non-vegetarian), Total Calorie. **(20 Marks)**
- Viewers will view all Recipe which is created by Chef **(25 Marks)**
- Create a Profile for both users **(15 Marks)**
- When a chef login the website only he/she can view his/her created recipe. **(10 Marks)**

> It took 2 hour 50 minutes for me which placed me 2nd position; total given time was 4 hours

</details>

<details>
<summary>Day-28-Profile Model (OneToOneField) (29-04-2024)</summary>

## Day 28 Topics
- Lab Exam 04 : Recipe Manager Project Recap
- Profile Model

### Profile Model
- To create profile we will use `OneToOneField`
    ```python
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    # Create your models here.

    class CustomUserModel(AbstractUser):
        GENDER=[
            ('male','Male'),
            ('female','Female'),
        ]
        gender=models.CharField(choices=GENDER,max_length=50)
        age=models.CharField(max_length=100)
        city=models.CharField(max_length=100)
        country=models.CharField(max_length=100)
        USER_TYPE=[
            ('chef','Chef'),
            ('viewer','Viewer'),
        ]
        user_type=models.CharField(choices=USER_TYPE,max_length=50)

        def __str__(self):
            return self.username
        
    class ChefProfileModel(models.Model):
        myuser = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
        experience=models.CharField(max_length=100)
        skill=models.CharField(max_length=100)
        resume_latter=models.CharField(max_length=100)
        profile_pic=models.ImageField(upload_to='static/profile_pic')

        def __str__(self):
            return self.myuser.username

    class ViewerProfileModel(models.Model):
        myuser = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
        favourite=models.CharField(max_length=100)
        profile_pic=models.ImageField(upload_to='static/profile_pic')

        def __str__(self):
            return self.myuser.username
    ```
    - Here we  created two profile `ChefProfileModel` and `ViewerProfileModel`
    - Both has `OneToOneField` relationship with `CustomUserModel` model
- Register both model in `admin.py`
    ```python
    from django.contrib import admin
    from recipeApp.models import CustomUserModel,RecipeModel,ChefProfileModel,ViewerProfileModel
    # Register your models here.

    class CustomUserModelDisplay(admin.ModelAdmin):
        list_display=['username','user_type','gender']

    admin.site.register(CustomUserModel,CustomUserModelDisplay)
    admin.site.register(RecipeModel)
    admin.site.register(ChefProfileModel)
    admin.site.register(ViewerProfileModel)
    ```

</details>

<details>
<summary>Day-29-Recipe Management Project recap Day 02 & Python Day 06 (30-04-2024)</summary>

## Day 29 Topics
- Lab Exam 04 : Recipe Manager Project Recap Day 02
- Python Day 06

### Python Day 06
- Nested if...else recap
- Test exam on previous day's class
- if...elif

### Nested if...else recap
- Problem 01: which one is the greater number among 4 using nested `if..else`
    ```python
    w=10
    x=20
    y=30
    z=40

    if w>x:
        if w>y:
            if w>z:
                print('w is greater')
            else:
                print('z is greater')
        else:
            if y>z:
                print('y is greater')
            else:
                print('z is greater')
    else:
        if x>y:
            if x>z:
                print('x is greater')
            else:
                print('z is greater')
        else:
            if y>z:
                print('y is greater')
            else:
                print('z is greater')
    ```

### Test exam on previous day's class
Which of the following is not a valid comparison operator in Python?
 - [ ] ==
 - [ ] !=
 - [ ] <=
 - [ ] ><

What is the output of the following code snippet?
```python
x = 5
y = 2
print(x ** y)
```
 - [ ] 10
 - [ ] 25
 - [ ] 7
 - [ ] 32

What is the output of the following code snippet?
```python
print(2 ** 3)
```
 - [ ] 6
 - [ ] 7
 - [ ] 8
 - [ ] 16

Which of the following is not a valid variable name in Python?
 - [ ] my_var
 - [ ] 2var
 - [ ] _var
 - [ ] var2

What is the output of the following code snippet?
```python
print("Hello" * 3)
```
 - [ ] HelloHelloHello
 - [ ] Hello3
 - [ ] HelloHello
 - [ ] 3Hello

What is the output of the following code snippet?
```python
print(10 / 3)
```
 - [ ] Error
 - [ ] 3.0
 - [ ] 3
 - [ ] 3.3333

What function can be used to convert a string to an integer in Python?
 - [ ] str()
 - [ ] int()
 - [ ] float()
 - [ ] bool(

What is the result of the expression `10 / 2` ?
 - [ ] 5.0
 - [ ] 5
 - [ ] 2.5
 - [ ] 2


What is the output of the following code snippet?
```python
x = 5
x += 2
print(x)
```
 - [ ] Error
 - [ ] 10
 - [ ] 7
 - [ ] 5

Which of the following is the correct way to assign a value to a variable in Python?
 - [ ] x := 5
 - [ ] x == 5
 - [ ] 5 = x
 - [ ] x = 5

What is the output of the following code snippet?
```python
print(5 == 5.0)
```
 - [ ] 1
 - [ ] Error
 - [ ] False
 - [ ] True

What symbol is used to denote comments in Python?
 - [ ] //
 - [ ] #
 - [ ] /*
 - [ ] %

What is the output of the following code snippet?
```python
x = 10
y = 3
print(x // y)
```
 - [ ] 4
 - [ ] 3.0
 - [ ] 3
 - [ ] 3.3333

What is the result of the expression `3 * "2"`?
 - [ ] Error
 - [ ] 32
 - [ ] "222"
 - [ ] 6

### if...elif
- Problem 02: which one is the greater number among 5 using `elif`
    ```python
    v=10
    w=20
    x=30
    y=40
    z=50

    if (v>=w and v>=x and v>=y and v>=z):
        print('v is greater')
    elif (w>=x and w>=y and w>=z):
        print('w is greater')
    elif (x>=y and x>=z):
        print('x is greater')
    elif (y>=z):
        print('y is greater')
    else:
        print('z is greater')
    ```
- Creating a simple application (Bkash) using condition
    ```python
    bkash_menu = '''
    1. Send Money
    2. Send Money to Non-Bkash User
    3. Mobile Recharge
    4. Payment
    5. Cash Out
    6. Pay Bill
    7. Microfinance
    8. Download Bkash App
    9. My Bkash
    10. Reset Pin
    '''
    print(bkash_menu)

    choice = int(input("Enter your choice: "))

    print(f'You choose: {choice}')

    if choice==1:
        receiver_number = int(input("Enter receiver number: "))
        if receiver_number:
            amount = int(input("Enter amount: "))
            if amount:
                pin = int(input("Enter pin: "))
                if pin:
                    print(f"{amount} BDT Sent Successful to {receiver_number}")
                else:
                    print("Please enter valid number")
            else:
                print("Please enter valid pin")
        else:
            print("please enter valid number")
    ```
    > Only option 1 implemented

</details>

<details>
<summary>Day-29-Bkash Simple Application using Python</summary>

## Creating a simple application (Bkash) using condition

- Using if..elif..else create an Bkash like application
    ```python
    bkash_menu = '''
    1. Send Money
    2. Send Money to Non-Bkash User
    3. Mobile Recharge
    4. Payment
    5. Cash Out
    6. Pay Bill
    7. Microfinance
    8. Download Bkash App
    9. My Bkash
    10. Reset Pin
    '''
    print(bkash_menu)

    choice = int(input("Enter your choice: "))

    print(f'You choose: {choice}')

    if choice==1:
        receiver_number = int(input("Enter receiver number: "))
        if receiver_number:
            amount = int(input("Enter amount: "))
            if amount:
                pin = int(input("Enter pin: "))
                if pin:
                    print(f"{amount} BDT Sent Successful to {receiver_number}")
                else:
                    print("Please enter valid number")
            else:
                print("Please enter valid pin")
        else:
            print("please enter valid number")
    elif choice==2:
        receiver_number = int(input("Enter receiver number: "))
        if receiver_number:
            amount = int(input("Enter amount: "))
            if amount:
                pin = int(input("Enter pin: "))
                if pin:
                    print(f"{amount} BDT Sent Successful to {receiver_number}")
                else:
                    print("Please enter valid number")
            else:
                print("Please enter valid amount")
        else:
            print("please enter valid number")
    elif choice==3:
        operator = int(input('''
    Choose Operator:
    1. Robi
    2. Airtel
    3. Banglalink
    4. Grameenphone
    5. Teletalk
        '''))
        if operator:
            mobile_number = int(input("Enter mobile number: "))
            if mobile_number:
                recharge_amount=int(input("Enter recharge amount: "))
                if recharge_amount:
                    pin = int(input("Enter pin: "))
                    if pin:
                        print(f"{recharge_amount} BDT Recharge Successful to {mobile_number}")
                    else:
                        print("Please enter valid pin")
                else:
                    print("Please enter valid recharge amount")
            else:
                print("Please enter valid number")
        else:
            print("please choose a valid option")
    elif choice==4:
        merchant_number = int(input("Enter merchant number: "))
        if merchant_number:
            amount=int(input("Enter amount: "))
            if amount:
                pin = int(input("Enter pin: "))
                if pin:
                    print(f"{amount} BDT Payment Successful to {merchant_number}")
                else:
                    print("Please enter valid pin")
            else:
                print("Please enter valid amount")
        else:
            ("Please enter valid number")
    elif choice==5:
        from_whom = int(input('''
    Choose an option:
    1. From Agent
    2. From ATM
    3. Priyo Agent Numbers
        '''))
        if from_whom:
            num= int(input("Enter number: "))
            if num:
                amount=int(input("Enter amount: "))
                if amount:
                    pin = int(input("Enter pin: "))
                    if pin:
                        print(f"{amount} BDT Cash Out Successful to {num}")
                    else:
                        print("Please enter valid pin")
                else:
                    print("Please enter valid amount")
            else:
                print("Please enter valid number")
        else:
            print("please choose a valid option")
    elif choice==6:
        bill_type = int(input('''
    Choose an option:
    1. Electricity (Prepaid)
    2. Electricity (Postpaid)
    3. Gas
    4. Water
    5. Internet & Phone
    6. TV
    7. City Services
    8. Education
    9. Financial Services
    10. Others
        '''))
        bill_number = int(input("Enter bill number: "))
        if bill_number:
            if bill_number:
                amount=int(input("Enter amount: "))
                if amount:
                    pin = int(input("Enter pin: "))
                    if pin:
                        print(f"{amount} BDT Pay Bill Successful to {bill_number}")
                    else:
                        print("Please enter valid pin")
                else:
                    print("Please enter valid amount")
            else:
                print("Please enter valid bill number")
        else:
            print("please choose a valid option")
    ```
    > Only option 1 to 6 implemented

</details>

<details>
<summary>Day-30-Job Portal Project User Profile (02-05-2024)</summary>

## Day 30 Topics
- Job Portal Project recap
- User Profile Model
- User Profile Update
- Recruiter posted job
- Task

### User Profile Model
- In job portal project app directory `models.py`
    ```python
    class CustomUserModel(AbstractUser):
        picture = models.ImageField(upload_to='static/profilePic')
        dob = models.DateField(auto_now_add=True)
        address = models.CharField(max_length=100)
        BLOOD_GROUP=[
            ('a+','A Positive'),
            ('a-','A Negative'),
            ('b+','B Positive'),
            ('b-','B Negative'),
            ('c+','C Positive'),
            ('c-','C Negative'),
            ('ab+','AB Positive'),
            ('ab-','AB Negative'),
            ('o+','O Positive'),
            ('o-','O Negative'),
        ]
        blood_group = models.CharField(choices=BLOOD_GROUP,max_length=100)
        USER_TYPE=[
            ('recruiter','Job Recruiter'),
            ('seeker','Job Seeker'),
        ]
        user_type=models.CharField(choices=USER_TYPE,max_length=100)

        def __str__(self):
            return self.username

    class JobSeekerProfile(models.Model):
        user = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='jobseekerprofile')
        skills=models.CharField(max_length=100)
        work_experience=models.CharField(max_length=100)

        def __str__(self):
            return self.user.user_type

    class JobRecruiterProfile(models.Model):
        user = models.OneToOneField(CustomUserModel,on_delete=models.CASCADE,related_name='jobrecruiterprofile')
        Skills_Required = models.CharField(max_length=200)
        Work_Schedule = models.CharField(max_length=50)
        def __str__(self):
            return self.user.user_type
    ```
    - Here `JobSeekerProfile` and `JobRecruiterProfile` models has `One to One` relationship with `CustomUserModel`
    - In `JobSeekerProfile` and `JobRecruiterProfile`
        - `CustomUserModel` is the model name of the custom user model to make the `One to One` relationship
        - `on_delete=models.CASCADE` is used so that when a user is deleted other info will also deleted
        - `related_name='jobrecruiterprofile'` which will be used in html page to get access; e.g: `{{ user.jobrecruiterprofile.Skills_Required }}`

### User Profile Update
- To update the user profile we will add the `updateprofile` function in `views.py`
    ```python
    @login_required
    def updateprofile(request):
        if request.method == "POST":
            myid = request.POST.get('myid')
            picture = request.FILES.get('picture')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            dob = request.POST.get('dob')
            address = request.POST.get('address')
            blood_group = request.POST.get('blood_group')
            user_type = request.POST.get('user_type')
            
            # seeker info
            seeker_id = request.POST.get('seeker_id')
            skills = request.POST.get('skills')
            work_experience = request.POST.get('work_experience')
            
            # recruiter info
            recruiter_id = request.POST.get('recruiter_id')
            Skills_Required = request.POST.get('Skills_Required')
            Work_Schedule = request.POST.get('Work_Schedule')
            
            print('myid:', myid)
            print('picture:', picture)
            print('first_name:', first_name)
            print('last_name:', last_name)
            print('username:', username)
            print('email:', email)
            print('dob:', dob)
            print('address:', address)
            print('blood_group:', blood_group)
            print('user_type:', user_type)
            print('seeker_id:', seeker_id)
            print('skills:', skills)
            print('work_experience:', work_experience)
            print('recruiter_id:', recruiter_id)
            print('Skills_Required:', Skills_Required)
            print('Work_Schedule:', Work_Schedule)

            if picture:
                user = CustomUserModel(
                    id=myid,
                    picture=picture,
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    dob=CustomUserModel.objects.get(id=myid).dob,
                    address=address,
                    blood_group=blood_group,
                    user_type=user_type,
                    password = CustomUserModel.objects.get(id=myid).password,
                )
            else:
                user = CustomUserModel(
                id=myid,
                picture=CustomUserModel.objects.get(id=myid).picture,
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                dob=CustomUserModel.objects.get(id=myid).dob,
                address=address,
                blood_group=blood_group,
                user_type=user_type,
                password = CustomUserModel.objects.get(id=myid).password,
            )
            if request.user.user_type == "seeker":
                seeker = JobSeekerProfile.objects.get(id=seeker_id)
                seeker.skills=skills
                seeker.work_experience=work_experience
                seeker.save()
            else:
                recruiter = JobRecruiterProfile.objects.get(id=recruiter_id)
                recruiter.Skills_Required=Skills_Required
                recruiter.Work_Schedule=Work_Schedule
                recruiter.save()

            user.save()
            return redirect('profile')
    ```
    - Here We take all the info from the edit page form
    - Then we checked if `picture` is present in user edited one
    - If `picture` is present then we update it otherwise we take those value from previously saved one which we get by `id`
        > We can check it separately for `dob` also but for now we are checking only once
    - Another tricky one is `password`, We have to give the model password otherwise it will store empty in password field in the model; So we assign the user password which we get by `id`
    - Now according to our application there are two types and both type has separate model, to update those we checked the `user_type` then we update it by `id`

### Recruiter posted job
- First create a function to filterout who created the job then we will sent that as dictionary in frontend
    ```python
    def postedjob(request):
        current_user=request.user
        posted_job=JobModel.objects.filter(Created_by=current_user)
        postjobDict={
            'posted_job':posted_job
        }
        return render(request,'postedjob.html',postjobDict)
    ```
- Now in `postedjob` html a for loop will do the rest
- Make sure to add the url name in posted job action button

### Task
- Complete User Profile
- Add Edit action button in user profile
- Complete Recruiter Job posted action button to view all the posted job by that recruiter

</details>

<details>
<summary>Day-31-Job Portal Project Time Challenge (04-05-2024)</summary>

## Day 31 Topics
- Job Portal Project Time Challenge
    - Field Requirement
- Model hidden field/attribute notes

### Job Portal Project Time Challenge
- Challenge: Finish the project within 2 Hours
    > It took around 2 hours for me
- Field Requirement
    - Signup (12 field)
        - Profile Photo
        - First Name
        - Last Name
        - Username
        - Password
        - Confirm Password
        - Age
        - Gender
        - City
        - Country
        - Blood Group (4 types)
        - User types (Recruiter,Seeker)
    - Add Job (11 field)
        - Company logo
        - Job title
        - Job description
        - Job location
        - Requirements
        - Qualifications
        - Job types (Full time, Part time)
        - Workplace (Remote, On-site)
        - Salary
        - Experience
        - Deadline
    - Recruiter Profile (3 field)
        - Company name
        - Company location
        - Recruiter Name
    - Seeker Profile (3 field)
        - Qualification
        - Experience
        - Skills

### Model hidden field/attribute notes
- While working on signup, we have to create the `CustomUserModel` using `AbstractUser`
- While working on Add Job, we have to create the `JobModel` with an extra field `Created_by` which will create relationship with `CustomUserModel` using `ForeignKey`; Make sure to add `on_delete` so that when that user is deleted , it's created job will also get deleted
- While working on Recruiter Profile, we have to create the `RecruiterProfileModel` with an extra field `user` which will create relationship with `CustomUserModel` using `OneToOneField`; In here we also have to add `on_delete` with `related_name`
- Similarly in Seeker Profile, `SeekerProfileModel` will also have `user` field with `OneToOneField` relationship with `CustomUserModel` including `on_delete` and `related_name`
- Now while accessing user data from `CustomUserModel` in html pages, we can use `{{user.field_name_in_model}}`; But while accessing `RecruiterProfileModel` or `SeekerProfileModel` we have to access it through `related_name`: `{{user.related_name.field_name_in_model}}`

</details>

<details>
<summary>Day-32-Job Portal More Profile Info & Template Mastering (05-05-2024)</summary>

## Day 32 Topics
- Job Portal Project Profile
    - More model in profile
    - Connect the Custom user data to other created model while signup
    - Template Mastering in Profile page

### More model in profile
- We will add more model which will be displayed in our profile page, and those model will have `OneToOneField` relationship

- Model for Recruiter
    - `RecruiterBasicInfoModel`
    - `RecruiterContactModel`
- Model for Seeker
    - `SeekerBasicInfoModel`
    - `SeekerContactModel`
    - `SeekerEducationModel`
    - `SeekerWorkExModel`
    > Each model has `OneToOneField` relationship with `CustomUserModel`

### Connect the Custom user data to other created model while signup
- Modify the `signup` function in `views.py` 
    ```python
    def signup(request):
        if request.method=="POST":
            profile_photo = request.FILES.get('profile_photo')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            city = request.POST.get('city')
            country = request.POST.get('country')
            blood_group = request.POST.get('blood_group')
            user_types = request.POST.get('user_types')

            if password==cpassword:
                user = CustomUserModel.objects.create_user(
                    profile_photo=profile_photo,
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    age=age,
                    gender=gender,
                    city=city,
                    country=country,
                    blood_group=blood_group,
                    user_types=user_types,
                )
                if user_types == 'recruiter':
                    RecruiterProfileModel.objects.create(user = user)
                    RecruiterBasicInfoModel.objects.create(user = user)
                    RecruiterContactModel.objects.create(user = user)
                elif user_types == 'seeker':
                    SeekerProfileModel.objects.create(user = user)
                    SeekerBasicInfoModel.objects.create(user = user)
                    SeekerContactModel.objects.create(user = user)
                    SeekerEducationModel.objects.create(user = user)
                    SeekerWorkExModel.objects.create(user = user)
                user.save()
                return redirect('signin')
            else:
                return redirect('signup')
        return render(request,'signup.html')
    ```
    - Here after checking the user type we pass the `user` in `user` of other created model; e.g: `RecruiterProfileModel.objects.create(user = user)`

### Template Mastering in Profile page
- To show the newly created model data we will do template mastering in profile page
    - First separate the current content in a div in another html file
    - `profile.html`
        ```html
        <div class="profile-container">
                <h3>Profile Photo</h3>    
                <div class="profile-photo">
                    <img src="/{{user.profile_photo}}" width="100px" alt="">
                </div>

                {% include 'info_button.html' %}
                
                {% block info %}

                {% endblock info %}
        </div>
        ```
        - Here we also separate the button too 
            > which is not mandatory
        - As it will be our master template for profile so the block content is empty ; now the name of block content is `block info` because we already used the `block content`
    - Now Extend the `profile.html` in the newly created `profiles_info.html` page
    - Make sure to create the `function` and `url` too for this `profiles_info.html`
    - Similarly we created other html pages for showing other model info in a specific block on the `profile.html` page

</details>

<details>
<summary>Day-33-Django Messages (06-05-2024)</summary>

## Day 33 Topics
- Job Portal Project Profile Edit
    - Auto selected of the current one (In select option edit)
- Django Messages
- Task

### Auto selected of the current one (In select option edit)
- We can use the condition inside option tag to auto select the current on in edit page
    ```html
    <label for="lname">Gender</label>
    <select id="country" name="gender">
        <option value="male" {% if user.gender == "male" %} selected {% endif %}>Male</option>
        <option value="female"{% if user.gender == "female" %} selected {% endif %} >Female</option>
    </select> <br> <br>
    ```
### Django Messages
- We can show the user messages after an operation is passed or failed
- Django available messages:
    | Constant | Purpose                                                                                   | Tag     |
    |----------|-------------------------------------------------------------------------------------------|---------|
    | DEBUG    | Development-related messages that will be ignored (or removed) in a production deployment | debug   |
    | INFO     | Informational messages for the user                                                       | info    |
    | SUCCESS  | An action was successful, e.g. “Your profile was updated successfully”                    | success |
    | WARNING  | A failure did not occur but may be imminent                                               | warning |
    | ERROR    | An action was not successful or some other failure occurred                               | error   |

    - Usages:
        ```python
        messages.debug(request, "%s SQL statements were executed." % count)
        messages.info(request, "Three credits remain in your account.")
        messages.success(request, "Profile details updated.")
        messages.warning(request, "Your account expires in three days.")
        messages.error(request, "Document deleted.")
        ```
    - Or we can define a dictionary to organize all the messages
        ```python
        all_messages = {
            ('debug_message' : '%s SQL statements were executed.'),
            ('info_message' : 'Three credits remain in your account.'),
            ('success_message' : 'Profile details updated.'),
            ('warning_message' : 'Your account expires in three days.'),
            ('error_message' : 'Document deleted.'),
        }
        # Now we can use those like this:
        messages.debug(request, all_messages['debug_message'])
        messages.info(request, all_messages['info_message'])
        messages.success(request, all_messages['success_message'])
        messages.warning(request, all_messages['warning_message'])
        messages.error(request, all_messages['error_message'])
        ```
    - Now to show this in html pages, we can create a `messages.html`
        ```jinja
        {% if messages %}
        {% for message in messages %}
            {% if message.tags == 'success' %}
            <p class="message success">{{ message }}</p>
            {% elif message.tags == 'warning' %}
            <p class="message warning">{{ message }}</p>
            {% endif %}
        {% endfor %}
        {% endif %}
        ```
    - Include this `messages.html` in the place where we want to show the message
### Task
- Show the required messages in signup / signin form

### Show the required messages in signup form
- We created a dictionary
    ```python
    all_messages={
        'account_success':'Account create successful!',
        'password_warning':'Password not match',
        'credential_warning':'Account credential not match',
        'age_warning':'age is not valid',
        'first_name_warning':'First Name should only contain letters.',
        'last_name_warning':'Last Name should only contain letters.',
        'username_warning':'Username Already exists',
        'age_warning':'Please put your age in number; e.g: 19',
        'age_warning2':'Your age must be between 18 and 150.',
        'city_name_warning':'City Name not valid',
        'country_name_warning':'Country Name not valid',
        'user_not_found_warning':'Cant find the username',
    }
    ```
    - Now to show any warning from this we can access it like this: `messages.warning(request, all_messages['first_name_warning'])`
- Everytime page get redirect it refreshed and all data erased, so we are rendering it with the preserve data which we get from the form and send it back as dictionary data and showing it in `value attribute` below `signin` function we send the `context` which is preserving the data we get from the form
    ```python
    def signin(request):
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')

            # Preserve form data in the template
            context={
                'username':username,
                'password':password,
            }
            # Check username exist or not
            existing_user = CustomUserModel.objects.filter(username=username).exists()
            if not existing_user:
                messages.warning(request,all_messages['user_not_found_warning'])
            
            user = authenticate(
                username=username,
                password=password,
                )
            if user:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.warning(request, all_messages['credential_warning'])
                return render(request,'signin.html',context)
        
        return render(request,'signin.html')
    ```

</details>

<details>
<summary>Day-34-Python Day 07 & Database Discussion (07-05-2024)</summary>

## Day 33 Topics
- Python Day 7
- Database discussion
### Python Day 7
- Exam 02
- If...else in single line
- Python ternary operation
- While loop

### Exam 02
How would you decrement n by 4 using a shorthand operator?
 - [ ] n -=4
 - [ ] n =- 4
 - [ ] n = n - 4
 - [ ] Both A and C

Which of the following is not a valid Python increment operation?
 - [ ] x += 1
 - [ ] x = x + 1
 - [ ] x++
 - [ ] x +=- 1

What is the output of the following nested condition?
```python
x = 5
y = 10
if x > y:
    if x > 10:
        print("A")
    else:
        print("B")
else:
    if y < 20:
        print("C")
    else:
        print("D")
```
 - [ ] A
 - [ ] B
 - [ ] C
 - [ ] D

Choose the correct way to declare a variable x with the value 100.
 - [ ] int x = 100
 - [ ] x = 100
 - [ ] var x = 100
 - [ ] x == 100

```python
if not False:
    print("Hello World")
else:
    print("Goodbye World")
```
 - [ ] Hello World
 - [ ] Goodbye World
 - [ ] Nothing, it's an error
 - [ ] Both A and B

Which condition will be true when $x = 3$ and $y = 5?$
```python
if x > y:
    print("X")
elif y > x:
    print("Y")
else:
    print("Equal")
```
 - [ ] X
 - [ ] Y
 - [ ] Equal
 - [ ] NONE

```python
x = 4
x *= 2
```
 - [ ] 8
 - [ ] 2
 - [ ] 6
 - [ ] 4

```python
x = 4
y = 15
print(x % y)
```
 - [ ] 4
 - [ ] 11
 - [ ] 3
 - [ ] 0

What is the output of the following code if $a = 10$ and $b = 20?$
```python
if a > b:
    print("A is greater")
elif b > a:
    print("B is greater")
else:
    print("A and B are equal")
```
 - [ ] A is greater
 - [ ] B is greater
 - [ ] A and B are equal
 - [ ] None of the above

Evaluate the following logical expression when x = True and y = False:
```python
if x and not y:
    print("True")
else:
    print("False")
```
 - [ ] True
 - [ ] False
 - [ ] Error
 - [ ] None

```python
a = 5
a *= 2
```
 - [ ] Subtracts 2 from a
 - [ ] Adds 2 to a
 - [ ] Divides a by 2
 - [ ] Multiplies a by 2
 - [ ] Other:___________

Which operator is used for integer division that discards the remainder?
 - [ ] **
 - [ ] //
 - [ ] /
 - [ ] %

```python
a = 8
b = '4'
print(a + b)
```
 - [ ] 8'4'
 - [ ] 12
 - [ ] 84
 - [ ] Error

If $a = 10$, what is the value of a after $a //= 3?$
 - [ ] 3
 - [ ] 3.33
 - [ ] 7
 - [ ] 4

print(2 + 3 * 4)
 - [ ] 20
 - [ ] 14
 - [ ] 5
 - [ ] 24

### If else in single line
- We can write if..else in single line
    ```python
    a=300
    b=100

    if a>b:print("a is greater") else: print("b is greater")
    ```

### Python ternary operation
- Which is greater between a,b 
    ```python
    a=300
    b=100

    print("a is greater")if a>b else print("b is greater")
    ```
- Which is greater between a,b,c
    ```python
    a=100
    b=200
    c=300

    print("a greater")if (a>b and a>c) else print("b is greater") if b>c else print("c is greater")
    ```
- Which is greater between a,b,c,d
    ```python
    a=100
    b=200
    c=300
    d=400

    print("a is greater") if (a>b and a>c and a>d) else print("b is greater") if b>c and b>d else print("c is greater") if c>d else print("d is greater")
    ```
- Which is greater between a,b,c,d,e
    ```python
    a=100
    b=200
    c=300
    d=400
    e=500

    print("a is greater") if (a>b and a>c and a>d and a>e) else print("b is greater") if b>c and b>d and b>e else print("c is greater") if c>d and c>e else print("d is greater") if d>e else print("e is greater")
    ```

### While loop
- It will run until the condition is false
    ```python
    i=1
    while i<6:
        print(i)
        i+=1
    ```

### Database discussion
- Field (Table head)
- Object (Table data)
- Query (SQL Query)
- ORM vs SQL query
    - ORM :arrow_right: `model_name.objects.get(id=id)`
    - SQL :arrow_right: `SELECT * FROM table_name WHERE id = 1;`
- Entities and Attributes
    | Entities |              Attributes                        |
    |----------|------------------------------------------------|
    |Student   | Student_ID (Primary Key), Name, Age, Gender    |
    |Book      | ISBN (Primary Key), Title, Author, Publish_Date|
    |Employee  | Employee_ID (Primary Key), Name, Department    |

</details>