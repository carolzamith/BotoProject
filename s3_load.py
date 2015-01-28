__author__ = 'carolina_zamith'

from boto.s3.connection import S3Connection


class testLoad:
    con = S3Connection('aws_access_key_id', 'aws_secret_key_id')

    bucket = con.get_bucket('bucket_name')
