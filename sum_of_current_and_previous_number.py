# Print the sum of the current number and the previous number

previous_number = 0
# Current number
for i in range(1,11):
    # Adding the current and previous
    number_sum = previous_number + i
    print("The current number:", i, "The previous number:", previous_number, "Sum:", number_sum)
    previous_number = i 


    
