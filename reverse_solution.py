

dataset = ["ant", "mouse", "cat", "dog", "sheep", "deer", "moose", "hippo", "elephant"]


def reverse_me(data):
    for index in range(len(data)//2):
        tempvar = data[index]
        data[index] = data[-1 -index]
        data[-1 -index] = tempvar
    return data
	
print(reverse_me(dataset))
