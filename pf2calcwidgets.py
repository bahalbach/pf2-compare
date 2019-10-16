import copy
from pf2calc import Selector, CombinedAttack, createTraces, createLevelTraces, creatureData
import plotly.graph_objects as go
from ipywidgets import widgets

levelDiff = widgets.BoundedIntText(
    value=0.0,
    min=-10.0,
    max=10.0,
    step=1.0,
    description='Level difference:',
    #continuous_update=False
)
attackBonus = widgets.BoundedIntText(
    value=0.0,
    min=-10.0,
    max=10.0,
    step=1.0,
    description='Attack bonus:',
    #continuous_update=False
)
damageBonus = widgets.BoundedIntText(
    value=0.0,
    min=-20.0,
    max=50.0,
    step=1.0,
    description='Damage bonus:',
    #continuous_update=False
)
weakness = widgets.BoundedIntText(
    value=0.0,
    min=-50.0,
    max=50.0,
    step=1.0,
    description='Weakness:',
    #continuous_update=False
)

targetACSelector = widgets.Dropdown(
    options=['average bestiary',
             'Extreme',
             'High',
             'Moderate',
             'Low'],
    value='Moderate',
    description='Target AC:'
)

targetSavesSelector = widgets.Dropdown(
#    options=['average bestiary high',
#             'average bestiary mid',
#             'average bestiary low',
#             'average bestiary fort',
#             'average bestiary ref',
#             'average bestiary will',
    options=['Extreme',
             'High',
             'Moderate',
             'Low',
             'Terrible'],
    value='Moderate',
    description='Target Save:'
)

def targetACChangedResponse(change):
    Selector.changeTargetAC(targetACSelector.value)
    updateEDBLGraph()  

def targetSavesChangedResponse(change):
    Selector.changeTargetSaves(targetSavesSelector.value)
    updateEDBLGraph() 

flatfootedBox = widgets.BoundedIntText(
    value=0,
    min=0,
    max=100.0,
    description='flat footed percent',
    disabled=False
)

persistentDamageWeightBox = widgets.BoundedFloatText(
    value=0,
    min=0,
    max=10.0,
    description='Persistent Damage Weight',
    disabled=False
)

percentageView = widgets.Dropdown(
        options = ['Expected Damage',
                   'Percent of First Selection',
                   'Percent of High HP',
                   'Percent of Moderate HP',
                   'Percent of Low HP'],
        value='Expected Damage'
)

byLevelView = widgets.Checkbox(
        value=False,
        description="By Level View"
)

levelSelector = widgets.IntSlider(
        value=1,
        min=1,
        max=20,
        step=1,
        continuous_update=False
)

weaponDamageDie = widgets.Dropdown(
        options=["1d4",
                 "1d6",
                 "1d8/1d6+1",
                 "1d10/1d8+1/1d6+2",
                 "1d12/1d10+1/1d8+2",
                 "1d12+1/1d10+2"],
        value="1d4",
        layout=widgets.Layout(width='auto')
)

weaponCritical = widgets.Dropdown(
        options=["none",
                 "deadly d6",
                 "deadly d8",
                 "deadly d10",
                 "deadly d12",
                 "fatal d8",
                 "fatal d10",
                 "fatal d12"],
        value="none",
        layout=widgets.Layout(width='auto')
)

criticalSpecialization = widgets.Dropdown(
        options=["other/none",
                 "dart/knife",
                 "flail/hammer/sword",
                 "pick"],
        value="other/none",
        layout=widgets.Layout(width='auto')
)

elementalRunesLabel = widgets.Label(
        value="Elemental Damage Rune Levels"
)

