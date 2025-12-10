# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022 replay file
# Internal Version: 2021_09_16-02.57.30 176069
# Run by elishje on Wed Dec 10 21:24:12 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=533.399963378906, 
    height=339.800445556641)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(pathName='M:/Documents/abacusfinal/final boss.cae')
#: The model database "M:\Documents\abacusfinal\final boss.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
o3 = session.openOdb(name='M:/Documents/abacusfinal/Job-4.odb')
#: Model: M:/Documents/abacusfinal/Job-4.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       7
#: Number of Node Sets:          13
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
odb = session.odbs['M:/Documents/abacusfinal/Job-4.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Element Label', odb=odb, step=0, frame=1, 
    outputPosition=INTEGRATION_POINT, variable=(('S', INTEGRATION_POINT), ), 
    stepFrame=SPECIFY)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['M:/Documents/abacusfinal/Job-4.odb'])
o3 = session.openOdb(name='M:/Documents/abacusfinal/Job-3.odb')
#: Model: M:/Documents/abacusfinal/Job-3.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       7
#: Number of Node Sets:          13
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
odb = session.odbs['M:/Documents/abacusfinal/Job-3.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Element Label', odb=odb, step=0, frame=1, 
    outputPosition=INTEGRATION_POINT, variable=(('S', INTEGRATION_POINT), ), 
    stepFrame=SPECIFY)
