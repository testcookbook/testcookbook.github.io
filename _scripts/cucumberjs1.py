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
mkdir -p features/step_definitions
mkdir -p features/support
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

def first_feature():
    txt = """
Feature: First Test
    Scenario: Adding Numbers
        Given numbers 2 and 5
        When they are added together
        Then the total should be 7
"""
    at.write('firstTest/features/first_feature.feature', txt)

def first_steps():
    txt = """
var assert = require('assert');
module.exports = function () {
    var a, b, t;
    this.Given(/^numbers (\d+) and (\d+)$/, function (arg1, arg2) {
        a = Number(arg1);
        b = Number(arg2);
    });

    this.When(/^they are added together$/, function () {
        t = a + b;
    });

    this.Then(/^the total should be (\d+)$/, function (arg1) {
        assert.equal(t, 7);
    });
}
"""
    at.write('firstTest/features/step_definitions/first_steps.js', txt)


cleanup()
create_project()
install_package()
test_script()
run_tests()
first_feature()
run_tests()
first_steps()
run_tests()
cleanup()
