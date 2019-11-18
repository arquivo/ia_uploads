import argparse
import os
from hashlib import md5

import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", help="Specify path to the configuration file.")
    parser.add_argument("--number_of_files", default=100, help="Number of files per bucket. (default = 100)")
    parser.add_argument("--hash", action="store_true", help="Generate md5 hash.")

    args = parser.parse_args()

    hashing = True if args.hash else False

    with open(args.config_path) as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)

    counter = 0
    cycle_number = 0
    str_item_number = str(cycle_number).zfill(4)

    files_directory = configs['files_directory']
    collection = configs['metadata']['collection']
    year = configs['year']
    pwacrawlid = configs['metadata']['pwacrawlid']

    for root, dirs, files in os.walk(files_directory):
        for file in files:
            if file.endswith("warc.gz") or file.endswith("arc.gz") or file.endswith(".warc"):
                if counter >= int(args.number_of_files):
                    cycle_number = cycle_number + 1
                    str_item_number = str(cycle_number).zfill(4)
                    counter = 0

                full_path_filename = os.path.join(root, file)

                item_name = "{}-{}-{}-{}".format(collection, pwacrawlid, year, str_item_number)

                hashit = md5(open(full_path_filename, 'rb').read()).hexdigest() if hashing else "-"

                print("{} {} {}".format(item_name, full_path_filename, hashit))
                counter = counter + 1


if __name__ == "__main__":
    main()
