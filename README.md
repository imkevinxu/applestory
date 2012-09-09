Applestory
================

Auto-generated from [imkevinxu](https://github.com/imkevinxu)'s [Django Project Builder](https://github.com/imkevinxu/django-projectbuilder)

### Development Team

* Kevin Xu <kevin@imkevinxu.com>
* Katherine Chen <katherine.l.l.chen@gmail.com>
* Viraj Bindra <viraj.s.bindra@gmail.com>

## Getting Started

### Dependencies

For best results, make sure you have at least:

* Python 2.7.2
* Django 1.4.1

### Installing the Application

    # after initial git clone of existing repo
    cd applestory/
    mkvirtualenv applestory                                           # requires proper virtualenv setup
    workon applestory                                                 # sets the virtual environment

    pip install -r requirements.txt                                   # installs all python packages
    python manage.py syncdb                                           # sets up django database
    python manage.py migrate applestory_app                           # migrates any south migrations

## Troubleshooting

### Workflow

In case something's not working after pulling, try one of these:

    workon applestory                                                 # make sure you're in the right virtual environment
    pip install -r requirements.txt                                   # make sure python packages are up to date
    python manage.py migrate applestory_app                           # make sure database schema is migrated

### Missing Dependencies

If you are missing some dependencies like `pip`, `django`, `virtualenv`, or`virtualenvwrapper`
then try downloading and running this [script](https://github.com/imkevinxu/django-projectbuilder/blob/master/install_dependencies.sh) or use this line of code:

    curl -O https://raw.github.com/imkevinxu/django-projectbuilder/master/install_dependencies.sh && source install_dependencies.sh && rm -f install_dependencies.sh

Script has only been tested with Mac OSX 10.7 Lion so far.