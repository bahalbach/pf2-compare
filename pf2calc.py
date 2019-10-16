import copy
from pf2calcMonsterStats import creatureData
from pf2calcAttacks import Strike, SaveAttack, Save, Effect, CombinedAttack, attackSwitcher




class Target:
    def __init__(self,AC,Fort,Ref,Will):
        self.ac = AC
        self.fort = Fort
        self.ref = Ref
        self.will = Will
        
    def getAC(self, level):
        if level in self.ac.keys():
            return self.ac[level]
        
    def getSaves(self, level):
        return self.fort[level]
    
    def setAC(self, ac):
        self.ac = ac
        
    def setSaves(self, saves):
        self.fort = saves
        self.ref = saves
        self.will = saves
        
    def contains(self, level):
        return level in self.ac and level in self.fort and level in self.ref and level in self.will
        
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


def critFailureChance(attackMinusAc):
    chance = 0
    if attackMinusAc < -10:
        chance = (-10 - attackMinusAc) * 5
        chance = min(chance, 95)
    elif attackMinusAc < -1:
        chance = 5
    return chance

def failureChance(attackMinusAc):
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
    
def calculateED(accuracy, defense, damageBonus, damageDice, dm=0, cd=0, fd=0, sd=0, keen=False, cs=False):
    # fd = failure damage, cd = crit added damage, dm is damage that applies on all hits, like weakness/resistance
    exD = 0
    if fd != 0 or sd != 0:
        exD += failureChance(accuracy-defense) * (fd + sd + dm)
    exD += successChance(accuracy-defense, keen) * ((damageBonus + damageDice) + sd + dm)
    exD += critSuccessChance(accuracy-defense, keen) * ((damageBonus + damageDice)*2 + sd + dm)
    if cd != 0:
        exD += critSuccessChance(accuracy-defense, keen) * cd
    return exD / 100



            
class Selector:
    
    selectedTarget = averageTarget # use averageTarget later
    selectedTarget.setSaves(creatureData['Saves']['Moderate'])
    selectedTarget.setAC(creatureData['AC']['Moderate'])
    selections = dict()
    keyList = list()
    
    def changeTargetAC(name):
        if name == 'average bestiary':
            Selector.selectedTarget.setAC(averageAcByLevel)
        else:
            Selector.selectedTarget.setAC(creatureData['AC'][name])
     
    def changeTargetSaves(name):
        Selector.selectedTarget.setSaves(creatureData['Saves'][name])
     
    def shouldAddWeaponDamage(key):
        attack = attackSwitcher[key][0]
        return attack.isWeapon and not attack.weaponDamage
    
    def isWeapon(key):
        attack = attackSwitcher[key][0]
        return attack.isWeapon
    
    def addSelection(key, value, wdd, wc, cs, r1, r2, r3, r4, ab, ad, db, minl, maxl):
        attack = attackSwitcher[value][0]
        newAttack = copy.deepcopy(attack)
        
        newAttack.setWeaponDamage(wdd)
        newAttack.setCriticalEffects(wc)
        newAttack.setCriticalSpecialization(cs)
        
        
        newAttack.setRuneDamage(r1,r2,r3,r4)
        
        newAttack.modifyAB(ab)
        newAttack.modifyAD(ad)
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
        atkList = attack
        atkList += attack
        Selector.selections[key] = atkList
        Selector.keyList.append(key)
        
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

class Context:
    def __init__(self, oldContext, chance, result):
        if oldContext:
            self.flatfooted = oldContext.origffstatus
            self.origffstatus = oldContext.origffstatus
            self.attackBonus = oldContext.attackBonus
            self.damageBonus = oldContext.damageBonus
            self.chance = oldContext.chance * chance
            self.totalDamage = oldContext.totalDamage
            self.totalPDamage = oldContext.totalPDamage
            
            self.thisStrikeBonus = 0
            self.thisDamageBonus = 0
        
            self.onFirstHitDamage = oldContext.onFirstHitDamage
            self.onSecondHitDamage = oldContext.onSecondHitDamage
            self.onThirdHitDamage = oldContext.onThirdHitDamage
            self.onEveryHitDamage = oldContext.onEveryHitDamage
            
            if result:
                if result.futureAttacksFF:
                    self.origffstatus = True
                    self.flatfooted = True
                elif result.nextAttackFF:
                    self.flatfooted = True
                elif not type(result.atk) is Strike:
                    self.flatfooted = oldContext.flatfooted
               
                if not type(result.atk) is Strike:
                    self.thisStrikeBonus = max(oldContext.thisStrikeBonus, result.nextStrikeBonus)
                else:
                    self.thisStrikeBonus = result.nextStrikeBonus
                    
                if result.addfirsthitdamage != 0:
                    self.onFirstHitDamage += result.addfirsthitdamage
                if result.addsecondhitdamage != 0:
                    self.onSecondHitDamage += result.addsecondhitdamage
                if result.addthirdhitdamage != 0:
                    self.onThirdHitDamage += result.addthirdhitdamage
                if result.addeveryhitdamage != 0:
                    self.onEveryHitDamage += result.addeveryhitdamage
                    
                
                if type(result.atk) is Strike and result.isHit():
                    self.totalDamage += self.onFirstHitDamage + self.onEveryHitDamage
                    self.onFirstHitDamage = self.onSecondHitDamage
                    self.onSecondHitDamage = self.onThirdHitDamage
                    self.onThirdHitDamage = 0
                
                self.totalDamage += result.damage
                self.totalPDamage += result.pdamage
                return
            
            return 
        self.flatfooted = False
        self.origffstatus = False
        self.attackBonus = 0
        self.damageBonus = 0
        self.chance = chance
        self.totalDamage = 0
        self.totalPDamage = 0
        
        self.thisStrikeBonus = 0
        self.thisDamageBonus = 0
        
        self.onFirstHitDamage = 0
        self.onSecondHitDamage = 0
        self.onThirdHitDamage = 0
        self.onEveryHitDamage = 0
        return
    
    def setFlatfooted(self):
        self.origffstatus = True
        self.flatfooted = True
        
    def setAttackBonus(self, ab):
        self.attackBonus = ab
        
    def setDamageBonus(self, db):
        self.damageBonus = db
        
    def getStrikeBonus(self):
        return self.attackBonus + self.thisStrikeBonus
    
    def getSaveAttackBonus(self):
        return self.attackBonus
    
    def getDCBonus(self):
        return self.attackBonus
    
    def getSaveBonus(self):
        return 0
    
    def getEffectBonus(self):
        return 0
    
    def getExtraDamage(self):
        return self.damageBonus + self.thisDamageBonus
    
    def getDamageBonus(self):
        return self.damageBonus
    
    
