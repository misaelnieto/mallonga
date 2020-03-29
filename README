# Mallonga - Noe's url shortener

Hello, this repo contains a Django app that implements the logic of a very
simple url shortener. I wrote this as a part of a job interview, so this was an
excellent oportunity to hone my skills with TDD, BDD and GitHub Actions.

## For users of the demo

If you want to use the demo site, just go to http://xxx.li and paste some url on
the form and hit the submit button.

These are the decision, tools and/or skills I used to develop this application:

* Sigh ... **Four days**. It took me that long to write it.
* **Short code algorithm**: Currently, a 8 digit string is being generated
  randomly, this gives us around 2.8 billion different codes. I researched a bit
  and we could use a [FNV
  hash](https://en.wikipedia.org/wiki/Fowler_Noll_Vo_hash). [This
  guy](https://anandjoshi.me/articles/2016-10/URL-Shortening) implemented it
  into [a small Django
  application](https://github.com/anandjoshi91/url-shortener/blob/master/shorturl/smallify/models.py).
  There's also the `short_url` package [available on
  PyPI](https://pypi.org/project/short_url/). I ended up not implementing any of
  these two. We can do that later.
* **Visual Studio**. I'm a bit ashamed to say this, but it's a beautiful generic
  editor/IDE. Even better than Sublime.
* **Malonga** means *short* in
  [Esperanto](https://en.wikipedia.org/wiki/Esperanto). I guess the right word
  to use would be: *malongilo* (*-ilo* means tool)
* **TDD First**. I really could do it. Models, views, templates, fixtures and so
  were written after the tests. As of now I'm really proud of it. I did this in
  several steps; take a look at the commits if you want to see what these steps
  look like.
* [Pipenv](https://pipenv.readthedocs.io/en/latest/). I never liked the
  `requirements.txt` thingie anyway.
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): I could write
  all the application with only one extra library. I had to pull the title page
  of the shortened url and I could have used python's HtmlParser, but I felt a
  bit lazy, so I just pulled `BeautifulSoup` and called it a day.
* You can check the demo [on this link](...). If you are curious what type of
  server I'm using, I'll let you know the server is
  [opalstack](https://www.opalstack.com/) (written by some guys who used to
  workfor webfaction). So no fancy serverless or Heroku, sorry to dissapoint.
* **Plain Django** for testing. No `pytest` nor `tox` this time.
* **Github actions** to automate tests whatnot. It's a WIP, though.

## Installation on your server

* Clone this repo.
* [Install](https://pipenv.pypa.io/en/latest/install/#installing-pipenv) Pipenv
* `cd` into the repo, run `pipenv install`.
* Now configure `mallonga` as a `wsgi` app for your server. Take a look at the
  Django documentation [on how install a Django
  app](https://docs.djangoproject.com/en/3.0/intro/install/) for different
  approaches.
  * Database: As a demo, the application can run with a SQLite database.
  * No configuration for static files is needed.
  * No configuration for media files is needed as well.
  * Configure the cron job for 


## Install locally

* Clone this repo.
* Make sure you have Pipenv installed.
* `cd` into the repo, run `pipenv install`. To install the development tools also run: `./pipenv install --dev`
* Create the database with `./manage.py migrate`.
* Launch the development server: `./manage.py runserver` and load http://localhost:8080/ on your browser.
* To run the tests: `manage.py test`.
* To run coverage: ???
* To run pep8 and pylint??
* To populate the DB with some data run: `./manage.py loaddata --app shortener links`

## TODO

[ ] There must be a background job that crawls the URL being shortened, pulls the <title> from the website and stores
it.

