import pyeapi


file = open('vlans.yml', 'r')
pyeapi.load_config('eapi.conf')
file_vlan_dict = yaml.safe_load(file)

pyeapi.load_config('eapi.conf')

connect = pyeapi.connect_to('leaf1')
raw_cmd_result = connect.enable('show vlan')

cmd_vlans_dict = raw_cmd_result[0]['result']['vlans']
print(cmd_vlans_dict)

for vlan in cmd_vlans_dict:
    print(cmd_vlans_dict[vlan]['name'])