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

martialAttackBonus2 = {i: martialAttackBonus[i]-5 for i in range(1,21)}
martialAttackBonus2a = {i: martialAttackBonus[i]-4 for i in range(1,21)}
martialAttackBonus3 = {i: martialAttackBonus[i]-10 for i in range(1,21)}
martialAttackBonus3a = {i: martialAttackBonus[i]-8 for i in range(1,21)}

martialAttackBonus2f = {i: martialAttackBonus[i]-3 for i in range(1,21)}
martialAttackBonus2fa = {i: martialAttackBonus[i]-2 for i in range(1,21)}
martialAttackBonus2mf = {i: martialAttackBonus[i]-2 for i in range(1,21)}
martialAttackBonus2mfa = {i: martialAttackBonus[i]-1 for i in range(1,21)}
martialAttackBonus3f = {i: martialAttackBonus[i]-6 for i in range(1,21)}
martialAttackBonus3fa = {i: martialAttackBonus[i]-4 for i in range(1,21)}
martialAttackBonus3mf = {i: martialAttackBonus[i]-4 for i in range(1,21)}
martialAttackBonus3mfa = {i: martialAttackBonus[i]-2 for i in range(1,21)}


casterAttackBonus = {i: cProf[i] + cStr[i] + wiBonus[i] for i in range(1,21)}

casterAttackBonus2 = {i: casterAttackBonus[i]-5 for i in range(1,21)}
casterAttackBonus3 = {i: casterAttackBonus[i]-10 for i in range(1,21)}


warpriestAttackBonus = {i: wProf[i] + wStr[i] + wiBonus[i] for i in range(1,21)}

warpriestAttackBonus2 = {i: warpriestAttackBonus[i]-5 for i in range(1,21)}
warpriestAttackBonus3 = {i: warpriestAttackBonus[i]-10 for i in range(1,21)}
warpriestAttackBonus2a = {i: warpriestAttackBonus[i]-4 for i in range(1,21)}
warpriestAttackBonus3a = {i: warpriestAttackBonus[i]-8 for i in range(1,21)}


fighterAttackBonus = {i: fProf[i] + mStr[i] + wiBonus[i] for i in range(1,21)}

fighterAttackBonus2 = {i: fighterAttackBonus[i]-5 for i in range(1,21)}
fighterAttackBonus2a = {i: fighterAttackBonus[i]-4 for i in range(1,21)}
fighterAttackBonus2ag = {i: fighterAttackBonus[i]-3 for i in range(1,21)}
fighterAttackBonus3 = {i: fighterAttackBonus[i]-10 for i in range(1,21)}
fighterAttackBonus3a = {i: fighterAttackBonus[i]-8 for i in range(1,21)}
fighterAttackBonus3ag = {i: fighterAttackBonus[i]-6 for i in range(1,21)}




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

shortswordFighterDamage = {i: 3.5*wDice[i]+mStr[i]+fwSpec[i]+eRune[i] for i in range(1,21)}
longswordFighterDamage = {i: 4.5*wDice[i]+mStr[i]+fwSpec[i]+eRune[i] for i in range(1,21)}
greatswordFighterDamage = {i: 6.5*wDice[i]+mStr[i]+fwSpec[i]+eRune[i] for i in range(1,21)}
bsdhaFighterDamage = {i: 7.5*wDice[i]+mStr[i]+fwSpec[i]+eRune[i] for i in range(1,21)} # bastard sword dualhanded assult

d12pad = {i: 6.5 for i in range(1,21)}
for i in d12pad:
    if i>=10:
        d12pad[i]+=6.5
    if i>=18:
        d12pad[i]+=6.5
greatswordpowerattackFighterDamage = {i: 6.5*wDice[i]+d12pad[i]+mStr[i]+fwSpec[i]+eRune[i] for i in range(1,21)}

def ffd(level):
    if level < 10:
        return 0
    return mStr[level] + fwSpec[level]
fighterFailDamage = {i: mStr[i] + fwSpec[i] for i in range(1,21) }
fighterBFFailDamage = {i: 6.5 for i in range(1,21)}
for i in fighterBFFailDamage:
    if i >= 18:
        fighterBFFailDamage[i] = 13


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
        def __init__(self, attack, damage, fd=None, cd=None):
            self.attack = attack
            self.damage = damage
            self.target = averageAcByLevel
            self.fd=fd
            self.cd=cd
            self.ab = 0
            self.db = 0
            self.keenLevel = 21
            self.ffonCritLevel = 21
            self.ffonSuccessLevel = 21
            self.ffonFailLevel = 21
            self.minL = 1
            self.maxL = 20
            
        def getAttack(self, level):
            if level>=self.minL and level<=self.maxL:
                return self.attack[level] + self.ab
            return None
        
        def getDamage(self, level):
            if level>=self.minL and level<=self.maxL:
                return self.damage[level] + self.db
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
            self.ffonCritLevel = level
        def setFFonSuccess(self, level):
            self.ffonSuccessLevel = level
        def setFFonFail(self, level):
            self.ffonFailLevel = level
        def setLevels(self, minl, maxl):
            self.minL, self.maxL = minl, maxl
            
            
# fighter, double slice, exacting strike, power attack, snagging strike
# combat grab
longswordfighterstrike = AtkSelection(fighterAttackBonus,longswordFighterDamage)
longswordfighterstrike.setFFonCrit(5)

longswordfightersnaggingstrike = AtkSelection(fighterAttackBonus,longswordFighterDamage)
longswordfightersnaggingstrike.setFFonCrit(1)
longswordfightersnaggingstrike.setFFonSuccess(1)

longswordfightercertainstrike = AtkSelection(fighterAttackBonus,longswordFighterDamage,fd=fighterFailDamage)
longswordfightercertainstrike.setFFonCrit(5)

