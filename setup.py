from setuptools import setup

setup(name='MCP23XXX',
      version='0.0.3',
      description='CraftBeerPi Plugin',
      author='Lawrence Wagy',
      author_email='lnwagy@gmail.com',
      url='',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],          
      'MCP23XXX': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['MCP23XXX'],
     )
