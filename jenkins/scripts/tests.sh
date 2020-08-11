#!/bin/bash

reports_folder="reports"

# This file should be executed in the root folder where `src` and `tests` folders
# are located.
python3w -m pipenv shell
mkdir "${reports_folder}"
pytest --junit-xml="${reports_folder}/report.xml"
