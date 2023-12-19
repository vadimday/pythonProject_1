try:
    sideA = int(input('input side A ->'))
    sideB = int(input('input side B ->'))
    area = sideA*sideB
    print("Площа прямокутника: ",area)
except Exception as e:
    print(e)