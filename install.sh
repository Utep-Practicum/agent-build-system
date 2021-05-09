#!/bin/bash
set -e


#Colors for added pizazz
RED='\033[0;31m'
BLUE='\033[0;36m'
GRN='\033[0;32m'
NC='\033[0m'

ABS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

OUTPUT_PREFIX="AGENT BUILD SYSTEM INSTALLER:"
OUTPUT_ERROR_PREFIX="$OUTPUT_PREFIX ERROR:"

### Helper functions
#
prompt_accepted_Yn() {
    read -r -p "$1 [Y/n] " yn
    case $yn in
        [nN]*) return 1 ;;
        *) return 0 ;;
    esac
}

#Install platform specific dependencies
PYTHON_EXEC="python3"
OS_VERSION="UNKNOWN"


###################### Check Kali Versions  #############################
if lsb_release -d | grep -iq 'kali'; then
    if lsb_release -r | grep -q '2020'; then
        OS_VERSION="kali_2020"
        echo -e "${GRN}Nice choice in Operating Systems! ;)${NC}"
        #works out of the box
    fi
    if lsb_release -r | grep -q '2019.2'; then
        OS_VERSION="kali_2019.2"
        echo -e "${RED}Kali 2019 has not been tested thoroughly and may not work out of the box.${NC}"
        echo -e "${RED}Use at your own risk, please do not revert our practicum team's grades if you are reading this note${NC}"
    fi
fi

if echo $OS_VERSION | grep -q "UNKNOWN"; then
    echo -e "${RED}This version of Linux is currently not supported. ${NC}"
    echo -e "${RED}Currently Supported: Kali_2020 ${NC}"
    exit 1
fi

# Updates
#echo "Running apt-get update"
#apt-get -y update
#echo "Running apt-get upgrade"
#apt-get upgrade

### Check if running as root
#
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}$OUTPUT_ERROR_PREFIX Please run this installation as root${NC}"
    exit 1
fi

### Install dependencies

#Removed python3-venv, virtualbox 5/6/21 -seb
REQUIRED_PROGRAMS="python3-pip gimp"
REQUIRED_PYTHON_PACKAGES="PyQt5 python-dateutil pyautogui opencv-python numpy opencv-python-headless" #Eventually add virtualbox

#Installs python3 and venv
echo -e "${GRN} $OUTPUT_PREFIX Installing Additional Dependencies ${NC}"
if [ -x "/usr/bin/apt-get" ]; then
    OS_VERSION="Debian"
    apt-get -y install $REQUIRED_PROGRAMS
else
    echo -e "${RED} $OUTPUT_ERROR_PREFIX Distribution not supported ${NC}"
    exit 1
fi


######might need to instantiate a venv enviornment in order to get vboxapi to work#######
### Create virtualenv if it doesn't currently exist
echo -e "${GRN} $OUTPUT_PREFIX Installing python dependencies ${NC}"
if [ ! -d "venv" ]; then
    $PYTHON_EXEC -m venv venv
fi

#source venv/bin/activate
pip install pip --upgrade
pip install $REQUIRED_PYTHON_PACKAGES

### Creating executable
#
echo -e "${BLUE} $OUTPUT_PREFIX Creating executables ${NC}"
cat > "$ABS_DIR"/Agent-Build-System <<-'EOFagent-build-system'
#!/bin/bash
prompt_accepted_Yn() {
    read -r -p "$1 [Y/n] " yn
    case $yn in
        [nN]*) return 1 ;;
        *) return 0 ;;
    esac
}
ABS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
if [ "$EUID" -ne 0 ]; then
	echo -e "${GRN} The Agent-Build-System must be run as root ${NC}"
	exit 1
fi
cd "$ABS_DIR"

#venv/bin/python3 GUI_manager.py #DOESNT WORK BECAUSE THE VENV DOESNT HAVE PYQT
python3 GUI_manager.py $1 $2
EOFagent-build-system

chmod +x "$ABS_DIR"/Agent-Build-System
echo
echo "***************************************************"
echo -e "${GRN} $OUTPUT_PREFIX Installation Complete ${NC}"
echo 
echo "To run the Agent-Build-System, invoke:"
echo "sudo ./agent-build-system "
echo
echo "To Run a specific component of the Agent-Build-System, invoke:"
echo "sudo ./agent-build-system component-name"