# Validating JSON with Python

JSON or Javascript object notation works quite well in Python.  There are 2 possible attributes that we need to look at to tell whether or not the JSON is in a proper format.  The first is making sure all the quotes, brackets and commas are in the right place.  The second is validating that result to a JSON schema.


## Validate basic JSON syntax

***test.py***

```python
import json

def validate_json_syntax(d):
    try:
        return json.loads(d)
    except ValueError:
        print('DEBUG: JSON data contains an error')
        return False

#will return the data
data = '{"firstName": "John", "lastName": "Doe"}'
print validate_json_syntax(data)

#will return false because JSON not valid
#missing quotes around lastName
data = '{"firstName": "John", lastName: "Doe"}'
print validate_json_syntax(data)
```

Run the test to see what output looks like.

***Terminal***
```
$ python test.py
{u'lastName': u'Doe', u'firstName': u'John'}
DEBUG: JSON data contains an error
False
```
Once we have loaded the JSON and we know that it is syntactically correct. We can now start testing the JSON schema. Lets load up that test.py again and add JSON schema.

***test.py***
```python
import json
from jsonschema import validate

def validate_json_syntax(d):
    try:
        return json.loads(d)
    except ValueError:
        print('DEBUG: JSON data contains an error')
        return False

data = '{"firstName": "John", "lastName": "Doe"}'
jsd = validate_json_syntax(data)

schema = {
    "type": "object",
    "properties": {
      "firstName": { "type": "string"},
      "lastName": { "type": "string"}
    }
}
#output will be None
print(validate(jsd, schema))

```
This just happens to be a happy path example for a JSON schema validation.  But what if for some reason we really wanted the lastName to be a number? Within the schema change type to number.  Then run the program and see what happens.

```python
schema = {
    "type": "object",
    "properties": {
      "firstName": { "type": "string"},
      "lastName": { "type": "number"}
    }
}
```

You should have some output that looks like.

***Terminal***
```
$ python test.py
jsonschema.exceptions.ValidationError: u'Doe' is not of type 'number'

Failed validating 'type' in schema['properties']['lastName']:
    {'type': 'number'}

On instance['lastName']:
    u'Doe'
```