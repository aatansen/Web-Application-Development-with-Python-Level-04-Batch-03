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

### Task : 
- Poster presentation based on Day 01 to Day 06
- Oral test tommorow (25-03-2024)

</details>