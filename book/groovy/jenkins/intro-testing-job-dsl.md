---
layout: default
---
# Testing Jenkins Job-Dsl scripts

Setting up Jenkins can feel like a daunting task if you are not into it an using it every day.  What is even more annoying at times is when either failure happens or you need to upgrade some plugin or the version of Jenkins itself.  

For those that like to code or script things, we can take some of the tediousness out of the whole process and allow you to get upfront messages describing the issue rather than waiting on Jenkins to fail.  You don't wanna be that guy that caused the builds to fail, do you?

So what does a Jenkins job look like as code?  Using the Job-Dsl plugin they look like the following.

*Sample Jenkins Job*
```groovy
freeStyleJob('Sample Job') {
    steps {
        shell('ls')
    }
}
```

This particular script really doesn't do a whole lot.  It creates a job called Sample Job on Jenkins and runs a bash command to list the files out on the workspace.  For our initial testing, this will work just fine.

If you would like to follow along with a working demo feel free to clone this repo. https://github.com/testcookbook/jenkins_harness

## Organizing the Jenkins harness

Now that you know what a simple job looks like we need to organize our dependencies.  Things like what version of Jenkins we want to use, and what plugins we need.  These are handled through the dependencies section of the build.gradle file.  

The first set of dependencies we need are the ones to compile the groovy scripts so that we can run tests against them.  In some demos, you may find they do not include ivy like we did below.  If you decide to use groovy grape for your scripts you will need to include it.  Make sure that your version number for the job-dsl-core matches what you want to use on your Jenkins build.

```groovy
dependencies {
    compile "org.jenkins-ci.plugins:job-dsl-core:1.5.9"
    compile "org.apache.ivy:ivy:2.4.0"
}
```

After these, we need to add the Spock framework for testing and Jenkins test harness.  Pay close attention to the versioning of the ones labeled jenkins-war.  That version will be the version of Jenkins that you are using.

```groovy
dependencies {
    compile "org.jenkins-ci.plugins:job-dsl-core:1.59"
    compile "org.apache.ivy:ivy:2.4.0"

    testCompile "org.spockframework:spock-core:1.1-groovy-2.4"
    // Jenkins Test Harness
    testCompile "org.jenkins-ci.main:jenkins-test-harness:2.26"
    testCompile "org.jenkins-ci.main:jenkins-war:2.46.2"
    testCompile "org.jenkins-ci.main:jenkins-war:2.46.2:war-for-test@jar"
}
```

Lastly, add your plugins. One of the mandatory plugins for this will be the job-dsl plugin.  Again make sure that the versions of these plugins match what you are expecting to run.

```groovy
dependencies {
    compile "org.jenkins-ci.plugins:job-dsl-core:1.5.9"
    compile "org.apache.ivy:ivy:2.4.0"

    testCompile "org.spockframework:spock-core:1.1-groovy-2.4"
    // Jenkins Test Harness
    testCompile "org.jenkins-ci.main:jenkins-test-harness:2.26"
    testCompile "org.jenkins-ci.main:jenkins-war:2.46.2"
    testCompile "org.jenkins-ci.main:jenkins-war:2.46.2:war-for-test@jar"

    // Job DSL plugin including dependencies
    testCompile "org.jenkins-ci.plugins:job-dsl:1.59"
    testCompile "org.jenkins-ci.plugins:job-dsl:1.59@jar"
    testCompile "org.jenkins-ci.plugins:structs:1.6@jar"

    // Jenkins plugins to install
    testPlugins "org.jenkins-ci.plugins:ghprb:1.31.4"
    testPlugins "com.coravy.hudson.plugins.github:github:1.19.0"
}
```

You may notice now that there are some versions of things that you have to write multiple times.  More than likely you may want to change or upgrade versioning on all of these.  An easier way to manage this is to create a variable that will store those common values.  Notice the ext closure with 2 variables jobDslVersion and jenkinsVersion.  

```groovy
ext {
    jobDslVersion = '1.59'
    jenkinsVersion = '2.46.2'
}

dependencies {
    compile "org.jenkins-ci.plugins:job-dsl-core:${jobDslVersion}"
    compile "org.apache.ivy:ivy:2.4.0"

    testCompile "org.spockframework:spock-core:1.1-groovy-2.4"

    // Jenkins Test Harness
    testCompile "org.jenkins-ci.main:jenkins-test-harness:2.26"
    testCompile "org.jenkins-ci.main:jenkins-war:${jenkinsVersion}"
    testCompile "org.jenkins-ci.main:jenkins-war:${jenkinsVersion}:war-for-test@jar"

    // Job DSL plugin including dependencies
    testCompile "org.jenkins-ci.plugins:job-dsl:${jobDslVersion}"
    testCompile "org.jenkins-ci.plugins:job-dsl:${jobDslVersion}@jar"
    testCompile "org.jenkins-ci.plugins:structs:1.6@jar"

    // Jenkins plugins to install
    testPlugins "org.jenkins-ci.plugins:ghprb:1.31.4"
    testPlugins "com.coravy.hudson.plugins.github:github:1.19.0"
}
```

## Testing

Once you have your predefined Jenkins harness setup with all the appropriate plugins, it is time for your first test.  This test will be run on all of the groovy files within the jobs directory.  What we want to do is load each script and look to see if any exceptions are thrown.  If there are exceptions then that will mean either we have an error in syntax, a missing method, and sometimes it could mean a wrong version of the plugin being used.

To get started we will create a new file called JobScriptsSpec.groovy in the src/test/groovy/ directory.

```groovy
import javaposse.jobdsl.dsl.DslScriptLoader
import javaposse.jobdsl.plugin.JenkinsJobManagement
import org.junit.ClassRule
import org.jvnet.hudson.test.JenkinsRule
import spock.lang.Shared
import spock.lang.Specification
import spock.lang.Unroll

class JobScriptsSpec extends Specification {
    @Shared
    @ClassRule
    JenkinsRule jenkinsRule = new JenkinsRule()

    @Unroll
    def 'test script #file.name'(File file) {
        given:
        def jobManagement = new JenkinsJobManagement(System.out, [:], new File('.'))

        when:
        new DslScriptLoader(jobManagement).runScript(file.text)

        then:
        noExceptionThrown()

        where:
        file << jobFiles
    }

    static List<File> getJobFiles() {
        List<File> files = []
        new File('jobs').eachFileRecurse {
            if (it.name.endsWith('.groovy')) {
                files << it
            }
        }
        files
    }
}
```

From glancing at this code there are 2 main parts.  The test defined after the @Unroll, and the list function called getJobFiles. If you are unfamiliar with groovy the @Unroll allows us to iterate over a subset of data.  In the case of our tests that will be the files found with the getter getJobFiles. This test will load each script one by one, load it into the Jenkins harness, run the script with the DslScriptLoader and test if an exception is thrown.

If you are using the sample repo you may notice that Gradle wrapper is included.  To run the tests.

```
# Linux / Mac
./gradlew test

# Windows
gradlew.bat test
```