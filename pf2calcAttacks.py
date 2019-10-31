# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:18:59 2019

@author: bhalb
"""
import copy
from pf2calcMonsterStats import creatureData

summonAnimalAttackB = [7,
7,
9,
9,
10,
10,
12,
12,
16,
16,
18,
18,
22,
22,
25,
25,
28,
28,
31,
31]
summonAnimalDamageB = [4.5,
4.5,
5.5,
5.5,
11,
11,
10.5,
10.5,
16,
16,
18,
18,
24,
24,
27,
27,
31.5,
31.5,
35.5,
35.5]
summonDragonAttackB = [14,
14,
19,
19,
21,
21,
25,
25,
28,
28,
31,
31]
summonDragonDamageB = [17.5,
17.5,
23.5,
23.5,
26.5,
26.5,
33,
33,
34.5,
34.5,
46,
46]
sumAniAttack = {i: summonAnimalAttackB[i-1] for i in range(1,21)}
sumAniDamage = {i: summonAnimalDamageB[i-1] for i in range(1,21)}
sumDraAttack = {i: summonDragonAttackB[i-9] for i in range(9,21)}
sumDraDamage = {i: summonDragonDamageB[i-9] for i in range(9,21)}


mProf = dict(zip(list(range(1,21)),list(range(1,21))))
for i in range(1,21):
    mProf[i] += 2
    if i >=5: 
        mProf[i] += 2
    if i >= 13: 
        mProf[i] += 2
        
cProf = dict(zip(list(range(1,21)),list(range(1,21))))
for i in range(1,21):
    cProf[i] += 2
    if i >=11: 
        cProf[i] += 2

wProf = dict(zip(list(range(1,21)),list(range(1,21))))
for i in range(1,21):
    wProf[i] += 2
    if i >=7: 
        wProf[i] += 2

fProf = copy.copy(mProf)
for i in fProf:
    fProf[i] += 2
    
sProf = {i: i+2 for i in range(1,21)}
for i in sProf:
    if i >= 7:
        sProf[i] += 2
    if i >= 15:
        sProf[i] += 2
    if i >= 19:
        sProf[i] +=2
        
wsProf = {i: i+2 for i in range(1,21)}
for i in wsProf:
    if i >= 11:
        wsProf[i] += 2
    if i >= 19:
        wsProf[i] += 2
    
mStr = {i: 4 for i in range(1,21)}
for i in mStr:
    if i >= 10:
        mStr[i] += 1
    if i >= 17:
        mStr[i] += 1
    if i >=20:
        mStr[i] +=1
        
cStr = {i: 3 for i in range(1,21)}
for i in cStr:
    if i >= 5:
        cStr[i] += 1
    if i >= 15:
        cStr[i] += 1

wStr = {i: 3 for i in range(1,21)}
for i in wStr:
    if i >= 5:
        wStr[i] += 1
    if i >= 15:
        wStr[i] += 1
    if i >= 17:
        wStr[i] += 1
        
wiBonus = {i: 0 for i in range(1,21)}
for i in wiBonus:
    if i >= 2:
        wiBonus[i] += 1
    if i >= 10:
        wiBonus[i] += 1
    if i >= 16:
        wiBonus[i] += 1
        
#mutagen item bonus
miBonus = {i: 1 for i in range(1,21)}
for i in miBonus:
    if i >= 3:
        miBonus[i] += 1
    if i >= 11:
        miBonus[i] += 1
    if i >= 17: 
        miBonus[i] +=1
        
wDice = {i: 1 for i in range(1,21)}
for i in wDice:
    if i >= 4:
        wDice[i] += 1
    if i >= 12:
        wDice[i] += 1
    if i >= 19:
        wDice[i] += 1
        
sDice = {i: int((i+1)/2) for i in range(1,21)}

martialAttackBonus = {i: mProf[i] + mStr[i] + wiBonus[i] for i in range(1,21)}

casterAttackBonus = {i: cProf[i] + cStr[i] + wiBonus[i] for i in range(1,21)}

warpriestAttackBonus = {i: wProf[i] + wStr[i] + wiBonus[i] for i in range(1,21)}

bombAttackBonus = {i: wProf[i] + wStr[i] + miBonus[i]-1 for i in range(1,21)}
pbombAttackBonus = {i: wProf[i] + wStr[i] + miBonus[i]-2 for i in range(1,21)}
mutagenstrikeAttackBonus = {i: wProf[i] + wStr[i] + miBonus[i] for i in range(1,21)}

fighterAttackBonus = {i: fProf[i] + mStr[i] + wiBonus[i] for i in range(1,21)}

cantripAttackBonus = {i: sProf[i] + mStr[i] for i in range(1,21)}
spellDC = {i: 10 + cantripAttackBonus[i] for i in range(1,21)}

basewolf = {i: i+5 for i in range(1,21)}
maturewolf = {i: i+6 for i in range(1,21)}
nimblewolf = {i: i+8 for i in range(1,21)}
specializedwolf = {i: i+12 for i in range(1,21)}

druidwolfattack = {i: basewolf[i] for i in range(1,21)}
for i in druidwolfattack:
    if i >= 4:
        druidwolfattack[i] = maturewolf[i]
    if i >= 8:
        druidwolfattack[i] = nimblewolf[i]
    if i >= 14:
        druidwolfattack[i] = specializedwolf[i]
        
rangerwolfattack = {i: basewolf[i] for i in range(1,21)}
for i in rangerwolfattack:
    if i >= 6:
        rangerwolfattack[i] = maturewolf[i]
    if i >= 10:
        rangerwolfattack[i] = nimblewolf[i]
    if i >= 16:
        rangerwolfattack[i] = specializedwolf[i]

basebear = {i: i+5 for i in range(1,21)}
maturebear = {i: i+6 for i in range(1,21)}
savagebear = {i: i+8 for i in range(1,21)}
specializedbear = {i: i+11 for i in range(1,21)}

druidbearattack = {i: basebear[i] for i in range(1,21)}
for i in druidbearattack:
    if i >= 4:
        druidbearattack[i] = maturebear[i]
    if i >= 8:
        druidbearattack[i] = savagebear[i]
    if i >= 14:
        druidbearattack[i] = specializedbear[i]
        
rangerbearattack = {i: basebear[i] for i in range(1,21)}
for i in rangerbearattack:
    if i >= 6:
        rangerbearattack[i] = maturebear[i]
    if i >= 10:
        rangerbearattack[i] = savagebear[i]
    if i >= 16:
        rangerbearattack[i] = specializedbear[i]

mwSpec = {i: 0 for i in range(1,21)}
for i in mwSpec:
    if i >= 7:
        mwSpec[i] = int((mProf[i]-i)/2)
    if i >= 15:
        mwSpec[i] = int((mProf[i]-i))
        
fwSpec = {i: 0 for i in range(1,21)}
for i in fwSpec:
    if i >= 7:
        fwSpec[i] = int((fProf[i]-i)/2)
    if i >= 15:
        fwSpec[i] = int((fProf[i]-i))
        
cwSpec = {i: 0 for i in range(1,21)}
for i in cwSpec:
    if i >= 13:
        cwSpec[i] = int((cProf[i]-i)/2)
        
eRune = {i: 0 for i in range(1,21)}
for i in eRune:
    if i >= 8:
        eRune[i] += 3.5
    if i>=15:
        eRune[i] += 3.5
        
propulsive10 = {i: 0 for i in range(1,21)}
for i in range(1,21):
    if i >= 10:
        propulsive10[i] += 1
    if i >= 20:
        propulsive10[i] += 1   
        
propulsive12 = {i: 0 for i in range(1,21)}
for i in range(1,21):
    if i >= 5:
        propulsive12[i] += 1
    if i >= 15:
        propulsive12[i] += 1        
propulsive14 = {i: 1 for i in range(1,21)}
for i in range(1,21):
    if i >= 10:
        propulsive12[i] += 1
propulsive16 = {i: 1 for i in range(1,21)}
for i in range(1,21):
    if i >= 5:
        propulsive12[i] += 1
        
bombSplashDamage = {i: 1 for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        bombSplashDamage[i] = 2
    if i >= 11:
        bombSplashDamage[i] = 3
    if i >= 17:
        bombSplashDamage[i] = 4
        
bomberSplashDamage = copy.copy(bombSplashDamage)
for i in range(4,21):
    bomberSplashDamage[i] = mStr[i]
    if i >= 10:
        bomberSplashDamage[i] = mStr[i] + bombSplashDamage[i]
    if i >= 17:
        bomberSplashDamage[i] = mStr[i] + bombSplashDamage[i] - 1

pbombSplashDamage = {i: 0 for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        pbombSplashDamage[i] = 1
    if i >= 11:
        pbombSplashDamage[i] = 2
    if i >= 17:
        pbombSplashDamage[i] = 3

pbomberSplashDamage = copy.copy(bomberSplashDamage)
for i in range(10,21):
    pbomberSplashDamage[i] = bomberSplashDamage[i] - 1

        
acidFlaskDamage = {i: 1 for i in range(1,21)}

acidFlaskPersDamage = {i: 3.5 for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        acidFlaskPersDamage[i] = 7
    if i >= 11:
        acidFlaskPersDamage[i] = 10.5
    if i >= 17:
        acidFlaskPersDamage[i] = 14

alchemistsFireDamage = {i: 4.5 for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        alchemistsFireDamage[i] = 9
    if i >= 11:
        alchemistsFireDamage[i] = 13.5
    if i >= 17:
        alchemistsFireDamage[i] = 18

alchemistsFirePersDamage = {i: 1 for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        alchemistsFirePersDamage[i] = 2
    if i >= 11:
        alchemistsFirePersDamage[i] = 3
    if i >= 17:
        alchemistsFirePersDamage[i] = 4

blfvDamage = {i: 3.5 for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        blfvDamage[i] = 7
    if i >= 11:
        blfvDamage[i] = 10.5
    if i >= 17:
        blfvDamage[i] = 14
        
thunderStoneDamage = {i: 2.5 for i in range(1,21)}
for i in range(1,21):
    if i >= 3:
        thunderStoneDamage[i] = 5
    if i >= 11:
        thunderStoneDamage[i] = 7.5
    if i >= 17:
        thunderStoneDamage[i] = 10
       
# perpetual infusions
pacidFlaskDamage = {i: 0 for i in range(1,21)}
for i in range(7,21):
    pacidFlaskDamage[i] = 1

pacidFlaskPersDamage = {i: 0 for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        pacidFlaskPersDamage[i] = 3.5
    if i >= 11:
        pacidFlaskPersDamage[i] = 7
    if i >= 17:
        pacidFlaskPersDamage[i] = 10.5

palchemistsFireDamage = {i: 0 for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        palchemistsFireDamage[i] = 4.5
    if i >= 11:
        palchemistsFireDamage[i] = 9
    if i >= 17:
        palchemistsFireDamage[i] = 13.5

palchemistsFirePersDamage = {i: 0 for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        palchemistsFirePersDamage[i] = 1
    if i >= 11:
        palchemistsFirePersDamage[i] = 2
    if i >= 17:
        palchemistsFirePersDamage[i] = 3

pblfvDamage = {i: 0 for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        pblfvDamage[i] = 3.5
    if i >= 11:
        pblfvDamage[i] = 7
    if i >= 17:
        pblfvDamage[i] = 10.5
        
pthunderStoneDamage = {i: 0 for i in range(1,21)}
for i in range(1,21):
    if i >= 7:
        pthunderStoneDamage[i] = 2.5
    if i >= 11:
        pthunderStoneDamage[i] = 5
    if i >= 17:
        pthunderStoneDamage[i] = 7.5
        
bestialClawDamage = {i: wDice[i]*2.5 for i in range(1,21)}
for i in bestialClawDamage:
    if i >= 3:
        bestialClawDamage[i] = wDice[i]*3.5
    if i >= 11:
        bestialClawDamage[i] = wDice[i]*4.5
    if i >= 17:
        bestialClawDamage[i] = wDice[i]*4.5 + 2
        
bestialJawDamage = {i: wDice[i]*3.5 for i in range(1,21)}
for i in bestialJawDamage:
    if i >= 3:
        bestialJawDamage[i] = wDice[i]*4.5
    if i >= 11:
        bestialJawDamage[i] = wDice[i]*5.5
    if i >= 17:
        bestialJawDamage[i] = wDice[i]*5.5 + 2
        
        
animalJawDamage = {i: wDice[i]*5.5 for i in range(1,21)}
for i in animalJawDamage:
    if i >= 7:
        animalJawDamage[i] = wDice[i]*6.5
        
animalClawDamage = {i: wDice[i]*3.5 for i in range(1,21)}
for i in animalClawDamage:
    if i >= 7:
        animalClawDamage[i] = wDice[i]*4.5
        
animalragedamage = {i: 2 for i in range(1,21)}
for i in animalragedamage:
    if i >= 7:
        animalragedamage[i] = 5
    if i >= 15:
        animalragedamage[i] = 12

dragonragedamage = {i: 4 for i in range(1,21)}
for i in dragonragedamage:
    if i >= 7:
        dragonragedamage[i] = 8
    if i >= 15:
        dragonragedamage[i] = 16

furyragedamage = {i: 2 for i in range(1,21)}
for i in furyragedamage:
    if i >= 7:
        furyragedamage[i] = 6
    if i >= 15:
        furyragedamage[i] = 12
        
giantragedamage = {i: 6 for i in range(1,21)}
for i in giantragedamage:
    if i >= 7:
        giantragedamage[i] = 10
    if i >= 15:
        giantragedamage[i] = 18

spiritragedamage = {i: 3 for i in range(1,21)}
for i in furyragedamage:
    if i >= 7:
        furyragedamage[i] = 7
    if i >= 15:
        furyragedamage[i] = 13
        
smiteevildamage = {i: 0 for i in range(1,21)}
for i in smiteevildamage:
    if i >= 6:
        smiteevildamage[i] = 4
    if i >= 13:
        smiteevildamage[i] = 6
        
sneakattackdamage = {i: 3.5 for i in range(1,21)}
for i in sneakattackdamage:
    if i >= 5:
        sneakattackdamage[i] = 7
    if i >= 11:
        sneakattackdamage[i] = 10.5
    if i >= 17:
        sneakattackdamage[i] = 14
        
rangerprecedgedamage1 = {i: 4.5 for i in range(1,21)}
for i in rangerprecedgedamage1:
    if i >= 11:
        rangerprecedgedamage1[i] = 9
    if i >= 19:
        rangerprecedgedamage1[i] = 13.5
        
rangerprecedgedamage2 = {i: 0 for i in range(1,21)}
for i in rangerprecedgedamage2:
    if i >= 17:
        rangerprecedgedamage2[i] = 4.5  
    if i >= 19:
        rangerprecedgedamage2[i] = 9  
        
rangerprecedgedamage3 = {i: 0 for i in range(1,21)}
for i in rangerprecedgedamage3:
    if i >= 19:
        rangerprecedgedamage3[i] = 4.5  
        
rangerbearsupportdamage = {i: 4.5 for i in range(1,21)}
for i in rangerbearsupportdamage:
    if i >= 10:
        rangerbearsupportdamage[i] = 9
        
druidwolfdamage = {i: 6.5 for i in range(1,21)}
for i in druidwolfdamage:
    if i >= 4:
        druidwolfdamage[i] = 12
    if i >= 8:
        druidwolfdamage[i] = 15 
    if i >= 14:
        druidwolfdamage[i] = 21.5 
        
rangerwolfdamage = {i: 6.5 for i in range(1,21)}
for i in rangerwolfdamage:
    if i >= 6:
        rangerwolfdamage[i] = 12
    if i >= 10:
        rangerwolfdamage[i] = 15 
    if i >= 16:
        rangerwolfdamage[i] = 21.5 
        
druidbeardamage = {i: 7.5 for i in range(1,21)}
for i in druidbeardamage:
    if i >= 4:
        druidbeardamage[i] = 13
    if i >= 8:
        druidbeardamage[i] = 18 
    if i >= 14:
        druidbeardamage[i] = 26.5 
        
rangerbeardamage = {i: 7.5 for i in range(1,21)}
for i in rangerbeardamage:
    if i >= 6:
        rangerbeardamage[i] = 13
    if i >= 10:
        rangerbeardamage[i] = 18
    if i >= 16:
        rangerbeardamage[i] = 26.5 
        
d6Damage = [3.5 * wDice[i] for i in wDice]
d8Damage = [4.5 * wDice[i] for i in wDice]
d10Damage = [5.5 * wDice[i] for i in wDice]
d12Damage = [6.5 * wDice[i] for i in wDice]

damageDiceConverter = {"1d4": [2.5,0],
                       "1d6": [3.5,0],
                       "1d8": [4.5,0],
                       "1d10": [5.5,0],
                       "1d12": [6.5,0],
                       "1d4+1": [2.5,1],
                       "1d6+1": [3.5,1],
                       "1d8+1": [4.5,1],
                       "1d10+1": [5.5,1],
                       "1d12+1": [6.5,1],
                       "1d4+2": [2.5,2],
                       "1d6+2": [3.5,2],
                       "1d8+2": [4.5,2],
                       "1d10+2": [5.5,2],
                       "1d12+2": [6.5,2]}

noneDamage = {i: 0 for i in range(1,21)}
deadlyd6Damage = {i: max(3.5,(wDice[i]-1)*3.5) for i in range(1,21)}
deadlyd8Damage = {i: max(4.5,(wDice[i]-1)*4.5) for i in range(1,21)}
deadlyd10Damage = {i: max(5.5,(wDice[i]-1)*5.5) for i in range(1,21)}
deadlyd12Damage = {i: max(6.5,(wDice[i]-1)*6.5) for i in range(1,21)}
fatald8Damage = {i: 4.5 + wDice[i]*4 for i in range(1,21)}
fatald10Damage = {i: 5.5 + wDice[i]*4 for i in range(1,21)}
fatald12Damage = {i: 6.5 + wDice[i]*2 for i in range(1,21)}

criticalDiceConverter = {"none": [False, noneDamage],
                 "deadly d6": [False, deadlyd6Damage],
                 "deadly d8": [False, deadlyd8Damage],
                 "deadly d10": [False, deadlyd10Damage],
                 "deadly d12": [False, deadlyd12Damage],
                 "fatal d8": [True, 4.5],
                 "fatal d10": [True, 5.5],
                 "fatal d12": [True, 6.5]
        }

d12pad = {i: 6.5 for i in range(1,21)}
for i in d12pad:
    if i>=10:
        d12pad[i]+=6.5
    if i>=18:
        d12pad[i]+=6.5

d10pad = {i: 5.5 for i in range(1,21)}
for i in d10pad:
    if i>=10:
        d10pad[i]+=5.5
    if i>=18:
        d10pad[i]+=5.5
        
d12bfd = {i: 0 for i in range(1,21)}
for i in d12bfd:
    if i>=10:
        d12bfd[i]+=6.5
    if i>=18:
        d12bfd[i]+=6.5
        
d10bfd = {i: 0 for i in range(1,21)}
for i in d10bfd:
    if i>=10:
        d10bfd[i]+=5.5
    if i>=18:
        d10bfd[i]+=5.5
        
alchemistDamage = {i: wStr[i] + cwSpec[i] for i in range(1,21)}
alchemistRangedDamage = {i: cwSpec[i] for i in range(1,21)}

strCasterDamage = {i: cStr[i] + cwSpec[i] for i in range(1,21)}
rangedCasterDamage = {i: cwSpec[i] for i in range(1,21)}
casterP10Damage = {i: propulsive10[i] + cwSpec[i] for i in range(1,21)}
casterP12Damage = {i: propulsive12[i] + cwSpec[i] for i in range(1,21)}
casterP14Damage = {i: propulsive14[i] + cwSpec[i] for i in range(1,21)}
casterP16Damage = {i: propulsive16[i] + cwSpec[i] for i in range(1,21)}

cantripASDamage = {i: mStr[i] + int((sDice[i]-1)/2)*4.5 for i in range(1,21)}
cantripASDamage[1] = 4.5
cantripASDamage[2] = 4.5
cantripASDamage[3] = 4.5
cantripASDamage[4] = 4.5
cantripDDamage = {i: mStr[i] + max(0,int((sDice[i]-1)/2))*3.5 for i in range(1,21)}
cantripTPDamage = {i: mStr[i] + sDice[i]*3.5 for i in range(1,21)}
cantripRFDamage = {i: mStr[i] + sDice[i]*2.5 for i in range(1,21)}
cantripASPDamage = {i: (sDice[i]+1)/2*1 for i in range(1,21)}
cantripPFPDamage = {i: sDice[i]*2.5 for i in range(1,21)}

magicMissleDamage = {i: int((sDice[i]+1)/2) * 3.5 for i in range(1,21)}
spellDamage45 = {i: sDice[i]*4.5 for i in range(1,21)}
spellDamage55 = {i: sDice[i]*5.5 for i in range(1,21)}
spellDamage7 = {i: sDice[i]*7 for i in range(1,21)}
spellDamage8 = {i: sDice[i]*8 for i in range(1,21)}
spellDamage9 = {i: sDice[i]*9 for i in range(1,21)}
spellDamage10 = {i: sDice[i]*10 for i in range(1,21)}
spellDamage11 = {i: sDice[i]*11 for i in range(1,21)}
spellDamage12 = {i: sDice[i]*12 for i in range(1,21)}
spellDamage13 = {i: sDice[i]*13 for i in range(1,21)}

martialDamage = {i: mStr[i] + mwSpec[i] for i in range(1,21)}
martialRangedDamage = {i: mwSpec[i] for i in range(1,21)}
martialP10Damage = {i: propulsive10[i] + mwSpec[i] for i in range(1,21)}
martialP12Damage = {i: propulsive12[i] + mwSpec[i] for i in range(1,21)}
martialP14Damage = {i: propulsive14[i] + mwSpec[i] for i in range(1,21)}
martialP16Damage = {i: propulsive16[i] + mwSpec[i] for i in range(1,21)}

barbariananimaldamage = {i: martialDamage[i] + animalragedamage[i] for i in range(1,21)}
barbarianagileanimaldamage = {i: martialDamage[i] + int(animalragedamage[i]/2) for i in range(1,21)}
barbariandragondamage = {i: martialDamage[i] + dragonragedamage[i] for i in range(1,21)}
barbarianfurydamage = {i: martialDamage[i] + furyragedamage[i] for i in range(1,21)}
barbariangiantdamage = {i: martialDamage[i] + giantragedamage[i] for i in range(1,21)}
barbarianspiritdamage = {i: martialDamage[i] + spiritragedamage[i] for i in range(1,21)}

championsmiteevildamage = {i: martialDamage[i] + smiteevildamage[i] for i in range(1,21)}

warpriestDamage = {i: wStr[i] + cwSpec[i] + 1 for i in range(1,21)}
warpriestDamage[1] -= 1

warpriestSmiteDamage = {i: warpriestDamage[i] + sDice[i]*4.5 for i in range(1,21)}



fighterDamage = {i: mStr[i]+fwSpec[i] for i in range(1,21)}
fighterrangedDamage = {i: fwSpec[i] for i in range(1,21)}
fighterpropulsive12Damage = {i: propulsive12[i]+fwSpec[i] for i in range(1,21)}
fighterpropulsive14Damage = {i: propulsive14[i]+fwSpec[i] for i in range(1,21)}
fighterpropulsive16Damage = {i: propulsive16[i]+fwSpec[i] for i in range(1,21)}
fighterd10paDamage = {i: mStr[i]+fwSpec[i]+d10pad[i] for i in range(1,21)}
fighterd12paDamage = {i: mStr[i]+fwSpec[i]+d12pad[i] for i in range(1,21)}
fighterd10bfDamage = {i: mStr[i]+fwSpec[i]+d10bfd[i] for i in range(1,21)}
fighterd12bfDamage = {i: mStr[i]+fwSpec[i]+d12bfd[i] for i in range(1,21)}


d12pad = {i: 6.5 for i in range(1,21)}
for i in d12pad:
    if i>=10:
        d12pad[i]+=6.5
    if i>=18:
        d12pad[i]+=6.5

def ffd(level):
    if level < 10:
        return 0
    return mStr[level] + fwSpec[level]
fighterFailDamage = {i: mStr[i] + fwSpec[i] for i in range(1,21) }

class Result:
    def __init__(self, damage, pdamage, atk):
        self.damage = damage
        self.pdamage = pdamage
        
        self.futureAttacksFF = False
        self.nextAttackFF = False
        self.trueStrike = False
        self.nextStrikeBonus = 0
        
        self.addfirsthitdamage = 0
        self.addsecondhitdamage = 0 
        self.addthirdhitdamage = 0 
        self.addeveryhitdamage = 0
        
        self.atk = atk
        self.ishit = False
        
    def setFutureAttacksFF(self):
        self.futureAttacksFF = True
    def setNextAttackFF(self):
        self.nextAttackFF = True
    def setTrueStrike(self):
        self.trueStrike = True
    def setNextStrikeBonus(self, bonus):
        self.nextStrikeBonus = bonus
        
    def setCrit(self):
        self.ishit = True
    def setHit(self):
        self.ishit = True
    def setFail(self):
        pass
    def setCritFail(self):
        pass
    def setCritSuccessSave(self):
        pass
    def setSuccessSave(self):
        pass
    def setFailSave(self):
        pass
    def setCritFailSave(self):
        pass
    
    def isHit(self):
        return self.ishit
        
class AtkSelection:
#         4 types: 'Strike', 'SaveAttack', 'Save', 'Effect'
        def __init__(self, attack, damage):
            
            self.attack = attack
            self.attackBonus = 0
            self.damage = damage
            self.additionalDamage = 0
            self.damageBonus = 0
            self.persDamage = copy.copy(noneDamage)
            self.splashDamage = None
            self.wDice = copy.copy(wDice) # number of dice
            self.damageDie = 0 # 3.5
            self.weaponDamage = None
            self.damageDieBonus = None
            self.runeDamage = None
            self.flatfootedDamage = copy.copy(noneDamage)
            self.failureDamage = copy.copy(noneDamage)
            self.certainStrike = False
            self.critDamage = copy.copy(noneDamage)
            self.critPersDamage = copy.copy(noneDamage)
            
            self.isWeapon = False
            
            self.critSpecLevel = 21
            self.keenLevel = 21
            self.ffonCritLevel = 21
            self.ffonSuccessLevel = 21
            self.ffonFailLevel = 21
            
            self.attackBonusOnFail = 0
            
            self.minL = 1
            self.maxL = 20
            
        def critSuccessResult(self, level, db):
            return 0
        
        def successResult(self, level, db):
            return 0
        
        def failureResult(self, level, db):
            return 0
        
        def critFailureResult(self, level, db):
            return 0
            
        def setWeaponDamage(self, weaponDamageDiceName):
            if self.isWeapon and not self.weaponDamage:
                self.damageDie = damageDiceConverter[weaponDamageDiceName][0]
                self.damageDieBonus = damageDiceConverter[weaponDamageDiceName][1]
                self.weaponDamage = {i: self.wDice[i]*self.damageDie for i in range(1,21)}
                
            
        def setCriticalEffects(self, weaponCriticalName):
            if self.isWeapon:
                cd = criticalDiceConverter[weaponCriticalName]
                if cd[0]:
                    for i in range(1,21):
                        self.critDamage[i] += cd[1] + wDice[i]*2*(cd[1] - self.damageDie)
                else:
                    for i in range(1,21):
                        self.critDamage[i] += cd[1][i]
            
        def setCriticalSpecialization(self, csName):
            if self.isWeapon:
                if csName == "other":
                    return
                elif csName == "knife":
                    for i in range(self.critSpecLevel,21):
                        self.critPersDamage[i] += 3.5 + wiBonus[i]
                elif csName == "hammer":
                    self.ffonCritLevel = min(self.ffonCritLevel,self.critSpecLevel)
                elif csName == "sword":
                    self.ffonCritLevel = min(self.ffonCritLevel,self.critSpecLevel)
                elif csName == "pick":
                    for i in range(self.critSpecLevel,21):
                        self.critDamage[i] += self.wDice[i] * 2
        
        def setRuneDamage(self, r1, r2, r3, r4):
            if self.isWeapon:
                self.runeDamage = {i: 0 for i in range(1,21)}
                for i in range(1,21):
                    if i >= r1:
                        self.runeDamage[i]+=3.5
                    if i >= r2:
                        self.runeDamage[i]+=3.5
                    if i >= r3:
                        self.runeDamage[i]+=3.5
                    if i >= r4:
                        self.runeDamage[i]+=3.5
            
        def getAttack(self, level):
            if level>=self.minL and level<=self.maxL:
                return self.attack[level] + self.attackBonus
            return None
        
        def getDamageBonus(self, level):
            if level>=self.minL and level<=self.maxL:
                d = self.damage[level] + self.additionalDamage
                if self.damageDieBonus:
                    d += self.damageDieBonus*self.wDice[level]
                return d
            return 0
        
        def getDamageDice(self, level):
            if level>=self.minL and level<=self.maxL:
                d = 0
                if self.weaponDamage:
                    d += self.weaponDamage[level]
                if self.runeDamage:
                    d += self.runeDamage[level]
                return d + self.damageBonus
            return 0
        
        def getPersistentDamage(self, level):
            if self.persDamage:
                return self.persDamage[level]
            return 0
        
        def getSplashDamage(self, level):
            if self.splashDamage:
                return self.splashDamage[level]
            return 0
        
        def getCriticalPersistentDamage(self, level):
            if self.critPersDamage:
                return self.critPersDamage[level]
            return 0
        
        def getFFDamage(self, level):
            if self.flatfootedDamage:
                return self.flatfootedDamage[level]
            return 0
        
        def getFailureDamage(self, level):
            if self.failureDamage:
                if self.failureDamage[level] != 0:
                    return self.failureDamage[level] + self.damageBonus
            return 0
        
        def getCriticalBonusDamage(self, level):
            if self.critDamage:
                return self.critDamage[level]
            return 0
        
        def getKeen(self, level):
            if level >= self.keenLevel:
                return True
            return False
        def ffonCrit(self, level):
            if level >= self.ffonCritLevel:
                return True
            return False
        def ffonSuccess(self, level):
            if level >= self.ffonSuccessLevel:
                return True
            return False
        def ffonFail(self, level):
            if level >= self.ffonFailLevel:
                return True
            return False
        
        def modifyAB(self, ab):
            self.attackBonus = ab
        def modifyDB(self, db):
            self.damageBonus = db
        def modifyAD(self, ad):
            self.additionalDamage = ad
            
        def setKeen(self, level):
            self.keenLevel = level
            
        def setFFonCrit(self, level):
            self.ffonCritLevel = min(level,self.ffonCritLevel)
        def setFFonSuccess(self, level):
            self.ffonSuccessLevel = min(level,self.ffonSuccessLevel)
        def setFFonFail(self, level):
            self.ffonFailLevel = min(level,self.ffonFailLevel)
            
        def setLevels(self, minl, maxl):
            self.minL = max(minl, self.minL)
            self.maxL = min(maxl, self.maxL)

class Strike(AtkSelection):
    def __init__(self, attack, damage, isWeapon=True, csLevel=21):
        super().__init__(attack, damage)
        self.critSpecLevel = csLevel
        self.isWeapon = isWeapon
        
    def critSuccessResult(self, level, context):
        damage = self.getDamageBonus(level)
        damage += self.getDamageDice(level)
        damage += context.getExtraDamage()
        damage = max(damage,1)
        if context.flatfooted:
            damage += self.getFFDamage(level)
        
        damage = damage * 2
        
        damage += self.getSplashDamage(level)
        damage += self.getCriticalBonusDamage(level)
        
        pdamage = self.getCriticalPersistentDamage(level)
        r = Result(max(0,damage), pdamage, self)
        r.setCrit()
        if self.ffonCrit(level):
            r.setFutureAttacksFF()
            
        return r
        
    def successResult(self, level, context):
        damage = self.getDamageBonus(level)
        damage += self.getDamageDice(level)
        if context.flatfooted:
            damage += self.getFFDamage(level)
        damage += context.getExtraDamage()
        damage = max(damage,1)
        
            
        damage += self.getSplashDamage(level)
        pdamage = self.getPersistentDamage(level)
        
        
        r = Result(max(0,damage), pdamage, self)
        r.setHit()
        if self.ffonSuccess(level):
            r.setFutureAttacksFF()
            
        return r
        
    def failureResult(self, level, context):
        damage = 0
        
        
        
        if self.certainStrike:
            damage += self.getFailureDamage(level)
            if damage == 0:
                damage = self.damageBonus
            damage += self.getDamageBonus(level)
        else:
             damage += self.getFailureDamage(level)
        if damage != 0:
            damage += context.getDamageBonus()
            damage = max(damage,1)
            # todo add context damge bonus, not extra dice
            
            
        r = Result(max(0,damage), 0, self)
        r.setFail()
        r.setNextStrikeBonus(self.attackBonusOnFail)
        if self.ffonFail(level):
            r.setFutureAttacksFF()
            
        return r
        
    def critFailureResult(self, level, context):
        r = Result(0,0, self)
        r.setCritFail()
        return r
    
class SaveAttack(AtkSelection):
    def __init__(self, attack, damage):
        super().__init__(attack, damage)

    
    
class Save(AtkSelection):
    def __init__(self, dc, damage):
        super().__init__(dc, damage)

        
    def getDC(self, level):
        return self.getAttack(level)
    
    def critSuccessResult(self, level, context):
        
        r = Result(0, 0, self)
        r.setCritSuccessSave()
        return r
        
    def successResult(self, level, context):
        damage = self.getDamageBonus(level)
        damage += context.getDamageBonus()
        damage = damage / 2
        
        r = Result(max(0,damage), 0, self)
        r.setSuccessSave()
        return r
        
    def failureResult(self, level, context):
        damage = self.getDamageBonus(level)
        damage += context.getDamageBonus()
            
        r = Result(max(0,damage), 0, self)
        r.setFailSave()
        
            
        return r
        
    def critFailureResult(self, level, context):
        damage = self.getDamageBonus(level)
        damage += context.getDamageBonus()
        damage = damage * 2
        
        r = Result(max(0,damage), 0, self)
        r.setCritFailSave()
        return r
    
class Effect(AtkSelection):
    def __init__(self, damage):
        super().__init__(casterAttackBonus, damage)
        self.flatfootNextStrike = False
        self.flatfoot = False
        self.trueStrike = False
        
        self.addfirsthitdamage = None
        self.addsecondhitdamage = None 
        self.addthirdhitdamage = None
        self.addeveryhitdamage = None
        
    def effectResult(self, level, context):
        damage = self.getDamageBonus(level)
        damage += context.getExtraDamage()
        r = Result(damage,0, self)
        if self.flatfoot:
            r.futureAttacksFF = True
        elif self.flatfootNextStrike:
            r.nextAttackFF = True
        
        r.trueStrike = self.trueStrike
        
        if self.addfirsthitdamage:
            r.addfirsthitdamage = self.addfirsthitdamage[level]
        if self.addsecondhitdamage:
            r.addsecondhitdamage = self.addsecondhitdamage[level]
        if self.addthirdhitdamage:
            r.addthirdhitdamage = self.addthirdhitdamage[level]
        if self.addeveryhitdamage:
            r.addeveryhitdamage = self.addeveryhitdamage[level]
                    
        return r
    
        
class CombinedAttack:
    PDWeight = 0
    def __init__(self, attackList, function=min):
        self.function=function
        self.attackList=attackList
        # what if attackList has a combined attack?
        #also update create Traces
        
    def choose(self, d, pd, newd, newpd):
        totaldamage = d + pd*CombinedAttack.PDWeight
        newtotal = newd + newpd**CombinedAttack.PDWeight
        if self.function(totaldamage,newtotal) == totaldamage:
            return d, pd
        elif self.function(totaldamage,newtotal) == newtotal:
            return newd, newpd
        elif self.function(totaldamage,newtotal) == totaldamage + newtotal:
            return d+newd, pd+newpd
        elif self.function(totaldamage,newtotal) == totaldamage - newtotal:
            return d-newd, pd-newpd
        else:
            print(d, pd, newd, newpd)
        
    def contains(self, level):
        for sr in self.attackList:
            if type(sr) is CombinedAttack:
                srhas = sr.contains(level)
            else:
                srhas = True
                for st in sr:
                    if not st.getAttack(level):
                        srhas = False
            if srhas: return True
        return False
    
    def validFor(self, level):
        #returns attack lists that work on specified level
        validAttackList = []
        for sr in self.attackList:
            if type(sr) is CombinedAttack:
                if sr.contains(level):
                    validAttackList.append(sr)
            else:
                srhas = True
                for st in sr:
                    if not st.getAttack(level):
                        srhas = False
                if srhas: validAttackList.append(sr)
        return validAttackList
        
    
alchemistStrike = Strike(warpriestAttackBonus, alchemistDamage)
alchemistRangedStrike = Strike(warpriestAttackBonus, alchemistRangedDamage)

alchemistacids = Strike(bombAttackBonus, alchemistRangedDamage)
alchemistacids.isWeapon = False
alchemistacids.weaponDamage = acidFlaskDamage
alchemistacids.persDamage = acidFlaskPersDamage
alchemistacids.critPersDamage = {i: acidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistacids.splashDamage = bombSplashDamage

alchemistbacids = Strike(bombAttackBonus, alchemistRangedDamage)
alchemistbacids.isWeapon = False
alchemistbacids.weaponDamage = acidFlaskDamage
alchemistbacids.persDamage = acidFlaskPersDamage
alchemistbacids.critPersDamage = {i: acidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbacids.splashDamage = bomberSplashDamage

alchemistpacids = Strike(pbombAttackBonus, alchemistRangedDamage)
alchemistpacids.isWeapon = False
alchemistpacids.weaponDamage = pacidFlaskDamage
alchemistpacids.persDamage = pacidFlaskPersDamage
alchemistpacids.critPersDamage = {i: pacidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistpacids.splashDamage = pbombSplashDamage

alchemistbpacids = Strike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpacids.isWeapon = False
alchemistbpacids.weaponDamage = pacidFlaskDamage
alchemistbpacids.persDamage = pacidFlaskPersDamage
alchemistbpacids.critPersDamage = {i: pacidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbpacids.splashDamage = pbomberSplashDamage

alchemistfires = Strike(bombAttackBonus, alchemistRangedDamage)
alchemistfires.isWeapon = False
alchemistfires.weaponDamage = alchemistsFireDamage
alchemistfires.persDamage = alchemistsFirePersDamage
alchemistfires.critPersDamage = {i: alchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistfires.splashDamage = bombSplashDamage

alchemistbfires = Strike(bombAttackBonus, alchemistRangedDamage)
alchemistbfires.isWeapon = False
alchemistbfires.weaponDamage = alchemistsFireDamage
alchemistbfires.persDamage = alchemistsFirePersDamage
alchemistbfires.critPersDamage = {i: alchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbfires.splashDamage = bomberSplashDamage

alchemistpfires = Strike(pbombAttackBonus, alchemistRangedDamage)
alchemistpfires.isWeapon = False
alchemistpfires.weaponDamage = palchemistsFireDamage
alchemistpfires.persDamage = palchemistsFirePersDamage
alchemistpfires.critPersDamage = {i: palchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistpfires.splashDamage = pbombSplashDamage

alchemistbpfires = Strike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpfires.isWeapon = False
alchemistbpfires.weaponDamage = palchemistsFireDamage
alchemistbpfires.persDamage = palchemistsFirePersDamage
alchemistbpfires.critPersDamage = {i: palchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbpfires.splashDamage = pbomberSplashDamage

alchemistfrosts = Strike(bombAttackBonus, alchemistRangedDamage)
alchemistfrosts.isWeapon = False
alchemistfrosts.weaponDamage = blfvDamage
alchemistfrosts.splashDamage = bombSplashDamage

alchemistbfrosts = Strike(bombAttackBonus, alchemistRangedDamage)
alchemistbfrosts.isWeapon = False
alchemistbfrosts.weaponDamage = blfvDamage
alchemistbfrosts.splashDamage = bomberSplashDamage

alchemistpfrosts = Strike(pbombAttackBonus, alchemistRangedDamage)
alchemistpfrosts.isWeapon = False
alchemistpfrosts.weaponDamage = pblfvDamage
alchemistpfrosts.splashDamage = pbombSplashDamage

alchemistbpfrosts = Strike(pbombAttackBonus, alchemistRangedDamage)
alchemistbpfrosts.isWeapon = False
alchemistbpfrosts.weaponDamage = pblfvDamage
alchemistbpfrosts.splashDamage = pbomberSplashDamage

alchemistlightnings = Strike(bombAttackBonus, alchemistRangedDamage)
alchemistlightnings.isWeapon = False
alchemistlightnings.setFFonCrit(1)
alchemistlightnings.setFFonSuccess(1)
alchemistlightnings.weaponDamage = blfvDamage
alchemistlightnings.splashDamage = bombSplashDamage

alchemistblightnings = Strike(bombAttackBonus, alchemistRangedDamage)
alchemistblightnings.isWeapon = False
alchemistblightnings.setFFonCrit(1)
alchemistblightnings.setFFonSuccess(1)
alchemistblightnings.weaponDamage = blfvDamage
alchemistblightnings.splashDamage = bomberSplashDamage

alchemistplightnings = Strike(pbombAttackBonus, alchemistRangedDamage)
alchemistplightnings.isWeapon = False
alchemistplightnings.setFFonCrit(1)
alchemistplightnings.setFFonSuccess(1)
alchemistplightnings.weaponDamage = pblfvDamage
alchemistplightnings.splashDamage = pbombSplashDamage

alchemistbplightnings = Strike(pbombAttackBonus, alchemistRangedDamage)
alchemistbplightnings.isWeapon = False
alchemistbplightnings.setFFonCrit(1)
alchemistbplightnings.setFFonSuccess(1)
alchemistbplightnings.weaponDamage = pblfvDamage
alchemistbplightnings.splashDamage = pbomberSplashDamage

alchemistbestialClawStrike = Strike(mutagenstrikeAttackBonus, alchemistDamage)
alchemistbestialClawStrike.weaponDamage = bestialClawDamage

alchemistbestialJawStrike = Strike(mutagenstrikeAttackBonus, alchemistDamage)
alchemistbestialJawStrike.weaponDamage = bestialJawDamage

alchemistferalClawStrike = Strike(mutagenstrikeAttackBonus, alchemistDamage)
alchemistferalClawStrike.weaponDamage = {i: bestialClawDamage[i] + wDice[i] for i in range(1,21)}

alchemistferalJawStrike = Strike(mutagenstrikeAttackBonus, alchemistDamage)
alchemistferalJawStrike.weaponDamage = {i: bestialJawDamage[i] + wDice[i] for i in range(1,21)}

alchemistAttackSwitcher = {'Alchemist Melee Strike': [alchemistStrike],
                    'Alchemist Ranged Strike': [alchemistRangedStrike],
                    'Alchemist Bestial Claw': [alchemistbestialClawStrike],
                    'Alchemist Bestial Jaw': [alchemistbestialJawStrike],
                    'Alchemist Feral Claw': [alchemistferalClawStrike],
                    'Alchemist Feral Jaw': [alchemistferalJawStrike],
                    'Alchemist Acid Flask': [alchemistacids],
                    'Alchemist Bomber Acid': [alchemistbacids],
                    'Alchemist Perpetual Acid': [alchemistpacids],
                    'Alchemist Bomber Perpetual Acid': [alchemistbpacids],
                    'Alchemist Fire': [alchemistfires],
                    'Alchemist Bomber Fire': [alchemistbfires],
                    'Alchemist Perpetual Fire': [alchemistpfires],
                    'Alchemist Bomber Perpetual Fire': [alchemistbpfires],
                    'Alchemist Bottled Lightning': [alchemistlightnings],
                    'Alchemist Bomber Lightning': [alchemistblightnings],
                    'Alchemist Perpetual Lightning': [alchemistplightnings],
                    'Alchemist Bomber Perpetual Lightning': [alchemistbplightnings],
                    'Alchemist Frost Vial': [alchemistfrosts],
                    'Alchemist Bomber Frost': [alchemistbfrosts],
                    'Alchemist Perpetual Frost': [alchemistpfrosts],
                    'Alchemist Bomber Perpetual Frost': [alchemistbpfrosts]}

# Barbarian
# rage, instinct, devastator


barbariananimaljaws = Strike(martialAttackBonus, barbariananimaldamage, csLevel=5)
barbariananimaljaws.weaponDamage = animalJawDamage
barbariananimalclaws = Strike(martialAttackBonus, barbarianagileanimaldamage, csLevel=5)
barbariananimalclaws.weaponDamage = animalClawDamage

barbariandragonstrike = Strike(martialAttackBonus, barbariandragondamage, csLevel=5)

barbarianfurystrike = Strike(martialAttackBonus, barbarianfurydamage, csLevel=5)

barbariangiantstrike = Strike(martialAttackBonus, barbariangiantdamage, csLevel=5)

barbarianspiritstrike = Strike(martialAttackBonus, barbarianspiritdamage, csLevel=5)

barbarianAttackSwitcher = {'Barbarian Animal Claw': [barbariananimalclaws],
                    'Barbarian Animal Jaw': [barbariananimaljaws],
                    'Barbarian Dragon Strike': [barbariandragonstrike],
                    'Barbarian Fury Strike': [barbarianfurystrike],
                    'Barbarian Giant Strike': [barbariangiantstrike],
                    'Barbarian Spirit Strike': [barbarianspiritstrike]}


casterstrike = Strike(casterAttackBonus, strCasterDamage, csLevel=11)
casterrangedstrike = Strike(casterAttackBonus, rangedCasterDamage, csLevel=11)
casterpropulsive10 = Strike(casterAttackBonus, casterP10Damage, csLevel=11)
casterpropulsive12 = Strike(casterAttackBonus, casterP12Damage, csLevel=11)
casterpropulsive14 = Strike(casterAttackBonus, casterP14Damage, csLevel=11)
casterpropulsive16 = Strike(casterAttackBonus, casterP16Damage, csLevel=11)

martialstrike = Strike(martialAttackBonus, martialDamage, csLevel=5)
martialrangedstrike = Strike(martialAttackBonus, martialRangedDamage, csLevel=5)
martialp10 = Strike(martialAttackBonus, martialP10Damage, csLevel=5)
martialp12 = Strike(martialAttackBonus, martialP12Damage, csLevel=5)
martialp14 = Strike(martialAttackBonus, martialP14Damage, csLevel=5)
martialp16 = Strike(martialAttackBonus, martialP16Damage, csLevel=5)

championsmiteevil = Strike(martialAttackBonus, championsmiteevildamage, csLevel=3)

warprieststrike = Strike(warpriestAttackBonus, warpriestDamage, csLevel=7)
warpriestsmite = Strike(warpriestAttackBonus, warpriestSmiteDamage, csLevel=7)

roguestrike = Strike(martialAttackBonus, martialDamage, csLevel=5)
roguestrike.flatfootedDamage = sneakattackdamage

rangerprecedge = Effect(noneDamage)
rangerprecedge.addfirsthitdamage = rangerprecedgedamage1
rangerprecedge.addsecondhitdamage = rangerprecedgedamage2
rangerprecedge.addthirdhitdamage = rangerprecedgedamage3

rangerbearsupport = Effect(noneDamage)
rangerbearsupport.addeveryhitdamage = rangerbearsupportdamage

bespellweapon = Effect(noneDamage)
bespellweapon.addeveryhitdamage = {i: 3.5 for i in range(1,21)}

otherAttackSwitcher = {'Caster Strike': [casterstrike],
                       'Caster Ranged Strike': [casterrangedstrike],
                       'Caster Propulsive 10': [casterpropulsive10],
                       'Caster Propulsive 12': [casterpropulsive12],
                       'Caster Propulsive 14': [casterpropulsive14],
                       'Caster Propulsive 16': [casterpropulsive16],
                       'Martial Strike': [martialstrike],
                       'Martial Ranged Strike': [martialrangedstrike],
                       'Martial Propulsive 10': [martialp10],
                       'Martial Propulsive 12': [martialp12],
                       'Martial Propulsive 14': [martialp14],
                       'Martial Propulsive 16': [martialp16],
                       'Champion Smite Evil': [championsmiteevil],
                       'Warpriest Strike': [warprieststrike],
                       'Warpriest Smite': [warpriestsmite],
                       'Rogue Strike': [roguestrike],
                       'Ranger Precision Edge': [rangerprecedge],
                       'Ranger Bear Support': [rangerbearsupport],
                       'Bespell Weapon': [bespellweapon]
                       }

cantripAS = Strike(cantripAttackBonus, cantripASDamage, isWeapon=False)
cantripAS.critPersDamage = cantripASPDamage
cantripEA = Save(spellDC, cantripRFDamage)
cantripD = Save(spellDC, cantripDDamage)
cantripDL = Strike(cantripAttackBonus, cantripRFDamage, isWeapon=False)
cantripPF = Strike(cantripAttackBonus, cantripRFDamage, isWeapon=False)
cantripPF.critPersDamage = cantripPFPDamage
cantripTP = Strike(cantripAttackBonus, cantripTPDamage, isWeapon=False)
cantripRF = Strike(cantripAttackBonus, cantripRFDamage, isWeapon=False)

cantripAttackSwitcher = {'Acid Splash': [cantripAS],
                  'Electric Arc': [cantripEA],
                  'Daze': [cantripD],
                  'Divine Lance': [cantripDL],
                  'Produce Flame': [cantripPF],
                  'Ray of Frost': [cantripRF],
                  'Telekinetic Projectile': [cantripTP]
                  }
# fighter, double slice, exacting strike, power attack, snagging strike
# combat grab
        
fighterstrike = Strike(fighterAttackBonus,fighterDamage, csLevel=5)

fighterexactingstrike = Strike(fighterAttackBonus, fighterDamage, csLevel=5)
fighterexactingstrike.attackBonusOnFail = 5

fightersnaggingstrike = Strike(fighterAttackBonus,fighterDamage, csLevel=5)
fightersnaggingstrike.setFFonCrit(1)
fightersnaggingstrike.setFFonSuccess(1)

fightercertainstrike = Strike(fighterAttackBonus,fighterDamage, csLevel=5)
fightercertainstrike.certainStrike = True

fighterpowerattack = Strike(fighterAttackBonus,fighterDamage, csLevel=5)
fighterpowerattack.wDice[i] += 1
for i in range(1,21):
    if i >= 10:
        fighterpowerattack.wDice[i] += 1
    if i >= 18:
        fighterpowerattack.wDice[i] += 1
fighterd10powerattack = Strike(fighterAttackBonus,fighterd10paDamage, csLevel=5)
fighterd12powerattack = Strike(fighterAttackBonus,fighterd12paDamage, csLevel=5)

fighterbrutishshove = Strike(fighterAttackBonus,fighterDamage, csLevel=5)
fighterbrutishshove.setFFonCrit(1)
fighterbrutishshove.setFFonSuccess(1)
fighterbrutishshove.setFFonFail(1)

fighterknockdown = Strike(fighterAttackBonus,fighterDamage, csLevel=5)
fighterknockdown.setFFonCrit(1)
fighterknockdown.setFFonSuccess(1)

fighterd10brutalfinish = Strike(fighterAttackBonus,fighterd10bfDamage, csLevel=5)
fighterd10brutalfinish.failureDamage = d10bfd
fighterd12brutalfinish = Strike(fighterAttackBonus,fighterd12bfDamage, csLevel=5)
fighterd12brutalfinish.failureDamage = d12bfd

fighterrangedstrike = Strike(fighterAttackBonus, fighterrangedDamage, csLevel=5)
fighterpropulsive12 = Strike(fighterAttackBonus, fighterpropulsive12Damage, csLevel=5)
fighterpropulsive14 = Strike(fighterAttackBonus, fighterpropulsive14Damage, csLevel=5)
fighterpropulsive16 = Strike(fighterAttackBonus, fighterpropulsive16Damage, csLevel=5)

fighterpropulsive12cs = Strike(fighterAttackBonus, fighterpropulsive12Damage, csLevel=5)
fighterpropulsive12cs.certainStrike = True
fighterpropulsive14cs = Strike(fighterAttackBonus, fighterpropulsive14Damage, csLevel=5)
fighterpropulsive14cs.certainStrike = True
fighterpropulsive16cs = Strike(fighterAttackBonus, fighterpropulsive16Damage, csLevel=5)
fighterpropulsive16cs.certainStrike = True

fighterpropulsive12es = Strike(fighterAttackBonus, fighterpropulsive12Damage, csLevel=5)
fighterpropulsive12es.attackBonusOnFail = 5
fighterpropulsive14es = Strike(fighterAttackBonus, fighterpropulsive14Damage, csLevel=5)
fighterpropulsive14es.attackBonusOnFail = 5
fighterpropulsive16es = Strike(fighterAttackBonus, fighterpropulsive16Damage, csLevel=5)
fighterpropulsive16es.attackBonusOnFail = 5

fighterAttackSwitcher = {'Fighter Melee Strike': 
                  [fighterstrike], 
                  'Fighter Exacting Strike':
                  [fighterexactingstrike],
                  'Fighter Snagging Strike': 
                  [fightersnaggingstrike], 
                  'Fighter Certain Strike': 
                  [fightercertainstrike],
                  'Fighter d10 Power Attack': 
                  [fighterd10powerattack], 
                  'Fighter d12 Power Attack': 
                  [fighterd12powerattack], 
                  'Fighter Brutish Shove': 
                  [fighterbrutishshove], 
                  'Fighter Knockdown': 
                  [fighterknockdown], 
                  'Fighter d10 Brutal Finish': 
                  [fighterd10brutalfinish], 
                  'Fighter d12 Brutal Finish': 
                  [fighterd12brutalfinish],
                  'Fighter Ranged Strike':
                  [fighterrangedstrike],
                  'Fighter propulsive 12':
                  [fighterpropulsive12],
                  'Fighter propulsive 14':
                  [fighterpropulsive14],
                  'Fighter propulsive 16':
                  [fighterpropulsive16],
                  'Fighter propulsive 12 es':
                  [fighterpropulsive12es],
                  'Fighter propulsive 14 es':
                  [fighterpropulsive14es],
                  'Fighter propulsive 16 es':
                  [fighterpropulsive16es],
                  'Fighter propulsive 12 cs':
                  [fighterpropulsive12cs],
                  'Fighter propulsive 14 cs':
                  [fighterpropulsive14cs],
                  'Fighter propulsive 16 cs':
                  [fighterpropulsive16cs]
                  }
    
    
druidwolf = Strike(druidwolfattack, druidwolfdamage, isWeapon=False)
rangerwolf = Strike(rangerwolfattack, rangerwolfdamage, isWeapon=False)
druidbear = Strike(druidbearattack, druidbeardamage, isWeapon=False)
rangerbear = Strike(rangerbearattack, rangerbeardamage, isWeapon=False)
  
animalcompanionAttackSwitcher = {'Druid Bear': [druidbear],
                          'Druid Wolf': [druidwolf],
                          'Ranger Bear': [rangerbear],
                          'Ranger Wolf': [rangerwolf]}

summonanimal = Strike(sumAniAttack, sumAniDamage, isWeapon=False)
summondragon = Strike(sumDraAttack, sumDraDamage, isWeapon=False)
summondragon.setLevels(9,20)

summonAttackSwitcher = {'Summon Animal': [summonanimal],
                        'Summon Dragon': [summondragon]}
 
attackExtreme = creatureData['Attack']['Extreme']
attackHigh = creatureData['Attack']['High']
attackModerate = creatureData['Attack']['Moderate']
attackLow = creatureData['Attack']['Low']
damageExtreme = creatureData['Damage']['Extreme']
damageHigh = creatureData['Damage']['High']
damageModerate = creatureData['Damage']['Moderate']
damageLow = creatureData['Damage']['Low']

monsterEH = Strike(attackExtreme,damageHigh,isWeapon=False)
monsterEM = Strike(attackExtreme,damageModerate,isWeapon=False)

monsterHE = Strike(attackHigh,damageExtreme,isWeapon=False)
monsterHH = Strike(attackHigh,damageHigh,isWeapon=False)
monsterHM = Strike(attackHigh,damageModerate,isWeapon=False)
monsterHL = Strike(attackHigh,damageLow,isWeapon=False)

monsterME = Strike(attackModerate,damageExtreme,isWeapon=False)
monsterMH = Strike(attackModerate,damageHigh,isWeapon=False)
monsterMM = Strike(attackModerate,damageModerate,isWeapon=False)
monsterML = Strike(attackModerate,damageLow,isWeapon=False)

monsterLH = Strike(attackLow,damageHigh,isWeapon=False)
monsterLM = Strike(attackLow,damageModerate,isWeapon=False)
monsterLL = Strike(attackLow,damageLow,isWeapon=False)
    
monsterAttackSwitcher = {'Monster Extreme Attack High Damage': [monsterEH],
                  'Monster Extreme Attack Moderate Damage': [monsterEM],
                  'Monster High Attack Extreme Damage': [monsterHE],
                  'Monster High Attack High Damage': [monsterHH],
                  'Monster High Attack Moderate Damage': [monsterHM],
                  'Monster High Attack Low Damage': [monsterHL],
                  'Monster Moderate Attack Extreme Damage': [monsterME],
                  'Monster Moderate Attack High Damage': [monsterMH],
                  'Monster Moderate Attack Moderate Damage': [monsterMM],
                  'Monster Moderate Attack Low Damage': [monsterML],
                  'Monster Low Attack High Damage': [monsterLH],
                  'Monster Low Attack Moderate Damage': [monsterLM],
                  'Monster Low Attack Low Damage': [monsterLL]   
                  }

#effects
flatfoot = Effect(noneDamage)
flatfoot.flatfoot = True

flatfootnext = Effect(noneDamage)
flatfootnext.flatfootNextStrike = True

effectAttackSwitcher = {'Flat Foot Target': [flatfoot],
                        'Flat Foot Next Strike': [flatfootnext]}


magicmissle = Effect(magicMissleDamage)
truestrike = Effect(noneDamage)
truestrike.trueStrike = True

basic45 = Save(spellDC, spellDamage45)
basic55 = Save(spellDC, spellDamage55)
basic7 = Save(spellDC, spellDamage7)
basic8 = Save(spellDC, spellDamage8)
basic9 = Save(spellDC, spellDamage9)

spellAttackSwitcher = {'Basic Save 1d8': [basic45],
                       'Basic Save 1d10': [basic55],
                       'Basic Save 2d6': [basic7],
                'Basic Save 2d6+1': [basic8],
                'Basic Save 2d8': [basic9],
                'Magic Missle': [magicmissle],
                'True Strike': [truestrike]}

attackSwitcher = {**alchemistAttackSwitcher,
                  **barbarianAttackSwitcher,
                  **otherAttackSwitcher,
                  **cantripAttackSwitcher,
                  **fighterAttackSwitcher,
                  **animalcompanionAttackSwitcher,
                  **summonAttackSwitcher,
                  **monsterAttackSwitcher,
                  **effectAttackSwitcher,
                  **spellAttackSwitcher}