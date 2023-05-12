### The Incentive Flanker Task Python version is created using PsychoPy3 on March 13, 2023
### by Serena J. Gu (RA at Columbia Center for Eating Disorders)
from ift_library import *
import ift_constants as c

def run():
    import os
    import re
    import csv
    import random
    import psychopy
    import numpy as np
    import pandas as pd
    from psychopy import visual, core, data, logging, gui
    from psychopy.hardware.emulator import launchScan

    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir)

    #########################Experiment Imformation########################
    psychopy.useVersion('2022.2.4')
    expName = 'IFT_2022'  # from the Builder filename that created this script
    expInfo = {'participant': '', 'TR': 1.000, 'volumes': 400, 'sync': 't',
        'startorder': ['Run1', 'Run2', 'Run3', 'Run4']}
    MR_settings = {'TR': expInfo['TR'], 'volumes': expInfo['volumes'], 'sync':expInfo['sync'], 'skip':0}
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName
    #print(f"#################################{expInfo}")

    #########################Saving Data File Info########################

    save_filename = f"{_thisDir}/data/{expInfo['participant']}_{expInfo['date']}_behav"
    save_output = f"{_thisDir}/data/{expInfo['participant']}_{expInfo['date']}_output"

    log_File = logging.LogFile(save_filename+'.log', level=logging.DEBUG)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    #########################Experiment Start########################
    win = visual.Window([1470,956],fullscr=True, winType='pyglet',
        monitor="testMonitor", units="height", color="#000000", colorSpace='hex',
        blendMode="avg")
    win.mouseVisible = False

    # lists = f"{_thisDir}/lists/{expInfo['startorder']}.xlsx"                
    # df = pd.read_excel(lists)

    showWelc(win)
    newInstruct(win, c.INST1_MRI, "space")
    newInstruct(win, c.INST2_MRI, "space")
    newInstruct(win, c.INST3, "space")
    showInstructCue(win, c.INST4, "stimuli/TUP.BMP", "25¢")
    newInstruct(win, c.INST5, "space")
    showInstructCue(win, c.INST6, "stimuli/NEUTRAL.BMP", "0¢")

    balance = 10.0
    number = int(expInfo['startorder'][-1])
    logfile = open(f"{save_filename}log.csv", "w", newline='')
    logger = csv.DictWriter(logfile, delimiter=',', fieldnames=["Trial", "Run", "Interference", "TrialCondition", 
            "Stim", "Target", "DollarString", "TrialOnset", "CueDuration", "Response", "RT", "Accuracy", "Earning", "Balance"])
    logger.writeheader()
    with open(f"{save_filename}.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=["Trial", "Run", "Interference", "TrialCondition", 
            "Stim", "Target", "DollarString", "Response", "RT", "Accuracy", "Earning", "Balance"])
        writer.writeheader()
        for step in range(4):
            current = ((step + number - 1) % 4) + 1
            lists = f"{_thisDir}/lists/Run{current}.xlsx"
            df = pd.read_excel(lists)
            newInstruct(win, f"Run{current} \n {c.INST_MRI % (balance,)}")
            newInstruct(win, c.START)
            money_gained = 0.0
            money_lost = 0.0
            incorrect = 0
            omission = 0
            n_trial = 1

            duration = expInfo['volumes'] * expInfo['TR']
            globalClock = core.Clock()
            vol = launchScan(win, MR_settings, globalClock=globalClock, wait_msg='loading...')
            event.waitKeys(keyList = ['t'])

            start_time = core.getTime()
            for i, row in df.iterrows():
                dollar = int(re.findall(r"(\d+)", row['DollarString'])[0])
                newCross(win, wait_time=row['FixDuration'])
                key, stim_onset, cue_duration = showCue(win, row['Path'], row['TxtDuration'], row['Stim'], row['DollarString'], zoom=1.5)
                csvrow = {
                    "Trial": n_trial,
                    "Run": f"Run{current}",
                    "Interference": row['CongIncong'],
                    "TrialCondition": row['Condition'],
                    "Stim": row['Stim'],
                    "Target": row['Target'],
                    "DollarString": row['DollarString'],
                    "Response": "None" if key is None else key[0][0],
                    "RT": "None" if key is None else key[1],
                    "Accuracy": "incorrect",
                    "Earning": dollar / 100.0
                }
                n_trial += 1
                if key is None or len(key) < 1:
                    showFeedback(win, color='red')
                    omission += 1
                    csvrow["Earning"] = 0.0
                elif key[0][0] != str(int(row['Answer'])):
                    showFeedback(win, color='red')
                    money_lost = money_lost - dollar / 100.0
                    incorrect += 1
                    csvrow["Earning"] = -dollar / 100.0
                else:
                    showFeedback(win, color='white')
                    money_gained = money_gained + dollar / 100.0
                    csvrow["Accuracy"] = "correct"
                csvrow["Balance"] = "%.2f" % (balance + money_gained + money_lost,)
                writer.writerow(csvrow)
                csvfile.flush()

                csvrow["TrialOnset"] = stim_onset - start_time
                csvrow["CueDuration"] = cue_duration

                logger.writerow(csvrow)
                logfile.flush()
                
            balance = balance + money_gained + money_lost
            result = c.RESULT%(f"Run{current}", len(df) - incorrect - omission, incorrect + omission, omission, incorrect, money_gained, money_lost, f"Run{current}", money_gained + money_lost, balance)
            end_of_block = newInstruct(win, result)
            win.flip()

    #cleanup
    logfile.close()
    win.close()
    core.quit()
