"""
component_reqs.py

Note the places you need to change to make it work for you. 
They are marked with keyword 'TODO'.
"""

## TODO: here goes the list of the environment variables, if any,
## required to export for the component to function properly.
env_vars = {
# 			'env_var1' : ['value1', 'value2'],
# 			'env_var2' : 'value3'
			}

## TODO: here goes the max amount of the memory required. 
memory = '20G'

## TODO: set this to True if the component is parallelizable.
parallel = False

## TODO: here goes the list of the required software/apps
## called by the component.  
requirements = {
				'star_binary': '__REQUIRED__',
				}

## TODO: here goes the version of the component seed.
seed_version = '2.4.2a'

## TODO: here goes the version of the component itself. 
version = '1.0.0'
