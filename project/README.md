> _This repository contains data engineering and data science projects and exercises using open data sources as part of the [SAKI](https://oss.cs.fau.de/teaching/specific/saki/) course, taught by the [FAU Chair for Open-Source Software (OSS)](https://oss.cs.fau.de/) in the Winter'23/24 semester. This repo is forked from [made-template repository](https://github.com/jvalue/made-template.git)

# Exploring the Impact of Air pollution on Bicycle sharing in Seoul

This project aims to analyze **the Impact of Air pollution on Bicycle sharing in Seoul** generated from several data collectors throughout the city to determine if Seoul is a suitable city for an enthusiastic bike to live in. The project is using two open data sources: [bike sharing Data in Seoul](https://www.kaggle.com/datasets/hmavrodiev/london-bike-sharing-dataset), which contains information on bicycle traffic in London, and [Air pollution Data of Seoul](https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data), which provides weather and climate data of London. For details see the [project plan](/project/project-plan.md).


**Important files of the project and their roles:**

- `project/etl_pipeline.py`: It will run an automated ETL pipeline that creates an SQLite database named `seoul.sqlite` that contains two tables representing two open data sources of the project.
- `project/tests.sh`: A bash script that will execute the component and system-level testing for the project by calling two other Python scripts, `project/test.py`.
- `project/report.ipynb`: This Jupyter notebook serves as the final report for the project, providing a comprehensive exploration of all aspects and findings. The report primarily investigates the impact of air pollution conditions in Seoul on bicycle traffic throughout the year, addressing various key questions, based on the data in `seoul.sqlite`. See the [report](project/report.ipynb).

**Project Pipeline using GitHub Action:** <br>

A project pipeline has been implemented using a GitHub action defined in [.github/workflows/ci-tests.yml](.github/workflows/ci-tests.yml). This pipeline is triggered whenever changes are made to the `project/` directory and pushed to the GitHub repository, or when a pull request is created and merged into the `main` branch. The `ci-tests.yml` workflow executes the `project/tests.sh` test script, and in case of any failures, it sends an error message.

## Project Setup

1. Clone this git repository
```bash
git clone https://github.com/RehnumaSSmrity/made-project-ws24.git
```
2. Install [Python](https://www.python.org/). Then create a virtual environment inside the repo and activate it.
```bash
python3 -m venv <env_name>
source <env_name>/bin/activate
```
3. Download and install the required Python packages for the project.
```bash
pip install -r requirements.txt
```
4. To run the project, go to the `project/` directory and run the `etl_pipeline.py` script. It will run the whole ETL pipeline and generate an SQLite database named `main.sqlite` that contains two tables, `bike_data` and `air`, representing two open data sources of the project.
```bash
cd project/
python3 etl_pipeline.py
```
5. To run the test script which will execute the component and system-level testing for the project, run the following command.
```bash
chmod +x tests.sh
sh tests.sh
```
6. Finally, run and explore the `project/report.ipynb` project notebook.

## Exercises (not part of the project)

During the semester we had to complete exercises, sometimes using [Python](https://www.python.org/), and sometimes using [Jayvee](https://github.com/jvalue/jayvee). Automated exercise feedback is provided using a GitHub action that is defined in [.github/workflows/exercise-feedback.yml](.github/workflows/exercise-feedback.yml).

1. [exercises/exercise1.jv](exercises/exercise1.jv)
2. [exercises/exercise2.py](exercises/exercise2.py)
3. [exercises/exercise3.jv](exercises/exercise3.jv)
4. [exercises/exercise4.py](exercises/exercise4.py)
5. [exercises/exercise5.jv](exercises/exercise5.jv)

The exercise feedback is executed whenever we make a change in files in the `exercise/` directory and push our local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, and open the `exercise-feedback` job and `Exercise Feedback` step.
