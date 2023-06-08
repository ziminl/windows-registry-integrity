


import winreg
def check_registry_exists(registry_key, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return registry_key.lower() in content.lower()
registry_key_to_check = r"HKEY_CURRENT_USER\Software\Microsoft"
txt_file_path = "r_dump.txt"
if check_registry_exists(registry_key_to_check, txt_file_path):
    print(f"The registry key '{registry_key_to_check}' exists in the file.")
else:
    print(f"The registry key '{registry_key_to_check}' does not exist in the file.")
    
    
    
    
