# run goodgodth.rb <with argument 5 items>
if ARGV.length != 5
  puts "Input  must be 5 arguments"
  exit
end
puts ARGV.inspect
summary = 0
ARGV.each { |item|
  summary += item.to_i
}
aveg = summary / 5.0
puts "arithmetic mean is :"+aveg.to_s
