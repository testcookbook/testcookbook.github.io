def include(project, diagram, text):
    fn = "../" + project + "/" + diagram + ".markdown"
    f = open(fn , 'w+')
    f.write(txt)
    f.close()

def code(project, diagram, text, language):
    fn = "../_includes/" + project + "/" + diagram + ".markdown"
    f = open(fn , 'w+')
    #s = "{% highlight" + language "%}"
    #e = "{% endhighlight %}"
    s = "```"+language
    e = "```"
    f.write(s + text + e)
    f.close()

class Jekyll:
    def __init__(self, project, language):
        self.project = project
        self.language = language

    def code(self, diagram, text):
        fn = "../_includes/" + self.project + "/" + diagram + ".markdown"
        f = open(fn , 'w+')
        #s = "{% highlight" + language "%}"
        #e = "{% endhighlight %}"
        s = "```"+self.language
        e = "```"
        f.write(s + text + e)
        f.close()
