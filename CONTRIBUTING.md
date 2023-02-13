# Contributing

All contributions are welcome!
If you know a dataset that belongs here (see criteria below) but is not listed,
please feel free to add it.

## Guidelines

* Read the criteria below
* Add one dataset per Pull Request.
* Add the dataset and its information as a table row.
* Make sure to maintain the table chronological order.
* Keep descriptions in the content and emotion cells concise.
* Check your spelling and grammar.
* Keep the table correctly aligned.
* Send a Pull Request with a short explanation of why does it belong to this list.

## Criteria

* The dataset must be related to the field of *Spoken Emotion Recognition*.
* The dataset should not be a duplicate.
* The dataset should not be provided in an active PR.
* The dataset should be available for researchers for free.
* The information about the dataset must be accessible for verification.

## How to contribute
First go to `src/` using `cd src`. Then add a the dictionary / part json data of the contributed dataset to `src/ser-datasets`. 
Make sure the json is valid, then run the `python generate_files.py` to update the restructured text file, csv file and the README.
That's it, Congrats! and thank you for your contribution. Now open a PR with your changes. I will review it and then publish the results :))