def graphTrace(routine, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus):
    y = 0
    py = 0
    
    if type(routine) is CombinedAttack:
        # what if it contains more combined attacks?
        for atk in routine.validFor(level):
            newy, newpy = graphTrace(atk, target, level, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus)
            if y == 0:
                y = newy
                py = newpy
            else:
                y, py = routine.choose(y, py, newy, newpy)
        return y, py
        
    oContext = Context(None, 1, None)
    oContext.setAttackBonus(attackBonus)
    oContext.setDamageBonus(damageBonus)
    normalContext = Context(oContext, 1-flatfootedStatus,None)
    ffContext = Context(oContext, flatfootedStatus, None)
    ffContext.setFlatfooted()
    contextList = [normalContext, ffContext]
    
    for atk in routine: #for each strike in that routine
        newContextList = []
        for context in contextList:
            # calculate the effects for this attack
            keenStatus = False
            if(type(atk) is Strike):
                totalBonus = atk.getAttack(level)
                totalBonus += context.getStrikeBonus()
                keenStatus = atk.getKeen(level)
            
                totalDC = target.getAC(level+levelDiff)
            
                if context.flatfooted:
                    totalDC -= 2
            elif(type(atk) is SaveAttack):
                totalBonus = atk.getAttack(level)
                totalBonus += context.getSaveAttackBonus()
                keenStatus = atk.getKeen(level)
            
                totalDC = target.getSaveDC(level+levelDiff)
            elif(type(atk) is Save):
                totalBonus = target.getSaves(level+levelDiff)
                totalBonus += context.getSaveBonus()
                
                totalDC = atk.getDC(level)
                totalDC += context.getDCBonus()
            elif(type(atk) is Effect):
                r = atk.effectResult(level, context)
                eContext = Context(context, 1, r)
                newContextList.append(eContext)
                continue
            else:
                # this should not happen
                print("attack type was", type(atk))
                continue
            
            # create a new context for each degree of success
            critSuccessPercent = critSuccessChance(totalBonus-totalDC, keen=keenStatus)
            critSuccessResult = atk.critSuccessResult(level, context)
            csContext = Context(context, critSuccessPercent/100, critSuccessResult)
            newContextList.append(csContext)
            
            successPercent = successChance(totalBonus-totalDC, keen=keenStatus)
            successResult = atk.successResult(level, context)
            sContext = Context(context, successPercent/100, successResult)
            newContextList.append(sContext)
            
            failurePercent = failureChance(totalBonus-totalDC)
            failureResult = atk.failureResult(level, context)
            fContext = Context(context, failurePercent/100, failureResult)
            newContextList.append(fContext)
            
            critFailurePercent = critFailureChance(totalBonus-totalDC)
            critFailureResult = atk.critFailureResult(level, context)
            cfContext = Context(context, critFailurePercent/100, critFailureResult)
            newContextList.append(cfContext)      
            
        # replace contextList with the list of newly created contexts
        contextList = newContextList
        
    for context in contextList:
        y += context.totalDamage * context.chance
        py += context.totalPDamage * context.chance
    
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
                if s.contains(i) and target.contains(i+levelDiff):
                    xList.append(i)
            else:
                for st in s:  
                    if not(st.getAttack(i) and target.contains(i+levelDiff)):
                        toAdd = False
                if toAdd:
                    xList.append(i)  
        for i in range(1,21): 
            if i in xList:
                # reset damage and things like flat footed status
                
                
                y, py = graphTrace(s, target, i, levelDiff, attackBonus, damageBonus, weakness, flatfootedStatus)
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
    
    if not target.contains(level+levelDiff):
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
                xList.append(target.getAC(level+levelDiff)-i)
                y, py = graphTrace(s, target, level, levelDiff, attackBonus+i, damageBonus, weakness, flatfootedStatus)
                yList.append(y)
                pyList.append(py)
        xLists.append(xList)
        yLists.append(yList)
        pyLists.append(pyList)
    
    return xLists, yLists, pyLists, Selector.keyList
        