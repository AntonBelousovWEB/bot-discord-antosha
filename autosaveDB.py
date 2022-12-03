import time
import subprocess

subprocess.check_call(['git', 'config', '--global', 'user.name', '"BoRoDaTeNkiY"'])
subprocess.check_call(['git', 'config', '--global', 'user.email', '"polpoltrop228@gmail.com"'])
subprocess.check_call(['git', 'init'])
subprocess.check_call(['git', 'remote', 'add', 'origin', f'https://BoRoDaTeNkiY:{}@github.com/BoRoDaTeNkiY/db2.git'])

while True:
    time.sleep(60)
    subprocess.check_call(['git', 'add', 'bot.db'])
    subprocess.check_call(['git', 'commit', '-m', 'updated_DataBase'])
    subprocess.check_call(['git', 'push', 'origin', 'master', '--force'])
    print("Database is updated!")
