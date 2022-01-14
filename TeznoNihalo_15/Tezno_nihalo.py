import math
casi = [12.41, 27.30, 42.12, 57.05, 71.68, 86.70, 101.60, 116.29, 131.33, 146.29, 160.95, 175.91, 190.80, 205.64, 220.54, 235.45, 250.21, 265.11, 279.98, 294.94, 309.70, 324.61, 339.49, 354.36, 369.26, 384.13, 398.98, 413.90, 428.76, 443.58]
casi2 = [12.19, 14.85, 14.83, 15.20, 14.62, 15.03, 14.92, 14.60, 14.66, 14.75, 14.97, 14.90, 14.87, 14.91, 14.97, 14.73, 14.97, 14.76, 14.93, 14.87, 14.99, 14.84, 14.71, 14.99, 14.70, 14.87, 14.75, 14.94, 15.00, 14.72]

x = 0
casi3 = []
for cas in casi2:
    x += cas
    casi3.append(round(x, 2))

#prva meritev
casovna_razlika_1 = casi[19]
casovna_razlika_2 = casi[20] - casi[0]
casovna_razlika_3 = casi[21] - casi[1]
casovna_razlika_4 = casi[22] - casi[2]
casovna_razlika_5 = casi[23] - casi[3]
casovna_razlika_6 = casi[24] - casi[4]
casovna_razlika_7 = casi[25] - casi[5]
casovna_razlika_8 = casi[26] - casi[6]
casovna_razlika_9 = casi[27] - casi[7]
casovna_razlika_10 = casi[28] - casi[8]
casovna_razlika_11 = casi[29] - casi[9]

#krogla
a = 0.043  # m
h = 0.005375  # m
gostota_zeleza = 7874 # kg/m3
polmer_krogle = (a ** 2 + 3 * h ** 2) / (6 * h)
volumen_krogle = (4 * math.pi * polmer_krogle ** 3) / 3
masa_krogle = (gostota_zeleza * volumen_krogle)

#zica
dolzina_zice = 2.18 # m
polmer_zice = 0.0016 / 2 # m
volumen_zice = (math.pi * polmer_zice ** 2) * dolzina_zice
masa_zice = (gostota_zeleza * volumen_zice)

#amplituda
zacetna_amplituda = 0.067 # m
koncna_amplituda = 0.056 # m
sprememba_amplitude = (zacetna_amplituda - koncna_amplituda) / 100
logaritemski_dekrament = math.log(zacetna_amplituda / (zacetna_amplituda - sprememba_amplitude))

#kot
kot = math.asin(zacetna_amplituda / dolzina_zice)

#s kroglo niha se k-krat toliksna prostornina zraka
k = 0.6

povprecna_vrednost = (casovna_razlika_1 + casovna_razlika_2 + casovna_razlika_3 + casovna_razlika_4 + casovna_razlika_5 + casovna_razlika_6 + casovna_razlika_7 + casovna_razlika_8 + casovna_razlika_9 + casovna_razlika_10 + casovna_razlika_11) / 11
vrednost = povprecna_vrednost / 100
g = (dolzina_zice * ((2 * math.pi / vrednost) ** 2))

g_s_popravki = (dolzina_zice * (2 * math.pi / vrednost) ** 2) * (1 + 0.5 * (math.sin(kot / 2)) ** 2 + (2 / 5) * (polmer_krogle / dolzina_zice) ** 2 - masa_zice / (6 * masa_krogle) + (1 + k) * (1.2 / 7800) + (logaritemski_dekrament / (2 * math.pi)) ** 2) 

print("Tezni pospesek: {}".format(g))
print("Tezni pospesek s popravki: {}".format(g_s_popravki))
print("Polmer krogle: {}".format(polmer_krogle))
print("Logaritemski dekrament: {}".format(logaritemski_dekrament))

#druga meritev
casovna_razlika_2_1 = casi3[19]
casovna_razlika_2_2 = casi3[20] - casi3[0]
casovna_razlika_2_3 = casi3[21] - casi3[1]
casovna_razlika_2_4 = casi3[22] - casi3[2]
casovna_razlika_2_5 = casi3[23] - casi3[3]
casovna_razlika_2_6 = casi3[24] - casi3[4]
casovna_razlika_2_7 = casi3[25] - casi3[5]
casovna_razlika_2_8 = casi3[26] - casi3[6]
casovna_razlika_2_9 = casi3[27] - casi3[7]
casovna_razlika_2_10 = casi3[28] - casi3[8]
casovna_razlika_2_11 = casi3[29] - casi3[9]

povprecna_vrednost_2 = (casovna_razlika_2_1 + casovna_razlika_2_2 + casovna_razlika_2_3 + casovna_razlika_2_4 + casovna_razlika_2_5 + casovna_razlika_2_6 + casovna_razlika_2_7 + casovna_razlika_2_8 + casovna_razlika_2_9 + casovna_razlika_2_10 + casovna_razlika_2_11) / 11
vrednost_2 = povprecna_vrednost_2 / 100
g_s_popravki_2 = (dolzina_zice * (2 * math.pi / vrednost_2) ** 2) * (1 + 0.5 * (math.sin(kot / 2)) ** 2 + (2 / 5) * (polmer_krogle / dolzina_zice) ** 2 - masa_zice / (6 * masa_krogle) + (1 + k) * (1.2 / 7800) + (logaritemski_dekrament / (2 * math.pi)) ** 2) 
print("Tezni pospesek s popravki 2: {}".format(g_s_popravki_2))