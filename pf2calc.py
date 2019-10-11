import copy
from pf2calcMonsterStats import creatureData
from pf2calcAttacks import AtkSelection, CombinedAttack, attackSwitcher




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
    
def calculateED(accuracy, defense, damage, dm=0, cd=0, fd=0, sd=0, keen=False):
    # fd = failure damage, cd = crit added damage, dm is damage that applies on all hits, like weakness/resistance
    exD = 0
    if fd != 0 or sd != 0:
        exD += failChance(accuracy-defense) * (fd + sd + dm)
    exD += successChance(accuracy-defense, keen) * (damage + sd + dm)
    exD += critSuccessChance(accuracy-defense, keen) * (damage + damage + sd + dm)
    if cd != 0:
        exD += critSuccessChance(accuracy-defense, keen) * cd
    return exD / 100



            
class Selector:
    
    selectedTarget = creatureData['AC']['High'] # use averageTarget later
    selections = dict()
    keyList = list()
    
    def changeTarget(name):
        if name == 'average bestiary AC':
            Selector.selectedTarget = averageAcByLevel
        else:
            Selector.selectedTarget = creatureData['AC'][name]
        
    def shouldAddWeaponDamage(key):
        attack = attackSwitcher[key][0]
        return attack.isWeapon and not attack.weaponDamage
    
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
    py = 0
    flatfootedChance = flatfootedStatus
    
    if type(strikeRoutine) is CombinedAttack:
        # what if it contains more combined attacks?
        for sr in strikeRoutine.validFor(level):
            newy = graphTrace(sr, target, level, attackBonus, damageBonus, weakness, flatfootedStatus)
            if y == 0:
                y = newy
            else:
                y = strikeRoutine.function(y, newy)
        return y, py
        
    for st in strikeRoutine: #for each strike in that routine
        a = st.getAttack(level)+attackBonus
        d = st.getDamage(level)+damageBonus
        ffd = st.getFFDamage(level)
        fd = st.getFD(level)
        cd = st.getCD(level)
        sd = st.getSplashDamage(level)
        keen = st.getKeen(level)
        
        pd = st.getPersistentDamage(level)
        cpd = st.getCriticalPersistentDamage(level)
        
        ac = target
                    
        ffed = calculateED(a,ac-2,d+ffd,dm=weakness,fd=fd,cd=cd,sd=sd,keen=keen)
        ed = calculateED(a,ac,d,dm=weakness,fd=fd,cd=cd,sd=sd,keen=keen)
        
        #persistent damage
        ffepd = calculateED(a,ac-2,pd,dm=weakness,cd=cpd,keen=keen)
        epd = calculateED(a,ac,pd,dm=weakness,cd=cpd,keen=keen)
        
        y += (flatfootedChance*ffed + (100-flatfootedChance)*ed) / 100
        py += (flatfootedChance*ffepd + (100-flatfootedChance)*epd) / 100
        
                    # check for effects on crit/failure
        ffonCritChance, ffonSuccessChance, ffonFailChance = 0, 0, 0
        if st.ffonCrit(level):
            ffonCritChance = (100-flatfootedChance) * critSuccessChance(a-ac, keen) / 100
        if st.ffonSuccess(level):
            ffonSuccessChance = (100-flatfootedChance) * successChance(a-ac, keen) / 100
        if st.ffonFail(level):
            ffonFailChance = (100-flatfootedChance) * failChance(a-ac)
        flatfootedChance += (ffonCritChance + ffonSuccessChance + ffonFailChance)
    return y, py
                    
	
def createTraces(levelDiff, flatfootedStatus, attackBonus, damageBonus, weakness):
#     print("c t")
    xLists = []
    yLists = []
    pyLists = []
    target = Selector.selectedTarget
    for k in Selector.keyList: #for each attack routine selection
        s = Selector.selections[k]
        xList = []
        yList = []
        pyList = []
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
                y, py = graphTrace(s, t, i, attackBonus, damageBonus, weakness, flatfootedStatus)
                yList.append(y)
                pyList.append(py)
        xLists.append(xList)
        yLists.append(yList)
        pyLists.append(pyList)
    
    return xLists, yLists, pyLists, Selector.keyList

def createLevelTraces(levelDiff, flatfootedStatus, attackBonus, damageBonus, weakness, level):
    xLists = []
    yLists = []
    pyLists = []
    target = Selector.selectedTarget
    
    if not (level+levelDiff in target):
        return xLists, yLists, pyLists, Selector.keyList
    
    for k in Selector.keyList: #for each attack routine selection
        s = Selector.selections[k]
        xList = []
        yList = []
        pyList = []
        
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
                xList.append(target[level+levelDiff]-i)
                y, py = graphTrace(s, target[level+levelDiff], level, attackBonus+i, damageBonus, weakness, flatfootedStatus)
                yList.append(y)
                pyList.append(py)
        xLists.append(xList)
        yLists.append(yList)
        pyLists.append(pyList)
    
    return xLists, yLists, pyLists, Selector.keyList
        