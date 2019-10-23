import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='cyan',
      version='1.0.0.0',
      description='Text Highlighter for CLI',
      url='https://github.com/sap218/cyan',
      author='Samantha C Pendleton',
      author_email='samanfapendle@outlook.com',
      license='MIT',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
      zip_safe=False,
      entry_points = {'console_scripts': ['cyan=cyan.cyan:main']},
      include_package_data = True
)
