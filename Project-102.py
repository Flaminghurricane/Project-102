import cv2
from cv2 import VideoCapture
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=VideoCaptureObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print("Snapshot has been taken")
    VideoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()

def upload_file(image_name):
    access_token='sl.BIL6jWBaCKBjfKHWhcr4wki-u-Cz7ZK3I7wNnjT1S9J5OcgW_fH5wJOyv1YIpJ7LiUHx2SeJocR7xpl_MeMLHGBqV15gJHntE9UR2Y6vxiZEfJ__StSS89ZeoGobYf7O8nRAuxY'
    file=image_name
    file_from=file
    file_to="/newFolder102"+(image_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overWrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=3):
            name=take_snapshot()
            upload_file(name)
main()
