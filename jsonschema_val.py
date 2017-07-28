import os
import json
import jsonschema
import sys

cwd = os.getcwd()
#base_dir_abs_path = cwd+'/'+sys.argv[3]
base_dir_abs_path = cwd+'/'
#schema_path = os.path.join('/home/abhay/work/tmp_schemas', 'isco_base_schema.json')

schema_path = os.path.join(base_dir_abs_path, sys.argv[1])
with open(schema_path) as file_object:
    schema = json.load(file_object)

# Your data
#data_path = os.path.join('/home/abhay/work/tmp_schemas', 'Sample_Catalogue_Item.json')
data_path = os.path.join(base_dir_abs_path, sys.argv[2])
with open(data_path) as data_object:
    data = json.load(data_object)

# Note that the second parameter does nothing.
resolver = jsonschema.RefResolver('file://' + base_dir_abs_path + '/', None)

# This will find the correct validator and instantiate it using the resolver.
# Requires that your schema a line like this: "$schema": "http://json-schema.org/draft-04/schema#"
jsonschema.validate(data, schema, resolver=resolver)
