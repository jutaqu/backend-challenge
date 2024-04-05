<div align="center">

<h3 align="center">backed-challenge</h3>

  <p align="center">
    A simple task manager to help you stay on track!
    <br />
    <a href="https://github.com/jutaqu/backend-challenge/tree/main"><strong>Explore the docs »</strong></a>
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


### Built With

* [![Django][Django-badge]][Django-url]
* [![Python][Python-badge]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Prerequisites

Install Django on your local machine
```
pip install django
```


### Installation

1. Fork and Clone the repo
   ```
   git clone https://github.com/jutaqu/backend-challenge.git
   ```
3. In your terminal, navigate to the project directory and create two users. Follow the prompts for username and password. Email is optional.
   ```
   python manage.py createsuperuser
   ```
2. In your terminal, navigate to the project directory and run the application
   ```
   python manage.py runserver
   ```
3. In the browser, navigate to the Django Admin page and verify the two users were created. Use one of the user credentials you created to log in.
   ```
   http://localhost:8000/admin/
   ```
4. In the browser, with the application still running, navigate to the application page and follow the User Stories below to test out the application
   ```
   http://localhost:8000/
   ```
5. You can log out and log in with the second user you created in the Django Admin page then navigate back to the application page in the browser to verify that users only see their own tasks and labels.
   ```
   http://localhost:8000/admin/
   http://localhost:8000/
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Our RESTful API framework allows a user to perform simple CRUD operations across a variety of features with full backend authentication services provided by Django.

Once logged in, a user has full access to their personal dashboard where they can create, retrieve, update, and delete tasks and labels.

## User Stories

**Create a task**
Given a user is logged in, when they click the 'Create Task' button at the bottom of Task List page, they are navigated to the task creation form. After filling out the requisite info and clicking the 'Create Task' button at the bottom of the form, the user is redirected back to the Task List page where they will see their newly created task.

**Update a task**
Given a user is logged in, when they click the 'Update' button to the right of a given task, they are navigated to the task update form. After verifying/updating any desired input and clicking the 'Update Task' button at the bottom of the form, the user is redirected back to the Task List page where they will see the existing task has been updated with the new information.

**Delete a task**
Given a user is logged in, when they click the 'Delete' button to the right of a given task, they are navigated to the delete confirmation page where they are prompted to confirm their choice. After clicking the 'Delete' button below the prompt, the user is redirected back to the Task List page where they will see the task is no longer listed. Alternatively, the user can click the 'Cancel' button on the delete confirmation page to abort the delete and be redirected back to the Task List page.

**Create a label**
Given a user is logged in and on the Label List page, when they click the 'Create Label' button at the bottom of the page, they are navigated to the label creation form. After filling out the requisite inputs and clicking the 'Create Label' button at the bottom of the form, the user is redirected back to the Label List page where they will see their newly created label.

**Update a label**
Given a user is logged and on the Label List page, when they click the 'Update' button to the right of a given label, they are navigated to the label update form. After verifying/updating any desired input and clicking the 'Update Label' button at the bottom of the form, the user is redirected back to the Label List page where they will see the existing label has been updated with the new information. Additionally, any task associated with that label will also be updated with the new data.

**Delete a label**
Given a user is logged in, when they click the 'Delete' button to the right of a given label, they are navigated to the delete confirmation page where they are prompted to confirm their choice. After clicking the 'Delete' button below the prompt, the user is redirected back to the Label List page where they will see the label is no longer listed. Alternatively, the user can click the 'Cancel' button on the delete confirmation page to abort the delete and be redirected back to the Label List page.
Additionally, any task with the given label will no longer have that label applied.



## Testing

You can run our built-in unit tests within using Django's built-in testing functionality. There are currently seven tests testing the various CRUD endpoints. To run the tests, simply navigate to your local repository in your terminal where this project resides and use the command:

python manage.py test

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Design

This 'backend-challenge' consists of a Python Django backend, a simple Django provided HTML GHI, and a provided SQL database that use a RESTful Django API framework to interact:

- **backend-challenge**    http://localhost:8000/
- **Django Admin**        http://localhost:8000/admin

## API Documentation

HIGH LEVEL OVERVIEW

This 'backend-challenge' project is a simple task manager consisting of two models: 'Task' and 'Label'. Tasks and labels share a Many-to-Many relationship allowing task instances to have many labels and any user-created label can be applied to multiple tasks.

This Project is a simple Python and Django backend utilizing HTML files to display the various forms and views to complete CRUD operations on both Task and Label instances.

The Project utilizes built in Django authentication and custom filtering to ensure that only logged in users can perform any operation and that each user only sees their own tasks and labels.

See the [open issues](https://github.com/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

* Justin Q. - justinqnr95@gmail.com

Project Link: [https://github.com/jutaqu/backend-challenge/tree/main](https://github.com/jutaqu/backend-challenge/tree/main)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Django-badge]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com
