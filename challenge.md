<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://gitlab.com/sweet-sixteens/level-up-fitness">
    <img src="images/Level-Up-Logo.png" alt="Logo" width="150" height="150">
  </a>

<h3 align="center">Level-Up Fitness</h3>

  <p align="center">
    An easy workout log, so you can work hard.
    <br />
    <a href="https://gitlab.com/sweet-sixteens/level-up-fitness"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/github_username/repo_name">View Demo</a>
    · -->
    <a href="https://gitlab.com/sweet-sixteens/level-up-fitness/-/issues">Report Bug</a>
    ·
    <a href="https://gitlab.com/sweet-sixteens/level-up-fitness/-/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

A simple exercise tracker to help you log your exercise routine and track goals over time.

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Docker][Docker-badge]][Docker-url]
* [![Python][Python-badge]][Python-url]
* [![FastAPI][FastAPI-badge]][FastAPI-url]
* [![React][React-badge]][React-url]
* [![JavaScript][JavaScript-badge]][JavaScript-url]
* [![Node.js][Node.js-badge]][Node.js-url]
* [![Vite][Vite-badge]][Vite-url]
* [![Bootstrap][Bootstrap-badge]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

1. Fork the repository to your own on GitLab.com
2. Clone the repository to a local directory
3. In the top level of the project directory create a file named '.env'
4. In the '.env' file enter the following:
```
DATABASE_URL_FROM_ENV=postgresql://example_user:password@postgres/example_db
SIGNING_KEY=12345678901234567890
VITE_API_HOST_FROM_ENV=http://localhost:8000
API_NINJAS_API_KEY=12345678901234567890
```

5. Change the signing key. It should be secret and unique to your project.
6. Change the API key to your own API key. See 'Installation' for details.
7. Open your command line terminal to the top-level of the project directory and run the following commands:
```
    <<<docker compose build>>>
    <<<docker volume create postgres-data>>>
    <<<docker compose up>>>
```
8. Wait for the containers to finish opening in your command line terminal. You can also verify their status in Docker Desktop
9. In your browser, navigate to http://localhost:5173 to view the project
10. In your browser, navigate to http://localhost:8000/docs to see the FastAPI route documentation.

### Prerequisites

Install Docker for your respective OS:
```
https://docs.docker.com/engine/install/
```
Verify you have set up the '.env' file from Step 4 in 'Getting Started'


### Installation

1. Get a free API Key at [https://api-ninjas.com/register](https://api-ninjas.com/register)
2. Fork and Clone the repo
   ```
   git clone https://gitlab.com/sweet-sixteens/level-up-fitness
   ```
3. Enter your Signing Key in `.env`
   ```
   SIGNING_KEY = 'ENTER YOUR SIGNING KEY';
   ```
4. Enter your API Key in `.env`
   ```
   API_NINJAS_API_KEY = 'ENTER YOUR API KEY';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Our RESTful API framework allows a user to perform simple CRUD operations across a variety of features with full backend and frontend authentication services provided by JWTdown-fastapi. Users are able to easily sign up and login to the site with full password protection provided by our authentication framework.

Once logged in, a user has full access to their personal dashboard where they can create, retrieve, update, and delete workouts for any specific date with the use of our easy-to-navigate calendar widget. To create workout, a user selects an exercise by first selectig a muscle group from the dropdown menu. Available exercises are then retrieved via a third-party API request handled by Fast API on the application backend. Once a user selects an exercise, they are then able to choose the apropriate score (time or reps) and input their desired quantity/duration and number of sets per exercise.

Additionally, a logged-in user has access to health data features allowing them to track their progress for stats like weight, BMI, and experience over time.

## User Stories

**Sign-up**
Given a new user navigates to the home page, when they enter their desired account info into the Sign Up form and their password matches the password confirmation text input and clicks 'Sign Up', then they are redirected to their User Dashboard.

**Log-in**
Given an existing user navigates to the home page, when they click Login and enter their correct account information into the form, then they are redirected to their User Dashboard.

**Log-out**
Given a user is logged in, when they click 'Logout' in the navbar, then they are redirected to the Login/Signup page.

**Sign-up Username Error**
Given a new user navigates to the home page and they attempt to put in a username that alread exists, when they click 'Sign up', then an error message appears at the top of the form inviting them to try a different username and password.

**Sign-up Password Confirmation Error**
Given a new user navigates to the home page and they attempt to enter a password that does not match the password confirmation text input, then an error message appears at the top of the form indicating that the passwords do not match.

**Log-in Error**
Given a new or existing user navigates to the home page and they attempt to enter a username and password combination that does not match any in the database, when they click 'Login', then an error message appears at the top of the form indicating that the username and password combination is invalid.

**User Dashboard Calendar Date Change**
Given a logged-in user is on the User Dashboard page, when they click on a day on the calendar, then the date populates in the workout table in the bottom right of the User Dashboard page.

Given a logged-in user has also previously created exercises for a given date, when they click on a day on the calendar, then the exercises associated with that date will populate in the workout table in the bottom right of the User Dashboard page.

**User Dashboard to Workout Form Navigation**
Given a logged-in user is on the User Dashboard page, when they click on day on the calendar and then click on the 'To this day's workout' button, then they are redirected to the User Workout Form page associated with that day.

**User Workout Form Submission**
Given a logged-in user is on the Workout Form page, when they select an option from each of the dropdown menus and click 'Add to workout', then an exercise is created in the database and populates in the table at the top of the Workout Form page.

**User Workout Edit Feature**
Given a logged-in user is on the Workout Form page, when they click the edit button to the right of an exercise in the table at the top of the form and fill out the associated fields and click 'Add to workout', then the associated exercise row is updated in the database and the new exercise data is displayed in the table at the top of the Workout Form page.

**User Exercise Delete**
Given a logged-in user is on the Workout Form page, when they click delete to the right of an exercise, then that workout row and data is removed from the database and the exercise is removed from the table at the top of the Workout Form page.

**User Health Data Form Submission**
Given a logged-in user is on the Health Data Form page, when they click 'Update my health information' and fill out each of the form fields and click 'Submit', then a row is created in the Health Data database and they are redirected to the User Health Data view page and see their most recent health data submission.

## Testing

You can run our built-in unit tests within the FastAPI Docker container with the command <<python -m pytest>>. You can also connect to the docker container from your terminal with the command <<docker exec -it level-up-fitness-fast-api-1 bash>> and once connected, you can utilize the same <<python -m pytest>> command to run the tests. There are four tests located in the api/tests/ folder.

-**Lucas K.** : </api/tests/test_create_healthdata.py>
  -Tests the functionality of the post route to create user health data. It overrides the account info and health data repository to prevent any connection to external resouces resulting in a fully localized unit test.

-**Hector R.** : </api/tests/test_create_exercise.py>
  -Tests the functionality of the post route to create user exercise data. It overrides the account info and exercise data repository to prevent any connection to external resources resulting in a fully localized unit test.

-**Jon S.** : </api/tests/test_get_exercise.py>
  -Tests the functionality of the get route to retrieve an individual user created exercise. It overrides the account info and exercise data repository to prevent any connection to external resources resulting in a fully localized unit test.

-**Justin Q.** : </api/tests/test_get_healthdata.py>
  -Tests the functionality of the get route to retrieve an individual's collective health data. It overrides the account info and health data repository to prevent any connection to external resouces resulting in a fully localized unit test.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Diagram

The Frontend consists of a React Single Page Application (SPA) with the following routes:

![App Map](./images/PageFlow.png)

![Login/Signup Page](./images/LoginLogoutPage.png)

![User Dashboard](./images/Dashboard.png)

![Health Data View](./images/HealthDataView.png)

![Health Data Form](./images/HealthDataForm.png)

![Workout Form](./images/WorkoutForm.png)

## Design

Level-Up Fitness is made up of a backend, a graphical human interface (ghi), and a postgreSQL database that use a RESTful API framework to interact:

The FastAPI docs page and the GHI can be accessed via their respective ports from the browswer. The database port is also listed for user convenience.

- **Level-Up Fitness**
- **FastAPI**    http://localhost:8000/
	- **api**
- **GHI**        http://localhost:5173/
    - **src**
- **Database**      http://localhost:5432/

## API Documentation

HIGH LEVEL OVERVIEW

You can view the **API route documentation** in your browser by navigating to http://localhost:8000/docs

Level-Up Fitness is comprised of three dependent microservices: FastAPI, GHI, and the Database.

The FastAPI backend utilizes Pydantic models for data formatting and validation and JWTdown-fastapi for user authentication processes such as account creation, login, logout, and password hashing and protection.

The GHI utilizes Vite for front-end deployment and a React Single Page Application (SPA) format for a seemless and fast user experience.

The database is a postgreSQL structure utilzing a migrations file located in the migrations folder for table creation. The queries folder holds the specfic database instructions handled by the backend to interact with the database for all of the CRUD routes needed to manage user, exercise, workout, and health data.


<!-- ROADMAP -->
## Roadmap

- [ ] Calculate user BMI via 3rd party API
- [ ] Generate a daily randomized workout
- [ ] Implement motivational quotes on homepage
- [ ] Delete user account along with associated workouts
- [ ] Allow users to post a workout to a common board for other users to complete
- [ ] Implement interactive graph to show user progress over time
- [ ] Track user stats for exercises and workouts completed
- [ ] Show a user leaderboard of top performers in specific categories
- [ ] Auto-populate a user's health data on the health data form based on their previous health data submission


See the [open issues](https://gitlab.com/sweet-sixteens/level-up-fitness/-/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

* Justin Q. - justinqnr95@gmail.com
* Jon S. - scott_j_m@icloud.com
* Lucas K. - lucasrkearns@gmail.com
* Hector R. - hreyes1113@gmail.com

Project Link: [https://gitlab.com/sweet-sixteens/level-up-fitness](https://gitlab.com/sweet-sixteens/level-up-fitness)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [FullCalendar](https://fullcalendar.io)
* [API Ninjas](https://api-ninjas.com)
* [Bootstrap](https://getbootstrap.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://ileriayo.github.io/markdown-badges/#markdown-badges -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://gitlab.com/sweet-sixteens/level-up-fitness/-/forks/new
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://gitlab.com/sweet-sixteens/level-up-fitness/-/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username




[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
