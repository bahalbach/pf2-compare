import copy
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

fighterAttackBonus = {i: fProf[i] + mStr[i] + wiBonus[i] for i in range(1,21)}





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

fighterDamage = {i: mStr[i]+fwSpec[i] for i in range(1,21)}
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



class Target:
    def __init__(self,AC,Fort,Ref,Will):
        self.ac = AC
        self.fort = Fort
        self.ref = Ref
        self.will = Will
        
    def getAC(self, level):
        if level in self.ac.keys():
            return self.ac[level]
        
averageAcByLevel = {-1: 15,
 0: 16,
 1: 17,
 2: 18,
 3: 19,
 4: 21,
 5: 22,
 6: 24,
 7: 25,
 8: 27,
 9: 28,
 10: 30,
 11: 31,
 12: 33,
 13: 34,
 14: 36,
 15: 37,
 16: 39,
 17: 40,
 18: 42,
 19: 44,
 20: 46}
 
averageTarget = Target(averageAcByLevel,None,None,None)


def critFailChance(attackMinusAc):
    chance = 0
    if attackMinusAc < -10:
        chance = (-10 - attackMinusAc) * 5
        chance = min(chance, 95)
    elif attackMinusAc < -1:
        chance = 5
    return chance

def failChance(attackMinusAc):
    chance = 0
    if attackMinusAc < -29:
        chance = 5
    elif attackMinusAc < -19:
        chance = (29 + attackMinusAc) * 5
    elif attackMinusAc < -10:
        chance = 45
    elif attackMinusAc < -1:
        chance = (-2 - attackMinusAc) * 5
    elif attackMinusAc < 9:
        chance = 5
    else:
        chance = 0
    return chance

def successChance(attackMinusAc, keen=False):
    chance = 5
    if attackMinusAc < -29:
        chance = 0
    elif attackMinusAc < -20:
        chance = 5
    elif attackMinusAc < -10:
        chance = (20 + attackMinusAc) * 5
    elif attackMinusAc < -1:
        chance = 50
    elif attackMinusAc < 9:
        chance = (8 - attackMinusAc) * 5
    else:
        chance = 5
        
    if keen and attackMinusAc>-20 and attackMinusAc<-9:
        chance -= 5
        
    return chance
        
def critSuccessChance(attackMinusAc, keen=False):
    chance = 5
    if attackMinusAc < -20:
        chance = 0
    elif attackMinusAc < -9:
        chance = 5
    elif attackMinusAc < 8:
        chance = (11 + attackMinusAc) * 5
    else:
        chance = 95
    
    if keen and attackMinusAc>-20 and attackMinusAc<-9:
        chance += 5
    
    return chance
    
def calculateED(accuracy, defense, damage, dm=0, cd=0, fd=0, keen=False):
    # fd = failure damage, cd = crit added damage, dm is damage that applies on all hits, like weakness/resistance
    exD = 0
    if fd != 0:
        exD += failChance(accuracy-defense) * (fd + dm)
    exD += successChance(accuracy-defense, keen) * (damage + dm)
    exD += critSuccessChance(accuracy-defense, keen) * (damage + damage + dm)
    if cd != 0:
        exD += critSuccessChance(accuracy-defense, keen) * cd
    return exD / 100


class AtkSelection:
#         attack
#         damage
#         target
        def __init__(self, attack, damage, csLevel=21, fd=None):
            self.attack = attack
            self.damage = damage
            self.persDamage = copy.copy(noneDamage)
            
            self.critSpecLevel = csLevel
            self.wDice = copy.copy(wDice) # number of dice
            self.damageDice = 0 # 3.5
            self.weaponDamage = None
            self.runeDamage = None
            
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
            self.damageDice = damageDiceConverter[weaponDamageDiceName]
            self.weaponDamage = {i: self.wDice[i]*self.damageDice for i in range(1,21)}
            
        def setCriticalEffects(self, weaponCriticalName):
            cd = criticalDiceConverter[weaponCriticalName]
            for i in range(1,21):
                self.cd[i] += cd[i]
            
        def setCriticalSpecialization(self, csName):
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
                return self.damage[level] + self.weaponDamage[level] + self.runeDamage[level] + self.db
            return None
        
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
        
# fighter, double slice, exacting strike, power attack, snagging strike
# combat grab
        
fighterstrike = AtkSelection(fighterAttackBonus,fighterDamage, csLevel=5)

fightersnaggingstrike = AtkSelection(fighterAttackBonus,fighterDamage, csLevel=5)
fightersnaggingstrike.setFFonCrit(1)
fightersnaggingstrike.setFFonSuccess(1)

fightercertainstrike = AtkSelection(fighterAttackBonus,fighterDamage, csLevel=5, fd=fighterFailDamage)

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


attackSwitcher = {'Fighter Strike': 
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
                  [fighterd12brutalfinish]
                  }


            
