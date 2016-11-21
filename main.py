import subprocess
from eknet import Eknet



# short for ---> [function(number) for number in numbers if condition(number)]


data = {}
get_ip = 'ipconfig getifaddr en0'.split()
get_submask = 'ipconfig getoption en0 subnet_mask'.split()
get_dns = 'ipconfig getoption en0 domain_name_server'.split()
get_default_gateway = 'netstat -nr | grep default'.split()
flush_dns = 'dscacheutil -flushcache'.split()
def get_stats():
    data['my_ip'] = subprocess.check_output(get_ip)
    data['netmask'] = subprocess.check_output(get_submask)
    data['dns'] = subprocess.check_output(get_dns)
    data['gateway'] = subprocess.check_output(get_default_gateway).split()[11]
# print data


get_stats()
eknet = Eknet(data)



eknet.display_raw_data()



