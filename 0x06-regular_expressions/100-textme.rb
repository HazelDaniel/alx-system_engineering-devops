#!/usr/bin/env ruby

str = ARGV[0]
pattern = /(?:(?<=\[from:)|(?<=\[to:)|(?<=\[flags:))([^\]]+)\]/
output = str.scan(pattern).join(",")
puts output
