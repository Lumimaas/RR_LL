import random

def juhuslik_aeg(ala, ule):
    aeg = random.uniform(ala, ule)
    sekundid = int(aeg)
    tuhandikud = int((aeg - sekundid) * 1000)
    return f"{sekundid:02d}.{tuhandikud:03d}"

def aja_vormindamine(aeg):
    tunnid = int(aeg // 3600)
    minutid = int((aeg // 60) % 60)
    sekundid = int(aeg % 60)
    tuhandikud = int((aeg % 1) * 1000)
    return f"{tunnid:02d}:{minutid:02d}:{sekundid:02d}.{tuhandikud:03d}"

def arvuta_taisringi_aeg(sektorid):
    taisringi_aeg = sum(float(sekundid) + float(tuhandikud) / 1000 for sekundid, tuhandikud in [sektor.split(".") for sektor in sektorid])
    return taisringi_aeg


votlused = ["George", "Lewis", "Max", "Charles", "Valtteri"]

tulemused = []
voistlus_info = []

parimad_sektoriajad = {1: {"nimi": "", "aeg": float('inf')},
                       2: {"nimi": "", "aeg": float('inf')},
                       3: {"nimi": "", "aeg": float('inf')}}

for votleja in votlused:
    sektorid = []
    koguaeg = 0
    koperdamised = []
    kiireim_ringi_aeg = float('inf')
    for ring in range(1, 11):
        apardus = random.randint(1, 10)
        if apardus == 2:
            sektor1 = juhuslik_aeg(30, 90)
            sektor2 = juhuslik_aeg(30, 90)
            sektor3 = juhuslik_aeg(30, 90)
            koperdamised.append(ring)
        else:
            sektor1 = juhuslik_aeg(23, 26)
            sektor2 = juhuslik_aeg(23, 26)
            sektor3 = juhuslik_aeg(23, 26)
            if ring == 10:
                kiireim_ringi_aeg = min(kiireim_ringi_aeg, arvuta_taisringi_aeg([sektor1, sektor2, sektor3]))
                parimad_sektoriajad[1] = {"nimi": votleja, "aeg": float(sektor1)} if float(sektor1) < parimad_sektoriajad[1]["aeg"] else parimad_sektoriajad[1]
                parimad_sektoriajad[2] = {"nimi": votleja, "aeg": float(sektor2)} if float(sektor2) < parimad_sektoriajad[2]["aeg"] else parimad_sektoriajad[2]
                parimad_sektoriajad[3] = {"nimi": votleja, "aeg": float(sektor3)} if float(sektor3) < parimad_sektoriajad[3]["aeg"] else parimad_sektoriajad[3]
        sektorid.extend([sektor1, sektor2, sektor3])
        koguaeg += arvuta_taisringi_aeg([sektor1, sektor2, sektor3])
        if ring == 10:
            votleja_info = [votleja, koguaeg, koperdamised, kiireim_ringi_aeg]
            tulemused.append(votleja_info)
            voistlus_info.append(votleja_info)

tulemused = sorted(tulemused, key=lambda x: x[1])

pohiaeg = tulemused[0][1]
esimese_koha_votleja = tulemused[0][0]
esimese_koha_kiireim_ringi_aeg = tulemused[0][3]

def printLog(*args, **kwargs):
    print(*args, **kwargs)
    with open('Result.txt','a') as file:
        print(*args, **kwargs, file=file)

printLog("Sõitjate tulemused:")
for tulemus in tulemused:
    nimi = tulemus[0][:10].ljust(10)
    koguaeg = aja_vormindamine(tulemus[1])
    ringid = str(tulemus[2])
    vahe = ""
    if tulemus[1] != pohiaeg:
        vahe = aja_vormindamine(tulemus[1] - pohiaeg)

    kiireim_ringi_aeg = "" if tulemus[0] != esimese_koha_votleja else aja_vormindamine(esimese_koha_kiireim_ringi_aeg)
    printLog(f"{nimi} {koguaeg} {vahe} {ringid} {kiireim_ringi_aeg}")

printLog("\nÜldised parimad sektoriajad:")
for sektor_index, sektor_info in parimad_sektoriajad.items():
    printLog(f"Sektor {sektor_index}: {sektor_info['nimi']} - {aja_vormindamine(sektor_info['aeg'])}")

kokku_liidetud_aeg = sum(sektor_info['aeg'] for sektor_info in parimad_sektoriajad.values())
printLog(f"\nKokku liidetud sektorite aeg: {aja_vormindamine(kokku_liidetud_aeg)}")
