import os
import sys
import time
import winreg as reg

# ANSI escape codes for text colors
CYAN = "\033[96m"
DARK_BLUE = "\033[34m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def spinning_jack_o_lantern_animation():
    frames = [
        """
        /}
      _,---~-LJ,-~-._
   ,-^  '   '   '    ^:,
  :   .    '      '     :
 :     /| .   /\\   '     :
:   . //|    // \\   '     :
:     `~` /| `^~`    '     ;
:  '     //|         '    :
:   \\-_  `~`    ,    '    :
;  . \\.\_,--,_;^/   ,    :
 :    ^-_!^!__/^   ,    :
  :,  ,  .        ,    :
    ^--_____     .   ;`
            `^''----`
        """,
        """
        /}
      _,---~-LJ,-~-._
   ,-^  '   '   '    ^:,
  :   .    '      '     :
 :     /| .   /\\   '     :
:   . //|    // \\   '     :
:     `~` /| `^~`    '     ;
:  '     //|         '    :
:   \\-_  `~`    ,    '    :
;  . \\.\_,--,_;^/   ,    :
 :    ^-_!^!__/^   ,    :
  :,  ,  .        ,    :
    ^--_____     .   ;`
            `^''----`
        """,
        """
        /}
      _,---~-LJ,-~-._
   ,-^  '   '   '    ^:,
  :   .    '      '     :
 :     /| .   /\\   '     :
:   . //|    // \\   '     :
:     `~` /| `^~`    '     ;
:  '     //|         '    :
:   \\-_  `~`    ,    '    :
;  . \\.\_,--,_;^/   ,    :
 :    ^-_!^!__/^   ,    :
  :,  ,  .        ,    :
    ^--_____     .   ;`
            `^''----`
        """
    ]

    loading_text = ["By Germanized Loading.  ", "By Germanized Loading.. ", "By Germanized Loading..."]
    start_time = time.time()
    end_time = start_time + 7  # Animation duration of 7 seconds
    while time.time() < end_time:
        # Determine the elapsed time and calculate the color gradient
        elapsed = time.time() - start_time
        if elapsed < 2.333:  # 1/3 of the way, fade from cyan to dark blue
            color = CYAN
        elif elapsed < 4.666:  # 2/3 of the way, fade from dark blue to cyan
            color = DARK_BLUE
        else:  # Fade out
            color = RESET
        
        for frame in frames:
            for text in loading_text:
                clear_screen()
                print(f"{color}{frame}{RESET}")
                print(f"{color}{text}{RESET}")
                time.sleep(0.3)
                if time.time() >= end_time:
                    break
            if time.time() >= end_time:
                break

def create_key(path, name, value, type=reg.REG_SZ):
    try:
        # Open the registry key
        key = reg.CreateKeyEx(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_SET_VALUE)
        # Set the registry value
        reg.SetValueEx(key, name, 0, type, value)
        # Close the registry key
        reg.CloseKey(key)
        print(f"{CYAN}Successfully created key: {path}\\{name}{RESET}")
    except PermissionError:
        print(f"{CYAN}Permission error: run the script as an administrator to modify registry keys.{RESET}")
    except Exception as e:
        print(f"{CYAN}Error creating key {path}\\{name}: {e}{RESET}")

