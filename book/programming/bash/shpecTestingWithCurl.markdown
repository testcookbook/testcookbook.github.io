---
layout: default
title:  "SHPEC and Curl to test endpoints"
description: "SHPEC and Curl to test endpoints"
---
# SHPEC and Curl to test endpoints

SHPEC makes it easy to wrap some Bash commands with some assertions.  Curl is a
data transfer tool that supports a wide variety of protocols.  To test endpoints
you will be transferring data from a HTTP or HTTPS resource.

**Ingredients**

* Bash
* Curl
* Date

**Special Ingredients**

If you are running a Mac you will need to install coreutils to get the same
GNU standard options for date.  Recommended Way is to install using homebrew.

```
brew install coreutils
```

**Bake Time**

15 min.

**Instructions**

Start by creating a project structure.

{% include bash/shpec_curl/createProject.markdown %}

Within the matchers directory create a file called *curl_matchers.sh*.

{% include bash/shpec_curl/curl_matchers.markdown %}

Notice that there are 2 matcher functions one for Status code and one for
Content-Type.  

The function *status_200()* takes in 1 argument $1 which will be the data returned
back from Curl.

The function *content_type()* will take 2 arguments $1 and $2.  $1 is the data
that comes from Curl and $2 is the Content-Type that we are looking for.

Once you have your matchers create a new file called *first_curl_shpec.sh* and
put in the following code.

{% include bash/shpec_curl/first_test.markdown %}

You will notice that immediately after the describe block there is a start,
output, end and runtime. The start and end variables get the time before and
after the Curl command.  This will allow us to calculate the milliseconds that
it took to run that specific command.  The difference of these 2 values will be
stored in runtime.

The other major variable that we are using is output.  This is where we are
storing the data returned from Curl.

Curl it self has a couple arguments that will help in producing the data we need
to create some useful tests.

```
curl -s -i some-url
```

The *-s* is used to suppress the progress bar from coming back in our data.  The
 *-i* adds header information to the return value.  This is where we can see
things like Content-Type, Cookies, etc.

This will produce a result like the following and returns it within the output
variable.

```
$ curl -s -i 'http://www.testcookbook.com/lib/REST/test.json'
HTTP/1.1 200 OK
Server: GitHub.com
Date: Mon, 28 Nov 2016 15:40:54 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 25
Last-Modified: Mon, 28 Nov 2016 11:28:51 GMT
Access-Control-Allow-Origin: *
Expires: Mon, 28 Nov 2016 15:50:54 GMT
Cache-Control: max-age=600
Accept-Ranges: bytes
X-GitHub-Request-Id: 2FDE25D5:59A4:126984DF:583C5006

{
  "name": "John Doe"
}
```

Once we have our data we can run asserts on the matchers that we created.
