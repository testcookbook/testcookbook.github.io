import automation as at
import jekyll_include as ji
from jekyll_include import Jekyll

global clojure
clojure = Jekyll("clojure/IntroClojureTest", "clojure")
bash = Jekyll("clojure/IntroClojureTest", "text")

def title(t):
    print "**************************************"
    print t
    print "**************************************"

def create_project():
    title("Create Project")
    cmds = """
lein new funapp
"""
    bash.code("createProject", cmds)
    at.run(cmds)

def cleanup():
    title("Clean up!")
    cmds = """
rm -Rf funapp
"""
    at.run(cmds)

def run_tests():
    title("Running Tests")
    cmds = """
cd funapp
lein test
"""
    bash.code("runTest", cmds)
    return at.run(cmds)

def fix_first_test():
    s = "    (is (= 1 1))))"
    at.replace_lines("funapp/test/funapp/core_test.clj", 6, 7, s)
    clojure.code("addListTest", s)

def add_list_test():
    s = """
(deftest addList-test
  (testing "Function should add up all numbers in the list"
    (is (= 6 (addList [1 2 3])))))
"""
    at.append("funapp/test/funapp/core_test.clj", s)
    clojure.code("addListTest", s)

def add_list_src():
    s = """
(defn addList
  "This will add all the numbers in a list"
  [x]
  (reduce + x))
"""
    at.append("funapp/src/funapp/core.clj", s)
    clojure.code("addList", s)
    #ji.code("clojure", "addList", s, "clojure")

cleanup()
create_project()
assert run_tests() == 1
fix_first_test()
assert run_tests() == 0
add_list_test()
assert run_tests() == 1
add_list_src()
assert run_tests() == 0
cleanup()
