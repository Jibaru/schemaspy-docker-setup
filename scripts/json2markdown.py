import json
from utils.fns import json_filenames

PATH_TO_JSONS = '../src/tables/json/es/'
PATH_TO_MD = '../src/tables/markdown/es/'


def process():
    filenames = json_filenames(PATH_TO_JSONS)
    print('[json2markdown] Encountered files: ')
    print(filenames)
    print('[json2markdown] Proccesing ...')

    for filename in filenames:
        file = open(PATH_TO_JSONS + filename + '.json')
        data = json.load(file)
        file.close()

        markdown = open(PATH_TO_MD + filename + '.md', 'w')
        markdown.write(f"# {data['name']} Table \n\n")
        markdown.write(f"{data['comments']}\n\n")

        markdown.write("## Columns:\n\n")

        for column in data['columns']:
            markdown.write(f"### {column['name']}\n\n")
            markdown.write(f"**Type:** `{column['type']}`\n\n")
            markdown.write(f"{column['comments']}\n\n")

        markdown.close()

    print('[json2markdown] Check the output at: ' + PATH_TO_MD)


if __name__ == '__main__':
    process()
