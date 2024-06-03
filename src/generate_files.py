
import csv
import json
from tabulate import tabulate


# load datasets
json_file_path = "ser-datasets.json"
with open(json_file_path, 'r') as j:
     content = json.loads(j.read())

# init keys
keys = ["Dataset", "Year", "Content", "Emotions", "Format", "Size", "Language", "Paper", "Access", "License", "Dataset-link", "Paper-link", "License-link"]
header = ["Dataset", "Year", "Content", "Emotions", "Format", "Size", "Language", "Paper", "Access", "License"]

md_0 = """***Spoken Emotion Recognition Datasets:*** *A collection of datasets (count={0})""".format(len(content.items()))
md_1 = """ for the purpose of emotion recognition/detection in speech.
The table is chronologically ordered and includes a description of the content of each dataset along with the emotions included.
The table can be browsed, sorted and searched under https://superkogito.github.io/SER-datasets/*
"""

md_2 = """## References

- Swain, Monorama & Routray, Aurobinda & Kabisatpathy, Prithviraj, Databases, features and classifiers for speech emotion recognition: a review, International Journal of Speech Technology, [paper](https://www.researchgate.net/publication/322602563_Databases_features_and_classifiers_for_speech_emotion_recognition_a_review#pf19)
- Dimitrios Ververidis and Constantine Kotropoulos, A State of the Art Review on Emotional Speech Databases, Artificial Intelligence & Information Analysis Laboratory, Department of Informatics Aristotle, University of Thessaloniki, [paper](http://poseidon.csd.auth.gr/papers/PUBLISHED/CONFERENCE/pdf/Ververidis2003b.pdf)
- A. Pramod Reddy and V. Vijayarajan, Extraction of Emotions from Speech-A Survey, VIT University, International Journal of Applied Engineering Research, [paper](https://www.ripublication.com/ijaer17/ijaerv12n16_46.pdf)
- Emotional Speech Databases, [document](https://link.springer.com/content/pdf/bbm%3A978-90-481-3129-7%2F1.pdf)
- Expressive Synthetic Speech, [website](http://emosamples.syntheticspeech.de/)
- Towards a standard set of acoustic features for the processing of emotion in speech, Technical university Munich, [document](https://asa.scitation.org/doi/pdf/10.1121/1.4739483)


## Contribution

- All contributions are welcome! If you know a dataset that belongs here (see [criteria](https://github.com/SuperKogito/SER-datasets/blob/master/CONTRIBUTING.md#criteria)) but is not listed, please feel free to add it. For more information on Contributing, please refer to [CONTRIBUTING.md](https://github.com/SuperKogito/SER-datasets/blob/master/CONTRIBUTING.md).

-  If you notice a typo or a mistake, please [report this as an issue](https://github.com/SuperKogito/SER-datasets/issues/new) and help us improve the quality of this list.


## Disclaimer
- The mainter and the contributors try their best to keep this list up-to-date, and to only include working links (using automated verification with the help of the [urlchecker-action](https://github.com/marketplace/actions/urlchecker-action)). However, we cannot guarantee that all listed links are up-to-date. Read more in [DISCLAIMER.md](https://github.com/SuperKogito/SER-datasets/blob/master/DISCLAIMER.md).
"""


print(" -> Generate Markdown Text")
def format_md_link(label, link):
    res = "[{0}]({1})".format(label, link) if "http" in link else label
    return res

# tabulate
table = []
for key, values in content.items():
    # add elements to row
    row = [format_md_link(key, values["Dataset-link"])]
    row += [values[k] for k in ["Year", "Content", "Emotions", "Format", "Size", "Language"]]
    row += [format_md_link(values["Paper"], values["Paper-link"]), values["Access"], format_md_link(values["License"], values["License-link"])]

    # add styles and add row to table
    row = ["<sub>{0}</sub>".format(e) for e in row]
    table.append(row)

table = tabulate(table, keys, tablefmt="pipe")
with open("../README.md", "w") as f:
    f.write(md_0)
    f.write(md_1)
    f.write(table)
    f.write(md_2)


print(" -> Generate Restructured Text")
def format_rst_link(label, link):
    res = "`{0} <{1}>`_".format(label, link) if "http" in link else label
    return res

# tabulate
table = []
for key, values in content.items():
    # add elements to row
    row = [format_rst_link(key, values["Dataset-link"])]
    row += [values[k] for k in ["Year", "Content", "Emotions", "Format", "Size", "Language"]]
    row += [format_rst_link(values["Paper"], values["Paper-link"]), values["Access"]]
    row += [format_rst_link(values["License"], values["License-link"])]

    # format and add row to csv
    table.append(row)

with open('ser-datasets.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(table)
