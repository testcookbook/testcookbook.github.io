import automation as at
import jekyll_include as ji
from jekyll_include import Jekyll

python = Jekyll("python/introPythonTest", "python")
bash = Jekyll("python/introPythonTest", "text")

def create_project():
    at.title("Create Project")
    cmds = """
mkdir -p firstTest
cd firstTest
mkdir features
mkdir step_definitions
npm init -f
"""
    bash.code("createProject", cmds)
    at.run(cmds)

def install_package():
    at.title("Install Packages")
    cmds = """
cd firstTest
npm install cucumber assert --save-dev
ls
"""
    bash.code("installPackages", cmds)
    at.run(cmds)

def test_script():
    s = at.getJson('firstTest/package.json')
    s["scripts"]["test"] = "./node_modules/.bin/cucumber-js"
    at.write_json('firstTest/package.json', s)

def cleanup():
    at.title("Clean up!")
    cmds = """
rm -Rf firstTest
"""
    at.run(cmds)

def run_tests():
    at.title("Running Tests")
    cmds = """
cd firstTest
npm test
"""
    bash.code("runTest", cmds)
    return at.run(cmds)

cleanup()
create_project()
install_package()
test_script()
run_tests()
cleanup()
