glas = "йуеыаоэяию"
sogl = "цкнгшщзхъфвпрлджчсмтьб"
glas_count = 0
sogl_count = 0
s = input()
for i in range(len(s)):
    if (s[i] in glas ):
        glas_count += 1
    elif (s[i] in sogl):
        sogl_count += 1
print(glas_count, sogl_count)