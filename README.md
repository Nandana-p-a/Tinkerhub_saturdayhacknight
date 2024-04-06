
![django notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/2db31367-8f96-4e88-8a8d-a1a75936204d)




**CGPA Generator**

A CGPA (Cumulative Grade Point Average) generator is a software tool designed to calculate a student's overall academic performance based on their grades in various subject over a semister. The generator takes the grades received in each course along with the credits associated with each course to comput the cumulative GPA. A CGPA generator simplifies the process of determining a student's academic standing and helps in evaluating progress throughout their academic career. 

## Team members
1. [Anika Sarah Sabu](https://github.com/Aneka-zera)
2. [Jeslia Jobi](https://github.com/Jeslia-Jobi)
3. [Nandana P A](https://github.com/Nandana-p-a)
4. [Parvathi Krishna](https://github.com/26parvathik)

## How it Works ?

 The project will have a user interface where users can input their subject name, course grades and credits. This interface is implemented using HTML templates rendered by Django's template engine. When the user submits their subject name, grades and credits, the backend will receive this data. It will then perform calculations to determine the CGPA based on the input provided.Django models is be used to define the structure of the data (e.g., subject name, grades, credits). These models will handle storing and retrieving data from a database.The application will calculate the CGPA by considering the grades obtained in each course and the respective credits. It may use a standard formula for CGPA calculation, such as weighted averaging.The application will validate user input to ensure it meets certain criteria, such as valid grades and positive credits. After calculating the CGPA, the application will display the result to the user. This result will typically include the calculated CGPA.The application will handle errors , providing feedback to the user if there are any issues with the input data or the calculation process. Depending on the project requirements, the application may include user authentication and authorization features to allow only registered users to access the CGPA calculator.
   
## Libraries used

1.Django 5.0.4

2.Python 3.11.9

3.HTML

## How to configure

instalation : 

$ pip3 install django

create a project : 

$ django-admin startproject core

$ cd core

Working on virtual environment.

## How to Run

$ python manage.py runserver
