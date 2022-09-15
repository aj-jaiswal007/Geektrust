#!/bin/bash


pip install -r requirements.txt

echo "Checking inputs"
python -m geektrust sample_input/input1.txt
echo "----------------------"
python -m geektrust sample_input/input2.txt
echo "----------------------"
python -m geektrust sample_input/input3.txt
echo "----------------------"
python -m geektrust sample_input/input4.txt
echo "----------------------"
python -m geektrust sample_input/input5.txt


echo "Running tests----"
coverage run -m unittest discover 
echo "Checking coverage----"
coverage report ./src/*.py ./src/*/*.py 
# To clean pycache files
# find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf