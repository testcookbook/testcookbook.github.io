---
layout: default
---
# Unit Test in Rust

Lets get started very quick an dirty with a new library.  

```
$ cargo new example_test
Created library `example_test` project
```

That should give you a new folder in your current directory with a structure like.

```
$ tree
.
├── Cargo.lock
├── Cargo.toml
├── src
│   └── lib.rs
```

Now that we have a project let's start testing.  Take a look at "lib.rs"

**lib.rs**
```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
    }
}
```

Well what do you know right from the start of creating a new project is a sample test module.
Though there is now a simple test it really doesn't do anything useful.  However if you are new
to Rust and want to see something run go ahead and watch everything pass.

```
cargo test
```

## Assertions

As it was just mentioned this test really does nothing useful at all.  All it does is run a 
test function and never asserts anything.  Let's change that by demonstrating 3 different 
assert macros.  

* assert! - Asserts based on a boolean. 
* assert_eq! - Asserts based on equality of 2 objects.
* assert_ne! - Asserts based on no equality of 2 objects.

In the "it_works" functions try out some examples and run them to see how things work.

```rust
#[test]
fn it_works() {
    //Passing Assertion
    assert!(true); 
    assert_eq!(1, 1);
    assert_ne!(1, 2);
}
```

```
$ cargo test 

Compiling example_test v0.1.0 (file:///working_dir/example_test)
      Finished dev [unoptimized + debuginfo] target(s) in 1.29 secs
       Running target/debug/deps/example_test-938c230a543dbf89
  
  running 1 test
  test tests::it_works ... ok
  
  test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured
  
     Doc-tests example_test
  
  running 0 tests
  
  test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured
```

## Testing your library.

Now that you know how to do some basic assertions you can now expand the knowledge. Let's 
write a test that will add 2 numbers and return a result.

```rust
pub fn add(a: i32, b:i32) -> i32 {
    return a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn add_test() {
        assert_eq!(add(2,2), 4);
    }
}
```