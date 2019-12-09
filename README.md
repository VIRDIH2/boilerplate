# README

## Creating a Virtual Environment
To work with this solution, you will need to create a virtual environment in Python using Ian Bicking’s virtualenv

To install virtualenv use pip install 
```
$ python -m pip install virtualenv 
```

Once this is installed, you can create the virtual environment by typing in
```
$ python -m venv {Dev Folder}\EnvName
```
`EnvName` is the name of the virtual environment you’re going to create. This command will create a subdirectory named `EnvName` containing all the stuff you need, the python interpreter and the pip utility, in `{Dev Folder}` 

## Activating a Virtual Environment
Once you have created a virtual environment, you will need to activate it. To activate the environment, open a command prompt and execute the “activate” script that you will find in the `EnvName/Scripts` directory

```
>  {Dev Folder}\EnvName\bin\activate
```

## Installing Packages in a Virtual Envrironment 

To install individual packages
```
$(EnvName) pip install packagename --trusted-host pypi.org --trusted-host files.pythonhosted.org
```

To install from requirements.txt
```
pip install -r {Dev Folder}\requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
```
Use this method if the environment is being set up for the first time and a requirements.txt is provided. 

**NOTE** 

After installing, be sure to update the ```requirements.txt``` file. Use pip's freeze command to generate or update a requirements.txt file for your project:

```
$(EnvName) pip freeze > {Dev Folder}\requirements.txt
```

## Running Test Cases
To run all test cases in one step
```
python -m unittest discover -s "unittest" 
```
`unittest` is the path or folder that contains all your test cases

## Known Issues 
pip install fails with SSL certificate verify failed
```ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify faile```

You can solve the problem by using this command 
```
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>
```

Microsoft Visual C++ 14.0 is required
	Go to Build Tools for Visual Studio 2017

	Select free download under Visual Studio Community 2017. This will download the installer. Run the installer.

	Select what you need under workload tab:

	Under Windows, there are 3 choices. Only check Desktop development with C++

