from datetime import datetime
import subprocess

if __name__ == '__main__':
    # time format: hour min sec
    target_time = 232323
    print('start successfully')
    while True:
        now = datetime.now().time()
        formatted_now = int(now.strftime('%H%M%S'))
        if target_time - formatted_now <= 1 and target_time - formatted_now > 0:
            subprocess.run(['python', './xxx.py'])
