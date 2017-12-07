# The Cleveland Tech Survey

Cleveland is a special place. Lots of the information provided by survey-type sites (Glassdoor, Stack Overflow, etc.) doesn't seem to accurately represent Cleveland. So the Cleveland Tech Survey is an attempt to help us learn more about what it's like to work in tech in Cleveland.

Pull requests are welcome!

## Development

To run the application locally using a bare debian / ubuntu box (likely OSX too), make sure you have python-2.7.14 and pip installed.

Install the pip requirements:

```sh
$ pip install -r requirements.txt
```

Start the server:

```sh
$ python manage.py runserver
```` 

or just run it in docker:

```sh
$ docker build -t tech-survey .
$ docker run -it -name tech-survey -p 5000:5000 tech-survey
```