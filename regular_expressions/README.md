# Regular Expressions

## Background

This project uses **Oniguruma** — the default regex library in Ruby.

Each script takes one argument and scans it using a regular expression pattern.

## Template used

```ruby
#!/usr/bin/env ruby
puts ARGV[0].scan(/REGEXP/).join
```

## Tasks

| File | Regex | Matches |
|---|---|---|
| `0-simply_match_school.rb` | `/School/` | The word "School" |
| `1-repetition_token_0.rb` | `/hbt{2,}n/` | `hbttn`, `hbttttn` (2+ t's) |
| `2-repetition_token_1.rb` | `/hbt?n/` | `hbn`, `hbtn` (0 or 1 t) |
| `3-repetition_token_2.rb` | `/hbt*n/` | `hbn`, `hbtn`, `hbttn` (0+ t's) |
| `4-repetition_token_3.rb` | `/hbt+n/` | `hbtn`, `hbttn` (1+ t's, no brackets) |
| `5-beginning_and_end.rb` | `/^h.n$/` | 3-char string: `h` + any char + `n` |
| `6-phone_number.rb` | `/^\d{10}$/` | Exactly 10 digits, nothing else |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | `/[A-Z]/` | Capital letters only |
| `8-textme.rb` | `\[from:(.+?)\]..` | Extracts sender, receiver, flags |

## Usage

```bash
chmod +x *.rb
./0-simply_match_school.rb "Best School"   # => School
./6-phone_number.rb "4155049898"           # => 4155049898
./8-textme.rb '[from:Google] [to:+1647] [flags:-1:0:-1]'  # => Google,+1647,-1:0:-1
```
