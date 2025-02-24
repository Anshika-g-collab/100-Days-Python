states_of_India = ['Madhya Pradesh' , 'Chhattisgarh' , 'Uttar Pradesh' , 'Rajasthan' ,'Maharashtra','Rajasthan']

print(states_of_India[0])
print(states_of_India[1])   
print(states_of_India)   

# .append(x) = a[len(a):] = [x]
states_of_India.append("Jharkhand")
print(states_of_India)

# .extend(iterable) = a[len(a):] = iterable
states_of_India.extend(['Kerela',"Manipur","Telengana"])
print(states_of_India)
