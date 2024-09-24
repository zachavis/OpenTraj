from setuptools import setup, find_packages

setup(
   name='opentraj',
   version='1.0',
   author='Javad Amirian',
   author_email='amiryan.j@gmail.com',
   packages=find_packages(),
#    scripts=['bin/script1','bin/script2'],
   url='https://github.com/crowdbotp/OpenTraj',
   license='MIT',
   description='Tools for analyzing trajectory datasets',
   long_description=open('README.md').read(),
   install_requires=[
        "numpy",
        "scipy",
        "scikit-learn",
        "pandas",
        "tqdm",
        "pykalman", 
        "PyYAML",       
   ],
   extras_require={
        'test': [
            "pylint",
            "pytest",
        ],
        'plot': [
            "matplotlib",
            "seaborn",
        ]
   }
)
