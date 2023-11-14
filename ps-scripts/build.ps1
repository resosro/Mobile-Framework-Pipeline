
function Run-Appium{
    echo "${param.mobile_app}"
    echo "${env.PWD}"

    appium
    emulator -avd Pixel_4_API_30
}
function Run{
    Run-Appium
}


Run






