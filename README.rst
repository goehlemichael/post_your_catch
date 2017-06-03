Uses Flask-Security (https://pythonhosted.org/Flask-Security/) with Flask-Admin using the SQLAlchemy backend. 

Currently has:

the 'login' & 'register' views


1. Clone the repository::

     git clone https://github.com/goehlemichael/post_your_catch.git
     cd post_your_catch

2. Create and activate a virtual environment::

     virtualenv venv
     source env/bin/activate or . venv/bin/activate

3. Install requirements::

     pip install -r 'requirements.txt'

4. Run the application::

     python app.py

The first time you run this example, a sample sqlite database gets populated automatically. To suppress this behavior,
comment the following lines in app.py:::

     if not os.path.exists(database_path):
         build_sample_db()
