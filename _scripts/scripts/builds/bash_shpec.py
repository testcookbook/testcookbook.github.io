import sys
sys.path.append("../")

import libs.automation as at
from libs.jekyll_include import Jekyll

bash = Jekyll("bash/shpec", "text")

def create_project():
    at.title("Create Project")
    cmds = """
mkdir shpec
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

def first_test():
    txt = """
describe "test"
  it "works"
    assert equal "test" "test"
   end
end
"""
    at.write('shpec/first_test_shpec.sh', txt)
    bash.code("first_test", txt)

create_project()
first_test()
run_tests()
cleanup()
