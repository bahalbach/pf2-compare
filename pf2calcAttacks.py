# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:18:59 2019

@author: bhalb
"""
import copy
from pf2calcMonsterStats import creatureData

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

fProf = mProf
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
        
d6Damage = [3.5 * wDice[i] for i in wDice]
d8Damage = [4.5 * wDice[i] for i in wDice]
d10Damage = [5.5 * wDice[i] for i in wDice]
d12Damage = [6.5 * wDice[i] for i in wDice]

damageDiceConverter = {"1d4": 2.5,
                       "1d6": 3.5,
                       "1d8/1d6+1": 4.5,
                       "1d10/1d8+1/1d6+2": 5.5,
                       "1d12/1d10+1/1d8+2": 6.5,
                       "1d12+1/1d10+2": 7.5}

noneDamage = {i: 0 for i in range(1,21)}
deadlyd6Damage = {i: max(3.5,(wDice[i]-1)*3.5) for i in range(1,21)}
deadlyd8Damage = {i: max(4.5,(wDice[i]-1)*4.5) for i in range(1,21)}
deadlyd10Damage = {i: max(5.5,(wDice[i]-1)*5.5) for i in range(1,21)}
deadlyd12Damage = {i: max(6.5,(wDice[i]-1)*6.5) for i in range(1,21)}
fatald8Damage = {i: 4.5 + wDice[i]*4 for i in range(1,21)}
fatald10Damage = {i: 5.5 + wDice[i]*4 for i in range(1,21)}
fatald12Damage = {i: 6.5 + wDice[i]*2 for i in range(1,21)}

criticalDiceConverter = {"none": noneDamage,
                 "deadly d6": deadlyd6Damage,
                 "deadly d8": deadlyd8Damage,
                 "deadly d10": deadlyd10Damage,
                 "deadly d12": deadlyd12Damage,
                 "fatal d8": fatald8Damage,
                 "fatal d10": fatald10Damage,
                 "fatal d12": fatald12Damage
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

martialDamage = {i: mStr[i] + mwSpec[i] for i in range(1,21)}

warpriestDamage = {i: wStr[i] + cwSpec[i] + 1 for i in range(1,21)}
warpriestDamage[1] -= 1


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

class AtkSelection:
#         attack
#         damage
#         target
        def __init__(self, attack, damage, csLevel=21, fd=None, isWeapon=True):
            self.attack = attack
            self.damage = damage
            self.persDamage = copy.copy(noneDamage)
            self.splashDamage = None
            self.isWeapon = isWeapon
            
            self.critSpecLevel = csLevel
            self.wDice = copy.copy(wDice) # number of dice
            self.damageDice = 0 # 3.5
            self.weaponDamage = None
            self.runeDamage = None
            
            self.flatfootedDamage = None
            
            if fd:
                self.fd = copy.copy(fd)
            else:
                self.fd = copy.copy(noneDamage)
            self.cd = copy.copy(noneDamage)
            self.critPersDamage = copy.copy(noneDamage)
            
            self.ab = 0
            self.db = 0
            
            self.keenLevel = 21
            self.ffonCritLevel = 21
            self.ffonSuccessLevel = 21
            self.ffonFailLevel = 21
            
            self.minL = 1
            self.maxL = 20
            
        def setWeaponDamage(self, weaponDamageDiceName):
            if self.isWeapon and not self.weaponDamage:
                self.damageDice = damageDiceConverter[weaponDamageDiceName]
                self.weaponDamage = {i: self.wDice[i]*self.damageDice for i in range(1,21)}
            
        def setCriticalEffects(self, weaponCriticalName):
            if self.isWeapon:
                cd = criticalDiceConverter[weaponCriticalName]
                for i in range(1,21):
                    self.cd[i] += cd[i]
            
        def setCriticalSpecialization(self, csName):
            if self.isWeapon:
                if csName == "other/none":
                    return
                elif csName == "dart/knife":
                    for i in range(self.critSpecLevel,21):
                        self.critPersDamage[i] += 3.5 + wiBonus[i]
                elif csName == "flail/hammer/sword":
                    self.ffonCritLevel = min(self.ffonCritLevel,self.critSpecLevel)
                elif csName == "pick":
                    for i in range(self.critSpecLevel,21):
                        self.cd[i] += self.wDice[i] * 2
        
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
                return self.attack[level] + self.ab
            return None
        
        def getDamage(self, level):
            if level>=self.minL and level<=self.maxL:
                d = self.damage[level] + self.db
                if self.weaponDamage:
                    d += self.weaponDamage[level]
                if self.runeDamage:
                    d += self.runeDamage[level]
                return d
            return None
        
        def getPersistentDamage(self, level):
            return self.persDamage[level]
        
        def getSplashDamage(self, level):
            if self.splashDamage:
                return self.splashDamage[level]
            return 0
        
        def getCriticalPersistentDamage(self, level):
            return self.critPersDamage[level]
        
        def getFFDamage(self, level):
            if self.flatfootedDamage:
                return self.flatfootedDamage[level]
            return 0
        
        def getFD(self, level):
            if self.fd:
                return self.fd[level] + self.db
            return 0
        
        def getCD(self, level):
            if self.cd:
                return self.cd[level]
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
            self.ab = ab
        def modifyDB(self, db):
            self.db = db
            
        def setKeen(self, level):
            self.keenLevel = level
        def setFFonCrit(self, level):
            self.ffonCritLevel = min(level,self.ffonCritLevel)
        def setFFonSuccess(self, level):
            self.ffonSuccessLevel = min(level,self.ffonSuccessLevel)
        def setFFonFail(self, level):
            self.ffonFailLevel = min(level,self.ffonFailLevel)
        def setLevels(self, minl, maxl):
            self.minL, self.maxL = minl, maxl
            
class CombinedAttack:
    def __init__(self, attackList, function=min):
        self.function=function
        self.attackList=attackList
        # what if attackList has a combined attack?
        #also update create Traces
        
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
        
    
alchemistStrike = AtkSelection(warpriestAttackBonus, alchemistDamage)
alchemistRangedStrike = AtkSelection(warpriestAttackBonus, alchemistRangedDamage)

alchemistacids = AtkSelection(bombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistacids.weaponDamage = acidFlaskDamage
alchemistacids.persDamage = acidFlaskPersDamage
alchemistacids.critPersDamage = {i: acidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistacids.splashDamage = bombSplashDamage

alchemistbacids = AtkSelection(bombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistbacids.weaponDamage = acidFlaskDamage
alchemistbacids.persDamage = acidFlaskPersDamage
alchemistbacids.critPersDamage = {i: acidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbacids.splashDamage = bomberSplashDamage

alchemistpacids = AtkSelection(pbombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistpacids.weaponDamage = pacidFlaskDamage
alchemistpacids.persDamage = pacidFlaskPersDamage
alchemistpacids.critPersDamage = {i: pacidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistpacids.splashDamage = pbombSplashDamage

alchemistbpacids = AtkSelection(pbombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistbpacids.weaponDamage = pacidFlaskDamage
alchemistbpacids.persDamage = pacidFlaskPersDamage
alchemistbpacids.critPersDamage = {i: pacidFlaskPersDamage[i]*2 for i in range(1,21)}
alchemistbpacids.splashDamage = pbomberSplashDamage

alchemistfires = AtkSelection(bombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistfires.weaponDamage = alchemistsFireDamage
alchemistfires.persDamage = alchemistsFirePersDamage
alchemistfires.critPersDamage = {i: alchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistfires.splashDamage = bombSplashDamage

alchemistbfires = AtkSelection(bombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistbfires.weaponDamage = alchemistsFireDamage
alchemistbfires.persDamage = alchemistsFirePersDamage
alchemistbfires.critPersDamage = {i: alchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbfires.splashDamage = bomberSplashDamage

alchemistpfires = AtkSelection(pbombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistpfires.weaponDamage = palchemistsFireDamage
alchemistpfires.persDamage = palchemistsFirePersDamage
alchemistpfires.critPersDamage = {i: palchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistpfires.splashDamage = pbombSplashDamage

alchemistbpfires = AtkSelection(pbombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistbpfires.weaponDamage = palchemistsFireDamage
alchemistbpfires.persDamage = palchemistsFirePersDamage
alchemistbpfires.critPersDamage = {i: palchemistsFirePersDamage[i]*2 for i in range(1,21)}
alchemistbpfires.splashDamage = pbomberSplashDamage

alchemistfrosts = AtkSelection(bombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistfrosts.weaponDamage = blfvDamage
alchemistfrosts.splashDamage = bombSplashDamage

alchemistbfrosts = AtkSelection(bombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistbfrosts.weaponDamage = blfvDamage
alchemistbfrosts.splashDamage = bomberSplashDamage

alchemistpfrosts = AtkSelection(pbombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistpfrosts.weaponDamage = pblfvDamage
alchemistpfrosts.splashDamage = pbombSplashDamage

alchemistbpfrosts = AtkSelection(pbombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistbpfrosts.weaponDamage = pblfvDamage
alchemistbpfrosts.splashDamage = pbomberSplashDamage

alchemistlightnings = AtkSelection(bombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistlightnings.setFFonCrit(1)
alchemistlightnings.setFFonSuccess(1)
alchemistlightnings.weaponDamage = blfvDamage
alchemistlightnings.splashDamage = bombSplashDamage

alchemistblightnings = AtkSelection(bombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistblightnings.setFFonCrit(1)
alchemistblightnings.setFFonSuccess(1)
alchemistblightnings.weaponDamage = blfvDamage
alchemistblightnings.splashDamage = bomberSplashDamage

alchemistplightnings = AtkSelection(pbombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistplightnings.setFFonCrit(1)
alchemistplightnings.setFFonSuccess(1)
alchemistplightnings.weaponDamage = pblfvDamage
alchemistplightnings.splashDamage = pbombSplashDamage

alchemistbplightnings = AtkSelection(pbombAttackBonus, alchemistRangedDamage, isWeapon=False)
alchemistbplightnings.setFFonCrit(1)
alchemistbplightnings.setFFonSuccess(1)
alchemistbplightnings.weaponDamage = pblfvDamage
alchemistbplightnings.splashDamage = pbomberSplashDamage

alchemistbestialClawStrike = AtkSelection(mutagenstrikeAttackBonus, alchemistDamage)
alchemistbestialClawStrike.weaponDamage = bestialClawDamage

alchemistbestialJawStrike = AtkSelection(mutagenstrikeAttackBonus, alchemistDamage)
alchemistbestialJawStrike.weaponDamage = bestialJawDamage

alchemistferalClawStrike = AtkSelection(mutagenstrikeAttackBonus, alchemistDamage)
alchemistferalClawStrike.weaponDamage = {i: bestialClawDamage[i] + wDice[i] for i in range(1,21)}

alchemistferalJawStrike = AtkSelection(mutagenstrikeAttackBonus, alchemistDamage)
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

# fighter, double slice, exacting strike, power attack, snagging strike
# combat grab
        
fighterstrike = AtkSelection(fighterAttackBonus,fighterDamage, csLevel=5)

fightersnaggingstrike = AtkSelection(fighterAttackBonus,fighterDamage, csLevel=5)
fightersnaggingstrike.setFFonCrit(1)
fightersnaggingstrike.setFFonSuccess(1)

fightercertainstrike = AtkSelection(fighterAttackBonus,fighterDamage, csLevel=5, fd=fighterFailDamage)

fighterpowerattack = AtkSelection(fighterAttackBonus,fighterDamage, csLevel=5)
fighterpowerattack.wDice[i] += 1
for i in range(1,21):
    if i >= 10:
        fighterpowerattack.wDice[i] += 1
    if i >= 18:
        fighterpowerattack.wDice[i] += 1
fighterd10powerattack = AtkSelection(fighterAttackBonus,fighterd10paDamage, csLevel=5)
fighterd12powerattack = AtkSelection(fighterAttackBonus,fighterd12paDamage, csLevel=5)

fighterbrutishshove = AtkSelection(fighterAttackBonus,fighterDamage, csLevel=5)
fighterbrutishshove.setFFonCrit(1)
fighterbrutishshove.setFFonSuccess(1)
fighterbrutishshove.setFFonFail(1)

fighterknockdown = AtkSelection(fighterAttackBonus,fighterDamage, csLevel=5)
fighterknockdown.setFFonCrit(1)
fighterknockdown.setFFonSuccess(1)

fighterd10brutalfinish = AtkSelection(fighterAttackBonus,fighterd10bfDamage, csLevel=5, fd=fighterd10bfDamage)
fighterd12brutalfinish = AtkSelection(fighterAttackBonus,fighterd12bfDamage, csLevel=5, fd=fighterd12bfDamage)

fighterpropulsive12 = AtkSelection(fighterAttackBonus, fighterpropulsive12Damage, csLevel=5)
fighterpropulsive14 = AtkSelection(fighterAttackBonus, fighterpropulsive14Damage, csLevel=5)
fighterpropulsive16 = AtkSelection(fighterAttackBonus, fighterpropulsive16Damage, csLevel=5)

fighterAttackSwitcher = {'Fighter Melee Strike': 
                  [fighterstrike], 
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
                  'Fighter propulsive 12':
                  [fighterpropulsive12],
                  'Fighter propulsive 14':
                  [fighterpropulsive14],
                  'Fighter propulsive 16':
                  [fighterpropulsive16]
                  }

attackSwitcher = {**alchemistAttackSwitcher,
                  **fighterAttackSwitcher}