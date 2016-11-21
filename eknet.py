class Eknet:
    data = {}

    # strings
    ip = ''
    netmask = ''
    dns = ''
    network_addr = ''
    broadcast_addr = ''
    default_gateway = ''

    def __init__(self, data):
        self.data = data
        self.netmask = data['netmask']
        self.ip = data['my_ip']
        self.dns = data['dns']
        self.default_gateway = data['gateway']
        self.network_addr = self.calc_network_addr(self.get_ip_bin(), self.get_subnet_bin())
        self.broadcast_addr = self.calc_broadcast_addr(self.get_ip_bin(), self.get_subnet_bin())
    # getters

    def get_ip_bin(self):
        return '.'.join(self.get_ip_bin_list())

    def get_subnet_bin(self):
        return '.'.join(self.get_subnet_bin_list())



    def get_subnet_bin_list(self):
        netmask = self.data['netmask'].split('.')
        netmask = ['{0:08b}'.format(int(octat)) for octat in netmask]
        return netmask

    def get_ip_bin_list(self):
        ip = self.data['my_ip'].split('.')
        ip = ['{0:08b}'.format(int(octat)) for octat in ip]
        return ip

    def mask_1s_count(self, bin_str):
        c = 0
        for bit in bin_str:
            if bit == '1':
                c += 1
            else:
                pass
        return c

    def calc_network_addr(self, ip, netmask):
        if type(ip) is list:
            ip = ''.join(ip)
        else:
            ip = ''.join(ip.split('.'))
        if type(netmask) is list:
            netmask = ''.join(netmask)
        else:
            netmask = ''.join(netmask.split('.'))

        network_bits = ip[:self.mask_1s_count(netmask)]  # str of bin reprenting network bits
        network_addr_str = network_bits + '0' * ( 32 - self.mask_1s_count(netmask))  # complete network address (concatenated with 0s)

        bin_net_addr = [network_addr_str[i:i + 8] for i in
                        range(0, len(network_addr_str), 8)]  # list of the octacts as binary representation

        ipv4_addr = self.bin_to_dec(bin_net_addr, 1)  # list of the octacts as integer representation

        return ipv4_addr

    # format: - 1 -> str
    #         - 0 -> list
    def bin_to_dec(self, binstr, str_format):

        if type(binstr) is str:
            binstr = binstr.split('.')
            if str_format:
                result = [str(int(octat, 2)) for octat in binstr]
                return '.'.join(result)
            else:
                return [int(octat, 2) for octat in binstr]
        elif type(binstr) is list:
            if str_format:
                result = [str(int(octat, 2)) for octat in binstr]
                return '.'.join(result)
            else:
                return [int(octat, 2) for octat in binstr]
        else:
            pass

    def dec_to_bin(self, decstr, str_format):
        if type(decstr) is str:
            decstr = decstr.split('.')
            if str_format:
                result = ['{0:08b}'.format(int(octat)) for octat in decstr]
                return '.'.join(result)
            else:
                return ['{0:08b}'.format(octat) for octat in decstr]
        elif type(decstr) is list:
            if str_format:
                result = ['{0:08b}'.format(octat) for octat in decstr]
                return '.'.join(result)
            else:
                return ['{0:08b}'.format(octat) for octat in decstr]
        else:
            pass


    def calc_broadcast_addr(self, ip, netmask):
        if type(ip) is list:
            ip = ''.join(ip)
        else:
            ip = ''.join(ip.split('.'))
        if type(netmask) is list:
            netmask = ''.join(netmask)
        else:
            netmask = ''.join(netmask.split('.'))

        network_bits = ip[:self.mask_1s_count(netmask)]  # str of bin reprenting network bits
        network_addr_str = network_bits + '1' * ( 32 - self.mask_1s_count(netmask))  # complete network address (concatenated with 0s)

        bin_net_addr = [network_addr_str[i:i + 8] for i in
                        range(0, len(network_addr_str), 8)]  # list of the octacts as binary representation

        ipv4_addr = [str(int(octat, 2)) for octat in bin_net_addr]  # list of the octacts as integer representation
        ipv4_addr_str = '.'.join(ipv4_addr)  # 1 string represting the ip address of broadcast

        return ipv4_addr_str



    def display_raw_data(self):
        print 'Current IP: \n', 'dec: ', self.ip , 'Bin: ', self.get_ip_bin()
        print '\nDefault Gateway: ', self.default_gateway
        print 'DNS server: ', self.dns
        print 'Subnet mask: ', self.netmask
        print 'Network IP: \n', 'dec: ', self.network_addr , '\nBin: ', self.dec_to_bin(self.network_addr, 1)
        print 'Broadcast IP', self.broadcast_addr
