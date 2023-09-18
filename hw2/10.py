date = int(input("Input birthday: " ))
month = input("Input month of birth (e.g. march, july etc): " )
if (month == 'January'):
    if (date < 20):
        astro = 'Capricorn'
    else:
        astro = 'Aquarius'
elif(month == 'February'):
    if(date < 19):
        astro = 'Aquarius'
    else:
        astro = 'Pisces'
elif (month == 'March'):
    if (date < 21):
        astro = 'Pisces' 
    else:
        astro = 'Aries'
elif (month == 'April'):
    if (date < 20):
        astro = 'Aries' 
    else:
        astro = 'Taurus'
elif (month == 'May'):
    if (date < 21):
        astro = 'Taurus' 
    else:
        astro = 'Gemini'
elif (month == 'June'):
    if (date < 21):
        astro = 'Gemini' 
    else:
        astro = 'Cancer'
elif (month == 'July'):
    if (date < 23):
        astro = 'Cancer' 
    else:
        astro = 'Leo'
elif (month == 'August'):
    if (date < 23):
        astro = 'Leo' 
    else:
        astro = 'Virgo'
elif (month == 'September'):
    if (date < 23):
        astro = 'Virgo' 
    else:
        astro = 'Libra'
elif (month == 'October'):
    if (date < 23):
        astro = 'Libra' 
    else:
        astro = 'Scorpio'
elif (month == 'November'):
    if (date < 22):
        astro = 'Scorpio' 
    else:
        astro = 'Sagittarius'
elif (month == 'December'):
    if (date < 22):
        astro = 'Sagittarius'
    else:
        astro = 'Capricorn'
print("Your Astrological sign is : ",astro)
