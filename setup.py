import setuptools

__version__ = '0.0.1'

Repo_Name = 'CNNClassifier'
Author_Name = 'Devendra Goswami'
Src_Repo = 'CNNClassifier'
Author_Email = 'pdevendragoswami@gmail.com'

with open('README.md','r') as file:
    long_description = file.read()

setuptools.setup(
    name = Src_Repo,
    version = __version__,
    author = Author_Name,
    author_email = Author_Email,
    description = 'End to end Image Classification',
    long_description = long_description,
    long_description_content = 'text/markdown',
    url = f"https://github.com/{Author_Name}/{Repo_Name}",
    project_url = {"Bug Tracker":f"https://github.com/{Author_Name}/{Repo_Name}"},
    package_dir = {"":"src"},
    packages=setuptools.find_packages(where='src')

)