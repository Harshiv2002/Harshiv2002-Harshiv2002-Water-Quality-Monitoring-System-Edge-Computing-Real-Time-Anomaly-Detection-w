import random
# Function to Read turbidity
def read_turbidity():
    result = random.choices([1,0], [0.1,0.9])[0]
    if result == 0:
        try:
            noise = random.uniform(-3,3)
            # Reading turbidity code here
            turbidity = 100 + noise # Generating Dummy values
        except:
            turbidity = None
    else:
        turbidity = 1000 #Insert Anomalies

    return turbidity


# Function to read temperature
def read_temp():
    result = random.choices([1,0], [0.01,0.99])[0]
    if result == 0:
        try:
            noise = random.uniform(-3,3) 
            # Reading turbidity code here
            temp = 100 + noise # Generating Dummy values
        except:
            temp = None
    else:
        temp = 1000 #Insert Anomalies

    return temp


