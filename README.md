# Booking website built in Django

A booking system created in Django, this can be used to hire out cars, campervans, tools, movie props, whatever you decide.

## Getting started

1. Clone this repo using your preferred method or follow the steps below.

### Cloning a repo

    1.1. Click 'Code' at the top of this repo
    1.2. Copy the URL
    1.3. If you would prefer to clone it using SSH, select the SSH tab instead and copy the URL
    1.4. On your computer open Git Bash. Change the directory to the folder where you would like to run the cloned directory and then type 'Git clone'. Paste the URL you copied from my repository in GitHub. Press enter and your local clone of my site will be created.

    Make sure you have a secret key saved in your IDE's settings before opening the repo

2. Once you have the repo open in your IDE, install requirements with pip:

            pip3 install -r requirements.txt

3. Run the initial migrations with:

            python3 manage.py migrate

4. If you have data to load, add the JSON files to the 'Vans' folder and laod them in with:

            python3 manage.py loaddata <your_file_name>
        
5. To create a superuser you can use in development type the command:

            python3 manage.py createsuperuser

Follow the prompts to set up your superuser.

6. To view the live preview of the site in development, use the command: 

            python3 manage.py runserver

7. To set up AWS for file hosting follow these instructions:

I used Amazon S3 to host images and fixtures. These are the steps I took and the steps you can take when cloning my site:

Create an Amazon AWS account
Create a bucket within your account
Attach a CORS policy
Attach a bucket policy
In IAM create a new user group
Attach an S3 bucket policy to your user group and set the permissions to only allow access to your project bucket
Create a new user and add to the group you created before
Download the access key file and keep it safe, you will not be able to download it again.
Add the settings to your IDE

8. To set up Stripe follow these instructions.

## Features

- Instagram feed - created with the API from Instagram: https://developers.facebook.com/docs/instagram-basic-display-api


## Technologies used

- 
- Pandas - for data manipulation, specifically the date ranges provided.