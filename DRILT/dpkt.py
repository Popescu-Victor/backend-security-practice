import dpkt
import socket
 
 
def build_packet():
    tcp = dpkt.tcp.TCP(
        sport=54321,
        dport=80,
        seq=1000,
        ack=0,
        flags=dpkt.tcp.TH_SYN,
        win=65535,
    )
 
    ip = dpkt.ip.IP(
        src=socket.inet_aton("192.168.1.10"),
        dst=socket.inet_aton("93.184.216.34"),  # example.com
        p=dpkt.ip.IP_PROTO_TCP,
    )
    ip.data = tcp
    ip.len = len(ip)
 
    eth = dpkt.ethernet.Ethernet(
        src=b"\x00\x0c\x29\x11\x22\x33",
        dst=b"\xff\xff\xff\xff\xff\xff",
        type=dpkt.ethernet.ETH_TYPE_IP,
    )
    eth.data = ip
 
    return bytes(eth)
 
 
def parse_packet(raw_bytes):
    eth = dpkt.ethernet.Ethernet(raw_bytes)
    print(f"Ethernet: src={eth.src.hex()} dst={eth.dst.hex()} type=0x{eth.type:04x}")
 
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        src_ip = socket.inet_ntoa(ip.src)
        dst_ip = socket.inet_ntoa(ip.dst)
        print(f"IP: {src_ip} -> {dst_ip}  proto={ip.p}")
 
        if isinstance(ip.data, dpkt.tcp.TCP):
            tcp = ip.data
            flags = []
            if tcp.flags & dpkt.tcp.TH_SYN:
                flags.append("SYN")
            if tcp.flags & dpkt.tcp.TH_ACK:
                flags.append("ACK")
            if tcp.flags & dpkt.tcp.TH_FIN:
                flags.append("FIN")
            print(f"TCP: sport={tcp.sport} dport={tcp.dport} flags={'/'.join(flags) or 'none'}")
 
 
if __name__ == "__main__":
    print("--- Building packet ---")
    raw = build_packet()
    print(f"Raw packet ({len(raw)} bytes): {raw.hex()}\n")
 
    print("--- Parsing packet ---")
    parse_packet(raw)
 
