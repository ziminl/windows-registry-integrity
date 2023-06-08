






import winreg
def save_registry_to_txt(file_path):
    reg_key = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    root_key = winreg.OpenKey(reg_key, r"Software")
    with open(file_path, 'w') as file:
        traverse_registry(root_key, file)

def traverse_registry(key, file, indent=''):
    num_subkeys, num_values, _ = winreg.QueryInfoKey(key)
    file.write(f"{indent}[{winreg.EnumKey(key)}]\n")
    for i in range(num_subkeys):
        subkey_name = winreg.EnumKey(key, i)
        subkey = winreg.OpenKey(key, subkey_name)
        traverse_registry(subkey, file, indent + '  ')
    for i in range(num_values):
        value_name, value, value_type = winreg.EnumValue(key, i)
        file.write(f"{indent}{value_name} = {value} ({value_type})\n")
    winreg.CloseKey(key)
    
output_file = "r_dump.txt"
save_registry_to_txt(output_file)
print(f"Registry saved to {output_file}")




