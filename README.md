# win-virtualenv-django-startup

This script was written to help automate creation of "virtualenv" environment for Django project on Windows computer.<br/> 
So, what, exactly, this script do:<br/>
<li>creating new virtualenv environment with selected <b>name</b> in your default virtualenv folder(%HOMEDRIVE%%HOMEPATH%\Envs) </li>
<li>downloading and installing <b>latest</b> version of Django into 
created in previous step 'virtualenv' environment(Note: internet connection needed)</li>
<li>creating new Django project with selected name in selected directory
(Note: name of the Django project is the same as a name of created earlier virtualenv environment)</li>
<li>Binding virtualenv with Django project folder(newly created one)</li><br/>
<p><b>To start</b> - just run this script from your command prompt(cmd.exe). During the execution(will take about 2-3 min), 
you'll be asked to input two parameters: <b>name</b> of the project(it is also a name for your virtualenv instance)
and <b>Windows path</b> to the directory, where you want to create new Django project with selected <b>name</b>.
<b>Note</b>: virtualenv does not support parameter <i>name</i> with spaces!
 Also, before you start, you need to have <b>python, pip, virtualenv, virtualenvwrapper-win</b>  already installed onto your system.<br/>
 After installation is finished, script would wrote details
 (name of the project and its folder path) into a .txt file 
 named "virtualenv_django_startup.txt" located at %HOMEDRIVE%%HOMEPATH%\Envs if it's possible.</p>
 <p>To bind your Django project with <b>"intelliJ IDEA community edition"</b>, 
 you need to open a project within intelliJ IDEA and select "new..." project SDK in "project structure" menu(Ctrl+Alt+Shift+S).
 Then, chose a path to your python installation  inside of the virtualenv directory
 (Usually looks like this: C:\Users\some_user_name\Envs\my_project_name\Scripts\python.exe).</p>
 <p>Executed commands:
 <li>mkvirtualenv &lt;name&gt;</li>
 <li>pip install django</li>
 <li>django-admin startproject &lt;name&gt;</li>
 <li>setprojectdir &lt;path&gt;</li></p>
 