odb = session.odbs['M:/Documents/abacusfinal/Job-3.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('RF', NODAL), ('U', NODAL), ), stepFrame=SPECIFY)
odb = session.odbs['M:/Documents/abacusfinal/Job-4.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
odb = session.odbs['M:/Documents/abacusfinal/Job-4.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('RF', NODAL), ('U', NODAL), ), stepFrame=SPECIFY)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['M:/Documents/abacusfinal/Job-4.odb'])
odb = session.odbs['M:/Documents/abacusfinal/Job-4.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
p = mdb.models['Model-1'].parts['Truss']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
odb = session.odbs['M:/Documents/abacusfinal/Job-4.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Truss-1'].elements
elements1 = e1.getSequenceFromMask(mask=('[#80 ]', ), )
leaf = dgm.LeafFromMeshElementLabels(elementSeq=elements1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.add(leaf=leaf)
dg = session.viewports['Viewport: 1'].assemblyDisplay.displayGroup
dg = session.DisplayGroup(name='DisplayGroup-2', objectToCopy=dg)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    visibleDisplayGroups=(dg, ))
dg = session.viewports['Viewport: 1'].assemblyDisplay.displayGroup
dg = session.DisplayGroup(name='DisplayGroup-3', objectToCopy=dg)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    visibleDisplayGroups=(dg, ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(viewCut=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(viewCut=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(viewCut=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(viewCut=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(viewCut=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(viewCut=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['M:/Documents/abacusfinal/Job-4.odb'])
odb = session.odbs['M:/Documents/abacusfinal/Job-4.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
#: 
#: Element: TRUSS-1.8
#:   Type: T2D2
#:   Material: STEEL
#:   Section: SET-14.Section-ASSEMBLY_TRUSS-1_SET-14, Homogeneous Solid Section, Thickness = 5
#:   Connect: 1, 6
#:   S, Mises (Not averaged): 531.25
#: 
#: Element: TRUSS-1.5
#:   Type: T2D2
#:   Material: STEEL
#:   Section: SET-14.Section-ASSEMBLY_TRUSS-1_SET-14, Homogeneous Solid Section, Thickness = 5
#:   Connect: 5, 1
#:   S, Mises (Not averaged): 400
#: 
#: Element: TRUSS-1.8
#:   Type: T2D2
#:   Material: STEEL
#:   Section: SET-14.Section-ASSEMBLY_TRUSS-1_SET-14, Homogeneous Solid Section, Thickness = 5
#:   Connect: 1, 6
#:   S, Mises (Not averaged): 531.25
odb = session.odbs['M:/Documents/abacusfinal/Job-3.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
#: 
#: Element: TRUSS-1.8
#:   Type: T2D2
#:   Material: STEEL
#:   Section: SET-14.Section-ASSEMBLY_TRUSS-1_SET-14, Homogeneous Solid Section, Thickness = 5
#:   Connect: 1, 6
#:   S, Mises (Not averaged): 531.25
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=OFF, 
    legend=OFF, title=OFF, state=OFF, annotations=OFF, compass=OFF)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(legend=ON)
session.printToFile(fileName='M:/Documents/My Pictures/modelF', format=EPS, 
    canvasObjects=(session.viewports['Viewport: 1'], ))
odb = session.odbs['M:/Documents/abacusfinal/Job-4.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.fitView()
session.printToFile(fileName='M:/Documents/My Pictures/modelR', format=EPS, 
    canvasObjects=(session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=3048.95, 
    farPlane=4504.51, width=1137.64, height=455.157, viewOffsetX=-1.41027, 
    viewOffsetY=15.9869)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3049.41, 
    farPlane=4504.04, width=1135.74, height=454.395, viewOffsetX=-21.3429, 
    viewOffsetY=13.9126)
session.viewports['Viewport: 1'].view.setValues(nearPlane=3056.33, 
    farPlane=4497.13, width=1006.21, height=402.572, viewOffsetX=8.9361, 
    viewOffsetY=1.06254)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=8.96411, 
    viewOffsetY=1.06587)
mdb.save()
#: The model database has been saved to "M:\Documents\abacusfinal\final boss.cae".
mdb.save()
#: The model database has been saved to "M:\Documents\abacusfinal\final boss.cae".
mdb.save()
#: The model database has been saved to "M:\Documents\abacusfinal\final boss.cae".
mdb.save()
#: The model database has been saved to "M:\Documents\abacusfinal\final boss.cae".
mdb.save()
#: The model database has been saved to "M:\Documents\abacusfinal\final boss.cae".
mdb.save()
#: The model database has been saved to "M:\Documents\abacusfinal\final boss.cae".
mdb.save()
#: The model database has been saved to "M:\Documents\abacusfinal\final boss.cae".
mdb.save()
#: The model database has been saved to "M:\Documents\abacusfinal\final boss.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=2874.96, 
    farPlane=4537.24, width=1295.25, height=630.012, viewOffsetX=46.9712, 
    viewOffsetY=-33.1074)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=3258.1, 
    farPlane=4908.14, width=1031.35, height=462.741, viewOffsetX=64.8729, 
    viewOffsetY=-32.6503)
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendFont='-*-verdana-medium-r-normal-*-*-180-*-*-p-*-*-*')
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendFont='-*-verdana-medium-r-normal-*-*-240-*-*-p-*-*-*')
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
    legendDecimalPlaces=2)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(
    fileName='C:/Users/elishje/OneDrive - NTNU/H25/cau/Introduction to finite element analysis/bilder/modelR', 
    format=EPS, canvasObjects=(session.viewports['Viewport: 1'], ))
odb = session.odbs['M:/Documents/abacusfinal/Job-3.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(
    fileName='C:/Users/elishje/OneDrive - NTNU/H25/cau/Introduction to finite element analysis/bilder/modelF', 
    format=EPS, canvasObjects=(session.viewports['Viewport: 1'], ))
odb = session.odbs['M:/Documents/abacusfinal/Job-4.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
odb = session.odbs['M:/Documents/abacusfinal/Job-3.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2958.42, 
    farPlane=4343.35, width=981.841, height=440.526, viewOffsetX=-1.64598, 
    viewOffsetY=1.64636)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.printToFile(
    fileName='C:/Users/elishje/OneDrive - NTNU/H25/cau/Introduction to finite element analysis/bilder/modelF', 
    format=EPS, canvasObjects=(session.viewports['Viewport: 1'], ))
odb = session.odbs['M:/Documents/abacusfinal/Job-4.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['M:/Documents/abacusfinal/Job-4.odb'])
odb = session.odbs['M:/Documents/abacusfinal/Job-4.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.printToFile(
    fileName='C:/Users/elishje/OneDrive - NTNU/H25/cau/Introduction to finite element analysis/bilder/modelR', 
    format=EPS, canvasObjects=(session.viewports['Viewport: 1'], ))
session.printToFile(
    fileName='C:/Users/elishje/OneDrive - NTNU/H25/cau/Introduction to finite element analysis/bilder/modelR', 
    format=EPS, canvasObjects=(session.viewports['Viewport: 1'], ))
odb = session.odbs['M:/Documents/abacusfinal/Job-3.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2884.56, 
    farPlane=4270.86, width=995.744, height=446.763, viewOffsetX=-1.2283, 
    viewOffsetY=-50.7811)
session.printToFile(
    fileName='C:/Users/elishje/OneDrive - NTNU/H25/cau/Introduction to finite element analysis/bilder/modelF', 
    format=EPS, canvasObjects=(session.viewports['Viewport: 1'], ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.printToFile(
    fileName='C:/Users/elishje/OneDrive - NTNU/H25/cau/Introduction to finite element analysis/bilder/modelF', 
    format=EPS, canvasObjects=(session.viewports['Viewport: 1'], ))
odb = session.odbs['M:/Documents/abacusfinal/Job-4.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.printToFile(
    fileName='C:/Users/elishje/OneDrive - NTNU/H25/cau/Introduction to finite element analysis/bilder/modelR', 
    format=EPS, canvasObjects=(session.viewports['Viewport: 1'], ))
