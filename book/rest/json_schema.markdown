---
layout: default
title:  "JSON Schema"
description: "Introduction to JSON schema."
---
# JSON Schema

JSON schema is a tool or document that provides a definition to a JSON document.
With a JSON schema you can validate and define what you can send or receive.
This is especially useful when you are working with a 3rd party as a consumer or
a provider.  

From a testing perspective a JSON schema gives us a clear way to understand and
validate responses, while at the same time we can also validate things that we
mock. I know what you might be thinking.  You mean we can test the things we are
testing with. To some degree yes.  From experience when I have worked on
projects where things are rapidly changing it can be hard to really understand
what changed and what tests I might need to adapt.  However using a JSON schema
can potentially help resolve finding some direction.

Now to start off we really need to build the most basic JSON schema that we can
come up with.

```json
{ }
```

It sure doesn't look like much does it.  In reality it isn't much.  It is just
an empty object in JSON format.  JSON schema itself is a JSON document.  Lets
try to make that schema a little more useful.  Lets say we need to get a JSON
response from the Telephone company, that contains a first name, last name, and
a telephone number. An example response is.

```json
{
  "firstName": "John",
  "lastName": "Doe",
  "phoneNumber": "(555)-888-5555"
}
```

Our schema for this would look like.

```json
{
  "title": "Telephone company response",
  "type": "object",
  "properties": {
    "firstName": {
      "type": "string"
    },
    "lastName": {
      "type": "string"
    },
    "phoneNumber": {
      "type": "string"
    }
  }
}
```

Awesome now we could validate our response from the Telephone company and test
that it is what it should be.  One thing to know about JSON schema is you can
also make certain things required or very strict if needed.  In this current
example for instance if the response didn't return a phoneNumber, then the
schema still passes.  However if the phone number came back as a 5558885555,
then it would have failed saying something like output was not a string.

Lets assume though that we have to have all 3 of those fields.  To do that we
can add one simple statement to the JSON schema.  Required.

```json
{
  "title": "Telephone company response",
  "type": "object",
  "properties": {
    "firstName": {
      "type": "string"
    },
    "lastName": {
      "type": "string"
    },
    "phoneNumber": {
      "type": "string"
    }
  },
  "required": ["firstName", "lastName", "phoneNumber"]
}
```

Now if the Telephone company sends a response without firstName, lastName, or
phoneNumber the schema will be invalid.

As you can see a JSON schema can be a valuable tool to both yourself and those
you may have to work with.  I would recommend that if you are working with other
providers or consumers that you provide the schema or ask for one.  These make
excellent contracts to work with and can ease communications during discussions.
