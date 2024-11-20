<a name="top"></a>
<p align="center"><img src="docs/rocket_launch.png"></p>
<h1 align="center">SpaceX API Client</h1>

<h3 align="center">
Full-stack implementation of a Python wrapper, Flask API and React Front-end.
Based on the Open Source SpaceX API.
</h3>

 <h3 align="center">
   <a href="https://spacex-client.onrender.com/">🚀 View the deployed application here</a>
 </h3>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
        <a href="#project-summary">Project Summary</a>
    </li>
    <li>
        <a href="#-about">About The Project</a>
        <ul>
            <li><a href="#built-with">Built With</a></li>
        </ul>
    </li>
    <li>
        <a href="#getting-started">Getting Started</a>
        <ul>
            <li><a href="#Requirements">Requirements</a></li>
            <li><a href="#build--launch-flask-api">Flask Build & Launch</a></li>
            <li><a href="#build--launch-react-frontend">React Build & Launch</a></li>
            <li><a href="#vscode-debugging">VSCode Debugging</a></li>
        </ul>
    </li>
    <li>
        <a href="#how-to-use">How to use</a>
        <ul>
            <li><a href="#api">Flask API</a></li>
            <li><a href="#front-end">Front-End</a></li>
        </ul>
    </li>
    <li>
        <a href="#unit-tests">Unit Tests</a>
        <ul>
            <li><a href="#python">Python</a></li>
            <li><a href="#react">React</a></li>
        </ul>
    </li>
    <li><a href="#faqs">FAQs</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## Project Summary
The answers to the questions...

* How many rockets have been launched each year?
* How many launches were made from each launch site?

...are answered by viewing the deployed application linked above.

Please navigate to the launch and launch site pages.

## About
**SpaceX API Client** is a full-stack solution which uses the [SpaceX API](https://github.com/r-spacex/SpaceX-API) to wrap and serve information to a dedicated front-end. It is made up of the following components:

- Python module which serves as a wrapper for the SpaceX API
- Flask API is an interface for the python module
- React front-end integrated with the Flask API 

The Python module is completely standalone, and is able to read, write and query the SpaceX API. It currently only supports launches and launch sites. 

### Built With

* ![React.js]
* ![Shadcn-url]
* ![vite-url]
* ![Tailwind]
* ![Python-url]
* ![TypeScript-url]
* ![Flask-url]

## Getting Started

To start using the application locally, please follow these steps.

### Requirements

* NodeJS 18.16.1
* Python 3.11.8

### Build & Launch Flask API
1. Navigate to the `api` folder of the project.

2. Create a Python virtual environment
   ```sh
   python -m venv env
   ```

3. Activate the virtual environment
    
    - Using Bash terminal
        ```bash
        source  env/Scripts/activate
        ```

    - Using PowerShell terminal
        ```bash
        ./env/Scripts/Activate
        ```
4. Install the python packages required for running the API
    ```sh
   pip install -r requirements.txt
   ```

5. Launch a default local instance via CLI
    ```sh
   flask run
   ```

Flask automatically detects the "app.py" file and runs on the default port of 5000, which is what the front-end client uses.

### Build & Launch React Frontend
1. Navigate to the `client` folder of the project

2. Install all required npm packages
    Install NPM packages
   ```sh
   npm install
   ```

    **WARNING**: If you are on the company network, you may need to create the following CLI environment variables, and/or remove npm specific proxies. Please follow the **fix** instructions on [this](https://confluence.devops.jlr-apps.com/x/LAr9Kw) confluence page before running `npm install`


3. Run a development instance
    ```sh
   npm run dev
   ```
Both the Flask and React applications must be running simultaneously in seperate terminals to ensure the React application works correctly.

The React application will be running on `http://localhost:5173/`. Navigate to this URL in your browser to open the front-end.

### VSCode Debugging

VSCode users can utilise it's built-in debugger to quickly launch instances of both flask and react applications. Please run the `API: Development` and `CLIENT: Development` run configurations in the `Run and Debug` mode.

When running the API, you will need to ensure your VSCode Python Interpreter is set to the python executable `./api/env/Scripts/python.exe`. 

1. Navigate to the Command Palette (Ctlr + Shift + P)
2. Select `Python: Select Interpreter`
3. Select `Enter interpreter path...`
4. Select the python executable `./api/env/Scripts/python.exe`
5. Restart any open terminals for the change to take effect.

**IMPORTANT**:
It is recommended to use the CLI launch commands instead of VSCode's debugger. This is due to the client's debugger being unstable.  

## How to use

### Flask API
The Flask API application receives HTTP requests using the prefix `/API/`, currently available routes using the deployed application include:

```
GET https://spacex-client.onrender.com/api/

GET https://spacex-client.onrender.com/api/get_all_launch_years

GET https://spacex-client.onrender.com/api/<year>/get_all_launch_years

GET https://spacex-client.onrender.com/api/get_all_launchpad_names

GET https://spacex-client.onrender.com/api/<id>/<shortname>/get_launchpad_with_launches
```

The variables in chevrons represent input parameters which are derived from the preceding GET requests.

### Front-End

The front-end client currently has three pages and can be navigated to on the same host as the API.

* [Homepage](https://spacex-client.onrender.com/)
* [Launches](https://spacex-client.onrender.com/launches)
* [Launch Sites](https://spacex-client.onrender.com/launches)

Explore the front-end capability as you wish

## Unit Tests

Both the front and backend are fully unit tested, with 100% line coverage on each.

### Python

1. Navigate to the root directory of the project

2. Run the tests with coverage output
    ```sh
    pytest --cov
    ```
3. Alternatively, use VSCode's test runner.

### React

1. Navigate to the `client` directory of the project

2. Run the tests with the coverage output
    ```sh
    npx vitest --coverage.enabled
    ```
3. Alternatively, use VSCode's test runner.

## FAQs

- How has the application been deployed?

    The application is hosted on Render, which offers free web-service and static site hosting. The Flask application is ran using Gunicorn. Flask is then used to serve the React application, which is typically not an ideal solution for productionised application, but has been done due to the small scale of this project, and time/cost constraints.  
    
    For productionised applications, it would be far better to use a dedicated web server, such as nginx, apache or iis, to handle the routing and serving of static files. This would then be hosted on a self-managed or cloud platform.


## Contact

Please contact me for any questions or assistance with running the components of this repository.

[Back to top](#top)


[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Tailwind]: https://img.shields.io/badge/tailwindcss-0F172A?&logo=tailwindcss
[vite-url]: https://img.shields.io/badge/-Vite-B73BFE?style=flat&logo=vite&logoColor=white
[Shadcn-url]: https://img.shields.io/badge/shadcn%2Fui-000?logo=shadcnui&logoColor=fff
[Python-url]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[TypeScript-url]: https://shields.io/badge/TypeScript-3178C6?logo=TypeScript&logoColor=FFF&style=flat-square
[Flask-url]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white
