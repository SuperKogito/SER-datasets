#!/bin/bash

echo "Rst and Md files generations"
python generate_files.py      

echo "Make html files"
make html 
