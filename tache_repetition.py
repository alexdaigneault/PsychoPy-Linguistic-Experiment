#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on October 31, 2019, at 16:01
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
expName = 'tache_repetition'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\daign\\Documents\\UQAM - Maitrise en linguistique\\Psycholinguistique\\Recherche\\tache_repetition.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files

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
    text="Vous entendrez des syllabes dans diverses conditions.\nVeuillez répéter les syllabes entendues.\nAppuyez sur la barre d'espacement lorsque vous êtes prêt.\n",
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
info_pratique = visual.TextStim(win=win, name='info_pratique',
    text='Veuillez répéter svp',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
info_next = visual.TextStim(win=win, name='info_next',
    text="Appuyez sur la barre d'espacement",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_next = keyboard.Keyboard()

# Initialize components for Routine "Explications_A"
Explications_AClock = core.Clock()
instruction_A = visual.TextStim(win=win, name='instruction_A',
    text="Dans la prochaine tâche, vous entendrez des syllabes dans le bruit.\nVeuillez répéter les syllabes entendues.\nAppuyez sur la barre d'espacement lorsque vous êtes prêt.",
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
info_A = visual.TextStim(win=win, name='info_A',
    text='Veuillez répéter svp',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
info_next_A = visual.TextStim(win=win, name='info_next_A',
    text="Appuyez sur la barre d'espacement",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_next_A = keyboard.Keyboard()

# Initialize components for Routine "Explications_AV"
Explications_AVClock = core.Clock()
instruction_AV = visual.TextStim(win=win, name='instruction_AV',
    text="Dans la prochaine tâche, vous visionnerez des vidéos.\nVous entendrez des syllabes dans le bruit.\nVeuillez répéter les syllabes.\nAppuyer sur la barre d'espacement lorsque vous êtes prêt.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_start_audiovisuel = keyboard.Keyboard()

# Initialize components for Routine "Condition_AV"
Condition_AVClock = core.Clock()
info_AV = visual.TextStim(win=win, name='info_AV',
    text='Veuillez répéter svp',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
info_next_AV = visual.TextStim(win=win, name='info_next_AV',
    text="Appuyez sur la barre d'espacement",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_next_AV = keyboard.Keyboard()

# Initialize components for Routine "Explications_AV"
Explications_AVClock = core.Clock()
instruction_AV = visual.TextStim(win=win, name='instruction_AV',
    text="Dans la prochaine tâche, vous visionnerez des vidéos.\nVous entendrez des syllabes dans le bruit.\nVeuillez répéter les syllabes.\nAppuyer sur la barre d'espacement lorsque vous êtes prêt.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_start_audiovisuel = keyboard.Keyboard()

# Initialize components for Routine "Condition_AVD"
Condition_AVDClock = core.Clock()
info_AVD = visual.TextStim(win=win, name='info_AVD',
    text='Veuillez répéter svp',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
info_next_AVD = visual.TextStim(win=win, name='info_next_AVD',
    text="Appuyez sur la barre d'espacement",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_next_AVD = keyboard.Keyboard()

# Initialize components for Routine "Explications_V"
Explications_VClock = core.Clock()
instruction_V = visual.TextStim(win=win, name='instruction_V',
    text="Dans la prochaine tâche, vous visionnerez des vidéos sans le son. \nVous devrez déduire les syllabes produites.\nVeuillez répéter les syllabes.\nAppuyer sur la barre d'espacement lorsque vous êtes prêt.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_start_visuel = keyboard.Keyboard()

# Initialize components for Routine "Condition_V"
Condition_VClock = core.Clock()
info_V = visual.TextStim(win=win, name='info_V',
    text='Veuillez répéter svp',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
info_next_V = visual.TextStim(win=win, name='info_next_V',
    text="Appuyez sur la barre d'espacement",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_next_V = keyboard.Keyboard()

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
    reponse_pratique = microphone.AdvAudioCapture(name='reponse_pratique', saveDir=wavDirName, stereo=True, chnl=0)
    key_next.keys = []
    key_next.rt = []
    # keep track of which components have finished
    PratiqueComponents = [pratique_audio, info_pratique, reponse_pratique, info_next, key_next]
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
        
        # *info_pratique* updates
        if info_pratique.status == NOT_STARTED and pratique_audio.status==FINISHED:
            # keep track of start time/frame for later
            info_pratique.frameNStart = frameN  # exact frame index
            info_pratique.tStart = t  # local t and not account for scr refresh
            info_pratique.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(info_pratique, 'tStartRefresh')  # time at next scr refresh
            info_pratique.setAutoDraw(True)
        if info_pratique.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > info_pratique.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                info_pratique.tStop = t  # not accounting for scr refresh
                info_pratique.frameNStop = frameN  # exact frame index
                win.timeOnFlip(info_pratique, 'tStopRefresh')  # time at next scr refresh
                info_pratique.setAutoDraw(False)
        
        # *reponse_pratique* updates
        if reponse_pratique.status == NOT_STARTED and info_pratique.status==STARTED:
            # keep track of start time/frame for later
            reponse_pratique.frameNStart = frameN  # exact frame index
            reponse_pratique.tStart = t  # local t and not account for scr refresh
            reponse_pratique.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reponse_pratique, 'tStartRefresh')  # time at next scr refresh
            reponse_pratique.status = STARTED
            reponse_pratique.record(sec=2, block=False)  # start the recording thread
        
        if reponse_pratique.status == STARTED and not reponse_pratique.recorder.running:
            reponse_pratique.status = FINISHED
        
        # *info_next* updates
        if info_next.status == NOT_STARTED and reponse_pratique.status==FINISHED:
            # keep track of start time/frame for later
            info_next.frameNStart = frameN  # exact frame index
            info_next.tStart = t  # local t and not account for scr refresh
            info_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(info_next, 'tStartRefresh')  # time at next scr refresh
            info_next.setAutoDraw(True)
        
        # *key_next* updates
        waitOnFlip = False
        if key_next.status == NOT_STARTED and info_next.status==STARTED:
            # keep track of start time/frame for later
            key_next.frameNStart = frameN  # exact frame index
            key_next.tStart = t  # local t and not account for scr refresh
            key_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next, 'tStartRefresh')  # time at next scr refresh
            key_next.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next.status == STARTED and not waitOnFlip:
            theseKeys = key_next.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_next.keys = theseKeys.name  # just the last key pressed
                key_next.rt = theseKeys.rt
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
    pratique_loop.addData('info_pratique.started', info_pratique.tStartRefresh)
    pratique_loop.addData('info_pratique.stopped', info_pratique.tStopRefresh)
    # reponse_pratique stop & responses
    reponse_pratique.stop()  # sometimes helpful
    if not reponse_pratique.savedFile:
        reponse_pratique.savedFile = None
    # store data for pratique_loop (TrialHandler)
    pratique_loop.addData('reponse_pratique.filename', reponse_pratique.savedFile)
    pratique_loop.addData('reponse_pratique.started', reponse_pratique.tStart)
    pratique_loop.addData('reponse_pratique.stopped', reponse_pratique.tStop)
    pratique_loop.addData('info_next.started', info_next.tStartRefresh)
    pratique_loop.addData('info_next.stopped', info_next.tStopRefresh)
    # check responses
    if key_next.keys in ['', [], None]:  # No response was made
        key_next.keys = None
    pratique_loop.addData('key_next.keys',key_next.keys)
    if key_next.keys != None:  # we had a response
        pratique_loop.addData('key_next.rt', key_next.rt)
    pratique_loop.addData('key_next.started', key_next.tStartRefresh)
    pratique_loop.addData('key_next.stopped', key_next.tStopRefresh)
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
    repeat_A = microphone.AdvAudioCapture(name='repeat_A', saveDir=wavDirName, stereo=True, chnl=0)
    key_next_A.keys = []
    key_next_A.rt = []
    # keep track of which components have finished
    Condition_AComponents = [Stimuli_Audio, info_A, repeat_A, info_next_A, key_next_A]
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
        
        # *info_A* updates
        if info_A.status == NOT_STARTED and Stimuli_Audio.status==FINISHED:
            # keep track of start time/frame for later
            info_A.frameNStart = frameN  # exact frame index
            info_A.tStart = t  # local t and not account for scr refresh
            info_A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(info_A, 'tStartRefresh')  # time at next scr refresh
            info_A.setAutoDraw(True)
        if info_A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > info_A.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                info_A.tStop = t  # not accounting for scr refresh
                info_A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(info_A, 'tStopRefresh')  # time at next scr refresh
                info_A.setAutoDraw(False)
        
        # *repeat_A* updates
        if repeat_A.status == NOT_STARTED and info_A.status==STARTED:
            # keep track of start time/frame for later
            repeat_A.frameNStart = frameN  # exact frame index
            repeat_A.tStart = t  # local t and not account for scr refresh
            repeat_A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repeat_A, 'tStartRefresh')  # time at next scr refresh
            repeat_A.status = STARTED
            repeat_A.record(sec=2, block=False)  # start the recording thread
        
        if repeat_A.status == STARTED and not repeat_A.recorder.running:
            repeat_A.status = FINISHED
        
        # *info_next_A* updates
        if info_next_A.status == NOT_STARTED and repeat_A.status==FINISHED:
            # keep track of start time/frame for later
            info_next_A.frameNStart = frameN  # exact frame index
            info_next_A.tStart = t  # local t and not account for scr refresh
            info_next_A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(info_next_A, 'tStartRefresh')  # time at next scr refresh
            info_next_A.setAutoDraw(True)
        
        # *key_next_A* updates
        waitOnFlip = False
        if key_next_A.status == NOT_STARTED and info_next_A.status==STARTED:
            # keep track of start time/frame for later
            key_next_A.frameNStart = frameN  # exact frame index
            key_next_A.tStart = t  # local t and not account for scr refresh
            key_next_A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next_A, 'tStartRefresh')  # time at next scr refresh
            key_next_A.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next_A.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next_A.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next_A.status == STARTED and not waitOnFlip:
            theseKeys = key_next_A.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_next_A.keys = theseKeys.name  # just the last key pressed
                key_next_A.rt = theseKeys.rt
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
    condition_A.addData('info_A.started', info_A.tStartRefresh)
    condition_A.addData('info_A.stopped', info_A.tStopRefresh)
    # repeat_A stop & responses
    repeat_A.stop()  # sometimes helpful
    if not repeat_A.savedFile:
        repeat_A.savedFile = None
    # store data for condition_A (TrialHandler)
    condition_A.addData('repeat_A.filename', repeat_A.savedFile)
    condition_A.addData('repeat_A.started', repeat_A.tStart)
    condition_A.addData('repeat_A.stopped', repeat_A.tStop)
    condition_A.addData('info_next_A.started', info_next_A.tStartRefresh)
    condition_A.addData('info_next_A.stopped', info_next_A.tStopRefresh)
    # check responses
    if key_next_A.keys in ['', [], None]:  # No response was made
        key_next_A.keys = None
    condition_A.addData('key_next_A.keys',key_next_A.keys)
    if key_next_A.keys != None:  # we had a response
        condition_A.addData('key_next_A.rt', key_next_A.rt)
    condition_A.addData('key_next_A.started', key_next_A.tStartRefresh)
    condition_A.addData('key_next_A.stopped', key_next_A.tStopRefresh)
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
    repeat_AV = microphone.AdvAudioCapture(name='repeat_AV', saveDir=wavDirName, stereo=True, chnl=0)
    key_next_AV.keys = []
    key_next_AV.rt = []
    # keep track of which components have finished
    Condition_AVComponents = [Stimuli_AV, info_AV, repeat_AV, info_next_AV, key_next_AV]
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
        
        # *info_AV* updates
        if info_AV.status == NOT_STARTED and Stimuli_AV.status==FINISHED:
            # keep track of start time/frame for later
            info_AV.frameNStart = frameN  # exact frame index
            info_AV.tStart = t  # local t and not account for scr refresh
            info_AV.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(info_AV, 'tStartRefresh')  # time at next scr refresh
            info_AV.setAutoDraw(True)
        if info_AV.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > info_AV.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                info_AV.tStop = t  # not accounting for scr refresh
                info_AV.frameNStop = frameN  # exact frame index
                win.timeOnFlip(info_AV, 'tStopRefresh')  # time at next scr refresh
                info_AV.setAutoDraw(False)
        
        # *repeat_AV* updates
        if repeat_AV.status == NOT_STARTED and info_AV.status==STARTED:
            # keep track of start time/frame for later
            repeat_AV.frameNStart = frameN  # exact frame index
            repeat_AV.tStart = t  # local t and not account for scr refresh
            repeat_AV.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repeat_AV, 'tStartRefresh')  # time at next scr refresh
            repeat_AV.status = STARTED
            repeat_AV.record(sec=2, block=False)  # start the recording thread
        
        if repeat_AV.status == STARTED and not repeat_AV.recorder.running:
            repeat_AV.status = FINISHED
        
        # *info_next_AV* updates
        if info_next_AV.status == NOT_STARTED and repeat_AV.status==FINISHED:
            # keep track of start time/frame for later
            info_next_AV.frameNStart = frameN  # exact frame index
            info_next_AV.tStart = t  # local t and not account for scr refresh
            info_next_AV.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(info_next_AV, 'tStartRefresh')  # time at next scr refresh
            info_next_AV.setAutoDraw(True)
        
        # *key_next_AV* updates
        waitOnFlip = False
        if key_next_AV.status == NOT_STARTED and info_next_AV.status==STARTED:
            # keep track of start time/frame for later
            key_next_AV.frameNStart = frameN  # exact frame index
            key_next_AV.tStart = t  # local t and not account for scr refresh
            key_next_AV.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next_AV, 'tStartRefresh')  # time at next scr refresh
            key_next_AV.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next_AV.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next_AV.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next_AV.status == STARTED and not waitOnFlip:
            theseKeys = key_next_AV.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_next_AV.keys = theseKeys.name  # just the last key pressed
                key_next_AV.rt = theseKeys.rt
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
    condition_AV.addData('info_AV.started', info_AV.tStartRefresh)
    condition_AV.addData('info_AV.stopped', info_AV.tStopRefresh)
    # repeat_AV stop & responses
    repeat_AV.stop()  # sometimes helpful
    if not repeat_AV.savedFile:
        repeat_AV.savedFile = None
    # store data for condition_AV (TrialHandler)
    condition_AV.addData('repeat_AV.filename', repeat_AV.savedFile)
    condition_AV.addData('repeat_AV.started', repeat_AV.tStart)
    condition_AV.addData('repeat_AV.stopped', repeat_AV.tStop)
    condition_AV.addData('info_next_AV.started', info_next_AV.tStartRefresh)
    condition_AV.addData('info_next_AV.stopped', info_next_AV.tStopRefresh)
    # check responses
    if key_next_AV.keys in ['', [], None]:  # No response was made
        key_next_AV.keys = None
    condition_AV.addData('key_next_AV.keys',key_next_AV.keys)
    if key_next_AV.keys != None:  # we had a response
        condition_AV.addData('key_next_AV.rt', key_next_AV.rt)
    condition_AV.addData('key_next_AV.started', key_next_AV.tStartRefresh)
    condition_AV.addData('key_next_AV.stopped', key_next_AV.tStopRefresh)
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
    repeat_AVD = microphone.AdvAudioCapture(name='repeat_AVD', saveDir=wavDirName, stereo=True, chnl=0)
    key_next_AVD.keys = []
    key_next_AVD.rt = []
    # keep track of which components have finished
    Condition_AVDComponents = [Stimuli_AVD, info_AVD, repeat_AVD, info_next_AVD, key_next_AVD]
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
        
        # *info_AVD* updates
        if info_AVD.status == NOT_STARTED and Stimuli_AVD.status==FINISHED:
            # keep track of start time/frame for later
            info_AVD.frameNStart = frameN  # exact frame index
            info_AVD.tStart = t  # local t and not account for scr refresh
            info_AVD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(info_AVD, 'tStartRefresh')  # time at next scr refresh
            info_AVD.setAutoDraw(True)
        if info_AVD.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > info_AVD.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                info_AVD.tStop = t  # not accounting for scr refresh
                info_AVD.frameNStop = frameN  # exact frame index
                win.timeOnFlip(info_AVD, 'tStopRefresh')  # time at next scr refresh
                info_AVD.setAutoDraw(False)
        
        # *repeat_AVD* updates
        if repeat_AVD.status == NOT_STARTED and info_AVD.status==STARTED:
            # keep track of start time/frame for later
            repeat_AVD.frameNStart = frameN  # exact frame index
            repeat_AVD.tStart = t  # local t and not account for scr refresh
            repeat_AVD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repeat_AVD, 'tStartRefresh')  # time at next scr refresh
            repeat_AVD.status = STARTED
            repeat_AVD.record(sec=2, block=False)  # start the recording thread
        
        if repeat_AVD.status == STARTED and not repeat_AVD.recorder.running:
            repeat_AVD.status = FINISHED
        
        # *info_next_AVD* updates
        if info_next_AVD.status == NOT_STARTED and repeat_AVD.status==FINISHED:
            # keep track of start time/frame for later
            info_next_AVD.frameNStart = frameN  # exact frame index
            info_next_AVD.tStart = t  # local t and not account for scr refresh
            info_next_AVD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(info_next_AVD, 'tStartRefresh')  # time at next scr refresh
            info_next_AVD.setAutoDraw(True)
        
        # *key_next_AVD* updates
        waitOnFlip = False
        if key_next_AVD.status == NOT_STARTED and info_next_AVD.status==STARTED:
            # keep track of start time/frame for later
            key_next_AVD.frameNStart = frameN  # exact frame index
            key_next_AVD.tStart = t  # local t and not account for scr refresh
            key_next_AVD.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next_AVD, 'tStartRefresh')  # time at next scr refresh
            key_next_AVD.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next_AVD.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next_AVD.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next_AVD.status == STARTED and not waitOnFlip:
            theseKeys = key_next_AVD.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_next_AVD.keys = theseKeys.name  # just the last key pressed
                key_next_AVD.rt = theseKeys.rt
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
    condition_AVD.addData('info_AVD.started', info_AVD.tStartRefresh)
    condition_AVD.addData('info_AVD.stopped', info_AVD.tStopRefresh)
    # repeat_AVD stop & responses
    repeat_AVD.stop()  # sometimes helpful
    if not repeat_AVD.savedFile:
        repeat_AVD.savedFile = None
    # store data for condition_AVD (TrialHandler)
    condition_AVD.addData('repeat_AVD.filename', repeat_AVD.savedFile)
    condition_AVD.addData('repeat_AVD.started', repeat_AVD.tStart)
    condition_AVD.addData('repeat_AVD.stopped', repeat_AVD.tStop)
    condition_AVD.addData('info_next_AVD.started', info_next_AVD.tStartRefresh)
    condition_AVD.addData('info_next_AVD.stopped', info_next_AVD.tStopRefresh)
    # check responses
    if key_next_AVD.keys in ['', [], None]:  # No response was made
        key_next_AVD.keys = None
    condition_AVD.addData('key_next_AVD.keys',key_next_AVD.keys)
    if key_next_AVD.keys != None:  # we had a response
        condition_AVD.addData('key_next_AVD.rt', key_next_AVD.rt)
    condition_AVD.addData('key_next_AVD.started', key_next_AVD.tStartRefresh)
    condition_AVD.addData('key_next_AVD.stopped', key_next_AVD.tStopRefresh)
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
    repeat_V = microphone.AdvAudioCapture(name='repeat_V', saveDir=wavDirName, stereo=True, chnl=0)
    key_next_V.keys = []
    key_next_V.rt = []
    # keep track of which components have finished
    Condition_VComponents = [Stimuli_V, info_V, repeat_V, info_next_V, key_next_V]
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
        
        # *info_V* updates
        if info_V.status == NOT_STARTED and Stimuli_V.status==FINISHED:
            # keep track of start time/frame for later
            info_V.frameNStart = frameN  # exact frame index
            info_V.tStart = t  # local t and not account for scr refresh
            info_V.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(info_V, 'tStartRefresh')  # time at next scr refresh
            info_V.setAutoDraw(True)
        if info_V.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > info_V.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                info_V.tStop = t  # not accounting for scr refresh
                info_V.frameNStop = frameN  # exact frame index
                win.timeOnFlip(info_V, 'tStopRefresh')  # time at next scr refresh
                info_V.setAutoDraw(False)
        
        # *repeat_V* updates
        if repeat_V.status == NOT_STARTED and info_V.status==STARTED:
            # keep track of start time/frame for later
            repeat_V.frameNStart = frameN  # exact frame index
            repeat_V.tStart = t  # local t and not account for scr refresh
            repeat_V.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repeat_V, 'tStartRefresh')  # time at next scr refresh
            repeat_V.status = STARTED
            repeat_V.record(sec=2, block=False)  # start the recording thread
        
        if repeat_V.status == STARTED and not repeat_V.recorder.running:
            repeat_V.status = FINISHED
        
        # *info_next_V* updates
        if info_next_V.status == NOT_STARTED and repeat_V.status==FINISHED:
            # keep track of start time/frame for later
            info_next_V.frameNStart = frameN  # exact frame index
            info_next_V.tStart = t  # local t and not account for scr refresh
            info_next_V.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(info_next_V, 'tStartRefresh')  # time at next scr refresh
            info_next_V.setAutoDraw(True)
        
        # *key_next_V* updates
        waitOnFlip = False
        if key_next_V.status == NOT_STARTED and info_next_V.status==STARTED:
            # keep track of start time/frame for later
            key_next_V.frameNStart = frameN  # exact frame index
            key_next_V.tStart = t  # local t and not account for scr refresh
            key_next_V.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_next_V, 'tStartRefresh')  # time at next scr refresh
            key_next_V.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_next_V.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_next_V.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_next_V.status == STARTED and not waitOnFlip:
            theseKeys = key_next_V.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_next_V.keys = theseKeys.name  # just the last key pressed
                key_next_V.rt = theseKeys.rt
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
    condition_V.addData('info_V.started', info_V.tStartRefresh)
    condition_V.addData('info_V.stopped', info_V.tStopRefresh)
    # repeat_V stop & responses
    repeat_V.stop()  # sometimes helpful
    if not repeat_V.savedFile:
        repeat_V.savedFile = None
    # store data for condition_V (TrialHandler)
    condition_V.addData('repeat_V.filename', repeat_V.savedFile)
    condition_V.addData('repeat_V.started', repeat_V.tStart)
    condition_V.addData('repeat_V.stopped', repeat_V.tStop)
    condition_V.addData('info_next_V.started', info_next_V.tStartRefresh)
    condition_V.addData('info_next_V.stopped', info_next_V.tStopRefresh)
    # check responses
    if key_next_V.keys in ['', [], None]:  # No response was made
        key_next_V.keys = None
    condition_V.addData('key_next_V.keys',key_next_V.keys)
    if key_next_V.keys != None:  # we had a response
        condition_V.addData('key_next_V.rt', key_next_V.rt)
    condition_V.addData('key_next_V.started', key_next_V.tStartRefresh)
    condition_V.addData('key_next_V.stopped', key_next_V.tStopRefresh)
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
