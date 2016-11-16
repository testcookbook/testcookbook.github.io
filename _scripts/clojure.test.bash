function create_project {
  lein new funapp
  cd funapp
}

function cleanup {
  cd ..
  rm -Rf funapp
}

function run_tests {
  lein test
}

function step1_passing_test {
  sed -i "s/0/1" test/funapp/core_test.clj
}
create_project
run_tests

step1_passing_test
run_tests

cleanup