class Selector:
    
    selectedTarget = averageAcByLevel # use averageTarget later
    selections = dict()
    keyList = list()
    
    def addSelection(key, value, wdd, wc, cs, r1, r2, r3, r4, ab, db, minl, maxl):
        attack = attackSwitcher[value][0]
        newAttack = copy.deepcopy(attack)
        
        newAttack.setWeaponDamage(wdd)
        newAttack.setCriticalEffects(wc)
        newAttack.setCriticalSpecialization(cs)
        newAttack.setRuneDamage(r1,r2,r3,r4)
        
        newAttack.modifyAB(ab)
        newAttack.modifyDB(db)
        
        newAttack.setLevels(minl, maxl)
        
        Selector.selections[key] = [newAttack]
        Selector.keyList.append(key)
		
    def combineSelections(key, keyList):
        # check if it's a combined attack, can't combine them
        atkList = []  
        for k in keyList:
            attack = Selector.selections.get(k)
            atkList += attack
        Selector.selections[key] = atkList
        Selector.keyList.append(key)
        
    def moveToTop(key):
        Selector.keyList.remove(key)
        Selector.keyList = [key] + Selector.keyList
    
    def doubleSelection(key, value):
        attack = Selector.selections.get(value)
        atkList = attack + attack
        Selector.selections[key] = atkList
        
    def removeSelection(key):
        Selector.selections.pop(key)
        Selector.keyList.remove(key)
        
    def rename(newKey, oldKey):
        attack = Selector.selections.get(oldKey)
        Selector.removeSelection(oldKey)
        Selector.selections[newKey] = attack
        Selector.keyList.append(newKey)
        
    def minSelections(newKey, oldKeyList):
        attackList = []
        for k in oldKeyList:
            attack = Selector.selections.get(k)
            attackList.append(attack)
        newAttack = CombinedAttack(attackList, function=min)
        Selector.selections[newKey] = newAttack
        Selector.keyList.append(newKey)
        
    
    def maxSelections(newKey, oldKeyList):
        attackList = []
        for k in oldKeyList:
            attack = Selector.selections.get(k)
            attackList.append(attack)
        newAttack = CombinedAttack(attackList, function=max)
        Selector.selections[newKey] = newAttack
        Selector.keyList.append(newKey)
    
    def canCombine(keyList):
        if len(keyList)==0:
            return False
        for key in keyList:
            attack = Selector.selections.get(key)
            if type(attack) is CombinedAttack:
                return False
        return True

def graphTrace(strikeRoutine, target, level, attackBonus, damageBonus, weakness, flatfootedStatus):
    y = 0
    flatfootedChance = flatfootedStatus
    
    if type(strikeRoutine) is CombinedAttack:
        # what if it contains more combined attacks?
        for sr in strikeRoutine.validFor(level):
            newy = graphTrace(sr, target, level, attackBonus, damageBonus, weakness, flatfootedStatus)
            if y == 0:
                y = newy
            else:
                y = strikeRoutine.function(y, newy)
        return y
        
    for st in strikeRoutine: #for each strike in that routine
        a = st.getAttack(level)+attackBonus
        d = st.getDamage(level)+damageBonus
        fd = st.getFD(level)
        cd = st.getCD(level)
        keen = st.getKeen(level)
        
        ac = target
                    
        ffed = calculateED(a,ac-2,d,dm=weakness,fd=fd,cd=cd,keen=keen)
        ed = calculateED(a,ac,d,dm=weakness,fd=fd,cd=cd,keen=keen)
                    
        y += (flatfootedChance*ffed + (100-flatfootedChance)*ed) / 100
                    # check for effects on crit/failure
        ffonCritChance, ffonSuccessChance, ffonFailChance = 0, 0, 0
        if st.ffonCrit(i):
            ffonCritChance = (100-flatfootedChance) * critSuccessChance(a-ac, keen) / 100
        if st.ffonSuccess(i):
            ffonSuccessChance = (100-flatfootedChance) * successChance(a-ac, keen) / 100
        if st.ffonFail(i):
            ffonFailChance = (100-flatfootedChance) * failChance(a-ac)
        flatfootedChance += (ffonCritChance + ffonSuccessChance + ffonFailChance)
    return y
                    
	
def createTraces(levelDiff, flatfootedStatus, attackBonus, damageBonus, weakness):
#     print("c t")
    xLists = []
    yLists = []
    target = Selector.selectedTarget
    for k in Selector.keyList: #for each attack routine selection
        s = Selector.selections[k]
        xList = []
        yList = []
        for i in range(1,21):
            toAdd = True
            if(type(s) is CombinedAttack):
                if s.contains(i) and i+levelDiff in target:
                    xList.append(i)
            else:
                for st in s:  
                    if not(st.getAttack(i) and i+levelDiff in target):
                        toAdd = False
                if toAdd:
                    xList.append(i)  
        for i in range(1,21): 
            if i in xList:
                # reset damage and things like flat footed status
                
                t = target[i+levelDiff]
                y = graphTrace(s, t, i, attackBonus, damageBonus, weakness, flatfootedStatus)
                yList.append(y)
        xLists.append(xList)
        yLists.append(yList)
    
    return xLists, yLists, Selector.keyList

def createLevelTraces(levelDiff, flatfootedStatus, attackBonus, damageBonus, weakness, level):
    xLists = []
    yLists = []
    target = Selector.selectedTarget
    
    if not (level+levelDiff in target):
        return xLists, yLists, Selector.keyList
    
    for k in Selector.keyList: #for each attack routine selection
        s = Selector.selections[k]
        xList = []
        yList = []
        
        # is this strike routine valid for this level?
        toAdd = True
        if(type(s) is CombinedAttack):
            if not s.contains(level):
                    toAdd = False
        else:
            for st in s:  
                if not(st.getAttack(level) ):
                    toAdd = False
        
        if toAdd:
            for i in range(-8,9):
                xList.append(i)
                y = graphTrace(s, target[level], level, attackBonus+i, damageBonus, weakness, flatfootedStatus)
                yList.append(y)
        xLists.append(xList)
        yLists.append(yList)
    
    return xLists, yLists, Selector.keyList
        