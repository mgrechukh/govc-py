from setuptools import setup

setup(name='govc',
      version='1.0',
      description='install govc binary',
      author='Mykoa Grechukh',
      author_email='mgrechukh@satelliz.com',
      packages=["govc"],
      entry_points={
          "console_scripts": [
              "govc = govc.__main__:main"
          ]
      }
)
