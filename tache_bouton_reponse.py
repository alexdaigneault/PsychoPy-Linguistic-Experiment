#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on October 30, 2019, at 16:07
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, microphone
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'tache_bouton_reponse'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\daign\\Documents\\UQAM - Maitrise en linguistique\\Psycholinguistique\\Recherche\\tache_bouton_reponse.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')

# Enable sound input/output:
microphone.switchOn()
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
instruction = visual.TextStim(win=win, name='instruction',
    text="Vous entendrez des sons dans diverses conditions.\nVeuillez sélectionner le son entendu.\nAppuyez sur la barre d'espacement lorsque vous êtes prêt!\n",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_start_pratique = keyboard.Keyboard()

# Initialize components for Routine "Pratique"
PratiqueClock = core.Clock()
pratique_audio = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='pratique_audio')
pratique_audio.setVolume(1)
choix_pratique = visual.TextStim(win=win, name='choix_pratique',
    text='Veuillez sélectionner le son entendu:\n\n                i               a\n                si             sa\n                zi             za',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_reponse_pratique = keyboard.Keyboard()

# Initialize components for Routine "Explications_A"
Explications_AClock = core.Clock()
instruction_A = visual.TextStim(win=win, name='instruction_A',
    text="Dans la prochaine tâche, vous entendrez des sons dans le bruit.\nVeuillez sélectionner le son entendu.\nAppuyez sur la barre d'espacement lorsque vous êtes prêt!",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_start_audio = keyboard.Keyboard()

# Initialize components for Routine "Condition_A"
Condition_AClock = core.Clock()
Stimuli_Audio = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Stimuli_Audio')
Stimuli_Audio.setVolume(1)
choix_A = visual.TextStim(win=win, name='choix_A',
    text='Veuillez sélectionner le son entendu:\n\n                u               ou\n                tu              tou\n                du             dou',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_reponse_A = keyboard.Keyboard()

# Initialize components for Routine "Explications_AV"
Explications_AVClock = core.Clock()
instruction_AV = visual.TextStim(win=win, name='instruction_AV',
    text="Dans la prochaine tâche, vous visionnerez des vidéos.\nVous entendrez des sons dans le bruit.\nVeuillez sélectionner le son entendu.\nAppuyer sur la barre d'espacement lorsque vous êtes prêt!",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_start_audiovisuel = keyboard.Keyboard()

# Initialize components for Routine "Condition_AV"
Condition_AVClock = core.Clock()
choix_AV = visual.TextStim(win=win, name='choix_AV',
    text='Veuillez sélectionner le son entendu:\n\n                u               ou\n                tu              tou\n                du             dou',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_reponse_AV = keyboard.Keyboard()

# Initialize components for Routine "Explications_AV"
Explications_AVClock = core.Clock()
instruction_AV = visual.TextStim(win=win, name='instruction_AV',
    text="Dans la prochaine tâche, vous visionnerez des vidéos.\nVous entendrez des sons dans le bruit.\nVeuillez sélectionner le son entendu.\nAppuyer sur la barre d'espacement lorsque vous êtes prêt!",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_start_audiovisuel = keyboard.Keyboard()

# Initialize components for Routine "Condition_AVD"
Condition_AVDClock = core.Clock()
choix_AVD = visual.TextStim(win=win, name='choix_AVD',
    text='Veuillez sélectionner le son entendu:\n\n                u               ou\n                tu              tou\n                du             dou',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_reponse_AVD = keyboard.Keyboard()

# Initialize components for Routine "Explications_V"
Explications_VClock = core.Clock()
instruction_V = visual.TextStim(win=win, name='instruction_V',
    text="Dans la prochaine tâche, vous visionnerez des vidéos sans le son. \nVous devrez déduire les sons produits.\nVeuillez sélectionner le son perçu.\nAppuyer sur la barre d'espacement lorsque vous êtes prêt!",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_start_visuel = keyboard.Keyboard()

# Initialize components for Routine "Condition_V"
Condition_VClock = core.Clock()
choix_V = visual.TextStim(win=win, name='choix_V',
    text='Veuillez sélectionner le son entendu:\n\n                u               ou\n                tu              tou\n                du             dou',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_reponse_V = keyboard.Keyboard()

# Initialize components for Routine "Fin"
FinClock = core.Clock()
Remerciement = visual.TextStim(win=win, name='Remerciement',
    text='Terminé!\n\nMerci de votre participation! \n\n:)',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction"-------
# update component parameters for each repeat
key_start_pratique.keys = []
key_start_pratique.rt = []
# keep track of which components have finished
InstructionComponents = [instruction, key_start_pratique]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction* updates
    if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction.frameNStart = frameN  # exact frame index
        instruction.tStart = t  # local t and not account for scr refresh
        instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
        instruction.setAutoDraw(True)
    
    # *key_start_pratique* updates
    waitOnFlip = False
    if key_start_pratique.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start_pratique.frameNStart = frameN  # exact frame index
        key_start_pratique.tStart = t  # local t and not account for scr refresh
        key_start_pratique.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start_pratique, 'tStartRefresh')  # time at next scr refresh
        key_start_pratique.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start_pratique.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start_pratique.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start_pratique.status == STARTED and not waitOnFlip:
        theseKeys = key_start_pratique.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_start_pratique.keys = theseKeys.name  # just the last key pressed
            key_start_pratique.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction.started', instruction.tStartRefresh)
thisExp.addData('instruction.stopped', instruction.tStopRefresh)
# check responses
if key_start_pratique.keys in ['', [], None]:  # No response was made
    key_start_pratique.keys = None
thisExp.addData('key_start_pratique.keys',key_start_pratique.keys)
if key_start_pratique.keys != None:  # we had a response
    thisExp.addData('key_start_pratique.rt', key_start_pratique.rt)
thisExp.addData('key_start_pratique.started', key_start_pratique.tStartRefresh)
thisExp.addData('key_start_pratique.stopped', key_start_pratique.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pratique_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_pratique.xlsx'),
    seed=None, name='pratique_loop')
thisExp.addLoop(pratique_loop)  # add the loop to the experiment
thisPratique_loop = pratique_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPratique_loop.rgb)
if thisPratique_loop != None:
    for paramName in thisPratique_loop:
        exec('{} = thisPratique_loop[paramName]'.format(paramName))

for thisPratique_loop in pratique_loop:
    currentLoop = pratique_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPratique_loop.rgb)
    if thisPratique_loop != None:
        for paramName in thisPratique_loop:
            exec('{} = thisPratique_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Pratique"-------
    # update component parameters for each repeat
    pratique_audio.setSound(stimuli_pratique, hamming=True)
    pratique_audio.setVolume(1, log=False)
    key_reponse_pratique.keys = []
    key_reponse_pratique.rt = []
    # keep track of which components have finished
    PratiqueComponents = [pratique_audio, choix_pratique, key_reponse_pratique]
    for thisComponent in PratiqueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PratiqueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Pratique"-------
    while continueRoutine:
        # get current time
        t = PratiqueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PratiqueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop pratique_audio
        if pratique_audio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pratique_audio.frameNStart = frameN  # exact frame index
            pratique_audio.tStart = t  # local t and not account for scr refresh
            pratique_audio.tStartRefresh = tThisFlipGlobal  # on global time
            pratique_audio.play(when=win)  # sync with win flip
        
        # *choix_pratique* updates
        if choix_pratique.status == NOT_STARTED and pratique_audio.status==FINISHED:
            # keep track of start time/frame for later
            choix_pratique.frameNStart = frameN  # exact frame index
            choix_pratique.tStart = t  # local t and not account for scr refresh
            choix_pratique.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choix_pratique, 'tStartRefresh')  # time at next scr refresh
            choix_pratique.setAutoDraw(True)
        
        # *key_reponse_pratique* updates
        waitOnFlip = False
        if key_reponse_pratique.status == NOT_STARTED and pratique_audio.status==FINISHED:
            # keep track of start time/frame for later
            key_reponse_pratique.frameNStart = frameN  # exact frame index
            key_reponse_pratique.tStart = t  # local t and not account for scr refresh
            key_reponse_pratique.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_reponse_pratique, 'tStartRefresh')  # time at next scr refresh
            key_reponse_pratique.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_reponse_pratique.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_reponse_pratique.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_reponse_pratique.status == STARTED and not waitOnFlip:
            theseKeys = key_reponse_pratique.getKeys(keyList=['end', 'pagedown', 'left', 'right', 'home', 'pageup'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_reponse_pratique.keys = theseKeys.name  # just the last key pressed
                key_reponse_pratique.rt = theseKeys.rt
                # was this 'correct'?
                if (key_reponse_pratique.keys == str(corrRP)) or (key_reponse_pratique.keys == corrRP):
                    key_reponse_pratique.corr = 1
                else:
                    key_reponse_pratique.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PratiqueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pratique"-------
    for thisComponent in PratiqueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pratique_audio.stop()  # ensure sound has stopped at end of routine
    pratique_loop.addData('pratique_audio.started', pratique_audio.tStartRefresh)
    pratique_loop.addData('pratique_audio.stopped', pratique_audio.tStopRefresh)
    pratique_loop.addData('choix_pratique.started', choix_pratique.tStartRefresh)
    pratique_loop.addData('choix_pratique.stopped', choix_pratique.tStopRefresh)
    # check responses
    if key_reponse_pratique.keys in ['', [], None]:  # No response was made
        key_reponse_pratique.keys = None
        # was no response the correct answer?!
        if str(corrRP).lower() == 'none':
           key_reponse_pratique.corr = 1;  # correct non-response
        else:
           key_reponse_pratique.corr = 0;  # failed to respond (incorrectly)
    # store data for pratique_loop (TrialHandler)
    pratique_loop.addData('key_reponse_pratique.keys',key_reponse_pratique.keys)
    pratique_loop.addData('key_reponse_pratique.corr', key_reponse_pratique.corr)
    if key_reponse_pratique.keys != None:  # we had a response
        pratique_loop.addData('key_reponse_pratique.rt', key_reponse_pratique.rt)
    pratique_loop.addData('key_reponse_pratique.started', key_reponse_pratique.tStartRefresh)
    pratique_loop.addData('key_reponse_pratique.stopped', key_reponse_pratique.tStopRefresh)
    # the Routine "Pratique" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'pratique_loop'


# ------Prepare to start Routine "Explications_A"-------
# update component parameters for each repeat
key_start_audio.keys = []
key_start_audio.rt = []
# keep track of which components have finished
Explications_AComponents = [instruction_A, key_start_audio]
for thisComponent in Explications_AComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Explications_AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Explications_A"-------
while continueRoutine:
    # get current time
    t = Explications_AClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Explications_AClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_A* updates
    if instruction_A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_A.frameNStart = frameN  # exact frame index
        instruction_A.tStart = t  # local t and not account for scr refresh
        instruction_A.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_A, 'tStartRefresh')  # time at next scr refresh
        instruction_A.setAutoDraw(True)
    
    # *key_start_audio* updates
    waitOnFlip = False
    if key_start_audio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start_audio.frameNStart = frameN  # exact frame index
        key_start_audio.tStart = t  # local t and not account for scr refresh
        key_start_audio.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start_audio, 'tStartRefresh')  # time at next scr refresh
        key_start_audio.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start_audio.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start_audio.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start_audio.status == STARTED and not waitOnFlip:
        theseKeys = key_start_audio.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_start_audio.keys = theseKeys.name  # just the last key pressed
            key_start_audio.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Explications_AComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Explications_A"-------
for thisComponent in Explications_AComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_A.started', instruction_A.tStartRefresh)
thisExp.addData('instruction_A.stopped', instruction_A.tStopRefresh)
# check responses
if key_start_audio.keys in ['', [], None]:  # No response was made
    key_start_audio.keys = None
thisExp.addData('key_start_audio.keys',key_start_audio.keys)
if key_start_audio.keys != None:  # we had a response
    thisExp.addData('key_start_audio.rt', key_start_audio.rt)
thisExp.addData('key_start_audio.started', key_start_audio.tStartRefresh)
thisExp.addData('key_start_audio.stopped', key_start_audio.tStopRefresh)
thisExp.nextEntry()
# the Routine "Explications_A" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condition_A = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_A.xlsx'),
    seed=None, name='condition_A')
thisExp.addLoop(condition_A)  # add the loop to the experiment
thisCondition_A = condition_A.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition_A.rgb)
if thisCondition_A != None:
    for paramName in thisCondition_A:
        exec('{} = thisCondition_A[paramName]'.format(paramName))

for thisCondition_A in condition_A:
    currentLoop = condition_A
    # abbreviate parameter names if possible (e.g. rgb = thisCondition_A.rgb)
    if thisCondition_A != None:
        for paramName in thisCondition_A:
            exec('{} = thisCondition_A[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Condition_A"-------
    # update component parameters for each repeat
    Stimuli_Audio.setSound(stimuli_A, hamming=True)
    Stimuli_Audio.setVolume(1, log=False)
    key_reponse_A.keys = []
    key_reponse_A.rt = []
    # keep track of which components have finished
    Condition_AComponents = [Stimuli_Audio, choix_A, key_reponse_A]
    for thisComponent in Condition_AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Condition_AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Condition_A"-------
    while continueRoutine:
        # get current time
        t = Condition_AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Condition_AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop Stimuli_Audio
        if Stimuli_Audio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli_Audio.frameNStart = frameN  # exact frame index
            Stimuli_Audio.tStart = t  # local t and not account for scr refresh
            Stimuli_Audio.tStartRefresh = tThisFlipGlobal  # on global time
            Stimuli_Audio.play(when=win)  # sync with win flip
        
        # *choix_A* updates
        if choix_A.status == NOT_STARTED and Stimuli_Audio.status==FINISHED:
            # keep track of start time/frame for later
            choix_A.frameNStart = frameN  # exact frame index
            choix_A.tStart = t  # local t and not account for scr refresh
            choix_A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choix_A, 'tStartRefresh')  # time at next scr refresh
            choix_A.setAutoDraw(True)
        
        # *key_reponse_A* updates
        waitOnFlip = False
        if key_reponse_A.status == NOT_STARTED and Stimuli_Audio.status==FINISHED:
            # keep track of start time/frame for later
            key_reponse_A.frameNStart = frameN  # exact frame index
            key_reponse_A.tStart = t  # local t and not account for scr refresh
            key_reponse_A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_reponse_A, 'tStartRefresh')  # time at next scr refresh
            key_reponse_A.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_reponse_A.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_reponse_A.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_reponse_A.status == STARTED and not waitOnFlip:
            theseKeys = key_reponse_A.getKeys(keyList=['end', 'pagedown', 'left', 'right', 'home', 'pageup'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_reponse_A.keys = theseKeys.name  # just the last key pressed
                key_reponse_A.rt = theseKeys.rt
                # was this 'correct'?
                if (key_reponse_A.keys == str(corrRA)) or (key_reponse_A.keys == corrRA):
                    key_reponse_A.corr = 1
                else:
                    key_reponse_A.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Condition_AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Condition_A"-------
    for thisComponent in Condition_AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Stimuli_Audio.stop()  # ensure sound has stopped at end of routine
    condition_A.addData('Stimuli_Audio.started', Stimuli_Audio.tStartRefresh)
    condition_A.addData('Stimuli_Audio.stopped', Stimuli_Audio.tStopRefresh)
    condition_A.addData('choix_A.started', choix_A.tStartRefresh)
    condition_A.addData('choix_A.stopped', choix_A.tStopRefresh)
    # check responses
    if key_reponse_A.keys in ['', [], None]:  # No response was made
        key_reponse_A.keys = None
        # was no response the correct answer?!
        if str(corrRA).lower() == 'none':
           key_reponse_A.corr = 1;  # correct non-response
        else:
           key_reponse_A.corr = 0;  # failed to respond (incorrectly)
    # store data for condition_A (TrialHandler)
    condition_A.addData('key_reponse_A.keys',key_reponse_A.keys)
    condition_A.addData('key_reponse_A.corr', key_reponse_A.corr)
    if key_reponse_A.keys != None:  # we had a response
        condition_A.addData('key_reponse_A.rt', key_reponse_A.rt)
    condition_A.addData('key_reponse_A.started', key_reponse_A.tStartRefresh)
    condition_A.addData('key_reponse_A.stopped', key_reponse_A.tStopRefresh)
    # the Routine "Condition_A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'condition_A'


# ------Prepare to start Routine "Explications_AV"-------
# update component parameters for each repeat
key_start_audiovisuel.keys = []
key_start_audiovisuel.rt = []
# keep track of which components have finished
Explications_AVComponents = [instruction_AV, key_start_audiovisuel]
for thisComponent in Explications_AVComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Explications_AVClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Explications_AV"-------
while continueRoutine:
    # get current time
    t = Explications_AVClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Explications_AVClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_AV* updates
    if instruction_AV.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_AV.frameNStart = frameN  # exact frame index
        instruction_AV.tStart = t  # local t and not account for scr refresh
        instruction_AV.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_AV, 'tStartRefresh')  # time at next scr refresh
        instruction_AV.setAutoDraw(True)
    
    # *key_start_audiovisuel* updates
    waitOnFlip = False
    if key_start_audiovisuel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start_audiovisuel.frameNStart = frameN  # exact frame index
        key_start_audiovisuel.tStart = t  # local t and not account for scr refresh
        key_start_audiovisuel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start_audiovisuel, 'tStartRefresh')  # time at next scr refresh
        key_start_audiovisuel.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start_audiovisuel.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start_audiovisuel.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start_audiovisuel.status == STARTED and not waitOnFlip:
        theseKeys = key_start_audiovisuel.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_start_audiovisuel.keys = theseKeys.name  # just the last key pressed
            key_start_audiovisuel.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Explications_AVComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Explications_AV"-------
for thisComponent in Explications_AVComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_AV.started', instruction_AV.tStartRefresh)
thisExp.addData('instruction_AV.stopped', instruction_AV.tStopRefresh)
# check responses
if key_start_audiovisuel.keys in ['', [], None]:  # No response was made
    key_start_audiovisuel.keys = None
thisExp.addData('key_start_audiovisuel.keys',key_start_audiovisuel.keys)
if key_start_audiovisuel.keys != None:  # we had a response
    thisExp.addData('key_start_audiovisuel.rt', key_start_audiovisuel.rt)
thisExp.addData('key_start_audiovisuel.started', key_start_audiovisuel.tStartRefresh)
thisExp.addData('key_start_audiovisuel.stopped', key_start_audiovisuel.tStopRefresh)
thisExp.nextEntry()
# the Routine "Explications_AV" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condition_AV = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_AV.xlsx'),
    seed=None, name='condition_AV')
thisExp.addLoop(condition_AV)  # add the loop to the experiment
thisCondition_AV = condition_AV.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition_AV.rgb)
if thisCondition_AV != None:
    for paramName in thisCondition_AV:
        exec('{} = thisCondition_AV[paramName]'.format(paramName))

for thisCondition_AV in condition_AV:
    currentLoop = condition_AV
    # abbreviate parameter names if possible (e.g. rgb = thisCondition_AV.rgb)
    if thisCondition_AV != None:
        for paramName in thisCondition_AV:
            exec('{} = thisCondition_AV[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Condition_AV"-------
    # update component parameters for each repeat
    Stimuli_AV = visual.MovieStim3(
        win=win, name='Stimuli_AV',units='pix', 
        noAudio = False,
        filename=stimuli_AV,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        size=[1366,768],
        depth=0.0,
        )
    key_reponse_AV.keys = []
    key_reponse_AV.rt = []
    # keep track of which components have finished
    Condition_AVComponents = [Stimuli_AV, choix_AV, key_reponse_AV]
    for thisComponent in Condition_AVComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Condition_AVClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Condition_AV"-------
    while continueRoutine:
        # get current time
        t = Condition_AVClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Condition_AVClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stimuli_AV* updates
        if Stimuli_AV.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli_AV.frameNStart = frameN  # exact frame index
            Stimuli_AV.tStart = t  # local t and not account for scr refresh
            Stimuli_AV.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli_AV, 'tStartRefresh')  # time at next scr refresh
            Stimuli_AV.setAutoDraw(True)
        
        # *choix_AV* updates
        if choix_AV.status == NOT_STARTED and Stimuli_AV.status==FINISHED:
            # keep track of start time/frame for later
            choix_AV.frameNStart = frameN  # exact frame index
            choix_AV.tStart = t  # local t and not account for scr refresh
            choix_AV.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choix_AV, 'tStartRefresh')  # time at next scr refresh
            choix_AV.setAutoDraw(True)
        
        # *key_reponse_AV* updates
        waitOnFlip = False
        if key_reponse_AV.status == NOT_STARTED and Stimuli_AV.status==FINISHED:
            # keep track of start time/frame for later
            key_reponse_AV.frameNStart = frameN  # exact frame index
            key_reponse_AV.tStart = t  # local t and not account for scr refresh
            key_reponse_AV.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_reponse_AV, 'tStartRefresh')  # time at next scr refresh
            key_reponse_AV.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_reponse_AV.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_reponse_AV.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_reponse_AV.status == STARTED and not waitOnFlip:
            theseKeys = key_reponse_AV.getKeys(keyList=['end', 'pagedown', 'left', 'right', 'home', 'pageup'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_reponse_AV.keys = theseKeys.name  # just the last key pressed
                key_reponse_AV.rt = theseKeys.rt
                # was this 'correct'?
                if (key_reponse_AV.keys == str(corrRAV)) or (key_reponse_AV.keys == corrRAV):
                    key_reponse_AV.corr = 1
                else:
                    key_reponse_AV.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Condition_AVComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Condition_AV"-------
    for thisComponent in Condition_AVComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    condition_AV.addData('Stimuli_AV.started', Stimuli_AV.tStartRefresh)
    condition_AV.addData('Stimuli_AV.stopped', Stimuli_AV.tStopRefresh)
    condition_AV.addData('choix_AV.started', choix_AV.tStartRefresh)
    condition_AV.addData('choix_AV.stopped', choix_AV.tStopRefresh)
    # check responses
    if key_reponse_AV.keys in ['', [], None]:  # No response was made
        key_reponse_AV.keys = None
        # was no response the correct answer?!
        if str(corrRAV).lower() == 'none':
           key_reponse_AV.corr = 1;  # correct non-response
        else:
           key_reponse_AV.corr = 0;  # failed to respond (incorrectly)
    # store data for condition_AV (TrialHandler)
    condition_AV.addData('key_reponse_AV.keys',key_reponse_AV.keys)
    condition_AV.addData('key_reponse_AV.corr', key_reponse_AV.corr)
    if key_reponse_AV.keys != None:  # we had a response
        condition_AV.addData('key_reponse_AV.rt', key_reponse_AV.rt)
    condition_AV.addData('key_reponse_AV.started', key_reponse_AV.tStartRefresh)
    condition_AV.addData('key_reponse_AV.stopped', key_reponse_AV.tStopRefresh)
    # the Routine "Condition_AV" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'condition_AV'


# ------Prepare to start Routine "Explications_AV"-------
# update component parameters for each repeat
key_start_audiovisuel.keys = []
key_start_audiovisuel.rt = []
# keep track of which components have finished
Explications_AVComponents = [instruction_AV, key_start_audiovisuel]
for thisComponent in Explications_AVComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Explications_AVClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Explications_AV"-------
while continueRoutine:
    # get current time
    t = Explications_AVClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Explications_AVClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_AV* updates
    if instruction_AV.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_AV.frameNStart = frameN  # exact frame index
        instruction_AV.tStart = t  # local t and not account for scr refresh
        instruction_AV.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_AV, 'tStartRefresh')  # time at next scr refresh
        instruction_AV.setAutoDraw(True)
    
    # *key_start_audiovisuel* updates
    waitOnFlip = False
    if key_start_audiovisuel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start_audiovisuel.frameNStart = frameN  # exact frame index
        key_start_audiovisuel.tStart = t  # local t and not account for scr refresh
        key_start_audiovisuel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start_audiovisuel, 'tStartRefresh')  # time at next scr refresh
        key_start_audiovisuel.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start_audiovisuel.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start_audiovisuel.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start_audiovisuel.status == STARTED and not waitOnFlip:
        theseKeys = key_start_audiovisuel.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_start_audiovisuel.keys = theseKeys.name  # just the last key pressed
            key_start_audiovisuel.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Explications_AVComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Explications_AV"-------
