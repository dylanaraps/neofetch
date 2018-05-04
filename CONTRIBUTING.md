# How to Contribute


## ShellCheck

For your contribution to be accepted, your changes need to pass
ShellCheck.

Run ShellCheck with the following command:

```sh
# Why do we exclude numerous tests?
# See: https://github.com/dylanaraps/neofetch/wiki/Shellcheck-Exclusions
shellcheck neofetch -e SC1090,SC2009,SC2012,SC2016,SC2034,SC2128,SC2153,SC2154,SC2178,SC2010,SC1004,SC1091,SC1117
```

**Note**: If you have trouble installing ShellCheck. You can open a pull
request on the repo and our Travis.ci hook will run ShellCheck for you.


## Coding Conventions

- Indent 4 spaces.
- Use [snake_case](https://en.wikipedia.org/wiki/Snake_case) for function
  and variable names.
- Keep lines below `100` characters long.
- Use `[[ ]]` for tests.


## No no's

- Don’t use `bc`.
- Don’t use `sed`.
    - Use `bash`'s built-in [parameter expansion](http://wiki.bash-hackers.org/syntax/pe).
- Don’t use `cat`.
    - Use `bash`'s built-in syntax (`file="$(< /path/to/file.txt)")`).
- Don’t use `grep "pattern" | awk '{ printf }'`.
    - Use `awk '/pattern/ { printf }'`


## If Statements

If the test only has one command inside of it; use the compact `if`
syntax. Otherwise the normal `if`/`fi` is just fine.

```sh
# Bad
if [[ "$var" ]]; then
    echo "$var"
fi

# Good
[[ "$var" ]] && echo "$var"

# Also good (Use this for longer lines.
[[ "$var" ]] && \
    echo "$var"
```


## Case Statements

Case statements need to be formatted in a specific way.

```sh
# Good example (Notice the indentation).
case "$var" in
    1) echo 1 ;;
    2)
        echo 1
        echo 2
    ;;

    *)
        echo 1
        echo 2
        echo 3
    ;;
esac
```
