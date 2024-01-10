1.  *** Get  interface/port information from a specific router: ***

    Command:
        show interfaces descriptions | except "\."

    Expected Output:
        Interface       Admin Link Description
        et-0/0/0        up    up   Uplink_From_32C_et-0/0/1
        et-0/0/1        up    up   Uplink_From_32C_et-1/0/1
        et-0/0/2        up    up   Uplink_From_32C_et-0/0/5
        et-0/0/3        up    up   Uplink_From_32C_et-1/0/5
        et-0/0/4        up    up   TO-IIG-NTTN-SW
        et-0/0/5        up    up   TO-ISP-NTTN-SW
        et-0/0/6        up    up   TO-Banani-Dist-SW
        et-0/0/7        up    up   TO-Mirpur-Zone-SW
        et-0/0/8        up    up   with_Uttara_Zonal_SW
        et-0/0/9        up    up   To-F@H-Upstream-SW*
        et-0/0/10       up    up   with_Uttara_Zonal_SW
        et-0/0/11       up    up   TO-Banani-Dist-SW-Temporary
        ge-0/0/1        up    up   **From-F@H-Upstream-SW****
        ae1             up    up   Uplink_From_32C
        ae2             up    up   TO-Mirpur-Zone-SW
        ae3             up    up   LACP-With-IIG-NTTN-SW_100G
        ae4             up    up   LACP-With-ISP-NTTN-SW_100G
        ae5             up    up   LACP_with_Uttara_Zonal_SW
        ae6             up    up   TO-Banani-Dist-SW
1.1 
2. *** VLAN Assign:***

    Command:
        set interfaces ge-0/0/1 vlan-tagging
        set interfaces ge-0/0/1 unit 551 description SSRM-Sec-IPT
        set interfaces ge-0/0/1 unit 551 vlan-id 551

    Notes:
        "set" command is used to assign/add any configuration.
        "ge-0/0/1" is the router connected interface with switch on which the client is connected physically.
        "unit 551" is subinterface of ge-0/0/1 for vlan 551.

3. *** VLAN Unassign/Delete: ***
    Command:
        delete interfaces ge-0/0/1 unit 551

    Notes:
        "delete" command is used to unassign/remove any configuration.
        "ge-0/0/1" is the router connected interface with switch on which the client is connected physically.
        "unit 551" is subinterface of ge-0/0/1 for vlan 551.
        ## If any vlan is removed then the interface should be assigned with new vlan but this will conflict with the unit ID. That's why 
        ## we need to remove the whole unit

4. *** P2P IP add for  IPv4 and IPv6: ***
    Command:
        set interfaces ge-0/0/1 unit 551 family inet address 10.1.17.73/30
        set interfaces ge-0/0/1 unit 551 family inet6 address fc00::10:1:17:73/127

        show | display set | match 551 
    Notes:
        ## IPs can be any subnet like /30, /29, /28 etc for IPv4 and /127, /126, /125 etc IPv6.
        ## So there should be option for that.

5. *** BW limit assignment (initial) ***
    Command:
        set firewall policer SSRM-Sec-IPT-BW if-exceeding bandwidth-limit 1000m
        set firewall policer SSRM-Sec-IPT-BW if-exceeding burst-size-limit 128k
        set firewall policer SSRM-Sec-IPT-BW then discard

    Notes:
        To assign bw, we need to make a firewall policy first then assign it on the interface/vlan level.

    Command:
        set interfaces ge-0/0/1 unit 551 family inet policer input SSRM-Sec-IPT-BW
        set interfaces ge-0/0/1 unit 551 family inet policer output SSRM-Sec-IPT-BW
    
    Notes:
        "SSRM-Sec-IPT-BW" is name of Bandwidth policer which we created earlier no applied on client connected interface/vlan.
        "bandwidth-limit" is maximum limit of assign bandwidth.

6. *** BW limit upgradation ***
    Command:
        set firewall policer SSRM-Sec-IPT-BW if-exceeding bandwidth-limit 1020m

    Notes:
        "Client bw is upgarded from 1000m to 1020m" 

7. *** BW limit downgradation ***
    Command:
        set firewall policer SSRM-Sec-IPT-BW if-exceeding bandwidth-limit 801m
    
    Notes:
        "Client bw is downgarded from 1020m to 800m" 

8. *** BW Buffering add ***
    Command:
        set firewall policer SSRM-Sec-IPT-BW if-exceeding bandwidth-limit 900m
    
    Notes:
        "Buffer 100m added with client actual bw for troubleshooting purpose" 

9. *** BW Buffering remove ***
    Command:
        set firewall policer SSRM-Sec-IPT-BW if-exceeding bandwidth-limit 800m
    
    Notes:
        "Buffer 100m removed and actual bw assigned" 

10. *** VLAN assignment shifting (During customer shifting occur from Switch to Router) ***
    Command:
        delete interfaces ge-0/0/1 unit 551
        set interfaces ae1 unit 551 description SSRM-Sec-IPT
        set interfaces ae1 unit 551 vlan-id 551
        set interfaces ae1 unit 551 family inet policer input SSRM-Sec-IPT-BW
        set interfaces ae1 unit 551 family inet policer output SSRM-Sec-IPT-BW
        set interfaces ae1 unit 551 family inet address 10.1.17.73/30
        set interfaces ae1 unit 551 family inet6 address fc00:10:1:17:73/127

    Notes:
        ## The steps of shifting or swaping vlan is first includes to delete the existing interface and then create
        a new interface. Above is the command that needed.
        ## This is not only needed for shifting client from switch to router, if client connected switch or POP change then this
        same configuration is needed.

11. *** While Changing NAS ***
    Command:
        On Current NAS:
            delete interfaces ge-0/0/1 unit 551
            delete firewall policer SSRM-Sec-IPT-BW

        On New NAS:
            set firewall policer SSRM-Sec-IPT-BW if-exceeding bandwidth-limit 1000m
            set firewall policer SSRM-Sec-IPT-BW if-exceeding burst-size-limit 128k
            set firewall policer SSRM-Sec-IPT-BW then discard

            set interfaces ae1 unit 551 description SSRM-Sec-IPT
            set interfaces ae1 unit 551 vlan-id 551
            set interfaces ae1 unit 551 family inet policer input SSRM-Sec-IPT-BW
            set interfaces ae1 unit 551 family inet policer output SSRM-Sec-IPT-BW
            set interfaces ae1 unit 551 family inet address 10.1.17.73/30
            set interfaces ae1 unit 551 family inet6 address fc00:10:1:17:73/127
    
    Notes:
        ## If the NAS changed then the "delete" command should run on the previous NAS for interface and firewall policer.
        ## Then the client should be configured as like before as discussed on steps 1 through 5.


*** Enable Rest api services ***

set system services rest control connection-limit 100
set system services rest http port 3000
set system services rest http addresses 10.172.16.4

#for https
set system services rest https port 3443
set system services rest https addresses 10.172.16.4
set system services rest https server-certificate testcert
set system services rest https cipher-list rsa-with-3des-ede-cbc-sha
set system services rest https mutual-authentication certificate-authority testca


#optional
set system services rest traceoptions flag all
set system services rest enable-explorer

commit and-quit

# for verifying

show configuration system services rest

*** Show all configuration ***
show | display set