for thisComponent in Explications_AVComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_AV.started', instruction_AV.tStartRefresh)
thisExp.addData('instruction_AV.stopped', instruction_AV.tStopRefresh)
# check responses
if key_start_audiovisuel.keys in ['', [], None]:  # No response was made
    key_start_audiovisuel.keys = None
thisExp.addData('key_start_audiovisuel.keys',key_start_audiovisuel.keys)
if key_start_audiovisuel.keys != None:  # we had a response
    thisExp.addData('key_start_audiovisuel.rt', key_start_audiovisuel.rt)
thisExp.addData('key_start_audiovisuel.started', key_start_audiovisuel.tStartRefresh)
thisExp.addData('key_start_audiovisuel.stopped', key_start_audiovisuel.tStopRefresh)
thisExp.nextEntry()
# the Routine "Explications_AV" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condition_AVD = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_AVD.xlsx'),
    seed=None, name='condition_AVD')
thisExp.addLoop(condition_AVD)  # add the loop to the experiment
thisCondition_AVD = condition_AVD.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition_AVD.rgb)
if thisCondition_AVD != None:
    for paramName in thisCondition_AVD:
        exec('{} = thisCondition_AVD[paramName]'.format(paramName))

for thisCondition_AVD in condition_AVD:
    currentLoop = condition_AVD
    # abbreviate parameter names if possible (e.g. rgb = thisCondition_AVD.rgb)
    if thisCondition_AVD != None:
        for paramName in thisCondition_AVD:
            exec('{} = thisCondition_AVD[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Condition_AVD"-------
    # update component parameters for each repeat
    Stimuli_AVD = visual.MovieStim3(
        win=win, name='Stimuli_AVD',units='pix', 
        noAudio = False,
        filename=stimuli_AVD,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        size=[1366,768],
        depth=0.0,
        )
    key_reponse_AVD.keys = []
    key_reponse_AVD.rt = []
    # keep track of which components have finished
    Condition_AVDComponents = [Stimuli_AVD, choix_AVD, key_reponse_AVD]
    for thisComponent in Condition_AVDComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Condition_AVDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Condition_AVD"-------
    while continueRoutine:
        # get current time
        t = Condition_AVDClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Condition_AVDClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stimuli_AVD* updates
        if Stimuli_AVD.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli_AVD.frameNStart = frameN  # exact frame index
            Stimuli_AVD.tStart = t  # local t and not account for scr refresh
            Stimuli_AVD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli_AVD, 'tStartRefresh')  # time at next scr refresh
            Stimuli_AVD.setAutoDraw(True)
        
        # *choix_AVD* updates
        if choix_AVD.status == NOT_STARTED and Stimuli_AVD.status==FINISHED:
            # keep track of start time/frame for later
            choix_AVD.frameNStart = frameN  # exact frame index
            choix_AVD.tStart = t  # local t and not account for scr refresh
            choix_AVD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choix_AVD, 'tStartRefresh')  # time at next scr refresh
            choix_AVD.setAutoDraw(True)
        
        # *key_reponse_AVD* updates
        waitOnFlip = False
        if key_reponse_AVD.status == NOT_STARTED and Stimuli_AVD.status==FINISHED:
            # keep track of start time/frame for later
            key_reponse_AVD.frameNStart = frameN  # exact frame index
            key_reponse_AVD.tStart = t  # local t and not account for scr refresh
            key_reponse_AVD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_reponse_AVD, 'tStartRefresh')  # time at next scr refresh
            key_reponse_AVD.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_reponse_AVD.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_reponse_AVD.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_reponse_AVD.status == STARTED and not waitOnFlip:
            theseKeys = key_reponse_AVD.getKeys(keyList=['end', 'pagedown', 'left', 'right', 'home', 'pageup'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_reponse_AVD.keys = theseKeys.name  # just the last key pressed
                key_reponse_AVD.rt = theseKeys.rt
                # was this 'correct'?
                if (key_reponse_AVD.keys == str(corrRAVD)) or (key_reponse_AVD.keys == corrRAVD):
                    key_reponse_AVD.corr = 1
                else:
                    key_reponse_AVD.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Condition_AVDComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Condition_AVD"-------
    for thisComponent in Condition_AVDComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    condition_AVD.addData('Stimuli_AVD.started', Stimuli_AVD.tStartRefresh)
    condition_AVD.addData('Stimuli_AVD.stopped', Stimuli_AVD.tStopRefresh)
    condition_AVD.addData('choix_AVD.started', choix_AVD.tStartRefresh)
    condition_AVD.addData('choix_AVD.stopped', choix_AVD.tStopRefresh)
    # check responses
    if key_reponse_AVD.keys in ['', [], None]:  # No response was made
        key_reponse_AVD.keys = None
        # was no response the correct answer?!
        if str(corrRAVD).lower() == 'none':
           key_reponse_AVD.corr = 1;  # correct non-response
        else:
           key_reponse_AVD.corr = 0;  # failed to respond (incorrectly)
    # store data for condition_AVD (TrialHandler)
    condition_AVD.addData('key_reponse_AVD.keys',key_reponse_AVD.keys)
    condition_AVD.addData('key_reponse_AVD.corr', key_reponse_AVD.corr)
    if key_reponse_AVD.keys != None:  # we had a response
        condition_AVD.addData('key_reponse_AVD.rt', key_reponse_AVD.rt)
    condition_AVD.addData('key_reponse_AVD.started', key_reponse_AVD.tStartRefresh)
    condition_AVD.addData('key_reponse_AVD.stopped', key_reponse_AVD.tStopRefresh)
    # the Routine "Condition_AVD" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'condition_AVD'


# ------Prepare to start Routine "Explications_V"-------
# update component parameters for each repeat
key_start_visuel.keys = []
key_start_visuel.rt = []
# keep track of which components have finished
Explications_VComponents = [instruction_V, key_start_visuel]
for thisComponent in Explications_VComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Explications_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Explications_V"-------
while continueRoutine:
    # get current time
    t = Explications_VClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Explications_VClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_V* updates
    if instruction_V.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_V.frameNStart = frameN  # exact frame index
        instruction_V.tStart = t  # local t and not account for scr refresh
        instruction_V.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_V, 'tStartRefresh')  # time at next scr refresh
        instruction_V.setAutoDraw(True)
    
    # *key_start_visuel* updates
    waitOnFlip = False
    if key_start_visuel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start_visuel.frameNStart = frameN  # exact frame index
        key_start_visuel.tStart = t  # local t and not account for scr refresh
        key_start_visuel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start_visuel, 'tStartRefresh')  # time at next scr refresh
        key_start_visuel.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start_visuel.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start_visuel.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start_visuel.status == STARTED and not waitOnFlip:
        theseKeys = key_start_visuel.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_start_visuel.keys = theseKeys.name  # just the last key pressed
            key_start_visuel.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Explications_VComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Explications_V"-------
