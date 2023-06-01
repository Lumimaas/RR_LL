# Kuidas koodi kasutada ja mis need file'id teevad?
Siin on kolm file'i, pythoni file'id saad selle järgi aru, et nende lõpus on ".py".
Mis need pythoni file'id teevad ja kuidas kasutada?

See projekt simuleerib võidusõidu tulemusi ja arvutab erinevaid statistilisi näitajaid, nagu parimad sektoriajad ja võistlejate üldine järjestus.

## Koodi kirjeldus

Koodi fail sisaldab järgmisi funktsioone:
- `juhuslik_aeg(ala, ule)`: tagastab juhusliku aja sekundites ja tuhandikutes vahemikus `ala` kuni `ule`.
- `aja_vormindamine(aeg)`: teisendab aja formaati "tunnid:minutid:sekundid.tuhandikud".
- `arvuta_taisringi_aeg(sektorid)`: arvutab täisringi aja, summeerides sektorite ajad.

Koodi peamised toimingud:
1. Määrab võistlejate nimekirja.
2. Simuleerib võistluste tulemusi 10 ringi jooksul, arvestades juhuslikke sektoriaegu.
3. Kogub võistlejate tulemused ja parimad sektoriajad.
4. Prindib võistlejate järjestuse, koguaja, vahe esimesega, ringide arvu ja kiireima ringiaja.
5. Prindib üldised parimad sektoriajad.
6. Prindib kokkuliidetud sektorite aja.

Kuidas käivitada
Veendu, et sul on Python 3.5 või uuem versioon installitud.

Lae alla koodifailid ja salvesta need ühte kausta.

Ava terminal või käsurealint ja navigeeri kausta, kuhu salvestasid koodifailid.

Käivita programm, sisestades järgmise käsu:

php
Copy code
python failinimi.py

  
Näiteks:

Copy code:
python race_simulation.py
  
  
Programm arvutab tulemused ja väljastab need nii konsoolile kui ka output.out faili.

