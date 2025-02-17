name=input("Enter Your Name:")
birth_year=int(input("Enter Your Birth year:"))

def age_t(birth_year):
    age=2025 - birth_year
    return print(f"Hey,{name},you are {age}year's old")

print(age_t(birth_year))


