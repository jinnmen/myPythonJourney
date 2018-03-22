#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import sys
import time
import datetime
import os
import ntpath
from subprocess import call, STDOUT, PIPE

##############SETTINGS###################
#settingFile defines the csv file used for list of hosts.
#   First line of the csv will be ignored.
#   colums and example are shown below
#   to make host part of specific maintenance add ○ to relevant column (maintenance day 1~3)
# <hostname>,<maitenance day 1>, <maitenance day 2>,<maitenance day 3>,<extensions list(separeted with ;)>
# wm0104.fonex.jp,○,,,1001;1002
#
#settingFile='./test.csv'
#settingFile='./input.csv'
settingFile='./output-real.csv'

password='......' # Used for fonex
#password='......' # Used for otts3/4
strategy = "....." # Ring startegy to be set
#strategy = "....."
username='.......' # Username used to login to freePBX
##############SETTINGS###################

def loginFreePBX(driver,host):
    print " Logging in on %s" % (host)
    driver.set_window_size(1200, 900) # Window size to something reasonable
    try:
        url = "http://"+host+"/admin/config.php?display=extensions"
        driver.get(url) # Load the page

        #driver.save_screenshot('login.png')　# Change sceenshot for debugging
        button = driver.find_element_by_id('login_admin') # Find the loginbutton element
        button.click()

        usernameElement = driver.find_elements_by_name('username') # Find the username input fields (visible and hidden)
        usernameElement[1].send_keys(username) # press the second element since the first one is not visible

        passwordElement = driver.find_elements_by_name('password') # Find the password input fields (visible and hidden)
        passwordElement[1].send_keys(password)  # press the second element since the first one is not visible

        send = driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/button[1]/span') # find the send button

        send.click() # Click it
        time.sleep(2) # just making sure the page has time to load, this probably could be removed.

        try:
            loginTest = driver.find_element_by_xpath("//a[@href='#custom_custom']") # Try finding element that exists on extension list page, to confirm that login was successfull
        except NoSuchElementException: # Print error if the element is not found
            print "     ERROR: Password or username wrong, check is password variable configured correctly."
            raise # Make sure that doesn't return True

        return True # return login OK

    except NoSuchElementException: # Error handling, screenshots, and return failed result
        print "     Failed to login check picture below."
        errorName = "error-"+host+".png"
        print "     Check %s for more details." % (errorName)
        driver.save_screenshot(errorName)
        return False
    except WebDriverException: # This triggers if the login page doesn't load properly
        print "     Failed to load freepBX front page, check host settings."
        errorName = "error-"+host+".png"
        print "     Check %s for more details." % (errorName)
        return False

def setNaisenRingStrategy(id,host, naisenList): # Function to set ring strategy to defined strategy on listed extensions
    driver = webdriver.Firefox() # Initialize the webdriver
    if loginFreePBX(driver,host): # Only execute code below if login was successfull
        for naisen in naisenList: # Loop through the extension list
            print "     Setting number %s to %s" % (naisen,strategy)
            url = "http://"+host+"/admin/config.php?display=extensions&extdisplay="+naisen
            driver.get(url) # Load the extension page for given host and extension

            try: # Make sure that the extension exists
                confirmNaisen = driver.find_element_by_id('devinfo_secret') # Look for element that only exists on extensions that exist
            except NoSuchElementException:
                print "         WARNING: Couldn't find extension, skipping"
                continue

            findmeFollow = driver.find_element_by_xpath("//a[@href='#findmefollow']") # Switch to Find me tab
            findmeFollow.click()

            dropdown = Select(driver.find_element_by_id('fmfm_strategy')) # Find the ringstrategy dropdown
            dropdown.select_by_visible_text(strategy) # Select the correct strategy

            submit = driver.find_element_by_id('submit') # Submit changes
            submit.click()

            time.sleep(1) # Wait to be sure

        print "     Applying settings on %s" % (host)

        applySettings = driver.find_element_by_id('button_reload')
        applySettings.click() # Apply in the end. This will crash if 0 extensions were changed

        time.sleep(1)

    driver.quit() # Make sure to close the browser

def combinePictures(screenshot1,screenshot2,nameCombined): # Combine 2 screenthos horizontaly
    call('montage ' + str(screenshot1) + ' ' + str(screenshot2) + '  -geometry +0+0 -tile 2x1 '+nameCombined, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE) # Call to imagemagic - montage and wait to finish

    os.remove(screenshot1) # remove the orginals only leave combined
    os.remove(screenshot2)

