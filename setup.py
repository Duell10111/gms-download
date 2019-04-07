import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='gms-download',  
     version='0.1',
     author="Duell10111",
     author_email="admin@duell10111.de",
     description="A GMS Download Skript",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Duell10111/gms-download",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=[
		'gmusicapi>=12.0.0',
		'loguru >=0.2, <0.3'
	],
    packages=setuptools.find_packages('src'),
	package_dir={
		'': 'src'
	},
    entry_points={
		'console_scripts': [
			'gmd = cli:run'
		]
	}
 )