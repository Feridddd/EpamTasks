from xml.etree.ElementTree import parse, Element
import xml.etree.ElementTree as ET
from collections import Counter
import re

file = 'mondial-3.0.xml'


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = ET.iterparse(filename, ('start', 'end'))
    next(doc)
    for_tag = []
    for_elem = []
    for event, elem in doc:
        if event == 'start':
            for_tag.append(elem.tag)
            for_elem.append(elem)
        elif event == 'end':
            if for_tag == path_parts:
                yield elem
            try:
                for_tag.pop()
                for_elem.pop()
            except IndexError:
                pass
    return for_tag, for_elem


def read_XML(filename):
    country_government = []
    distinct_governments = set()
    countries = parse_and_remove(filename, 'country')

    for country in countries:
        name = country.attrib['name']
        if re.search(r'\s', name):
            government = country.attrib['government']
            if len(government.strip()) > 0:
                country_government.append((name, government.strip()))
    for name, government in country_government:
        distinct_governments.add(government)

    return sorted(distinct_governments)


def main():
    result = read_XML(file)
    print(*result, sep=", ")


if __name__ == "__main__":
    main()
