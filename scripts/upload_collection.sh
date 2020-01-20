#usage: ia-upload [-h] [--AWS_ACCESS_KEY_ID_ENV ACCESS]
#                 [--AWS_SECRET_ACCESS_KEY_ENV SECRET] [--debug]
#                 config_path uploadlist_file_path
#
#positional arguments:
#  config_path           Specify path to the configuration file.
#  uploadlist_file_path  Specify path of the file with the arcs upload list.
#
#optional arguments:
#  -h, --help            show this help message and exit
#  --AWS_ACCESS_KEY_ID_ENV ACCESS
#                        Specify ENVIROMENT variable from where to get ACCESS
#                        KEY.
#  --AWS_SECRET_ACCESS_KEY_ENV SECRET
#                        Specify ENVIROMENT variable from where to get SECRET
#                        KEY.
#  --debug               Set upload debug mode.

ia-upload /configs/upload.awp24.conf uploadlist.awp24.txt

# send email after
echo "Upload collection terminated or something happened!! Check it!" | mailx -s "IA UPloads Call for Action!" daniel.bicho@fccn.pt
