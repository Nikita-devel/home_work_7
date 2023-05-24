from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.1',
    description='Sorting files be category',
    url='https://github.com/Nikita-devel/home_work_7',
    author='Chumak Nikita',
    author_email='brseven90@gmail.com',
    license='UA',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.sort:main']}
)