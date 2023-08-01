#!/usr/bin/env ruby

str = ARGV[0]
pattern = /(?<=\[from:)([^\]]+)\]\s*.*(?<=\[to:)([^\]]+)\]\s*.*(?<=\[flags:)([^\]]+)\]/
output = str.scan(pattern)
output.each do |match|
  puts "#{match[0]}"",""#{match[1]}"",""#{match[2]}"
end
