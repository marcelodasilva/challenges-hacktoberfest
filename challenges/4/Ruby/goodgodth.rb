#run goodgodth.rb <input number>
if ARGV.length != 1
  puts "Input must be only argument"
  exit
end

input = ARGV[0].to_f
def ftoc( n )
  return ((n - 32) * 5.0 / 9.0).round(3)
end
puts "Temperature in Fahrenheit : "+input.to_s+ " equals "+ftoc(input).to_s+" in Celsius"
