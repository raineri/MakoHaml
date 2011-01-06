from setuptools import setup

setup(name='makohaml',
      version = '0.1',
      packages = ['makohaml'],
      author = 'Jesse Miller, Raineri Bello',
      author_email = 'raineri.bello@gmail.com',
      description = 'HAML like syntax for Mako templates',
      keywords = 'haml mako converter',
      url = 'http://github.com/raineri/MakoHaml',
      
      entry_points = {
          'console_scripts' : ['makohaml = makohaml.makohaml:convert_files',
                               'makohaml-watcher = makohaml.makohaml_watcher:watch_folder']
      }
    )
