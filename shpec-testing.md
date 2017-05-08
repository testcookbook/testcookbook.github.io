# Introduction to SHPEC {#introduction-to-shpec}

SHPEC brings a simple yet powerful ability to testing bash scripts, or even testing other systems using a set of bash commands. Getting started you will need a few ingredients.

**Ingredients**

* Bash - If using Linux or Mac this is easy. On Windows if you have Git bash that will work too.
* SHPEC - Install from
  [https://github.com/rylnd/shpec](https://github.com/rylnd/shpec)

**Bake Time**

* 5 min

**Instructions**

Start off by creating a directory to build tests in.

```bash
mkdir shpec
```

Create a file called “first\_test\_shpec.sh” and fill it with the code below.

```bash
describe "test"
  it "works"
    assert equal "test" "test"
   end
end

```

Lastly run the tests.

```bash
shpec
```

Now that you have a simple set of tests experiment using some of the other matchers available.

```
Binary Matchers
equal         # equality
unequal       # inequality
gt            # algebraic '
>
'
lt            # algebraic '
<
'
match         # regex match
no_match      # lack of regex match

Unary Matchers
present       # string presence
blank         # string absence
file_present  # file presence
file_absent   # file absence
symlink       # tests a symlink's target
test          # evaluates a test string
```



