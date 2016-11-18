import os

class Jekyll:
    def __init__(self, project, language):
        self.project = project
        self.language = language

    def code(self, diagram, text):
        fn = os.getcwd() + "/../_includes/" + self.project + "/" + diagram + ".markdown"
        f = open(fn , 'w+')
        #s = "{% highlight" + language "%}"
        #e = "{% endhighlight %}"
        s = "```"+self.language
        e = "```"
        f.write(s + text + e)
        f.close()