elementalRune1 = widgets.IntText(
    value=8.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
elementalRune2 = widgets.IntText(
    value=15.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
elementalRune3 = widgets.IntText(
    value=21.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)
elementalRune4 = widgets.IntText(
    value=21.0,
    step=1.0,
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)

classSelector = widgets.Dropdown(
        options=["Alchemist",
                 "Barbarian",
                 "Bard", 
                 "Champion",
                 "Cleric",
                 "Druid",
                 "Fighter",
                 "Monk",
                 "Ranger",
                 "Rogue",
                 "Sorcerer",
                 "Wizard",
                 "Animal Companion",
                 "Cantrips",
                 "Spells",
                 "Caster Strikes",
                 "Martial Strikes",
                 "Monster",
                 "Effects"],
        value="Fighter",
        layout=widgets.Layout(width='auto')
)
alchemistOptions = ['Alchemist Melee Strike',
                    'Alchemist Ranged Strike',
                    'Alchemist Bestial Claw',
                    'Alchemist Bestial Jaw',
                    'Alchemist Feral Claw',
                    'Alchemist Feral Jaw',
                    'Alchemist Acid Flask',
                    'Alchemist Bomber Acid',
                    'Alchemist Perpetual Acid',
                    'Alchemist Bomber Perpetual Acid',
                    'Alchemist Fire',
                    'Alchemist Bomber Fire',
                    'Alchemist Perpetual Fire',
                    'Alchemist Bomber Perpetual Fire',
                    'Alchemist Bottled Lightning',
                    'Alchemist Bomber Lightning',
                    'Alchemist Perpetual Lightning',
                    'Alchemist Bomber Perpetual Lightning',
                    'Alchemist Frost Vial',
                    'Alchemist Bomber Frost',
                    'Alchemist Perpetual Frost',
                    'Alchemist Bomber Perpetual Frost']
barbarianOptions = ['Martial Strike',
                    'Barbarian Animal Claw',
                    'Barbarian Animal Jaw',
                    'Barbarian Dragon Strike',
                    'Barbarian Fury Strike',
                    'Barbarian Giant Strike',
                    'Barbarian Spirit Strike'
                    ]
bardOptions = ['Caster Strike']
championOptions = ['Martial Strike',
                   'Champion Smite Evil']
cantripOptions = ['Acid Splash',
                  'Electric Arc',
                  'Daze',
                  'Divine Lance',
                  'Produce Flame',
                  'Ray of Frost',
                  'Telekinetic Projectile']
casterstrikeOptions = ['Caster Strike',
                       'Caster Ranged Strike',
                       'Caster Propulsive 10',
                       'Caster Propulsive 12',
                       'Caster Propulsive 14',
                       'Caster Propulsive 16']
clericOptions = ['Caster Strike',
                 'Warpriest Strike']
druidOptions = ['Caster Strike']
fighterOptions = ['Fighter Melee Strike',
                  'Fighter Exacting Strike',
             'Fighter Snagging Strike',
             'Fighter Certain Strike',
             'Fighter d10 Power Attack',
             'Fighter d12 Power Attack',
             'Fighter Brutish Shove',
             'Fighter Knockdown',
             'Fighter d10 Brutal Finish',
             'Fighter d12 Brutal Finish',
             'Fighter propulsive 12',
             'Fighter propulsive 14',
             'Fighter propulsive 16',
             'Fighter propulsive 12 es',
             'Fighter propulsive 14 es',
             'Fighter propulsive 16 es',
             'Fighter propulsive 12 cs',
             'Fighter propulsive 14 cs',
             'Fighter propulsive 16 cs'
             ]
martialstrikeOptions = ['Martial Strike',
                        'Martial Ranged Strike',
                        'Martial Propulsive 10',
                        'Martial Propulsive 12',
                        'Martial Propulsive 14',
                        'Martial Propulsive 16']
monkOptions = ['Martial Strike']
rangerOptions = ['Martial Strike',
                        'Martial Ranged Strike',
                        'Martial Propulsive 10',
                        'Martial Propulsive 12',
                        'Martial Propulsive 14',
                        'Martial Propulsive 16']
rogueOptions = ['Rogue Strike',
                'Flat Foot Next Strike']
sorcererOptions = ['Caster Strike']
wizardOptions = ['Caster Strike']
animalcompanionOptions = []
monsterOptions = ['Monster Extreme Attack High Damage',
                  'Monster Extreme Attack Moderate Damage',
                  'Monster High Attack Extreme Damage',
                  'Monster High Attack High Damage',
                  'Monster High Attack Moderate Damage',
                  'Monster High Attack Low Damage',
                  'Monster Moderate Attack Extreme Damage',
                  'Monster Moderate Attack High Damage',
                  'Monster Moderate Attack Moderate Damage',
                  'Monster Moderate Attack Low Damage',
                  'Monster Low Attack High Damage',
                  'Monster Low Attack Moderate Damage',
                  'Monster Low Attack Low Damage'   
                  ]
effectOptions = ['Flat Foot Target',
                 'Flat Foot Next Strike']
spellOptions = ['Basic Save 2d6',
                'Basic Save 2d6+1',
                'Basic Save 2d8',
                'Magic Missle']

selectionSwitcher = {"Alchemist": alchemistOptions, 
                     "Barbarian": barbarianOptions,
                     "Bard": bardOptions,
                     "Cantrips": cantripOptions,
                     "Caster Strikes": casterstrikeOptions,
                     "Champion": championOptions,
                     "Cleric": clericOptions,
                     "Druid": druidOptions,
                     "Fighter": fighterOptions,
                     "Monk": monkOptions,
                     "Martial Strikes": martialstrikeOptions,
                     "Ranger": rangerOptions,
                     "Rogue": rogueOptions,
                     "Sorcerer": sorcererOptions,
                     "Wizard": wizardOptions,
                     "Animal Companion": animalcompanionOptions,
                     "Monster": monsterOptions,
                     "Effects": effectOptions,
                     "Spells": spellOptions}


selector = widgets.SelectMultiple(
    options=fighterOptions,
    value=[fighterOptions[0]],
    description='Selection:',
    layout=widgets.Layout(width='auto', height='100%'),
    disabled=False,
)

def classSelectorResponse(b):
    selector.options = selectionSwitcher[classSelector.value]
    #selector.value = [selector.options[0]]

selections = widgets.SelectMultiple(
    options=[],
    # rows=10,
    description='Current selections:',
    layout=widgets.Layout(width='80%', height='100%'),
    disabled=False
)

selectorAddButton = widgets.Button(description="Add Selections")
def on_addSelection_clicked(b):
    #add to selections
    for s in selector.value:
        name = s
        if Selector.shouldAddWeaponDamage(s):
            name += " " + weaponDamageDie.value
        if not weaponCritical.value == "none" and Selector.isWeapon(s):
            name += " " + weaponCritical.value
        if not criticalSpecialization.value == "other/none" and Selector.isWeapon(s):
            name += " " + criticalSpecialization.value
        if attackModifier.value != 0:
            if attackModifier.value > 0:
                name += " +"
            else:
                name += " "
            name += str(attackModifier.value) + "a"
        if additionalDamage.value != 0:
            if additionalDamage.value > 0:
                name += " +"
            else:
                name += " "
            name += str(additionalDamage.value) + "ad"
        if damageModifier.value != 0:
            if damageModifier.value > 0:
                name += " +"
            else:
                name += " "
            name += str(damageModifier.value) + "d"
        minLevel = levelLimiter.value[0]
        maxLevel = levelLimiter.value[1]
        if not (name in selections.options):
            selections.options += (name,)
            Selector.addSelection(name,s,weaponDamageDie.value,
                                  weaponCritical.value,criticalSpecialization.value,
                                  elementalRune1.value,elementalRune2.value,
                                  elementalRune3.value,elementalRune4.value,
                                  attackModifier.value,
                                  additionalDamage.value,
                                  damageModifier.value,
                                  minLevel,maxLevel)
    attackModifier.value = 0
    additionalDamage.value = 0
    damageModifier.value = 0
            
    updateEDBLGraph()
selectorAddButton.on_click(on_addSelection_clicked)

attackModifier = widgets.BoundedIntText(
    value=0.0,
    min=-10.0,
    max=10.0,
    step=1.0,
    description='Attack Bonus:',
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)

additionalDamage = widgets.BoundedIntText(
    value=0.0,
    min=-50.0,
    max=50.0,
    step=1.0,
    description='Additional Damage:',
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)

damageModifier = widgets.BoundedIntText(
    value=0.0,
    min=-50.0,
    max=50.0,
    step=1.0,
    description='Damage Bonus:',
    layout=widgets.Layout(width='auto')
    #continuous_update=False
)

levelLimiter = widgets.IntRangeSlider(
    value=[1, 20],
    min=1,
    max=20,
    step=1,
    description = 'Level Range',
    layout=widgets.Layout(width='auto')
)

removeSelectionButton = widgets.Button(description="Remove Selections")
def on_removeSelection_clicked(b):
    #remove from selections
    if (selections.value):
        l = list(selections.options)
        for s in selections.value:    
            Selector.removeSelection(s)
            l.remove(s)
        selections.options = l
        updateEDBLGraph()
removeSelectionButton.on_click(on_removeSelection_clicked)

movetotopButton = widgets.Button(description="Move to top")
def on_movetotop_clicked(b):
    if(selections.value and selections.value[0]):
        v = selections.value[0]
        Selector.moveToTop(v)
        l = list(selections.options)
        l.remove(v)
        selections.options = [v] + l
        updateEDBLGraph()
movetotopButton.on_click(on_movetotop_clicked)

combineSelectionButton = widgets.Button(description="Combine Selections")
def on_combineSelection_clicked(b):
    # check if it's a combined attack, can't combine them
    if not Selector.canCombine(selections.value):
        return
    
    if len(selections.value) == 1:
        name = selections.value[0]
        name += " + " + selections.value[0]
        if not (name in selections.options):
            value = selections.value[0]
            Selector.doubleSelection(name, value)
            selections.options += (name,)
            
            # remove parts from Selections
            l = list(selections.options)  
            Selector.removeSelection(value)
            l.remove(value)
            selections.options = l
     
            updateEDBLGraph()
            
    if len(selections.value) >1:
        name = selections.value[0]
        for i in range(len(selections.value)-1):
            name += " + " + selections.value[i+1]
            
        if not (name in selections.options):
            # add combination to Selections  
            value = selections.value
            Selector.combineSelections(name, value)
            selections.options += (name,)
            
            # remove parts from Selections
            l = list(selections.options)
            for s in value:   
                Selector.removeSelection(s)
                l.remove(s)
            selections.options = l
     
            updateEDBLGraph()
combineSelectionButton.on_click(on_combineSelection_clicked)

minButton = widgets.Button(description="Min/rename Selections")
def on_minButton_clicked(b):
    if (newNameBox.value == ""):
        return
    newName = newNameBox.value
    newNameBox.value = ""
    if len(selections.value) == 1:
        oldName = selections.value[0]
        if newName == oldName:
            return
        
        Selector.rename(newName, oldName)
        
        selections.options += (newName,)
        l = list(selections.options)  
        l.remove(oldName)
        selections.options = l
        updateEDBLGraph()
    
    if len(selections.value) >1:
        oldNames = selections.value
        Selector.minSelections(newName, oldNames)
        selections.options += (newName,)
        
        l = list(selections.options)
        for s in oldNames:   
            if not(newName == s):
                Selector.removeSelection(s)
                l.remove(s)
        selections.options = l
        updateEDBLGraph()
minButton.on_click(on_minButton_clicked)

maxButton = widgets.Button(description="Max/rename Selections")
def on_maxButton_clicked(b):
    if (newNameBox.value == ""):
        return
    newName = newNameBox.value
    newNameBox.value = ""
    if len(selections.value) == 1:
        oldName = selections.value[0]
        if newName == oldName:
            return
        
        Selector.rename(newName, oldName)
        
        selections.options += (newName,)
        l = list(selections.options)  
        l.remove(oldName)
        selections.options = l
        updateEDBLGraph()
    
    if len(selections.value) >1:
        oldNames = selections.value
        Selector.maxSelections(newName, oldNames)
        selections.options += (newName,)
        
        l = list(selections.options)
        for s in oldNames:   
            if not(newName == s):
                Selector.removeSelection(s)
                l.remove(s)
        selections.options = l
        updateEDBLGraph()
maxButton.on_click(on_maxButton_clicked)

newNameBox = widgets.Text(value="",layout=widgets.Layout(width='auto'))

g = go.FigureWidget() 
g.update_layout(title_text="Expected damage by level",
                  title_font_size=20,
               legend_orientation="h",
               legend_y=-0.2,
               height=500
               )
g.layout.xaxis.range = [0,20]
g.layout.yaxis.range = [0,60]

def updateEDBLGraph():
    CombinedAttack.PDWeight = persistentDamageWeightBox.value
    if byLevelView.value:
        xLists, yLists, pyLists, nameList = createLevelTraces(levelDiff.value, 
                                            flatfootedBox.value, 
                                            attackBonus.value,
                                            damageBonus.value,
                                            weakness.value,
                                            levelSelector.value)
        titleText="Expected damage for level " + str(levelSelector.value) + " vs Level " + str(levelSelector.value+levelDiff.value) + " Target with " + str(targetACSelector.value) + " AC and " + str(targetSavesSelector.value) + " Saves"
        xaxisText="vs AC"
    else:
        xLists, yLists, pyLists, nameList = createTraces(levelDiff.value, 
                                            flatfootedBox.value, 
                                            attackBonus.value,
                                            damageBonus.value,
                                            weakness.value)
        titleText="Expected damage by level"+ " vs Level+" + str(levelDiff.value) + " Target with " + str(targetACSelector.value) + " AC and " + str(targetSavesSelector.value) + " Saves"
        xaxisText="Level"
#     print("selected: ", xLists, yLists)
#     print(Selector.selectedAttack[1])
#     for i in range(1,21):
#         if i in fighterAttackBonus and i+levelDiff.value in averageAcByLevel:
# #             print(selectedAttack[i])
#             xList.append(i)
#             yList.append(calculateED(Selector.selectedAttack[i]+attackBonus.value,averageAcByLevel[i+levelDiff.value],Selector.selectedDamage[i]+damageBonus.value,dm=weakness.value))
    
# add persistent damage to damage
    for i in range(len(yLists)):
        for ii in range(len(yLists[i])):
            yLists[i][ii] += persistentDamageWeightBox.value * pyLists[i][ii]
            
    wantedView = percentageView.value
    if wantedView == 'Percent of First Selection' and len(yLists)>0:
        firsty = copy.copy(yLists[0])
        firstx = xLists[0]
        for i in range(len(firstx)):
            xi = firstx[i]
            for ii in range(0,len(yLists)):
                xl = xLists[ii]
                yl = yLists[ii]
                if xi in xl:
                    xii = xl.index(xi)
                    
                    yl[xii] = 100 * yl[xii] / firsty[i]
        
        # remove x,y pairs not in firstx
        for i in range(1,len(xLists)):
            for ii in range(1,21):
                if not ii in firstx:
                    if ii in xLists[i]:
                        xi = xLists[i].index(ii)
                        yLists[i].pop(xi)
                        xLists[i].pop(xi)
                        
    elif wantedView == 'Percent of High HP' or wantedView == 'Percent of Moderate HP' or wantedView == 'Percent of Low HP':
        if wantedView == 'Percent of High HP':
            hpList = creatureData['HP']['High']
        if wantedView == 'Percent of Moderate HP':
            hpList = creatureData['HP']['Moderate']
        if wantedView == 'Percent of Low HP':
            hpList = creatureData['HP']['Low']
        if byLevelView.value:
            comparisonHP = hpList[levelSelector.value+levelDiff.value]
            for i in range(len(xLists)):
                for ii in range(len(xLists[i])):
                    y = 100 * yLists[i][ii] / comparisonHP
                    yLists[i][ii] = y
        else:
            for i in range(len(xLists)):
                for ii in range(len(xLists[i])):
                    x = xLists[i][ii]
                    comparisonHP = hpList[x+levelDiff.value]
                    y = 100 * yLists[i][ii] / comparisonHP
                    yLists[i][ii] = y
    
    maxY = 0
    for l in yLists:
        for y in l:
            maxY = max(maxY,y)
            
    minX = 100
    maxX = 0
    for l in xLists:
        for x in l:
            minX = min(minX,x)
            maxX = max(maxX,x)
            
            
    with g.batch_update():
        g.data = []
        for i in range(len(xLists)):
            g.add_trace(go.Scatter(x=xLists[i],y=yLists[i],name=nameList[i]))
        
        # update legend size
        g.update_layout(height=500+10*len(nameList))
        
        g.update_layout(title_text=titleText,
                        xaxis_title_text=xaxisText,
                        yaxis_title_text=wantedView)
        
        # should update the axis so the data fits
        if percentageView.value == 'Percent of First Selection':
            g.layout.yaxis.range = [0,200]
        else:
            if maxY > 15:
                if maxY > 30:
                    if maxY > 60:
                        if maxY > 120:
                            if maxY > 240:
                                g.layout.yaxis.range = [0,480]
                            else:
                                g.layout.yaxis.range = [0,240]
                        else:
                            g.layout.yaxis.range = [0,120]
                    else:
                        g.layout.yaxis.range = [0,60]
                else:
                    g.layout.yaxis.range = [0,30]
            else:
                g.layout.yaxis.range = [0,15]
        if byLevelView.value:
            g.layout.xaxis.range = [minX-2,maxX+2]
        else:
            g.layout.xaxis.range = [1,20]
            
def edblResponse(change):
    updateEDBLGraph()        

levelDiff.observe(edblResponse, names="value")
attackBonus.observe(edblResponse, names="value")
damageBonus.observe(edblResponse, names="value")
weakness.observe(edblResponse, names="value")
flatfootedBox.observe(edblResponse, names="value")
percentageView.observe(edblResponse, names="value")
byLevelView.observe(edblResponse, names="value")
levelSelector.observe(edblResponse, names="value")
persistentDamageWeightBox.observe(edblResponse, names="value")

targetACSelector.observe(targetACChangedResponse, names="value")
targetSavesSelector.observe(targetSavesChangedResponse, names="value")
classSelector.observe(classSelectorResponse, names="value")


adjustments = widgets.HBox([levelDiff,attackBonus,damageBonus,weakness])
targetRow = widgets.HBox([targetACSelector, targetSavesSelector,flatfootedBox,persistentDamageWeightBox,percentageView])
levelViewRow = widgets.HBox([byLevelView,levelSelector])

selectorModifiers = widgets.VBox([selectorAddButton,attackModifier,additionalDamage,damageModifier,levelLimiter])
weaponModifiers = widgets.VBox([weaponDamageDie,weaponCritical,criticalSpecialization])
runeModifiers = widgets.VBox([elementalRunesLabel,elementalRune1,elementalRune2,elementalRune3,elementalRune4])
selectorBox = widgets.VBox([classSelector,selector])
selectorRow = widgets.HBox([selectorBox,selectorModifiers,weaponModifiers,runeModifiers])

selectionsButtons = widgets.VBox([removeSelectionButton,movetotopButton,combineSelectionButton,minButton,maxButton,newNameBox])
selectionsBox = widgets.HBox([selections,selectionsButtons])

ExpectedDamageByLevelWidget = widgets.VBox([adjustments,
              targetRow,
              levelViewRow,
              g,
             selectorRow,
             selectionsBox])