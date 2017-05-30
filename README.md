## Post Your Catch

using Flask on virtual environment

    sudo pip install virtualenv
    cd ~(where you pulled repo)
    virtualenv venv
    . venv/bin/activate
    pip install Flask
    pip install Flask-SQLAlchemy
    python
    from main import db
    db.create_all()

    python main.py
