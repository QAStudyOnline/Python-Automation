import json
import csv
import xml.etree.ElementTree as ET


def read_and_print_json(file_path):
    with open(file_path) as file:
        content = file.read()
        print(content)
        value = json.loads(content)
        print(value)
    print("#######################################")
    for row in value:
        print(row)
        for element in row:
            print("#######################################")
            print(element, ": => ", row[element])


def read_and_print_csv(file_path):
    with open(file_path) as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            print(row)
            for element in row:
                print(element, ": => ", row[element])


def read_and_print_xml(file_path):
    xml_file = ET.parse(file_path)
    root = xml_file.getroot()
    print(root.items())
    for elem in root:
        for sub_elem in elem:
            print(sub_elem.tag, ": => ", sub_elem.text)


# read_and_print_csv("002_lesson\\resources\\data.csv")
# read_and_print_json("002_lesson\\resources\\data.json")
read_and_print_xml("002_lesson\\resources\\data.xml")
