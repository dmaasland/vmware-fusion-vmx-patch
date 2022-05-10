# VMware Fusion VMX optimizer

Makes VM's not suck on VMware Fusion

## Create alias

From project folder:

```bash
echo -e "\n# VMX Patch\nalias vmxpatch=\"$(which python3) $PWD/vmxpatch.py\"" >> ~/.bash_profile
source ~/.bash_profile
```

## Usage

Help

```
usage: vmxpatch.py [-h] [-t tweaks] <vm dir> [<vm dir> ...]

positional arguments:
  <vm dir>    Path to the virtual machine directory.

optional arguments:
  -h, --help  show this help message and exit
  -t tweaks   Path to .vmx file containing tweaks
```

Basic example

```bash
vmxpatch ~/Virtual\ Machines.localized/*
[INFO] Processing VMX /Users/donny/Virtual Machines.localized/Dev Ubuntu 20.04.vmwarevm/Dev Ubuntu 20.04.vmx
[INFO] Creating backup file /Users/donny/Virtual Machines.localized/Dev Ubuntu 20.04.vmwarevm/Dev Ubuntu 20.04.vmx.1652169442.backup
[INFO] Writing new vmx
[INFO] Processing VMX /Users/donny/Virtual Machines.localized/Docker Dev.vmwarevm/Docker Dev.vmx
[INFO] Creating backup file /Users/donny/Virtual Machines.localized/Docker Dev.vmwarevm/Docker Dev.vmx.1652169442.backup
[INFO] Writing new vmx
[INFO] Processing VMX /Users/donny/Virtual Machines.localized/ESET Nederland.vmwarevm/ESET Nederland.vmx
[INFO] Creating backup file /Users/donny/Virtual Machines.localized/ESET Nederland.vmwarevm/ESET Nederland.vmx.1652169442.backup
[CRITICAL] VMX file /Users/donny/Virtual Machines.localized/ESET Nederland.vmwarevm/ESET Nederland.vmx is encrypted, impossible to patch!
[INFO] Processing VMX /Users/donny/Virtual Machines.localized/Kali-Linux-2021.2-vmware-amd64.vmwarevm/Kali-Linux-2021.2-vmware-amd64.vmx
[INFO] Creating backup file /Users/donny/Virtual Machines.localized/Kali-Linux-2021.2-vmware-amd64.vmwarevm/Kali-Linux-2021.2-vmware-amd64.vmx.1652169442.backup
[INFO] Writing new vmx
[INFO] Processing VMX /Users/donny/Virtual Machines.localized/Kortana.vmwarevm/Kortana.vmx
[INFO] Creating backup file /Users/donny/Virtual Machines.localized/Kortana.vmwarevm/Kortana.vmx.1652169442.backup
[INFO] Writing new vmx
[INFO] Processing VMX /Users/donny/Virtual Machines.localized/WiFi AP.vmwarevm/WiFi AP.vmx
[INFO] Creating backup file /Users/donny/Virtual Machines.localized/WiFi AP.vmwarevm/WiFi AP.vmx.1652169442.backup
[INFO] Writing new vmx
```
