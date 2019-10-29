ran10 = 10.times.map { rand(100) }
puts ran10.inspect
summary = 0
ran10.each { |item|
    summary += item
}
puts summary
