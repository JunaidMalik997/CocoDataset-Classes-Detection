# OBJECT DETECTION USING COCO DATASET PRE_TRAINED MODEL
Flask Machine Learning Model Deployment 


# COCO DATASET:

The MS COCO (Microsoft Common Objects in Context) dataset is a large-scale object detection, segmentation, key-point detection, and captioning dataset. The dataset consists of 328K images containing 80 Classes.

# Pre-Trained Model:

COCO Dataset has a pre-trained model that is able to detect all 80 classes present in it. To download the pre-trained model click the link below:

https://pjreddie.com/media/files/yolov3.weights

Config file is provided in the repository.

# How to run the Code:

Create a separate Virtual Environment, and download all the packages given in `requirements.txt` using `pip`.

Run `app.py` file which contains Flask Code. It contains all the necessary imports, after running it you will be able to run this Flask web app in your local computer. After running the app the main page should look as follows: 

![mainpage](https://user-images.githubusercontent.com/58310295/142594355-b04031e7-9fbd-4590-a047-a25684d5f522.JPG)

The classes page should look as follows:

![classpage](https://user-images.githubusercontent.com/58310295/142604768-596cca95-01c0-4ade-9dd9-bfc3dc92dfb3.JPG)
 
To check the detection code open `files` folder and open `testmain.py` file. `Pre-trained model`, `config files` and `coco.names` file paths is to be placed inside it.

# Model Deployment on Heroku:

The ultimate goal of any Machine Learning Model and as a matter of fact every web application is deployment from Development environment to Production Environment so that the users can use it in an interactive way. In a similar way this Pre-trained Model alongwith the web app is deployed on Web using Heroku. 

To deploy this Model, we make use of Heroku CLI and Gitbash. To deploy the web app create an account on Heroku, which is a cloud application platform:

https://www.heroku.com/

Download Heroku CLI using the following link

https://devcenter.heroku.com/articles/heroku-cli

Download Git using the following link

https://git-scm.com/download/win

## Step 1

Open `Gitbash` terminal. Go to the project directory and activate the Virtual Environment by using the following command:

`source venv/Scripts/activate`

## Step 2

Install `gunicorn` using `pip install gunicorn`

Now we need to let Heroku know that we are using gunicorn, so we create a file called a `Procfile` using following command

`touch Procfile`

A Procfile will be created inside project folder. Write the following line inside it:

`web: gunicorn app:app`

## Step 3

We also need to let Heroku know all other requirements in our app. So we need a `requirements.txt` file. To generate this file, type the following command on Gitbash terminal

`pip freeze > requirements.txt`

A requirements.txt file will be generated inside the project folder. This contains all the packages that we pip installed for our project.

## Step 4

To push the code to Heroku for deployment it should be in the form of Git repository. To do it, we do the following

`git init`

It creates a Master branch i.e. an empty git repository. To put all the code to the repository run the following command:

`git add .`

Now, we need to commit it to the repositry. We added it, now we need to save it. To do it run:

`git commit -am 'initial commit'`

## Step 5

Login to Heroku Account, using:

`heroku login`

If you don't have an account, create an account on Heroku and then login.

## Step 6

Now to create the app on Heroku run:

`heroku create`

To rename the website run:

`heroku rename your-website-name`

## Step 7

Now as a final step we need to push our code to heroku. To do this, run the following command:

`git push heroku master`

Reload the page, and magic!! Our website is live on the web.

# Visit Website:

Visit my website, using the following link:

https://object-detection-coco.herokuapp.com/

Upload any image, containing 80 classes of COCO dataset and you will get Object Detection on the go. The output image is stored in the cloud, form where you can view it in full size and download it.

# Website Constraints:

1. If you upload any image, that doesn't contain any of those 80 classes, the program will crash. I am trying to fix it as soon as possible.

2. Images greater than 1 MB are not accepted.

3. Allowed Image types are jpg, jpeg, png and gif

# Demo Video:

https://user-images.githubusercontent.com/58310295/142611566-e1ab5877-8f52-44b5-9988-a8824802fb07.mp4



