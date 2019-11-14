import argparse
import os
from hashlib import md5

import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", help="Specify path to the configuration file.")
    parser.add_argument("--number_of_files", default=100, help="Number of files per bucket.")

    args = parser.parse_args()

    with open(args.config_path) as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)

    counter = 0
    cycle_number = 0
    str_item_number = str(cycle_number).zfill(4)

    files_directory = configs['files_directory']
    collection = configs['collection']
    year = configs['year']
    pwacrawlid = configs['metadata']['pwacrawlid']

    for filename in os.listdir(files_directory):

        if counter == args.number_of_files:
            cycle_number = cycle_number + 1
            str_item_number = str(cycle_number).zfill(4)
            counter = 0

        full_path_filename = os.path.join(files_directory, filename)

        if os.path.isfile(full_path_filename):
            item_name = "{}-{}-{}-{}".format(collection, pwacrawlid, year, str_item_number)
            hash = md5(open(full_path_filename, 'rb').read()).hexdigest()

        print("{} {} {}".format(item_name, filename, hash))


if __name__ == "__main__":
    main()
