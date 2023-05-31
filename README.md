create a folder where u want to make the project
open the folder in the IDE
now create a virtual environment in the folder

------------  CREATION OF A VIRTUAL ENVIROMENT -----------------------

cd to the project folder
run python -m virtualenv 'virtual_env_name'
run virtual_env_name/Scripts/activate

----------------------------------------------------------------------

now ur virtual env is active
so now and clone the git repo directly to project folder (this folder also has the venv)
after cloning it might be so that your virtual enviroment shutsdown after
every period of use.

if that happens run & path/to/virtual/enviroment(From C:)/Scripts/Activate.ps1
with that ur virtual enviroment will be active again

now just install requirements.txt by executing pip install -r requirements.txt 
if you encounter fatal error then run python -m pip install -r requirements.txt

