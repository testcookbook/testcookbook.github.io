"""
    Note if on Mac you will need coreutils for date.
    brew install coreutils
"""

import libs.automation as at
from libs.jekyll_include import Jekyll

bash = Jekyll("bash/shpec_curl", "text")

def create_project():
    at.title("Create Project")
    cmds = """
mkdir shpec
mkdir -p shpec/matchers
"""
    bash.code("createProject", cmds)
    at.run(cmds)

def cleanup():
    at.title("Cleanup")
    cmds = """
rm -rf shpec
"""
    at.run(cmds)

def run_tests():
    at.title("Run Tests")
    cmds = """
shpec
"""
    bash.code("runTests", cmds)
    at.run(cmds)

def build_matcher1():
    cmds = """
status_200() {
  assert present "$1" "HTTP/1.1 200 OK"
}

content_type() {
  assert present "$1" "Content-Type: $2;"
}
"""
    at.write('shpec/matchers/curl_matchers.sh', cmds)
    bash.code("curl_matchers", cmds)

def first_test():
    txt = """
describe "SHPEC Curl Endpoint Test"
  start="$(date +%s%3N)"
  output="$(curl -s -i 'http://www.testcookbook.com/lib/REST/test.json')"
  end="$(date +%s%3N)"
  runtime=$((end-start))

  it "has runtime less than 1 second"
    assert lt $runtime "1000"
  end

  it "returns a 200 status code"
    assert status_200 "$output"
  end

  it "returns an application/json contentType"
    assert content_type "$output" "application/json"
  end
end
"""
    at.write('shpec/first_test_shpec.sh', txt)
    bash.code("first_test", txt)

create_project()
build_matcher1()
first_test()
run_tests()
cleanup()
