
from ftplib import FTP
import os

host = "34.90.99.147"


# connect to host on default port i.e 21
ftp = FTP(host=host)
login_status = ftp.login()
print(login_status)
print("osman")
# change directory to upload
ftp.cwd('pub')

# print the content of directory
print(ftp.dir())
fp = open("/Users/osman/Desktop/bil452/hw2/test213.txt", 'rb')
# upload file
ftp.storbinary('STOR %s' % os.path.basename("test213.txt"), fp, 1024)
fp.close()

print(ftp.dir())