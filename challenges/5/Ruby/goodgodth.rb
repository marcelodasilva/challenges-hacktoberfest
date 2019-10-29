#run goodgodth.rb <number1> <number2>
if ARGV.length != 2
  puts "Input must be 2 arguments"
  exit
end
if ARGV[0].to_i == ARGV[1].to_i
  puts "All number equals"
else
  puts (ARGV[0].to_i > ARGV[1].to_i) ? ARGV[0].to_s : ARGV[1].to_s
end
#puts (ARGV[0].to_i > ARGV[1].to_i) ? ARGV[0].to_s+" bigger than "+ARGV[1].to_s : ARGV[0].to_s+" smaller than "+ARGV[1].to_s
