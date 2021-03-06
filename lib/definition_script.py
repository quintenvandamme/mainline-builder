from .definition import *
from .get_url import *

empty = ''
empty1 = ' '
wget = '      wget'
cd = '      cd'

line1=('#! /usr/bin/env bash')
line3=('KERNEL_VER="' + (KERNEL_VER_INPUT) + '"')
line3_1=('VER_STAND="' + (VER_STAND) + '"')
line4=('VER_STR="' + (VER_STR) + '"')
line6=('while [[ $# -gt 0 ]]; do')
line7=('  PROG_ARGS+=("${1}")')
line8=('  case "${1}" in')
line9=('    -amd|--amd64)')
line10=('      mkdir /tmp/ubuntukernel$KERNEL_VER')
line11=('      cd /tmp/ubuntukernel$KERNEL_VER')
line16=('      sudo dpkg -i *.deb')
line18=('      rm -r /tmp/ubuntukernel$KERNEL_VER')
line19=('      if [ -f "/boot/initrd.img-$KERNEL_VER-$VER_STR-generic" ] ')
line19_1=('      if [ -f "/boot/initrd.img-$VER_STAND-$VER_STR-generic" ] ')
line20=('      then')
line21=('          echo linux $KERNEL_VER is successfully installed!')
line22=('      else')
line23=('          echo an error occurred while installing')
line24=('      fi')
line25=('      break')
line26=('      ;;')
line27=('    -arm|--arm64)')
line38=('    -r|--remove)')
line39=('      echo only remove kernel if you have a newer one!')
line40=('      sleep 2')
line41=('      sudo apt remove linux-headers-$KERNEL_VER-$VER_STR')
line41_1=('      sudo apt remove linux-headers-$VER_STAND-$VER_STR')
line42=('      sudo apt remove linux-image-unsigned-$KERNEL_VER-$VER_STR-generic ')
line42_1=('      sudo apt remove linux-image-unsigned-$VER_STAND-$VER_STR-generic ')
line43=('      sudo apt remove linux-modules-$KERNEL_VER-$VER_STR-generic')
line43_1=('      sudo apt remove linux-modules-$VER_STAND-$VER_STR-generic')
line46=('          echo linux $KERNEL_VER is successfully removed!')
line48=('          echo an error occurred while removing linux $KERNEL_VER')
line52=('        esac')
line53=('done')

text1=('# linux ' + (KERNEL_VER_INPUT))
text3=('## amd64')
text5=('### install')
text6=('```bash')
text7=('cd /tmp/ && wget https://raw.githubusercontent.com/hexa-one/ubuntumainline/main/catalog/' + (KERNEL_VER_INPUT) +'/install.sh && chmod +x install.sh && sudo ./install.sh -amd')
text8=(text6).replace("bash", "")
text9=('### remove')
text11=(text7).replace("-amd", "-r")
text13=('## arm64')
text17=(text7).replace("-amd", "-arm")
text25=('kernel by [`https://kernel.ubuntu.com`](https://kernel.ubuntu.com/)')

from .get_url import main
main()

from .check_type import main as maintype
KERNEL_TYPE = maintype()
RC=("rc")
if KERNEL_TYPE == RC:
    wget1, wget2, wget3, wget4, wget5, wget6, wget7 = rc()
else: 
    wget1, wget2, wget3, wget4, wget5, wget6, wget7 = mainline()