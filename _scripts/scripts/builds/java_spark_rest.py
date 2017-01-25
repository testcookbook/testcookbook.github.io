import libs.automation as at
import libs.jekyll_include as ji
from libs.jekyll_include import Jekyll

java = Jekyll("java/spark_rest", "java")
bash = Jekyll("java/spark_rest", "text")

def create_project():
    at.title("Create Project")
    cmds = """
mkdir restapi
cd restapi
gradle init --type=java-library
"""
    bash.code("createProject", cmds)
    at.run(cmds)

def update_build_gradle():
    at.title("Update build.gradle")
    txt = """apply plugin: 'application'
mainClassName = "RestApi"
"""
    at.replace_lines('restapi/build.gradle', 10, 11, txt);
    txt = """
    compile 'com.google.guava:guava:20.0'
    compile 'com.sparkjava:spark-core:2.5.4'
    compile 'org.slf4j:slf4j-simple:1.7.21'
"""
    at.replace_lines('restapi/build.gradle', 22, 23, txt);

def build_package():
    at.title("Build Packages")
    cmds = """
cd restapi
gradle build
"""
    bash.code("installPackages", cmds)
    at.run(cmds)

def cleanup():
    at.title("Clean up!")
    cmds = """
rm -Rf restapi
"""
    at.run(cmds)

def run_tests():
    at.title("Running Tests")
    cmds = """
cd restapi
gradle test
"""
    bash.code("runTest", cmds)
    return at.run(cmds)

def main_java():
    txt = """
import static spark.Spark.*;

public class RestApi {
    public static void main(String[] args) {
        get("/", (req, res) -> "Root Route");
        get("/hello", (req, res) -> "Hello World");
    }
}
"""
    at.write("restapi/src/main/java/RestApi.java", txt)
    java.code("RestApi", txt)

cleanup()
create_project()
update_build_gradle()
build_package()
main_java()

#test_script()
run_tests()
cleanup()
