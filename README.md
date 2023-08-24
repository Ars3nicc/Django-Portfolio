# Personalized e-Portfolio Website V2

### Created in 2022 by Franz Manrique
Developed purposely for displaying and showcasing the author's profile, details, and working projects. The portfolio website is used solely for professional purposes such as **portfolios** and **job applications**. No particular frameworks and other backend features included. Just pure HTML and simple designs. Enjoy viewing! 

## What's new with E-Portfolio V2?
Integrated smooth backend streamlining and pipelines, polished and rendered using Django framework. This version of portfolio can now explicitly use Python structures such as modelling data and emerge WebSockets and GraphQL, this also renders css without glitches. For example, hovering a particular component will now reset or become too "buggy".

### TO DOs:
1. Improvise javascript rendering
2. Configure backend pipeline
3. ~~Streamline email notification and request~~
4. Configure `commission page` and enable backend services
5. Implement WebSocket for end-to-end chat messages
6. Partially implement machine learning for automated website interactions.
7. Implement React components for front-end UI/UX design.
8. Initiate cookies and tokens

## Features
> Portfolio components which includes particular features that enables an interactive approach to the design interface.
### Email request using SMTP
SMTP (or Simple Mail Transfer Protocol) is the communication network layer that sends and receives email. Just as the HTTP (Hyper Text Transfer Protocol) handles app-related data traffic (the pages that load over the web when you a visit a website), SMTP handles email traffic.
![SMTP Concept Map](https://global-uploads.webflow.com/5ebea55066f36f531dec5b32/64cc4a7945d018fd927a9d88_2.webp)

>Additional implementation for email request
We need to modify the settings file in order to make sending emails work in Django, this can be imported to the `settings.py`.

Paste the following lines to your settings file
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_username@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
```



# How to run application
> Follow the simple steps below to build the necessary libraries and components for the application.

Install virtual environment
```
virtualenv env
// Navigate to the specific directory to activate env
.\env\scripts\activate
```
Migrate the local database
```
python manage.py makemigrations
python manage.py migrate
```
Run the Django local server
```
python manage.py runserver
```




## For any other informations or inquiry, send me an email
>Primary email address
`franzmanrique2121@gmail.com`
>Secondary email address
`frm.manrique@gmail.com`