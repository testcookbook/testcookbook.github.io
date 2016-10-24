---
layout: default
title:  "Validating JSON with Ruby"
description: "Simple how to validate JSON format with Ruby"
---
# Validating JSON with Ruby

There are a couple of different steps to determining whether a JSON is correct.
The first and most important is to determine if the JSON document that you
received has all the right commas, quotes, and format that it can be read.  To
do this we can create a simple function that will return true or false.  We will
read in the json and pass it to the JSON.parse function.  If it fails then the
rescue will fire up and allow the function to return false.

```ruby
require 'json'

def is_json_valid(json)
  begin
    JSON.parse(json)
    return true
  rescue JSON::ParserError => e
    return false
  end
end
```

<div class="w3-panel w3-pale-yellow w3-bottombar w3-topbar w3-border-green">
{% include tipIcon.html%}
If you wanted a little more information on the error you could also add an
output to the console or custom log.
</div>

The second important step in validating your JSON file is to compare it with a
JSON schema validation.  To do this we will start by importing a gem called
json-schema.

<div class="w3-card">
<header class="w3-container w3-grey">
  {% include cliIcon.html%}
  Command Line
</header>
<div class="w3-container">
{% highlight shell %}
$ gem install json-schema
{% endhighlight %}
</div>
</div>

After the gem is installed you can start crafting your Ruby code.

```ruby
require 'json'
require 'json-schema'

def validate(schema, file)
  begin
    JSON::Validator.validate(schemaJson, fileJson)
    return true
  rescue
      JSON::Schema::ValidationError => e
      return e.message
  end
end

file = File.read('someFile.json')
schema = File.read('someSchema.json')
validate(JSON.parse(schema), JSON.parse(file))
```

The validate function will either return true or the error message.  You could
also have it just return true or false.  It really depends on what kind of
information you would like to deal with.


You could also whip up a little RSpec magic to test your JSON as well.

```ruby
require 'json'
require 'json-schema'

def validate(schema, file)
  begin
    JSON::Validator.validate(schemaJson, fileJson)
    return true
  rescue
      JSON::Schema::ValidationError => e
      return e.message
  end
end

file = File.read('someFile.json')
schema = File.read('someSchema.json')

RSpec.describe "Is JSON Valid" do
  it 'should be a valid JSON' do
    expect(validate(JSON.parse(schema), JSON.parse(file))).to be_truthy
  end
end

```
