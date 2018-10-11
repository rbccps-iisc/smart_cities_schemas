#!/bin/bash
for filename in ./example_items/*.json; do
     echo $filename
     python jsonschema_val.py $filename
done