def getNaisenRingStrategy(id, host, naisenList): # confirm ringstrategy for given host and list of extensions
    driver = webdriver.Firefox() # Initialize the webdriver

    if loginFreePBX(driver,host): # Only continue if the login was successfull
        for naisen in naisenList: # Loop through the extensions
            print "     Taking screenshot number %s" % (naisen)
            url = "http://"+host+"/admin/config.php?display=extensions&extdisplay="+naisen
            driver.get(url) # Open the page

            try: # Confirm that the extensions exists
                confirmNaisen = driver.find_element_by_id('devinfo_secret') # Look for element that only exists on extensions that exist
            except NoSuchElementException: # If the extensions wasn't found throw an error
                print "         WARNING: Couldn't find extension, skipping"
                continue

            timeNow = datetime.datetime.now().strftime("%Y%m%d") # This is pretty much useless now that the date doesn't appear in the Combined filename
            folderPath = "./output/"+folder+"/"+str(i)+"-"+host+"/"+naisen+'-'+host # Build the folderpath
            screenshotName1 = folderPath+"-1-"+timeNow+".png" # Make the screenshot path 1
            screenshotName2 = folderPath+"-2-"+timeNow+".png" # Make the screenshot path 2
            screenshotNameCombined = folderPath+"-"+timeNow+".png" # Combined filepath

            createFolder(screenshotName1) # Make sure the folder exists
            driver.save_screenshot(screenshotName1) # Save screenshot 1

            findmeFollow = driver.find_element_by_xpath("//a[@href='#findmefollow']")
            findmeFollow.click() # Move to Find me tab

            driver.save_screenshot(screenshotName2) # Save screenshot 2

            combinePictures(screenshotName1,screenshotName2,screenshotNameCombined) # Combine sceeenshots 1 and 2

        screenshots = "./output/"+folder+"/"+str(i)+"-"+host+"/*.png" # Filepath for all screenshots of extensions
        call('convert ' +str(screenshots)+' -append '+os.path.dirname(screenshotName1)+"/all.png", shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE) # Make one huge png

    driver.quit() # Close the browser

def createFolder(path): # Function to make sure that the directory of the filepath exists
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

def setCertAndPorts(index,host): # Function to install fonexCertificate and change the portmap of RESTful Phone Apps to https 3443
    # Prepare names for the screenshots
    folderString = "./output/"+folder+"/"+str(i)+"-"+host
    screenshotName1 = folderString+"/cert-"+host+"-1.png"
    screenshotName2 = folderString+"/cert-"+host+"-2.png"
    outputName = folderString+"/cert-"+host+".png"

    driver = webdriver.Firefox() # Initialize the webdriver
    if loginFreePBX(driver,host): # Only proceed if login was successfull
        print "     Installing certificate and setting RESTful Phone Apps"
        url = "http://"+host+"/admin/config.php?display=sysadmin&view=ssl"
        driver.get(url) # Load the page
        try: # Confirm that the page loaded correctly, if it didn't it usually means that the admin module is not installed/activated
            settingsButton = driver.find_element_by_xpath("//a[@href='#manage']") # This only wroks if the admin module is properly installed
        except NoSuchElementException: # If not found print error, quit the browser and return false
            print "         WARNING: System Admin module is not activated, skipping"
            driver.quit()
            return False
        settingsButton.click() # Click the button if it was found


        dropdown = Select(driver.find_element_by_id('certid')) # Find the Dropdown menu
        try: # Try finding the fonexCertificate, this might fail if the certificate is not there or it is written in different manner
            dropdown.select_by_visible_text('fonexCertificate') # look for the prefined name
            time.sleep(1) # Wait to be sure

            certInstall = driver.find_element_by_id('caninstallcert') #Find the install button
            certInstall.click() # click the install button

            time.sleep(8) # Wait for the inslattion to be complete
        except NoSuchElementException: # Print error but keep going
            print "         WARNING: Couldn't find fonexCertificate, skipping"

        createFolder(screenshotName1)
        driver.save_screenshot(screenshotName1) # Screenshot of the installed certificate

        url = "http://"+host+"/admin/config.php?display=sysadmin&view=portmgmt"
        driver.get(url) # Open the port management page

        dropdown = Select(driver.find_element_by_id('select-sslrestapps')) # Find the dropdown for the RESTful Phone Apps (HTTPS)
        try: # Try finding the 3443 port, if not found certificate is most likely not installed properly
            dropdown.select_by_visible_text('Port 3443 (Default)') # Select https 3443
            submit = driver.find_element_by_id('updateports') # Find the update button
            submit.click() # Click it
            time.sleep(5) # Wait for bit
        except NoSuchElementException: # Print error but keep going
            print "         WARNING: Couldn't find https port 3443 settings, check certificate settings..."
        driver.save_screenshot(screenshotName2) # Take screenshot of the result

        combinePictures(screenshotName1,screenshotName2,outputName) # Combine the certificate and RESTful Phone Apps screenshots
    driver.quit() # Quit the browser

