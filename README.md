# SC-T-220-VLN2 [![Build Status](https://travis-ci.com/GudniNatan/SC-T-220-VLN2.svg?token=JMPEzNCssa8wvM9yqz3h&branch=master)](https://travis-ci.com/GudniNatan/SC-T-220-VLN2)


Þetta er git repo fyrir áfangann SC-T-220-VLN2 vorið 2019 í HR. Það notast við Django og postgresql og er svo dreift með heroku á [vln2.gng.is](http://vln2.gng.is/).

## Um Castle Apartments
Castle Apartments er vefkerfi þar sem hægt er að kaupa og selja íbúðir. Það nýtist við einskonar uppboðskerfi þar sem hver sem er getur boðið í íbúðir, seljendur geta svo séð tilboðin og valið það besta.

Kerfið býður upp á ýmsa hluti eins og víðamikla leit af íbúðum, innskráningarkerfi til að flýta fyrir því að kaupa íbúð, svo er hægt að skoða öll smáatriði um íbúð áður en hún er keypt á flottri íbúðasíðu. 

Kerfið er hannað til að virka hvar sem er í heiminum og að það sé eins þægilegt og mögulegt er að kaupa sér íbúð. Það styður bæði farsíma og þá sem eru ekki með javascript. Allar myndir eru þjappaðar til að flýta fyrir niðurhleðslu, og kerfið er auglýsingafrjálst.



## Uppsetning
Python 3.7 er krafist fyrir þetta verkefni. Til að keyra þetta þarf fyrst að installa öllum nauðsynlegum pökkum. Þægilegasta leiðin er að nota pycharm til að gera þetta, þá bara smelliru á install requirements þegar þú ert beðinn um það. Annars er hægt að gera:
```pip install -r requirements.txt```

Það gæti tekið smá tíma að installa, svo þú getur fengið þér kaffibolla meðan þú býður...

Síðan á að virka að keyra serverinn með:  
```python manage.py runserver```

### Troubleshooting
Ef ske kynni að það kemur villa við að láta inn öll requirements þá biðjumst við forláts.  

- Fyrir alla pakka sem við höfum prófað hefur það virkað að láta hann inn manually með pip install.

- Það virðist líka virka að nota PyCharm til að installa pökkunum.

- Ef þessi villa kemur upp:  ```error: Microsoft Visual C++ 14.0 is required.``` Þá er lausnin að fara hingað: https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019  og sækja Build Tools for Visual Studio 2019. Það gæti líka virkað að installa pakkanum manually með pip.


## Gert af
Guðni Natan Gunnarsson  
Pálmi Chanachai Rúnarsson  
Ólafur Andri Davíðsson  
Þór Breki Davíðsson

## License
[MIT License](https://github.com/GudniNatan/SC-T-220-VLN2/blob/master/LICENSE)