for thisComponent in Explications_VComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_V.started', instruction_V.tStartRefresh)
thisExp.addData('instruction_V.stopped', instruction_V.tStopRefresh)
# check responses
if key_start_visuel.keys in ['', [], None]:  # No response was made
    key_start_visuel.keys = None
thisExp.addData('key_start_visuel.keys',key_start_visuel.keys)
if key_start_visuel.keys != None:  # we had a response
    thisExp.addData('key_start_visuel.rt', key_start_visuel.rt)
thisExp.addData('key_start_visuel.started', key_start_visuel.tStartRefresh)
thisExp.addData('key_start_visuel.stopped', key_start_visuel.tStopRefresh)
thisExp.nextEntry()
# the Routine "Explications_V" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condition_V = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_V.xlsx'),
    seed=None, name='condition_V')
thisExp.addLoop(condition_V)  # add the loop to the experiment
thisCondition_V = condition_V.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition_V.rgb)
if thisCondition_V != None:
    for paramName in thisCondition_V:
        exec('{} = thisCondition_V[paramName]'.format(paramName))

for thisCondition_V in condition_V:
    currentLoop = condition_V
    # abbreviate parameter names if possible (e.g. rgb = thisCondition_V.rgb)
    if thisCondition_V != None:
        for paramName in thisCondition_V:
            exec('{} = thisCondition_V[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Condition_V"-------
    # update component parameters for each repeat
    Stimuli_V = visual.MovieStim3(
        win=win, name='Stimuli_V',units='pix', 
        noAudio = False,
        filename=stimuli_V,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        size=[1366,768],
        depth=0.0,
        )
    key_reponse_V.keys = []
    key_reponse_V.rt = []
    # keep track of which components have finished
    Condition_VComponents = [Stimuli_V, choix_V, key_reponse_V]
    for thisComponent in Condition_VComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Condition_VClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Condition_V"-------
    while continueRoutine:
        # get current time
        t = Condition_VClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Condition_VClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stimuli_V* updates
        if Stimuli_V.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli_V.frameNStart = frameN  # exact frame index
            Stimuli_V.tStart = t  # local t and not account for scr refresh
            Stimuli_V.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli_V, 'tStartRefresh')  # time at next scr refresh
            Stimuli_V.setAutoDraw(True)
        
        # *choix_V* updates
        if choix_V.status == NOT_STARTED and Stimuli_V.status==FINISHED:
            # keep track of start time/frame for later
            choix_V.frameNStart = frameN  # exact frame index
            choix_V.tStart = t  # local t and not account for scr refresh
            choix_V.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choix_V, 'tStartRefresh')  # time at next scr refresh
            choix_V.setAutoDraw(True)
        
        # *key_reponse_V* updates
        waitOnFlip = False
        if key_reponse_V.status == NOT_STARTED and Stimuli_V.status==FINISHED:
            # keep track of start time/frame for later
            key_reponse_V.frameNStart = frameN  # exact frame index
            key_reponse_V.tStart = t  # local t and not account for scr refresh
            key_reponse_V.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_reponse_V, 'tStartRefresh')  # time at next scr refresh
            key_reponse_V.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_reponse_V.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_reponse_V.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_reponse_V.status == STARTED and not waitOnFlip:
            theseKeys = key_reponse_V.getKeys(keyList=['end', 'pagedown', 'left', 'right', 'home', 'pageup'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_reponse_V.keys = theseKeys.name  # just the last key pressed
                key_reponse_V.rt = theseKeys.rt
                # was this 'correct'?
                if (key_reponse_V.keys == str(corrRV)) or (key_reponse_V.keys == corrRV):
                    key_reponse_V.corr = 1
                else:
                    key_reponse_V.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Condition_VComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Condition_V"-------
    for thisComponent in Condition_VComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    condition_V.addData('Stimuli_V.started', Stimuli_V.tStartRefresh)
    condition_V.addData('Stimuli_V.stopped', Stimuli_V.tStopRefresh)
    condition_V.addData('choix_V.started', choix_V.tStartRefresh)
    condition_V.addData('choix_V.stopped', choix_V.tStopRefresh)
    # check responses
    if key_reponse_V.keys in ['', [], None]:  # No response was made
        key_reponse_V.keys = None
        # was no response the correct answer?!
        if str(corrRV).lower() == 'none':
           key_reponse_V.corr = 1;  # correct non-response
        else:
           key_reponse_V.corr = 0;  # failed to respond (incorrectly)
    # store data for condition_V (TrialHandler)
    condition_V.addData('key_reponse_V.keys',key_reponse_V.keys)
    condition_V.addData('key_reponse_V.corr', key_reponse_V.corr)
    if key_reponse_V.keys != None:  # we had a response
        condition_V.addData('key_reponse_V.rt', key_reponse_V.rt)
    condition_V.addData('key_reponse_V.started', key_reponse_V.tStartRefresh)
    condition_V.addData('key_reponse_V.stopped', key_reponse_V.tStopRefresh)
    # the Routine "Condition_V" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'condition_V'


# ------Prepare to start Routine "Fin"-------
# update component parameters for each repeat
key_end.keys = []
key_end.rt = []
# keep track of which components have finished
FinComponents = [Remerciement, key_end]
for thisComponent in FinComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Fin"-------
while continueRoutine:
    # get current time
    t = FinClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Remerciement* updates
    if Remerciement.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Remerciement.frameNStart = frameN  # exact frame index
        Remerciement.tStart = t  # local t and not account for scr refresh
        Remerciement.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Remerciement, 'tStartRefresh')  # time at next scr refresh
        Remerciement.setAutoDraw(True)
    
    # *key_end* updates
    waitOnFlip = False
    if key_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_end.frameNStart = frameN  # exact frame index
        key_end.tStart = t  # local t and not account for scr refresh
        key_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_end, 'tStartRefresh')  # time at next scr refresh
        key_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_end.status == STARTED and not waitOnFlip:
        theseKeys = key_end.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_end.keys = theseKeys.name  # just the last key pressed
            key_end.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin"-------
for thisComponent in FinComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Remerciement.started', Remerciement.tStartRefresh)
thisExp.addData('Remerciement.stopped', Remerciement.tStopRefresh)
# check responses
if key_end.keys in ['', [], None]:  # No response was made
    key_end.keys = None
thisExp.addData('key_end.keys',key_end.keys)
if key_end.keys != None:  # we had a response
    thisExp.addData('key_end.rt', key_end.rt)
thisExp.addData('key_end.started', key_end.tStartRefresh)
thisExp.addData('key_end.stopped', key_end.tStopRefresh)
thisExp.nextEntry()
# the Routine "Fin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
