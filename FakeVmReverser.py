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

def delete_key(path, name):
    try:
        # Open the registry key
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, path, 0, reg.KEY_SET_VALUE)
        if name is None:
            # Delete the entire key
            reg.DeleteKey(key, "")
        else:
            # Delete the registry value
            reg.DeleteValue(key, name)
        reg.CloseKey(key)
        print(f"{CYAN}Successfully deleted key/value: {path}\\{name if name else ''}{RESET}")
    except FileNotFoundError:
        print(f"{CYAN}Key/value not found: {path}\\{name if name else ''}{RESET}")
    except PermissionError:
        print(f"{CYAN}Permission error: run the script as an administrator to modify registry keys.{RESET}")
    except Exception as e:
        print(f"{CYAN}Error deleting key {path}\\{name if name else ''}: {e}{RESET}")

def remove_vm_keys():
    vm_registry_keys = [
        # VMware Keys
        (r"SYSTEM\CurrentControlSet\Services\Disk\Enum", "0"),
        (r"SYSTEM\CurrentControlSet\Services\Disk\Enum", "1"),
        (r"HARDWARE\ACPI\DSDT\VMWARE__\00000001", None),
        (r"HARDWARE\ACPI\FADT\VMWARE__\00000001", None),
        (r"HARDWARE\ACPI\RSDT\VMWARE__\00000001", None),
        (r"SOFTWARE\VMware, Inc.\VMware Tools", "InstallPath"),
        (r"SYSTEM\CurrentControlSet\Services\VMware Tools", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\VMware Tools", "ImagePath"),

        # VirtualBox Keys
        (r"SOFTWARE\Oracle\VirtualBox Guest Additions", "InstallDir"),
        (r"SYSTEM\CurrentControlSet\Services\VBoxService", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\VBoxService", "ImagePath"),
        (r"SYSTEM\CurrentControlSet\Services\VBoxGuest", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\VBoxGuest", "ImagePath"),
        (r"SYSTEM\CurrentControlSet\Services\VBoxAdditions", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\VBoxAdditions", "ImagePath"),
        (r"HARDWARE\ACPI\DSDT\VBOX__\00000001", None),
        (r"HARDWARE\ACPI\FADT\VBOX__\00000001", None),
        (r"HARDWARE\ACPI\RSDT\VBOX__\00000001", None),

        # Parallels Keys
        (r"SOFTWARE\Parallels\Parallels Tools", "InstallPath"),
        (r"SYSTEM\CurrentControlSet\Services\prl_service", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\prl_service", "ImagePath"),
        (r"HARDWARE\ACPI\DSDT\PARALLEL__\00000001", None),
        (r"HARDWARE\ACPI\FADT\PARALLEL__\00000001", None),
        (r"HARDWARE\ACPI\RSDT\PARALLEL__\00000001", None),

        # Microsoft Virtual Machine Additions Keys
        (r"SOFTWARE\Microsoft\Virtual Machine Additions", "InstallPath"),
        (r"SYSTEM\CurrentControlSet\Services\vmadditions", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\vmadditions", "ImagePath"),

        # Microsoft Virtual Machine Guest Keys
        (r"SOFTWARE\Microsoft\Virtual Machine\Guest", "InstallPath"),

        # Hyper-V Keys
        (r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Virtualization\Hyper-V", "InstallPath"),
        (r"SYSTEM\CurrentControlSet\Services\Hyper-V-Guest-Integration-Service", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\Hyper-V-Guest-Integration-Service", "ImagePath"),

        # KVM Keys
        (r"SOFTWARE\KVM", "InstallDir"),
        (r"SYSTEM\CurrentControlSet\Services\kvm_service", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\kvm_service", "ImagePath"),

        # Citrix Keys
        (r"SOFTWARE\Citrix", "InstallDir"),
        (r"SYSTEM\CurrentControlSet\Services\ctxsvc", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\ctxsvc", "ImagePath"),

        # Cuckoo Sandbox Keys
        (r"SOFTWARE\Cuckoo Sandbox", "InstallDir"),
        (r"SYSTEM\CurrentControlSet\Services\CuckooSandbox", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\CuckooSandbox", "ImagePath"),

        # VirusTotal Keys
        (r"SOFTWARE\VirusTotal", "InstallPath"),
        (r"SYSTEM\CurrentControlSet\Services\VirusTotal", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\VirusTotal", "ImagePath"),

        # Hybrid Analysis Keys
        (r"SOFTWARE\Hybrid Analysis", "InstallPath"),
        (r"SYSTEM\CurrentControlSet\Services\HybridAnalysis", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\HybridAnalysis", "ImagePath"),

        # Wireshark Keys
        (r"SOFTWARE\Wireshark", "InstallDir"),
        (r"SYSTEM\CurrentControlSet\Services\Wireshark", "DisplayName"),
        (r"SYSTEM\CurrentControlSet\Services\Wireshark", "ImagePath"),
    ]

    for path, name in vm_registry_keys:
        delete_key(path, name)

def main_menu():
    while True:
        clear_screen()
        print(f"{CYAN}Virtual Machine Environment Script - By Germanized{RESET}")
        print(f"{CYAN}1. Remove VM Registry Keys{RESET}")
        print(f"{CYAN}2. Exit{RESET}")

        choice = input(f"{CYAN}Enter your choice: {RESET}")

        if choice == "1":
            spinning_jack_o_lantern_animation()
            remove_vm_keys()
            input(f"{CYAN}Press Enter to return to the main menu...{RESET}")
        elif choice == "2":
            break
        else:
            print(f"{CYAN}Invalid choice. Please try again.{RESET}")
            time.sleep(2)

if __name__ == "__main__":
    main_menu()
