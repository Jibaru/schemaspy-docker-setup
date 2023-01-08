import os

def json_filenames(path):
    filenames = filter(lambda filename: '.json' in filename, os.listdir(path))
    return [filename.split('.')[0] for filename in filenames]

if __name__ == '__main__':
    pass