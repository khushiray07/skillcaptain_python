def person_age(age):
    if age < 18:
        return  "You are a minor."
    elif 18 <= age <= 65:
        return "You are an adult."        
    else:
        return "You are a senior citizen."
print(person_age(15))
print(person_age(35))
print(person_age(70))
