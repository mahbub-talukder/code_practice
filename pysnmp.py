from pysnmp.hlapi import *
from pysnmp import hlapi  

def get_snmp_data(hostname, community, oid):
    # Create an SNMP GET Command Generator object
    g = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((hostname, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    error_indication, error_status, error_index, var_binds = next(g)

    if error_indication:
        print("Error: %s" % error_indication)
        return None
    elif error_status:
        print("Error: %s at %s" % (error_status.prettyPrint(), error_index and var_binds[int(error_index)-1][0] or "?"))
        return None
    else:
        for var_bind in var_binds:
            name, value = var_bind
            return str(value)

if __name__ == "__main__":
    # Replace these values with the appropriate ones for your device
    hostname = "103.161.68.200"
    community = "public"
    oid = "1.3.6.1.4.1.14988.1.1"  # Example OID for getting system description

    data = get_snmp_data(hostname, community, oid)
    if data:
        print("Device data:", data)
