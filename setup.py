import os
import platform

# rasa installation instructions

if platform.system() == 'Linux':
  os.system('python3 -m pip install virtualenv')
  os.system('python3 -m venv ./venv2')
  os.system('. ./venv2/bin/activate; pip3 install -U pip setuptools wheel')
  os.system('. ./venv2/bin/activate; pip install -r requirements.txt')

else:
  print("Use Linux Operating System")