def add_vm_keys():
    vm_registry_keys = [
        # VMware Keys
        (r"SYSTEM\CurrentControlSet\Services\Disk\Enum", "0", "VMware Virtual disk SCSI Disk Device", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\Disk\Enum", "1", "VBOX HARDDISK", reg.REG_SZ),
        (r"HARDWARE\ACPI\DSDT\VMWARE__\00000001", None, b"\x00\x00\x00\x00", reg.REG_BINARY),
        (r"HARDWARE\ACPI\FADT\VMWARE__\00000001", None, b"\x00\x00\x00\x00", reg.REG_BINARY),
        (r"HARDWARE\ACPI\RSDT\VMWARE__\00000001", None, b"\x00\x00\x00\x00", reg.REG_BINARY),
        (r"SOFTWARE\VMware, Inc.\VMware Tools", "InstallPath", "C:\\Program Files\\VMware\\VMware Tools\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\VMware Tools", "DisplayName", "VMware Tools", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\VMware Tools", "ImagePath", "C:\\Program Files\\VMware\\VMware Tools\\VMToolsSvc.exe", reg.REG_SZ),

        # VirtualBox Keys
        (r"SOFTWARE\Oracle\VirtualBox Guest Additions", "InstallDir", "C:\\Program Files\\Oracle\\VirtualBox Guest Additions\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\VBoxService", "DisplayName", "VBoxService", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\VBoxService", "ImagePath", "C:\\Program Files\\Oracle\\VirtualBox Guest Additions\\VBoxService.exe", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\VBoxGuest", "DisplayName", "VBoxGuest", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\VBoxGuest", "ImagePath", "C:\\Program Files\\Oracle\\VirtualBox Guest Additions\\VBoxGuest.sys", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\VBoxAdditions", "DisplayName", "VBoxAdditions", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\VBoxAdditions", "ImagePath", "C:\\Program Files\\Oracle\\VirtualBox Guest Additions\\VBoxAdditions.sys", reg.REG_SZ),
        (r"HARDWARE\ACPI\DSDT\VBOX__\00000001", None, b"\x00\x00\x00\x00", reg.REG_BINARY),
        (r"HARDWARE\ACPI\FADT\VBOX__\00000001", None, b"\x00\x00\x00\x00", reg.REG_BINARY),
        (r"HARDWARE\ACPI\RSDT\VBOX__\00000001", None, b"\x00\x00\x00\x00", reg.REG_BINARY),

        # Parallels Keys
        (r"SOFTWARE\Parallels\Parallels Tools", "InstallPath", "C:\\Program Files\\Parallels\\Parallels Tools\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\prl_service", "DisplayName", "Parallels Service", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\prl_service", "ImagePath", "C:\\Program Files\\Parallels\\Parallels Tools\\prl_service.exe", reg.REG_SZ),
        (r"HARDWARE\ACPI\DSDT\PARALLEL__\00000001", None, b"\x00\x00\x00\x00", reg.REG_BINARY),
        (r"HARDWARE\ACPI\FADT\PARALLEL__\00000001", None, b"\x00\x00\x00\x00", reg.REG_BINARY),
        (r"HARDWARE\ACPI\RSDT\PARALLEL__\00000001", None, b"\x00\x00\x00\x00", reg.REG_BINARY),

        # Microsoft Virtual Machine Additions Keys
        (r"SOFTWARE\Microsoft\Virtual Machine Additions", "InstallPath", "C:\\Program Files\\Microsoft Virtual Machine Additions\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\vmadditions", "DisplayName", "Microsoft Virtual Machine Additions", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\vmadditions", "ImagePath", "C:\\Program Files\\Microsoft Virtual Machine Additions\\vmadditions.sys", reg.REG_SZ),

        # Microsoft Virtual Machine Guest Keys
        (r"SOFTWARE\Microsoft\Virtual Machine\Guest", "InstallPath", "C:\\Program Files\\Microsoft Virtual Machine Guest\\", reg.REG_SZ),

        # Hyper-V Keys
        (r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Virtualization\Hyper-V", "InstallPath", "C:\\Program Files\\Hyper-V\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\Hyper-V-Guest-Integration-Service", "DisplayName", "Hyper-V Guest Integration Service", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\Hyper-V-Guest-Integration-Service", "ImagePath", "C:\\Windows\\System32\\vmmemctl.sys", reg.REG_SZ),

        # KVM Keys
        (r"SOFTWARE\KVM", "InstallDir", "C:\\Program Files\\KVM\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\kvm_service", "DisplayName", "KVM Service", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\kvm_service", "ImagePath", "C:\\Program Files\\KVM\\kvm_service.exe", reg.REG_SZ),

        # Citrix Keys
        (r"SOFTWARE\Citrix", "InstallDir", "C:\\Program Files\\Citrix\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\ctxsvc", "DisplayName", "Citrix Service", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\ctxsvc", "ImagePath", "C:\\Program Files\\Citrix\\ctxsvc.exe", reg.REG_SZ),

        # Cuckoo Sandbox Keys
        (r"SOFTWARE\Cuckoo Sandbox", "InstallDir", "C:\\Program Files\\Cuckoo Sandbox\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\CuckooSandbox", "DisplayName", "Cuckoo Sandbox Service", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\CuckooSandbox", "ImagePath", "C:\\Program Files\\Cuckoo Sandbox\\cuckoo_service.exe", reg.REG_SZ),

        # VirusTotal Keys
        (r"SOFTWARE\VirusTotal", "InstallPath", "C:\\Program Files\\VirusTotal\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\VirusTotal", "DisplayName", "VirusTotal Service", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\VirusTotal", "ImagePath", "C:\\Program Files\\VirusTotal\\virustotal_service.exe", reg.REG_SZ),

        # Hybrid Analysis Keys
        (r"SOFTWARE\Hybrid Analysis", "InstallPath", "C:\\Program Files\\Hybrid Analysis\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\HybridAnalysis", "DisplayName", "Hybrid Analysis Service", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\HybridAnalysis", "ImagePath", "C:\\Program Files\\Hybrid Analysis\\hybrid_analysis_service.exe", reg.REG_SZ),

        # Wireshark Keys
        (r"SOFTWARE\Wireshark", "InstallDir", "C:\\Program Files\\Wireshark\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\Wireshark", "DisplayName", "Wireshark", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\Wireshark", "ImagePath", "C:\\Program Files\\Wireshark\\wireshark.exe", reg.REG_SZ),

        # Ghidra Keys
        (r"SOFTWARE\Ghidra", "InstallPath", "C:\\Program Files\\Ghidra\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\Ghidra", "DisplayName", "Ghidra Service", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\Ghidra", "ImagePath", "C:\\Program Files\\Ghidra\\ghidra_service.exe", reg.REG_SZ),

        # Intezer Keys
        (r"SOFTWARE\Intezer", "InstallDir", "C:\\Program Files\\Intezer\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\Intezer", "DisplayName", "Intezer Service", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\Intezer", "ImagePath", "C:\\Program Files\\Intezer\\intezer_service.exe", reg.REG_SZ),

        # REMnux Keys
        (r"SOFTWARE\REMnux", "InstallDir", "C:\\Program Files\\REMnux\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\REMnux", "DisplayName", "REMnux Service", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\REMnux", "ImagePath", "C:\\Program Files\\REMnux\\remnux_service.exe", reg.REG_SZ),

        # Joe Security GmbH Keys
        (r"SOFTWARE\JoeSecurity", "InstallDir", "C:\\Program Files\\Joe Security GmbH\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\JoeSecurity", "DisplayName", "Joe Security Service", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\JoeSecurity", "ImagePath", "C:\\Program Files\\Joe Security GmbH\\joesecurity_service.exe", reg.REG_SZ),

        # Radare2 Keys
        (r"SOFTWARE\Radare2", "InstallDir", "C:\\Program Files\\Radare2\\", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\Radare2", "DisplayName", "Radare2 Service", reg.REG_SZ),
        (r"SYSTEM\CurrentControlSet\Services\Radare2", "ImagePath", "C:\\Program Files\\Radare2\\radare2_service.exe", reg.REG_SZ),
    ]

    for path, name, value, *rest in vm_registry_keys:
        type = reg.REG_SZ  # Default type
        if rest:
            type = rest[0]
        create_key(path, name, value, type)

def menu():
    clear_screen()
    print(f"{CYAN}Welcome to the VM Environment Emulator!{RESET}")
    print(f"{CYAN}This script will add VM-related registry keys to make your system look like a VM. By Germanized{RESET}\n")

    print("Choose an option:")
    print("1. Add VM registry keys")
    print("2. Exit")

    choice = input("\nEnter your choice: ")
    if choice == '1':
        spinning_jack_o_lantern_animation()
        add_vm_keys()
        print(f"{CYAN}All registry keys have been added successfully! Fuck Scarecrow Imade mine Open SRC{RESET}")
    elif choice == '2':
        sys.exit()
    else:
        print(f"{CYAN}Invalid choice. Please choose 1 or 2.{RESET}")

if __name__ == "__main__":
    menu()
