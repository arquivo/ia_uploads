import argparse
import os

import yaml
from internetarchive import upload

failed_lines = []


def upload_single_file(line, identifier, arc_file_path, configs, access, secret, debug):
    result = upload(identifier, files=arc_file_path, metadata=configs['metadata'], access_key=access,
                    secret_key=secret, verbose=True, retries=10, retries_sleep=60, debug=debug)
    if hasattr(result[0], 'status_code'):
        print("{}\t{}".format(result[0].status_code, line))
    else:
        print("{}\tstatus_code\t{}".format("ERROR", line))


def ia_upload(config, upload_list, access, secret, debug):
    with open(config) as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)

        with open(upload_list, mode='r') as input_file:
            for line in input_file.readlines():
                identifier, arc, file_md5 = line.split()

                arc_file_path = os.path.join(configs['files_directory'], arc)
                try:
                    upload_single_file(line, identifier, arc_file_path, configs, access, secret, debug)
                except IOError:
                    failed_lines.append(line)

        # try to re-upload the ones that gave error in the end
        for line in failed_lines:
            identifier, arc, file_md5 = line.split()
            arc_file_path = os.path.join(configs['files_directory'], arc)
            try:
                upload_single_file(line, identifier, arc_file_path, configs, access, secret, debug)
            except IOError:
                print("{}\tIOError\t{}".format("ERROR", line))


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

    ia_upload(args.config_path, args.uploadlist_file_path, access, secret, debug)


if __name__ == '__main__':
    main()
