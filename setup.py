
from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))

setup(
  name = 'brainly_scraperbr',        
  packages = ['brainly_scraperbr'],   
  version = '0.0.6T',    
  license='MIT',     
  description = 'brainly scraper brasil', 
  author = 'bieldlucacn',                  
  author_email = 'aaa@gmail.com',     
  url = 'https://github.com/bieldlucacn/brainly-scraper-br',       
  keywords = ['brainly', 'scraper','brasil'], 
  install_requires=[           
          'requests',
          'html_text'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)