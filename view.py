__author__ = 'carolina_zamith'

import s3_load as s3

if s3.testLoad:

    print('SUCESSO !!')

    for i in range(9):#s3.testLoad.allbuckets:
        print(s3.testLoad.allbuckets.markers[i])