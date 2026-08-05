def details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

details(name = "Yatharth", age = 18, city = "Lucknow")        