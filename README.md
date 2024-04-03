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
### Show table data dinamically using dictionary
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
<summary>Day-13-View Action & All Model Table Data in Single Page (31-03-2024)</summary>

## Day 13 Topics:-
- Security & code editor
- Python Basics
- Variable
- View Action 
- Task

### Security & code editor
Compiler / Interpreter -->Translator (Python has both)

- Interpreter--> (line by line)
- Compiler--> (Run at once)
- Security (csrf,session-hijack,man in the middle attack,vulnerability)
- Authentication

### Python Basics
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
