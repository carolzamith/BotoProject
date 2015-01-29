__author__ = 'carolina_zamith'

from boto.s3.connection import S3Connection


class testLoad:
    con = S3Connection('AKIAITMDI3AFF7LZCNEA','M9omGA4BVygQRfEipdITlX+oV+xopGZW1OH0Ow4S')
    allbuckets = con.get_all_buckets()
    mybucket = con.get_bucket('bn-data-test')
    #assert isinstance(mybucket, object)
    #listaBucket = mybucket.list()
    #lista = con.lookup('mybucket.name')


