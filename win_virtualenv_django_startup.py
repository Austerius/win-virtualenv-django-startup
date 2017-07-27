import subprocess
import os
import shlex
import shutil

# script author: Alexander Shums'kii
# https://github.com/Austerius
current_dir = os.getcwd()
# Getting input for new project name(same as virtualenv alias)
project_name = input("Enter a name for your new project: ")
if " " in project_name:
    print("Virtualenv doesnt support names with spaces.")
    print("Exiting...")
    os._exit(1)
print("Currently you are at: {path}". format(path=current_dir))
print("Enter full or relative path to where you wish to create new project folder \'{}\': ".format(project_name))
# Getting input for installation path (the 'path' should already exist)
installation_path = input()
# Well, we gonna check if user inputted correct path for installation
if not os.path.exists(installation_path):
    print("Path is incorrect!(example path: C:\\Users\\user\\projects_folder)")
    os._exit(1)
full_path = ""
# Ok, if inputted path consist ":"(like 'C:') - we considering it a "full/absolute path"
if ":" in installation_path:
    if installation_path[-1] == ":":
        installation_path += "\\"
    full_path = os.path.normpath(installation_path)  # normalizing our inputted path
else:
    full_path = os.path.join(current_dir, installation_path)
if " " in full_path:
    print("Virtualenv does not support spaces in file path.")
    print("Exiting...")
    os._exit(1)
# forming first command to execute in subprocess.Popen; shlex.quote - protection from command line injection
command1 = "mkvirtualenv {}".format(shlex.quote(project_name))  # creating new virtualenv alias with our project name
proc = subprocess.Popen(command1, shell=True, cwd=full_path, universal_newlines=True, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
print("Wait a bit, process executing:")
out, err = proc.communicate()
if err != "":  # if we have something in err PIPE  - then terminate script with sys.exit()
    print("Cant create virtualenv directory")
    print("Error message", err)
    os._exit(1)
if out != "":
    if "already exists" in out:
        print("Cant create virtualenv directory - it already exists")
        os._exit(1)
    else:
        print("1st command output: ", out)
# initializing default virtualenv path on Windows
default_virtualenv_path = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], "Envs")
is_all_ok = False
# checking if a default virtualenv path exist
if os.path.exists(os.path.join(default_virtualenv_path, project_name)):
    is_all_ok = True
else:
    print("Warning: cant find virtualenv installing directory. Continuing...")
# installing django into new created virtualenv
command2 = "workon {} & pip install django".format(shlex.quote(project_name))
proc = subprocess.Popen(command2, shell=True, cwd=full_path, universal_newlines=True, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
print("Wait a bit, process executing:")
out, err = proc.communicate()
if err != "":
    print("Cant install Django")
    print("Error message: ", err)
    # deleting just created virtualenv folder and exiting from script
    if is_all_ok:
        shutil.rmtree(os.path.join(default_virtualenv_path, project_name))
    os._exit(1)
if out != "":
    print("2nd command output", out)
# here we creating new django project using our virtualenv django installation
command3 = "workon {name} & django-admin startproject {name}".format(name=shlex.quote(project_name))
proc = subprocess.Popen(command3, shell=True, cwd=full_path, universal_newlines=True, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
print("Wait a bit, process executing:")
out, err = proc.communicate()
if err != "":
    print("Cant run django-admin startproject command")
    print("Error message: ", err)
    if is_all_ok:
        shutil.rmtree(os.path.join(default_virtualenv_path, project_name))  # deleting virtualenv folder before exiting
    os._exit(1)
# here we will save an absolute path to just created django project
django_dir = os.path.join(full_path, project_name)
if out != "":
    print("3d command output: ", out)
# Binding virtualenv to our new django directory
command4 = "workon {name} & setprojectdir {dir}".format(name=shlex.quote(project_name), dir=django_dir)
proc = subprocess.Popen(command4, shell=True, cwd=full_path, universal_newlines=True, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
out, err = proc.communicate()
if err != "":
    print("Cant bind virtualenv to project directory")
    print("Error message: ", err)
    if os.path.exists(django_dir):
        shutil.rmtree(django_dir)  # deleting new created django project directory
    if is_all_ok:
        shutil.rmtree(os.path.join(default_virtualenv_path, project_name))
    os._exit(1)
if out != "":
    print("4th command output: ", out)
# writing project, virtualenv name and django project path to .txt file in default virtualenv folder
# file name is virtualenv_django_startup.txt
if is_all_ok:
    txt_path = os.path.join(default_virtualenv_path, 'virtualenv_django_startup.txt')
    try:
        with open(txt_path, 'a') as changes_file:
            changes_file.write("\nCreated new virtualenv environment with name \'{name}\' and new django project at: "
                               "{path} \n".format(name=project_name, path=django_dir))
            print("Wrote results to: {}".format(txt_path))
    except Exception as e:
        print(e)
        print("Couldn't write to a file 'virtualenv_django_startup.txt', but everything else is ok!")
        print("Created new virtualenv environment with name \'{name}\' and new django project at: "
              "{path}".format(name=project_name, path=os.path.join(full_path, project_name)))

print("All processes finished execution")
