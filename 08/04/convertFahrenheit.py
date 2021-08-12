def convertFahrenheit(temp):
    cTemp = (temp-32) * 5/9
    kTemp = cTemp + 273.15
    return cTemp, kTemp
