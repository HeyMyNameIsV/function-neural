x_input=[0.3,-0.2,0.7]
weights=[0.4,0.3,0.6]

threshold=0.5

def step(sum_function: float):
    if sum_function > threshold:
        return 1
    
    else:
        return 0
        
def perceptron():
    sum_function=0
    for x,w in zip(x_input,weights):
        sum_function+=x*w
        print(sum_function)
    
    return step(sum_function)

output=perceptron()

print(output)
  