greatswordfighterstrike = AtkSelection(fighterAttackBonus,greatswordFighterDamage)
greatswordfighterstrike.setFFonCrit(5)

greatswordfighterpowerattack = AtkSelection(fighterAttackBonus,greatswordpowerattackFighterDamage)
greatswordfighterpowerattack.setFFonCrit(5)

greatswordfighterbrutishshove = AtkSelection(fighterAttackBonus,greatswordFighterDamage)
greatswordfighterbrutishshove.setFFonCrit(1)
greatswordfighterbrutishshove.setFFonSuccess(1)
greatswordfighterbrutishshove.setFFonFail(1)

greatswordfighterknockdown = AtkSelection(fighterAttackBonus,greatswordFighterDamage)
greatswordfighterknockdown.setFFonCrit(1)
greatswordfighterknockdown.setFFonSuccess(1)

greatswordfightercertainstrike = AtkSelection(fighterAttackBonus,greatswordFighterDamage,fd=fighterFailDamage)
greatswordfightercertainstrike.setFFonCrit(5)

greatswordfighterbrutalfinish = AtkSelection(fighterAttackBonus,greatswordpowerattackFighterDamage,fd=fighterBFFailDamage)
greatswordfighterbrutalfinish.setFFonCrit(5)

shortswordfighterstrike = AtkSelection(fighterAttackBonus,shortswordFighterDamage)
shortswordfighterstrike.setFFonCrit(5)

shortswordfightersnaggingstrike = AtkSelection(fighterAttackBonus,longswordFighterDamage)
shortswordfightersnaggingstrike.setFFonCrit(5)
shortswordfightersnaggingstrike.setFFonSuccess(1)

shortswordfightercertainstrike = AtkSelection(fighterAttackBonus,shortswordFighterDamage,fd=fighterFailDamage)
shortswordfightercertainstrike.setFFonCrit(5)

bastardswordfighterdualhandedassult = AtkSelection(fighterAttackBonus,bsdhaFighterDamage)
bastardswordfighterdualhandedassult.setFFonCrit(5)

attackSwitcher = {'Fighter Longsword Strike': 
                  [longswordfighterstrike], 
                  'Fighter Longsword Snagging Strike': 
                  [longswordfightersnaggingstrike], 
                  'Fighter Longsword Certain Strike': 
                  [longswordfightercertainstrike],
                  'Fighter Greatsword Strike': 
                  [greatswordfighterstrike], 
                  'Fighter Greatsword Power Attack': 
                  [greatswordfighterpowerattack], 
                  'Fighter Greatsword Brutish Shove': 
                  [greatswordfighterbrutishshove], 
                  'Fighter Greatsword Knockdown': 
                  [greatswordfighterknockdown], 
                  'Fighter Greatsword Certain Strike': 
                  [greatswordfightercertainstrike], 
                  'Fighter Greatsword Brutal Finish': 
                  [greatswordfighterbrutalfinish], 
                  'Fighter Shortsword Strike': 
                  [shortswordfighterstrike],
                  'Fighter Shortsword Snagging Strike': 
                  [shortswordfightersnaggingstrike],
                  'Fighter Shortsword Certain Strike': 
                  [shortswordfightercertainstrike],
                  'Fighter Bastardsword Dual-Handed Assult': 
                  [bastardswordfighterdualhandedassult],
                  }


            
class Selector:
    
    selectedAttack = fighterAttackBonus
    selectedDamage = longswordFighterDamage
    selectedTarget = averageAcByLevel
    selections = dict()
    keyList = list()
    
    def addSelection(key, value, ab, db, minl, maxl):
        attack = attackSwitcher[value][0]
        newAttack = copy.copy(attack)
        newAttack.modifyAB(ab)
        newAttack.modifyDB(db)
        newAttack.setLevels(minl, maxl)
        Selector.selections[key] = [newAttack]
        Selector.keyList.append(key)
		
    def combineSelections(key, keyList):
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

		
def createTrace(levelDiff, flatfootedStatus, attackBonus, damageBonus, weakness):
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
            for st in s:  
                if not(st.getAttack(i) and i+levelDiff in target):
                    toAdd = False
            if toAdd:
                xList.append(i)  
        for i in range(1,21): 
            if i in xList:
                # reset damage and things like flat footed status
                y = 0
                flatfootedChance = flatfootedStatus
                for st in s: #for each strike in that routine
                    a = st.getAttack(i)+attackBonus
                    t = target[i+levelDiff]
                    d = st.getDamage(i)+damageBonus
                    fd = st.getFD(i)
                    cd = st.getCD(i)
                    keen = st.getKeen(i)
                    
                    ffed = calculateED(a,t-2,d,dm=weakness,fd=fd,cd=cd,keen=keen)
                    ed = calculateED(a,t,d,dm=weakness,fd=fd,cd=cd,keen=keen)
                    
                    y += (flatfootedChance*ffed + (100-flatfootedChance)*ed) / 100
                    # check for effects on crit/failure
                    ffonCritChance, ffonSuccessChance, ffonFailChance = 0, 0, 0
                    if st.ffonCrit(i):
                        ffonCritChance = (100-flatfootedChance) * critSuccessChance(a-t, keen) / 100
                    if st.ffonSuccess(i):
                        ffonSuccessChance = (100-flatfootedChance) * successChance(a-t, keen) / 100
                    if st.ffonFail(i):
                        ffonFailChance = (100-flatfootedChance) * failChance(a-t)
                    flatfootedChance += (ffonCritChance + ffonSuccessChance + ffonFailChance) 
                    
                    
                yList.append(y)
        xLists.append(xList)
        yLists.append(yList)
    return xLists, yLists, Selector.keyList