@echo off

set reports_folder="reports"
mkdir %reports_folder%
pytest --junit-xml="%reports_folder%/report.xml"
