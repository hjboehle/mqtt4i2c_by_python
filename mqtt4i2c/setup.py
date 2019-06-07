'''
Created on 18.12.2018

@author: hjboehle
'''

from setuptools import setup

setup(name='mqtt4i2c', 
      version='0.1.0', 
      description = 'using MQTT with I2C-Devices (I2C-Configuration in a XML file)', 
      long_description = 'With MQTT4I2C it is possible to integrate I2C devices via the MQTT protocol. The configuration for the integration of the I2C devices is carried out via a configuration in a XML file.', 
      classifiers = [
          'Development Status :: 1 - Planning', 
          'Environment :: Console', 
          'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)', 
          'Natural Language :: English', 
          'Operating System :: POSIX :: Linux', 
          'Programming Language :: Python :: 3.6', 
          'Topic :: Home Automation'
          ], 
      keywords = 'I2C MQTT Raspberry Pi smarthome smart home', 
      url = 'https://github.com/hjboehle/mqtt4i2c_by_python', 
      author = 'Hans Juergen Boehle', 
      author_email = 'hj@boehle.info', 
      license = 'GPL v3', 
      packages = ['mqtt4i2c'], 
      zip_safe = False,  
      install_requires = ['paho-mqtt', 'xmlschema'])