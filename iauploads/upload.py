import argparse
import os

import yaml
from internetarchive import upload


# TODO add logging
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", help="Specify path to the configuration file.")
    parser.add_argument("uploadlist_file_path", help="Specify path of the file with the arcs upload list.")
    parser.add_argument('--AWS_ACCESS_KEY_ID_ENV', dest="access", default="AWS_ACCESS_KEY",
                        help="Specify ENVIROMENT variable from where to get ACCESS KEY.")
    parser.add_argument('--AWS_SECRET_ACCESS_KEY_ENV', dest="secret", default="AWS_SECRET_ACCESS_KEY",
                        help="Specify ENVIROMENT variable from where to get SECRET KEY.")
    parser.add_argument('--debug', action="store_true", help="Set upload debug mode.")

    args = parser.parse_args()

    debug = True if args.debug else False

    access = os.environ[args.access]
    secret = os.environ[args.secret]

    with open(args.config_path) as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)

        with open(args.upload_file_path, mode='rb') as input_file:
            for line in input_file.readlines():
                identifier, arc, file_md5 = line.split()

                # returns a list of requests.Response
                # what to do with this?
                result = upload(identifier, files=os.path.join(configs['files_directory'], arc),
                                metadata=configs['metadata'],
                                access_key=access,
                                secret_key=secret, verbose=True, retries=10, retries_sleep=300, debug=debug)


if __name__ == '__main__':
    main()
