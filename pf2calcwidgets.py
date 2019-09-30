from pf2calc import *
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

selector = widgets.SelectMultiple(
    options=['Fighter Longsword Strike',
             'Fighter Longsword Snagging Strike',
             'Fighter Longsword Certain Strike',
             'Fighter Greatsword Strike',
             'Fighter Greatsword Power Attack',
             'Fighter Greatsword Brutish Shove',
             'Fighter Greatsword Knockdown',
             'Fighter Greatsword Certain Strike',
             'Fighter Greatsword Brutal Finish',
             'Fighter Shortsword Strike',
             'Fighter Shortsword Snagging Strike',
             'Fighter Shortsword Certain Strike',
             'Fighter Bastardsword Dual-Handed Assult'
             ],
    value=['Fighter Longsword Strike'],
    description='Selection:',
    layout=widgets.Layout(width='50%'),
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
        if attackModifier.value != 0:
            name += " +a" + str(attackModifier.value)
        if damageModifier.value != 0:
            name += " +d" + str(damageModifier.value)
        minLevel = levelLimiter.value[0]
        maxLevel = levelLimiter.value[1]
        if not (name in selections.options):
            selections.options += (name,)
            Selector.addSelection(name,s,attackModifier.value,damageModifier.value,minLevel,maxLevel)
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

g = go.FigureWidget() 
g.update_layout(title_text="Expected damage by level",
                  title_font_size=30,
               legend_orientation="h",
               height=500
               )
g.layout.xaxis.range = [0,20]
g.layout.yaxis.range = [0,60]

def updateEDBLGraph():
    xLists, yLists, nameList = createTrace(levelDiff.value, 
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
    with g.batch_update():
        g.data = []
        for i in range(len(xLists)):
            g.add_trace(go.Scatter(x=xLists[i],y=yLists[i],name=nameList[i]))
            
def edblResponse(change):
    updateEDBLGraph()        

levelDiff.observe(edblResponse, names="value")
attackBonus.observe(edblResponse, names="value")
damageBonus.observe(edblResponse, names="value")
weakness.observe(edblResponse, names="value")
flatfootedBox.observe(edblResponse, names="value")


adjustments = widgets.HBox([levelDiff,attackBonus,damageBonus,weakness])
targetRow = widgets.HBox([targetSelector,flatfootedBox,persistentDamageWeightBox])

selectorModifiers = widgets.VBox([selectorAddButton,attackModifier,damageModifier,levelLimiter])
selectorBox = widgets.HBox([selector,selectorModifiers])

selectionsButtons = widgets.VBox([removeSelectionButton,movetotopButton,combineSelectionButton])
selectionsBox = widgets.HBox([selections,selectionsButtons])

ExpectedDamageByLevelWidget = widgets.VBox([adjustments,
              targetRow,
              g,
             selectorBox,
             selectionsBox])