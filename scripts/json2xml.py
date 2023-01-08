import json
from xml.dom import minidom
from utils.fns import json_filenames

PATH_TO_JSONS = '../src/tables/json/es/'
PATH_TO_XML = '../src/tables/xml/es/'


def process():
    filenames = json_filenames(PATH_TO_JSONS)
    print('[json2xml] Encountered files: ')
    print(filenames)
    print('[json2xml] Proccesing ...')

    for filename in filenames:
        file = open(PATH_TO_JSONS + filename + '.json')
        data = json.load(file)
        file.close()

        xml = minidom.Document()

        tableTag = xml.createElement('table')
        tableTag.setAttribute('name', data['name'].lower())
        tableTag.setAttribute('comments', data['comments'])

        for column in data['columns']:
            columnTag = xml.createElement('column')
            columnTag.setAttribute('name', column['name'])
            columnTag.setAttribute('comments', column['comments'])

            tableTag.appendChild(columnTag)

        xml.appendChild(tableTag)

        xml_content = xml.childNodes[0].toprettyxml(indent="\t")

        with open(PATH_TO_XML + filename + '.xml', "w") as f:
            f.write(xml_content)

    print('[json2xml] Check the output at: ' + PATH_TO_XML)


if __name__ == '__main__':
    process()
