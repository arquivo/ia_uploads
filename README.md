# IA Uploads

## Install
```pip install git+https://github.com/arquivo/iauploads.git```

## Usage

```<command> --help``` gives more information about each command utilization.

Write the configuration yaml file with the metadata about the collections to be uploaded (ex. iaupload_awp24.yml).
Example of contents:

```
files_directory: ./tests/arcs
year: 2017
metadata:
    collection: "portuguese-web-archive"
    mediatype: "web"
    pwacrawlid: "crawl_test"
    external_identifier: "urn:X-pwacrawlid:crawl_test"
    title: "Crawl test collection to test uploads for internet archive"
    adder: "Portuguese Web Archive"
    creator: "Portuguese Web Archive"
    contributor: "Portuguese Web Archive"
    coverage: "3 million web files crawled between 2011-05-20 and 2012-02-05."
    description: "Contains an extraordinary crawl of content interesting to enable web preservation such as format specifications from W3C."
    language: "Portuguese and English."
    subject: "Crawl test collection to test uploads for internet archive"
    notes: "Just some fake information"
    credits: "Internet Archive Heritrix team."
    date: "2017-01-01"
```

Generate list with all WARC files to upload and their bucket number:

```
ia-generate-items iaupload_awp24.yml > iaupload_awp24_list.txt
```

```
bash$ ia-upload iaupload_awp24.yml awp24_uploadlist.txt > awp24_ia_upload.log

 uploading IAH-20170731142400-00027-p82.arquivo.pt.arc.gz: [################################] 97/97 - 00:00:14
 uploading IAH-20170731141418-00000-p82.arquivo.pt.arc.gz: [################################] 96/96 - 00:00:31
 uploading IAH-20170731142402-00028-p82.arquivo.pt.arc.gz: [################################] 96/96 - 00:01:18
 uploading IAH-20170731141418-00001-p82.arquivo.pt.arc.gz: [################################] 98/98 - 00:00:15
 uploading IAH-20170731142413-00029-p82.arquivo.pt.arc.gz: [################################] 96/96 - 00:00:16
 uploading IAH-20170731141418-00002-p82.arquivo.pt.arc.gz: [################################] 96/96 - 00:00:21
 uploading IAH-20170731142447-00030-p82.arquivo.pt.arc.gz: [                                ] 2/96 - 00:02:10
 
```