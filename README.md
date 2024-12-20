# VITTLER Recipe Book by Matt Cowen


![Vittler Responsive Image](/static/images/readme/amiresponsivetest.png)

This is a full-stack framework project built using Django, Python, HTML and CSS. My goal is to create a functioning and responsive website for recipe sharing. This project has been built for educational purposes.

**[Visit my website](https://vittler-2d3fb1b45f48.herokuapp.com/)**  
  

# Overview

Eating is easy. Decisions are hard. Vittler aims to provide a provide an all-inclusive service to help you choose what to cook, how to cook it, and organise
your recipes in an easily editable personal recipe book. Whether you're a stay at home parent or a bodybuilder (or both!), Vittler allows you to search for and collect recipes
to suit your tastes!

# Table of Contents

1. [UX](#ux)
    - [User Stories](#user-stories)

2. [Scope](#scope)
    - [Site Features](#site-features)
    - [Future Features](#future-features)

3. [Wireframes](#wireframes)

4. [Database schema](#database-schema)

5. [Structure](#structure)
    - [Models](#models)

6. [Surface](#surface)
    - [Colour Scheme](#colour-scheme)
    - [Fonts](#fonts)

7. [Technologies Used](#technologies-used)

8. [Testing](#testing)

9. [Deployment](#deployment)

10. [Credits](#credits)


# UX

The UX was developed with the target user in mind. The target is a wide net, and as such the UX had to be accessible and
attractive to a wide range of user.


The users will be looking for:

- An easy to navigate site, with clear signposting for browsing, uploading and saving recipes
- The ability to sign up to add and save recipes.
- The ability to collect recipes that they like into their own dedicated recipe book.
- the ability to edit and recipes that they have submitted.


The site admin will be looking for:

- an easy and intuitive way of managing content and users on the site.


## User Stories


- As a Site Admin, I will be able to manage all aspects of submitted recipes.
- As a Site Admin, I can approve or disapprove recipes so that I can filter out repeat/incomprehensible recipes.
- As a site admin, I can manage users.



- As a Site User I can browse all available recipes.
- As a Site User I can view the contents of the recipes in a pop-out modal.
- As a Site User I can modify or delete my recipe if I have made a mistake or angered my grandmother.
- As a Site User I can view a paginated list of recipes so that I can select which view in greater detail.
- As a Site User I can search the full list of available recipes so I can locate specific recipes.
- As a Site User I will see a home page so I will know what the site offers.
- As a Site User I can easily navigate to login, register, library and recipe book pages.
- As a Site User I can register an account so that I can submit recipes to the library, and store select recipes in my Recipe Book.
- As a Site User I can log in/out off my account if I wish so that I can connect or disconnect from the website.


![Kanban Board](/static/images/readme/kanban.png)
*Project kanban board*

#
# Scope

## **Site Features**

1. **Navigation Bar**
- The navigation bar appears on every page so users can easily navigate through the site. It adds an active class to the current url for better UX.
- Navigation bar has links for "Home", "Recipe Library", "Register" and "Login" when there is no logged in user.
-  Navigation bar has links for "Home", "Recipe Library", "My Recipe Boook", "Add Recipe" and "Logout" when a user is logged in.
- If the user is logged in then their username will appear on the right hand side of the nav bar.
- The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size.


![NavBar](/static/images/readme/navbar.png)

---

2. **Footer**
The footer, present on all pages, comprises of copyright information on the left hand side, and social links on the right.

![Footer](/static/images/readme/footer.png)

---

3. **Landing Page**
The landing page offers a simple hero section with a call to action to either start viewing recipes (available to both logged in and non-registered users) or to sign up (only displays if user is not logged in).

![Landing Page Logged Out](/static/images/readme/homepageloggedout.png)

![Landing Page Logged In](/static/images/readme/homepageloggedin.png)

---

4. **Recipe Library Page**
The recipe library page offers a paginated view of all recipes within the recipe library, presented in card format, popping out to full detail in a modal. If the user is logged in, they are offered the ability to add recipes to their Recipe Book. If they are logged in and the recipe is one they have submitted to the site, they have the option of editing or deleting the recipe within the full info view. The edit functionality allows them to edit the recipe right there in the modal.

![Recipe Library Page](/static/images/readme/recipelibrary.png)

![Recipe Library Search](/static/images/readme/recipesearch.png)

---

5. **My Recipe Book Page**
The My Recipe Book page offers a paginated view of all of the recipes that the logged in user has added to their recipe book from the recipe library. It gives them the option of viewing the recipe details in a pop out modal, and to remove the recipe from their recipe book. This view was modelled directly on the recipe library page.

---

6. **Add Recipe Page**
The Add Recipe page provides a simple form for users to submit their own personal recipes to be displayed in the recipe library.

![Submit Recipe Page](/static/images/readme/submitrecipe.png)

---

7. **Login Page**
- The Login page allows users to log in. It is also generated by allauth and styled using crispy forms.

![Submit Recipe Page](/static/images/readme/loginpage.png)

---

8. **Logout Page**
- The Login page asks users to confirm they wish to log out. It is also generated by allauth and styled using crispy forms.

---

9. **Register Page**
- The register page allows users to create a new account by providing necessary information such as username, email, password. It is generated by allauth and styled using crispy forms.




## **Future Features**

The original scope was to include bot meal planning and comment/rating functionality to the site, but I decided this was far above and beyond the necessary requirements for this project.


# **Wireframes**

All wireframes were created using [Balsamiq](https://balsamiq.com/).

---

![Landing Page Wireframe](/static/images/readme/balsamiqhomepageloggedin.png)
*The landing page*

---

![Library Page Wireframe](/static/images/readme/recipebookwireframe.png)
*The recipe library page*

![Library Page Wireframe With Modal](/static/images/readme/Recipebookwireframepopup.png)
*The recipe library page with modal*

---

![SignUp Page Wireframe](/static/images/readme/balsamiqsignup.png)
*The sign up page*

---

![Login Page Wireframe](/static/images/readme/balsamiqlogin.png)
*The log in page*

---


# **Database Schema**

Before I set to migrating any models to my database, I created an entity relationship diagram to help me see how the models would link together. As both Meal Planning and Comments/Ratings ended up as a future feature, the models to provide this functionality did not get used.

The entity relationship diagrams were created using [dbdiagram.io](https://dbdiagram.io/).

![ERD Diagram](/static/images/readme/dbdiagram.png)


## **Models**

### **Recipe Model**

![Recipe Model](/static/images/readme/recipemodel.png)

---

### **MyRecipes Model (displayed in ERD as recipe_book)**

![MyRecipes Model](/static/images/readme/myrecipemodel.png)


# **Surface**

## **Design**

I wanted the website to have a clean and functional design, with clear calls to action.

## **Colour Scheme**

The colour scheme was developed as the site evolved, and came to complement the generated logo for Vittler. It aims to convey natural ingredients, and the simplicity of a home-made recipe book.


## **Fonts** 

I opted for two free license font from Google fonts:

- [Montserrat](https://fonts.google.com/specimen/Montserrat) -Clear and direct, used for Hero Text
- [Quicksand](https://fonts.google.com/specimen/Quicksand) - A little more informal font, to add to the feeling of a personal recipe book. Used for the rest of the site.


# **Testing**

## **Code Validation**

### **HTML**

![HTML Validation](/static/images/readme/htmlvalidatepass.png)
*The HTML for the landing page, the submit recipe page, and all authentification pages passed validation with no errors.*

![HTML Validation Bug](/static/images/readme/htmlvalidationbug.png)
*The HTML for the Recipe Library and My Recipe Book pages threw up a lot of errors (several for each recipe), as the automatic formatting of crispy forms gives an ID to each of the fields in the form. As this form is iterated over within a tuple for each of the recipes, this means that there are duplicated IDs for each of these fields. As none of the rest of the code references these IDs for functionality, this has been registered as a known bug.*

### **CSS**
![CSS Validation](/static/images/readme/csstest1.png)
*The CSS passed a vildation service with no errors.*

### **JS**
![JS Validation](/static/images/readme/JSHinttest.png)
*The JavaScript passed through a linter with no errors.*

## **Manual Testing**

All responsiveness and basic functionality of the site was tested manually, and ran into no issues.

## **Unit Testing**

I wrote a suite of tests to test a select few aspects of my python code:

### **Forms**
![Form Test](/static/images/readme/unittestform.png)

*These tests confirm that with the correct data a form can be submitted, and without required data, cannot.*

### Views
![Views Test pt1](/static/images/readme/unittestviews1.png)

*This displays the test objects to be used for these tests*

![Views Test pt2](/static/images/readme/unittestviews2.png)

*This displays tests to confirm that the recipe_list view works correctly, the search returns the correct data and that recipes can be added and removed from my_recipes*

### Tests passed:
![Unit Tests Pass](/static/images/readme/unittestspass.png)

*All tests passed!*


## Known Bugs

 - Duplicated IDs as a result of iterating cripsy forms.

# **Deployment**

The site was deployed on Heroku and connected to GitHub for version control. This was done by following the below steps:

- Log in to GitHub and create a new repository, using the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template).
- Sign up for Heroku and create a new account.
- Create a new app and choose a suitable region for deployment.
- In the app settings, go to config vars and click "reveal config vars".
- The app requires configuration for the following variables: SECRET_KEY, DATABASE_URL, CLOUDINARY_URL. Assign the corresponding values from your project's env.py to these variables.
- Integrate Heroku with your GitHub by choosing the GitHub integration option in Heroku.
- Locate and select the GitHub repository you created earlier from the CI template.
- Choose manual deployment from the selected branch of your GitHub repository.
- Deploy by clicking the manual deploy button.
- Once deployed, the site is accessible through the live link provided at the top of the document.


# **Technologies Used**

## **Languages**
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)

## **Frameworks, Libraries and Programs**

- [GitHub](https://github.com/) - GitHub is a web-based platform for version control using Git, enabling collaborative software development and hosting of code repositories. GitHub connects to GitPod and Heroku.
- [GitPod](https://gitpod.io/workspaces) - Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository.
- [Heroku](https://www.heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilized/tested.
- [Django](https://www.djangoproject.com/) - Django is a high-level web framework for building web applications rapidly with a clean and pragmatic design.
- [ElephantSQL](https://api.elephantsql.com) - ElephantSQL is a hosted PostgreSQL database service that can be seamlessly integrated with Django applications, providing scalable and reliable database solutions.
- [Gunicorn](https://gunicorn.org/) - Gunicorn is a pure-Python HTTP server for WSGI applications.
- [Dj Database URL](https://pypi.org/project/dj-database-url/) - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- [Bootstrap](https://getbootstrap.com/) - Bootstrap is a front-end framework for developing responsive and mobile-first websites quickly and efficiently.
- [Cloudinary](https://cloudinary.com) - Cloudinary is a cloud-based media management platform that offers solutions for storing, optimizing, and delivering images and videos for web and mobile applications.
- [Psycopg2](https://www.psycopg.org/) - Psycopg is a PostgreSQL adapter for the Python programming language, providing a robust and efficient interface to interact with PostgreSQL databases.
- [Summernote](https://summernote.org/) - Summernote is a Django app that enables users to easily integrate a rich text editor into their web applications, enhancing event creation and description functionality.
- [Django-allauth](https://www.intenct.nl/projects/django-allall/) - A comprehensive authentication app for Django, supporting social authentication, registration, and account management.
- [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Django Crispy Forms is a Django app that provides a better way to generate forms in your Django application.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) - WhiteNoise allows your web app to serve its own static files, making it simpler to deploy on services like Heroku.
- [Font Awesome](https://fontawesome.com/) - Font Awesome is a library of scalable vector icons that can be easily customized and used to enhance the visual appeal of websites and applications.
- [Balsamiq](https://balsamiq.com/) - Balsamiq is a wireframing tool used for creating low-fidelity mockups of user interfaces, allowing for quick and easy visualization of design ideas.
- [Am I Responsive](http://ami.responsivedesign.is/) - Am I Responsive is a web tool that allows users to quickly preview how their website appears on various devices and screen sizes, helping to ensure responsiveness and compatibility across platforms.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - The W3C CSS Validator is a tool used to check the validity and syntax of CSS code, ensuring compliance with web standards set by the World Wide Web Consortium (W3C).
- [W3C Markup Validator](https://validator.w3.org/#validate_by_input) - The W3C Markup Validator is a tool used to check the validity and syntax of HTML code, ensuring compliance with web standards set by the World Wide Web Consortium (W3C).
- [JSHint](https://jshint.com/) - JSHint is a static code analysis tool used for checking JavaScript code for errors, potential problems, and stylistic inconsistencies.
- [Pep8ci](https://pep8ci.herokuapp.com/) - Pep8ci provides Python developers with a tool to check their code against the PEP 8 style guide for adherence to coding standards.


---

The full list of requirements for the project along with versions can be seen below.
  
- asgiref==3.8.1
- cloudinary==1.36.0
- crispy-bootstrap5==0.7
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==4.2.7
- django-allauth==0.57.0
- django-bootstrap-v5==1.0.11
- django-crispy-forms==2.1
- django-multiselectfield==0.1.13
- django-summernote==0.8.20.0
- gunicorn==20.1.0
- oauthlib==3.2.2
- psycopg2==2.9.6
- PyJWT==2.8.0
- python3-openid==3.2.0
- requests-oauthlib==1.3.1
- sqlparse==0.5.2
- urllib3==1.26.20
- whitenoise==5.3.0

# **Credits**

## **Tech Support**

- [W3Schools](https://www.w3schools.com/) - Used to help understand certain aspects of python.

- [Stack Overflow](https://stackoverflow.com/) - Used to detrmine whether other people have already figured out issues I was running into!

- [ChatGPT](https://openai.com/gpt) - Used for example text on the site and plain English explanations of particularly tricky bits of code. Also used to determine structure of two unit tests. 

- [Code Institute](https://codeinstitute.net/) - Taught me all I know, and provided the initial framework for the Recipe model, taken from the I think therefore I blog walkthrough project.

---


## **Media**

- [GoogleFonts](https://fonts.google.com/)

- [ChatGPT](https://chatgpt.com/) - ChatGPT was used to generate the logo artwork, and the albanian sausage cake artwork.

- [Unsplash](https://unsplash.com/) - Unsplash was used to access free license imagery to add to the recipes.

---

### **Acknowledgements**

-Thank you to all my fellow Bootcamp students, our facilitator, the SME tutors and the coding coach staff for the support provided in the creation of this project. And my darling brother for providing a solid ReadMe framework.
