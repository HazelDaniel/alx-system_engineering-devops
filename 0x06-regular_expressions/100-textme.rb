#!/usr/bin/env ruby

str = ARGV[0]
pattern = /(?:(?<=\[from:)|(?<=\[to:)|(?<=\[flags:))([^\]]+)\]/
puts(str.scan(pattern).join(','))
