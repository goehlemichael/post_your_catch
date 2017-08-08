# Post Your Catch

## What is "Post Your Catch"?

 Post your catch is a service for selling freshly caught fish
 
## How does "Post Your Catch" work?

 Post your catch is a listing where you can list any fish you would like to sell locally. It works similar to "craigslist", however listings do not stay longer than a day.
 
## Why would someone want to use "Post Your Catch"?

Anyone who would like to sell legally caught fish can post their fresh catch. This enables buyers to contact them and offer a price

## When will Post Your Catch be ready for use?

Currently this web application is under development and not ready for production. There will be mobile applications that work with the main web service. these mobile applications will make it easier to post your catch on the web service.

## Development Setup (for contributing to the source code)

Uses Flask-Security (https://pythonhosted.org/Flask-Security/) with Flask-Admin using the SQLAlchemy backend. 

I suggest using virtualenv for development

(https://virtualenv.pypa.io/en/stable/installation/)

1. Clone the repository::

     git clone https://github.com/goehlemichael/post_your_catch.git
     cd post_your_catch

2. Create and activate a virtual environment::

     virtualenv venv
     source venv/bin/activate

3. Install requirements::

     pip install -r 'requirements.txt'

4. Run the application::

     python app.py

The first time you run this example, a sample sqlite database gets populated automatically. To suppress this behavior,
comment the following lines in app.py:::

     if not os.path.exists(database_path):
         build_pyc_db()

The default admin login/password is admin/admin