def selectMain(): # Select the maintenance date
    maintenance = raw_input("Select maintenance date 1/2/3 : ")
    accepted_strings = {'1', '2', '3'} # List of acceptable inputs
    if maintenance not in accepted_strings: # if not acceptable input, print error and exit
         print "Wrong input exiting...."
         raise SystemExit
    return maintenance # return the selection

def doHost(index,hostname,dateCheck,naisenList,whatDo): # Execute dry run or setCertAndPorts or setNaisenRingStrategy or getNaisenRingStrategy based on given input
    if dateCheck == "○": # Check if host is set for maintenance
        if whatDo == "dry": # In case of dryrun only print what would happen
            if len(hostArray[4]) != 0:  # Confirm that there are extensions configured
                print "%02d. Processing host %s, set/get following extensions： %s" % (index,hostname,naisenList)
            else: # No extensions configured for this host
                print "%02d. Processing host %s, only cert/port, no extensions defined" % (index,hostname)
        elif whatDo =="setCert": # Run certificate / portmap settings
            print "%02d. Setting cert and port on %s " % (index,hostname)
            setCertAndPorts(index,hostname) # install certificate and set ports
        elif len(hostArray[4]) != 0: # Only hosts that have extensions configured
            if whatDo =="setNaisen":
                print "%02d. Processing host %s, setting following extensions： %s" % (index,hostname,naisenList)
                setNaisenRingStrategy(index,hostname,naisenList) # set the ringstrategy for listed extensions
            elif whatDo =="getNaisen":
                print "%02d. Processing host %s, getting following extensions： %s" % (index,hostname,naisenList)
                getNaisenRingStrategy(index,hostname,naisenList) # get screenshot of configured ring strategys
        else: # No extensions configured, no need to do anything but print a message
            print "%02d. Skipping host %s , no extensions configured." % (i,hostArray[0])
    else: # Host wasn't configured with "○" on the chosen maintenance date, skipping
        print "%02d. Skipping host %s, no ○ set for this date." % (index,hostname)


with open(settingFile) as f: # Open file line by line to content
    content = f.readlines()

hosts = [x.strip() for x in content] # Remove extra whitepsace if any
del hosts[0] # Remove header infromation

folder = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") # Define foldername
i = 1

print "csv file used : %s" % (settingFile)
print "Hosts marked with ○ on selected column will be processed (will be asked next)"
print "What do you want to do? possible options are following."
print "     1. set extension ring strategy to %s" % (strategy)
print "     2. set certificate and port settings"
print "     3. get extension ring strategy"
print "     4. Run test run to see affected hosts and extensions"
print "     5. Print current schedule"
print "     *. or anything else to exit"
var = raw_input("Please enter 1/2/3/4/5 : ") # Ask user for input
if var == "1":
    do="setNaisen"
elif var == "2":
    do="setCert"
elif var == "3":
    do="getNaisen"
elif var == "4":
    do="dry"
elif var == "5":
    do="schedule"
else:
    print "Exiting..."
    raise SystemExit


if do == "schedule": # Print header for schedule
    print "-------------------------------------------------"
    print "host\t\t\t1\t2\t3"
    print "-------------------------------------------------"
else: # If not in schedule mode ask which maintenance is in question
    maintenance = selectMain()

for hostData in hosts: # Loop through hosts
    hostArray = hostData.split(",")  # Split single line of csv file to list
    naisenList = hostArray[4].split(";") # Split list of extensions to an list
    if do == "schedule":
        print "%s\t\t%s\t%s\t%s" % (hostArray[0],hostArray[1],hostArray[2],hostArray[3])
    elif maintenance == "1": # If maintennace 1 was selected run doHost and pass it host, 2nd column of csv, list of extensions and what to do
        doHost(i,hostArray[0],hostArray[1],naisenList,do)
    elif maintenance == "2": # If maintennace 2 was selected run doHost and pass it host, 3rd column of csv, list of extensions and what to do
        doHost(i,hostArray[0],hostArray[2],naisenList,do)
    elif maintenance == "3": # If maintennace 3 was selected run doHost and pass it host, 4th column of csv, list of extensions and what to do
        doHost(i,hostArray[0],hostArray[3],naisenList,do)

    i=i+1
if do == "schedule":
    print "-------------------------------------------------"
    print "----Only hosts with single ○ will be procesed----"
    print "-------------------------------------------------"
