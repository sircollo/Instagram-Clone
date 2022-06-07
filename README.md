# instgram-clone
## Author
[Collins Sirwani](https://github.com/sircollo)

## Description
This is a clone of instagram website built using Django Framework

### Prerequisites
You need to install the following:
```
  Django - 4.0.4
  Virtual Environment
```

### Installation
```
  -Git clone https://github.com/sircollo/Instagram-Clone

  -cd Instagram-Clone

  -install virtual env

  -pip install -r requirements.txt

  -python3.8 manage.py runserver

```
## Technologies Used

  * Python3.8
  * Django 4.0.4
  * Bootstrap
  * PostgreSQL
  * CSS
  * Heroku

## Running tests
```
  -python3.8 manage.py test instagram
```

### Breakdown of tests
Unittest to test model classes methods like save, update and delete. e.g
```
  def test_save_method(self):
    self.image.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)
```
The above tests if an image instance can be saved.

## User Story
A user can:

  * Sign in to the application to start using.
  * Upload pictures to the application.
  * See his/her profile with all my pictures.
  * Follow other users and see their pictures on the timeline.
  * Like a picture and leave a comment on it.

## BDD
Feature: Test add new user to database

Scenario: A new user can input registration details and login using the details

  Given I am a new user and on the register page

  When I add my user information and click 'Sign Up' button

  Then I am redirected to login page

  Then I input my login details

  Then I click sign in

  Then I can use the application

### Deployment
Read here on how to [Deploy](https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0)


### Preview

[Live Link](https://insta-kram.herokuapp.com/)


### License

[MIT License](https://github.com/sircollo/Instagram-Clone/blob/master/license)

Copyright (c) 2022 Collins Sirwani
