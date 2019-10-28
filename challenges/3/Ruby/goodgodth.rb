#run goodgodth.rb <input number>
if ARGV.length != 1
  puts "Input must be only argument"
  exit
end

input = ARGV[0].to_i
def fibonacci( n )
  return  n  if ( 0..1 ).include? n
  ( fibonacci( n - 1 ) + fibonacci( n - 2 ) )
end
puts fibonacci( input )
