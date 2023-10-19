*** Settings ***
Library    AppiumLibrary

#[Setup Suite]    Open Application    http://localhost:4723/wd/hub    platformName=Android    platformVersion=Android 10    deviceName=emulator-5554    appPackage=de.eso.launcheraudi    appActivity=.ui.LauncherActivity

#[Suite Teardown]    Close Application
*** Test Cases ***
Testcase 1
    [Documentation]    Enabling Wi-fi in settings
    Log    Test1 started.
    Open Application    http://localhost:4723/wd/hub    platformName=Android    platformVersion=Android 10    deviceName=emulator-5554    appPackage=de.eso.launcheraudi    appActivity=.ui.LauncherActivity
    Click Element   xpath=//android.widget.LinearLayout//android.widget.TextView[@text='Settings']
    Wait Until Page Contains Element    xpath=//android.widget.RelativeLayout//android.widget.TextView[@text='Connection']    timeout=5    error=element not found
    Click Element   xpath=//android.widget.RelativeLayout//android.widget.TextView[@text='Connection']
    Wait Until Page Contains Element    xpath=//android.widget.RelativeLayout//android.widget.TextView[@text='Network & internet']    timeout=4    error=network button nai milra
    Click Element    xpath=//android.widget.RelativeLayout//android.widget.TextView[@text= 'Network & internet']
    #Click Element   id=android:id/widget_frame
    #Wait Until Page Contains Element    class=android.widget.LinearLayout    timeout=4    error=network button nai milra
    #Click Element    class=android.widget.LinearLayout
    Set Network Connection Status   connection Status=2
    Log    xpath element found.
    #Swipe By Percent    50    80    50    25    duration=2000
    #Close Application
    #Go Back
    #Log    application is closed

Testcase 2
    [Documentation]    Volume Control in settings
    Log    Test2 started.
    Open Application    http://localhost:4723/wd/hub    platformName=Android    platformVersion=Android 10    deviceName=emulator-5554    appPackage=de.eso.launcheraudi    appActivity=.ui.LauncherActivity
    Click Element   xpath=//android.widget.LinearLayout//android.widget.TextView[@text='Settings']
    #Swipe By Percent    50    80    50    25    duration=2000
    #Swipe By Percent    50    80    50    25    duration=2000
    #Swipe By Percent    50    80    50    25    duration=2000
    Wait Until Page Contains Element    xpath=//android.widget.RelativeLayout//android.widget.TextView[@text='Sound']    timeout=5    error=element not found
    Click Element   xpath=//android.widget.RelativeLayout//android.widget.TextView[@text='Sound']
    Click A Point    x=1172    y=754    duration=1500
    Click A Point    x=1378    y=293    duration=1000

Testcase 3
    [Documentation]    Browser
    Log    Test3 started.
    Open Application    http://localhost:4723/wd/hub    platformName=Android    platformVersion=Android 10    deviceName=emulator-5554    appPackage=de.eso.launcheraudi    appActivity=.ui.LauncherActivity
    Swipe By Percent    50    80    50    25    duration=1000
    Swipe By Percent    50    80    50    25    duration=1000
    Swipe By Percent    50    80    50    25    duration=1000
    Swipe By Percent    50    80    50    25    duration=1000
    Click Element   xpath=//android.widget.LinearLayout//android.widget.TextView[@text='WebView Browser Tester']
    Wait Until Page Contains Element    id=org.chromium.webview_shell:id/url_field    timeout=5    error=element not found
    Clear Text    id=org.chromium.webview_shell:id/url_field
    Input text    id=org.chromium.webview_shell:id/url_field    www.yahoo.com
    Click Element   accessibility_id=Load URL