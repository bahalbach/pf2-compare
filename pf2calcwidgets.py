import copy
from pf2calc import Selector, createTraces, createLevelTraces
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

targetSelector = widgets.Dropdown(
    options=['average bestiary AC'],
    value='average bestiary AC',
    description='Target:'
)

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

percentageView = widgets.Checkbox(
        value=False,
        description="Percentage View"
)

byLevelView = widgets.Checkbox(
        value=False,
        description="By Level View"
)

levelSelector = widgets.IntSlider(
        value=1,
        min=1,
        max=20,
        step=1
)

weaponDamageDie = widgets.Dropdown(
        options=["1d4",
                 "1d6",
                 "1d8/1d6+1",
                 "1d10/1d8+1/1d6+2",
                 "1d12/1d10+1/1d8+2",
                 "1d12+1/1d10+2"],
        value="1d4"
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
        value="none"
)

criticalSpecialization = widgets.Dropdown(
        options=["other/none",
                 "dart/knife",
                 "flail/hammer/sword",
                 "pick"],
        value="other/none"
)

elementalRunesLabel = widgets.Label(
        value="Elemental Damage Rune Levels"
)

elementalRune1 = widgets.IntText(
    value=8.0,
    step=1.0
    #continuous_update=False
)
elementalRune2 = widgets.IntText(
    value=15.0,
    step=1.0
    #continuous_update=False
)
elementalRune3 = widgets.IntText(
    value=21.0,
    step=1.0
    #continuous_update=False
)
elementalRune4 = widgets.IntText(
    value=21.0,
    step=1.0
    #continuous_update=False
)


selector = widgets.SelectMultiple(
    options=['Fighter Strike',
             'Fighter Snagging Strike',
             'Fighter Certain Strike',
             'Fighter d10 Power Attack',
             'Fighter d12 Power Attack',
             'Fighter Brutish Shove',
             'Fighter Knockdown',
             'Fighter d10 Brutal Finish',
             'Fighter d12 Brutal Finish'
             ],
    value=['Fighter Strike'],
    description='Selection:',
    layout=widgets.Layout(width='30%'),
    disabled=False,
)

selections = widgets.SelectMultiple(
    options=[],
    # rows=10,
    description='Current selections:',
    layout=widgets.Layout(width='80%'),
    disabled=False
)

selectorAddButton = widgets.Button(description="Add Selections")
def on_addSelection_clicked(b):
    #add to selections
    for s in selector.value:
        name = s
        name += " " + weaponDamageDie.value
        if not weaponCritical.value == "none":
            name += " " + weaponCritical.value
        if not criticalSpecialization.value == "other/none":
            name += " " + criticalSpecialization.value
        if attackModifier.value != 0:
            name += " +a" + str(attackModifier.value)
        if damageModifier.value != 0:
            name += " +d" + str(damageModifier.value)
        minLevel = levelLimiter.value[0]
        maxLevel = levelLimiter.value[1]
        if not (name in selections.options):
            selections.options += (name,)
            Selector.addSelection(name,s,weaponDamageDie.value,
                                  weaponCritical.value,criticalSpecialization.value,
                                  elementalRune1.value,elementalRune2.value,
                                  elementalRune3.value,elementalRune4.value,
                                  attackModifier.value,damageModifier.value,minLevel,maxLevel)
    attackModifier.value = 0
    damageModifier.value = 0
            
    updateEDBLGraph()
selectorAddButton.on_click(on_addSelection_clicked)

attackModifier = widgets.BoundedIntText(
    value=0.0,
    min=-10.0,
    max=10.0,
    step=1.0,
    description='Attack Bonus:',
    #continuous_update=False
)

damageModifier = widgets.BoundedIntText(
    value=0.0,
    min=-50.0,
    max=50.0,
    step=1.0,
    description='Damage Bonus:',
    #continuous_update=False
)

levelLimiter = widgets.IntRangeSlider(
    value=[1, 20],
    min=0,
    max=20,
    step=1,
    description = 'Level Range'
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

minButton = widgets.Button(description="Min Selections")
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

maxButton = widgets.Button(description="Max Selections")
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

newNameBox = widgets.Text(value="")

g = go.FigureWidget() 
g.update_layout(title_text="Expected damage by level",
                  title_font_size=30,
               legend_orientation="h",
               height=500
               )
g.layout.xaxis.range = [0,20]
g.layout.yaxis.range = [0,60]

def updateEDBLGraph():
    if byLevelView.value:
        xLists, yLists, nameList = createLevelTraces(levelDiff.value, 
                                            flatfootedBox.value, 
                                            attackBonus.value,
                                            damageBonus.value,
                                            weakness.value,
                                            levelSelector.value)
    else:
        xLists, yLists, nameList = createTraces(levelDiff.value, 
                                            flatfootedBox.value, 
                                            attackBonus.value,
                                            damageBonus.value,
                                            weakness.value)
#     print("selected: ", xLists, yLists)
#     print(Selector.selectedAttack[1])
#     for i in range(1,21):
#         if i in fighterAttackBonus and i+levelDiff.value in averageAcByLevel:
# #             print(selectedAttack[i])
#             xList.append(i)
#             yList.append(calculateED(Selector.selectedAttack[i]+attackBonus.value,averageAcByLevel[i+levelDiff.value],Selector.selectedDamage[i]+damageBonus.value,dm=weakness.value))
    if percentageView.value and len(yLists)>0:
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
                        
    with g.batch_update():
        g.data = []
        for i in range(len(xLists)):
            g.add_trace(go.Scatter(x=xLists[i],y=yLists[i],name=nameList[i]))
        
        # update legend size
        g.update_layout(height=500+10*len(nameList))
        
        # should update the axis so the data fits
        if percentageView.value:
            g.layout.yaxis.range = [0,200]
        else:
            g.layout.yaxis.range = [0,60]
        if byLevelView.value:
            g.layout.xaxis.range = [-10,10]
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

adjustments = widgets.HBox([levelDiff,attackBonus,damageBonus,weakness])
targetRow = widgets.HBox([targetSelector,flatfootedBox,persistentDamageWeightBox,percentageView])
levelViewRow = widgets.HBox([byLevelView,levelSelector])

selectorModifiers = widgets.VBox([selectorAddButton,attackModifier,damageModifier,levelLimiter])
weaponModifiers = widgets.VBox([weaponDamageDie,weaponCritical,criticalSpecialization])
runeModifiers = widgets.VBox([elementalRunesLabel,elementalRune1,elementalRune2,elementalRune3,elementalRune4])
selectorBox = widgets.HBox([selector,selectorModifiers,weaponModifiers,runeModifiers])

selectionsButtons = widgets.VBox([removeSelectionButton,movetotopButton,combineSelectionButton,minButton,maxButton,newNameBox])
selectionsBox = widgets.HBox([selections,selectionsButtons])

ExpectedDamageByLevelWidget = widgets.VBox([adjustments,
              targetRow,
              levelViewRow,
              g,
             selectorBox,
             selectionsBox])