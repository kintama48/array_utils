from distutils.core import setup
setup(
  name = 'array_utils',         
  packages = ['array_utils'],   
  version = '0.1',      
  license='AFL-3.0',        
  description = 'Contains some common numpy array methods', 
  author = 'Abdullah_Baig',                   
  author_email = 'rebelschaos@gmail.com',      
  url = 'https://github.com/kintama48/',   
  download_url = 'https://github.com/kintama48/array_utils/archive/refs/tags/v_0.1.tar.gz',    
  keywords = ['AMAX', 'AMIN', 'LINSPACE', 'WITHOUT NUMPY'],   
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: AFL-3.0',  
    'Programming Language :: Python :: 3',
    "Operating System :: OS Independent",
  ],
)
