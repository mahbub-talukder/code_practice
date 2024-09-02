set version 20.4R3.8
set system root-authentication encrypted-password "$6$SOBgtUEn$yD4OCooO2TMb9tffkpl21dq5lSinEkWsDUw/3XSvfUwur00Wfpy018WsIqsNagTagrcqWZRz4fVHOh8eLS0b61"
set system login user devops uid 2000
set system login user devops class super-user
set system login user devops authentication encrypted-password "$6$HSGT5eR7$YmXgH4wARz8UO8a8pRZYvRcneZCjMkpYFP5o2voOZaY7CV4das9Nv8pMOw9oZ6WV28.k3JjJbGo6.dQmj2y291"
set system services ssh port 4545
set system syslog file messages any notice
set system syslog file messages authorization info
set system syslog file interactive-commands interactive-commands any
set system processes dhcp-service traceoptions file dhcp_logfile
set system processes dhcp-service traceoptions file size 10m
set system processes dhcp-service traceoptions level all
set system processes dhcp-service traceoptions flag packet
set logical-systems BDIX-RT
set logical-systems FNA-RT interfaces ge-0/0/6 unit 1009 description STT24040002_Zelda-Labadie_PNI-2
set logical-systems FNA-RT interfaces ge-0/0/6 unit 1009 vlan-id 1009
set logical-systems FNA-RT interfaces ge-0/0/6 unit 1009 family inet policer input STT24040002_Zelda-Labadie_PNI-2
set logical-systems FNA-RT interfaces ge-0/0/6 unit 1009 family inet policer output STT24040002_Zelda-Labadie_PNI-2
set logical-systems FNA-RT interfaces ge-0/0/6 unit 1009 family inet address 10.10.25.14/30
set logical-systems FNA-RT firewall policer STT24040002_Zelda-Labadie_PNI-2 if-exceeding bandwidth-limit 150m
set logical-systems FNA-RT firewall policer STT24040002_Zelda-Labadie_PNI-2 if-exceeding burst-size-limit 1m
set logical-systems FNA-RT firewall policer STT24040002_Zelda-Labadie_PNI-2 then discard
set logical-systems GGC-RT interfaces ge-0/0/2 unit 1007 description STT24040002_Zelda-Labadie_BDIX
set logical-systems GGC-RT interfaces ge-0/0/2 unit 1007 vlan-id 1007
set logical-systems GGC-RT interfaces ge-0/0/2 unit 1007 family inet policer input STT24040002_Zelda-Labadie_BDIX
set logical-systems GGC-RT interfaces ge-0/0/2 unit 1007 family inet policer output STT24040002_Zelda-Labadie_BDIX
set logical-systems GGC-RT interfaces ge-0/0/2 unit 1007 family inet address 10.12.25.14/30
set logical-systems GGC-RT interfaces ge-0/0/6 unit 137 description STT24070001_Ariann_Ullrich_Bowie_IIG_1st
set logical-systems GGC-RT interfaces ge-0/0/6 unit 137 vlan-id 137
set logical-systems GGC-RT interfaces ge-0/0/6 unit 137 family inet policer input STT24070001_Ariann_Ullrich_Bowie_IIG_1st
set logical-systems GGC-RT interfaces ge-0/0/6 unit 137 family inet policer output STT24070001_Ariann_Ullrich_Bowie_IIG_1st
set logical-systems GGC-RT interfaces ge-0/0/6 unit 137 family inet address 10.17.19.90/30
set logical-systems GGC-RT interfaces ge-0/0/7 unit 1023 description STT24040002_Zelda-Labadie_PNI-2
set logical-systems GGC-RT interfaces ge-0/0/7 unit 1023 vlan-id 1023
set logical-systems GGC-RT interfaces ge-0/0/7 unit 1023 family inet policer input STT24040002_Zelda-Labadie_PNI-2
set logical-systems GGC-RT interfaces ge-0/0/7 unit 1023 family inet policer output STT24040002_Zelda-Labadie_PNI-2
set logical-systems GGC-RT interfaces ge-0/0/7 unit 1023 family inet address 10.10.25.14/30
set logical-systems GGC-RT interfaces ge-0/0/7 unit 1024 description STT24040002_Zelda-Labadie_IPT
set logical-systems GGC-RT interfaces ge-0/0/7 unit 1024 vlan-id 1024
set logical-systems GGC-RT interfaces ge-0/0/7 unit 1024 family inet policer input STT24040002_Zelda-Labadie_IPT
set logical-systems GGC-RT interfaces ge-0/0/7 unit 1024 family inet policer output STT24040002_Zelda-Labadie_IPT
set logical-systems GGC-RT interfaces ge-0/0/7 unit 1024 family inet address 10.11.25.14/30
set logical-systems GGC-RT firewall policer STT24040002_Zelda-Labadie_BDIX if-exceeding bandwidth-limit 152m
set logical-systems GGC-RT firewall policer STT24040002_Zelda-Labadie_BDIX if-exceeding burst-size-limit 1m
set logical-systems GGC-RT firewall policer STT24040002_Zelda-Labadie_BDIX then discard
set logical-systems GGC-RT firewall policer STT24040002_Zelda-Labadie_IPT if-exceeding bandwidth-limit 165m
set logical-systems GGC-RT firewall policer STT24040002_Zelda-Labadie_IPT if-exceeding burst-size-limit 1m
set logical-systems GGC-RT firewall policer STT24040002_Zelda-Labadie_IPT then discard
set logical-systems GGC-RT firewall policer STT24040002_Zelda-Labadie_PNI-2 if-exceeding bandwidth-limit 150m
set logical-systems GGC-RT firewall policer STT24040002_Zelda-Labadie_PNI-2 if-exceeding burst-size-limit 1m
set logical-systems GGC-RT firewall policer STT24040002_Zelda-Labadie_PNI-2 then discard
set logical-systems GGC-RT firewall policer STT24070001_Ariann_Ullrich_Bowie_IIG_1st if-exceeding bandwidth-limit 100m
set logical-systems GGC-RT firewall policer STT24070001_Ariann_Ullrich_Bowie_IIG_1st if-exceeding burst-size-limit 1m
set logical-systems GGC-RT firewall policer STT24070001_Ariann_Ullrich_Bowie_IIG_1st then discard
set logical-systems IIG-RT interfaces ge-0/0/3 unit 201 description STT24060013_Ebony-Rohan_IIG
set logical-systems IIG-RT interfaces ge-0/0/3 unit 201 vlan-id 201
set logical-systems IIG-RT interfaces ge-0/0/3 unit 201 family inet policer input STT24060013_Ebony-Rohan_IIG
set logical-systems IIG-RT interfaces ge-0/0/3 unit 201 family inet policer output STT24060013_Ebony-Rohan_IIG
set logical-systems IIG-RT interfaces ge-0/0/3 unit 201 family inet address 10.50.201.201/32
set logical-systems IIG-RT firewall policer STT24060013_Ebony-Rohan_IIG if-exceeding bandwidth-limit 100m
set logical-systems IIG-RT firewall policer STT24060013_Ebony-Rohan_IIG if-exceeding burst-size-limit 1m
set logical-systems IIG-RT firewall policer STT24060013_Ebony-Rohan_IIG then discard
set logical-systems IPT-RT              
set logical-systems PNI-RT interfaces ge-0/0/7 unit 149 description STT24070001_Ariann_Ullrich_Bowie_PNI_2nd
set logical-systems PNI-RT interfaces ge-0/0/7 unit 149 vlan-id 149
set logical-systems PNI-RT interfaces ge-0/0/7 unit 149 family inet policer input STT24070001_Ariann_Ullrich_Bowie_PNI_2nd
set logical-systems PNI-RT interfaces ge-0/0/7 unit 149 family inet policer output STT24070001_Ariann_Ullrich_Bowie_PNI_2nd
set logical-systems PNI-RT interfaces ge-0/0/7 unit 149 family inet address 10.18.19.65/30
set logical-systems PNI-RT firewall policer STT24070001_Ariann_Ullrich_Bowie_PNI_2nd if-exceeding bandwidth-limit 100m
set logical-systems PNI-RT firewall policer STT24070001_Ariann_Ullrich_Bowie_PNI_2nd if-exceeding burst-size-limit 1m
set logical-systems PNI-RT firewall policer STT24070001_Ariann_Ullrich_Bowie_PNI_2nd then discard
set interfaces ge-0/0/0 description uplink
set interfaces ge-0/0/0 unit 0 family inet address 103.134.26.214/30
set interfaces ge-0/0/1 description int-01
set interfaces ge-0/0/1 vlan-tagging    
set interfaces ge-0/0/1 unit 4 vlan-id 25
set interfaces ge-0/0/1 unit 11 description STT24040002_Zelda-Labadie_IPT
set interfaces ge-0/0/1 unit 11 vlan-id 11
set interfaces ge-0/0/1 unit 11 family inet policer input STT24040002_Zelda-Labadie_IPT
set interfaces ge-0/0/1 unit 11 family inet policer output STT24040002_Zelda-Labadie_IPT
set interfaces ge-0/0/1 unit 11 family inet address 10.1.1.105/30
set interfaces ge-0/0/1 unit 635 vlan-id 635
set interfaces ge-0/0/2 description int-2
set interfaces ge-0/0/2 vlan-tagging    
set interfaces ge-0/0/3 description int-3
set interfaces ge-0/0/3 vlan-tagging    
set interfaces ge-0/0/3 unit 11 description STT24040002_Zelda-Labadie_IPT
set interfaces ge-0/0/3 unit 11 vlan-id 11
set interfaces ge-0/0/3 unit 11 family inet policer input STT24040002_Zelda-Labadie_IPT
set interfaces ge-0/0/3 unit 11 family inet policer output STT24040002_Zelda-Labadie_IPT
set interfaces ge-0/0/3 unit 11 family inet address 10.1.1.11/32
set interfaces ge-0/0/3 unit 11 family inet address 10.1.1.23/31
set interfaces ge-0/0/3 unit 155 description SNL24050001_Keeley-Weissnat_GGC
set interfaces ge-0/0/3 unit 155 vlan-id 155
set interfaces ge-0/0/3 unit 155 family inet policer input SNL24050001_Keeley-Weissnat_GGC
set interfaces ge-0/0/3 unit 155 family inet policer output SNL24050001_Keeley-Weissnat_GGC
set interfaces ge-0/0/3 unit 155 family inet address 10.50.63.71/32
set interfaces ge-0/0/3 unit 180 description SNL24050001_Keeley-Weissnat_FNA
set interfaces ge-0/0/3 unit 180 vlan-id 180
set interfaces ge-0/0/3 unit 180 family inet policer input SNL24050001_Keeley-Weissnat_FNA
set interfaces ge-0/0/3 unit 180 family inet policer output SNL24050001_Keeley-Weissnat_FNA
set interfaces ge-0/0/3 unit 180 family inet address 10.50.64.78/32
set interfaces ge-0/0/3 unit 202 description STT24060013_Ebony-Rohan_IPT
set interfaces ge-0/0/3 unit 202 vlan-id 202
set interfaces ge-0/0/3 unit 202 family inet policer input STT24060013_Ebony-Rohan_IPT
set interfaces ge-0/0/3 unit 202 family inet policer output STT24060013_Ebony-Rohan_IPT
set interfaces ge-0/0/3 unit 202 family inet address 10.50.202.202/32
set interfaces ge-0/0/3 unit 406 description STT24060002_Davonte-Quigley_FNA
set interfaces ge-0/0/3 unit 406 vlan-id 406
set interfaces ge-0/0/3 unit 406 family inet policer input STT24060002_Davonte-Quigley_FNA
set interfaces ge-0/0/3 unit 406 family inet policer output STT24060002_Davonte-Quigley_FNA
set interfaces ge-0/0/3 unit 406 family inet address 10.20.0.17/30
set interfaces ge-0/0/3 unit 500 description STT24060002_Davonte-Quigley_GGC
set interfaces ge-0/0/3 unit 500 vlan-id 500
set interfaces ge-0/0/3 unit 500 family inet policer input STT24060002_Davonte-Quigley_GGC
set interfaces ge-0/0/3 unit 500 family inet policer output STT24060002_Davonte-Quigley_GGC
set interfaces ge-0/0/3 unit 500 family inet address 10.20.0.21/30
set interfaces ge-0/0/3 unit 561 description STT24050005_Marc-Bergnaum_FNA
set interfaces ge-0/0/3 unit 561 vlan-id 561
set interfaces ge-0/0/3 unit 561 family inet policer input STT24050005_Marc-Bergnaum_FNA
set interfaces ge-0/0/3 unit 561 family inet policer output STT24050005_Marc-Bergnaum_FNA
set interfaces ge-0/0/3 unit 561 family inet address 10.50.31.39/32
set interfaces ge-0/0/4 description int-4
set interfaces ge-0/0/4 vlan-tagging    
set interfaces ge-0/0/4 unit 400 description STT24060002_Davonte-Quigley_IPT
set interfaces ge-0/0/4 unit 400 vlan-id 400
set interfaces ge-0/0/4 unit 400 family inet policer input STT24060002_Davonte-Quigley_IPT
set interfaces ge-0/0/4 unit 400 family inet policer output STT24060002_Davonte-Quigley_IPT
set interfaces ge-0/0/4 unit 400 family inet address 10.20.0.9/30
set interfaces ge-0/0/4 unit 1030 description STT24040002_Zelda-Labadie_IPT
set interfaces ge-0/0/4 unit 1030 vlan-id 1030
set interfaces ge-0/0/4 unit 1030 family inet policer input STT24040002_Zelda-Labadie_IPT
set interfaces ge-0/0/4 unit 1030 family inet policer output STT24040002_Zelda-Labadie_IPT
set interfaces ge-0/0/4 unit 1030 family inet address 10.11.29.14/30
set interfaces ge-0/0/5 description int-5
set interfaces ge-0/0/5 vlan-tagging    
set interfaces ge-0/0/5 unit 154 description STT24040002_Kirsten-Gorczany_GGC
set interfaces ge-0/0/5 unit 154 vlan-id 154
set interfaces ge-0/0/5 unit 154 family inet policer input STT24040002_Kirsten-Gorczany_GGC
set interfaces ge-0/0/5 unit 154 family inet policer output STT24040002_Kirsten-Gorczany_GGC
set interfaces ge-0/0/5 unit 154 family inet address 10.50.45.64/32
set interfaces ge-0/0/5 unit 564 description STT24050002_Alessandro-Krajcik_GGC
set interfaces ge-0/0/5 unit 564 vlan-id 564
set interfaces ge-0/0/5 unit 564 family inet policer input STT24050002_Alessandro-Krajcik_GGC
set interfaces ge-0/0/5 unit 564 family inet policer output STT24050002_Alessandro-Krajcik_GGC
set interfaces ge-0/0/5 unit 564 family inet address 10.50.64.45/32
set interfaces ge-0/0/6 description int-6
set interfaces ge-0/0/6 vlan-tagging    
set interfaces ge-0/0/6 unit 47 description STT24050007_Monte-Anderson_GGC
set interfaces ge-0/0/6 unit 47 vlan-id 47
set interfaces ge-0/0/6 unit 47 family inet policer input STT24050007_Monte-Anderson_GGC
set interfaces ge-0/0/6 unit 47 family inet policer output STT24050007_Monte-Anderson_GGC
set interfaces ge-0/0/6 unit 47 family inet address 10.50.48.79/32
set interfaces ge-0/0/6 unit 564 description STT24050008_Alana-Dooley_GGC
set interfaces ge-0/0/6 unit 564 vlan-id 564
set interfaces ge-0/0/6 unit 564 family inet policer input STT24050008_Alana-Dooley_GGC
set interfaces ge-0/0/6 unit 564 family inet policer output STT24050008_Alana-Dooley_GGC
set interfaces ge-0/0/6 unit 564 family inet address 10.50.31.49/32
set interfaces ge-0/0/7 description int-7
set interfaces ge-0/0/7 vlan-tagging    
set interfaces ge-0/0/8 description int-8
set interfaces ge-0/0/8 vlan-tagging    
set interfaces fxp0 unit 0 family inet dhcp vendor-id Juniper-vmx-VM6667F09327
set interfaces fxp0 unit 0 family inet6 dhcpv6-client client-type stateful
set interfaces fxp0 unit 0 family inet6 dhcpv6-client client-ia-type ia-na
set interfaces fxp0 unit 0 family inet6 dhcpv6-client client-identifier duid-type duid-ll
set interfaces fxp0 unit 0 family inet6 dhcpv6-client vendor-id Juniper:vmx:VM6667F09327
set firewall policer SNL24050001_Keeley-Weissnat_FNA if-exceeding bandwidth-limit 100m
set firewall policer SNL24050001_Keeley-Weissnat_FNA if-exceeding burst-size-limit 1m
set firewall policer SNL24050001_Keeley-Weissnat_FNA then discard
set firewall policer SNL24050001_Keeley-Weissnat_GGC if-exceeding bandwidth-limit 100m
set firewall policer SNL24050001_Keeley-Weissnat_GGC if-exceeding burst-size-limit 1m
set firewall policer SNL24050001_Keeley-Weissnat_GGC then discard
set firewall policer STT24040002_Kirsten-Gorczany_GGC if-exceeding bandwidth-limit 100m
set firewall policer STT24040002_Kirsten-Gorczany_GGC if-exceeding burst-size-limit 1m
set firewall policer STT24040002_Kirsten-Gorczany_GGC then discard
set firewall policer STT24040002_Zelda-Labadie_IPT if-exceeding bandwidth-limit 165m
set firewall policer STT24040002_Zelda-Labadie_IPT if-exceeding burst-size-limit 1m
set firewall policer STT24040002_Zelda-Labadie_IPT then discard
set firewall policer STT24050002_Alessandro-Krajcik_GGC if-exceeding bandwidth-limit 200m
set firewall policer STT24050002_Alessandro-Krajcik_GGC if-exceeding burst-size-limit 1m
set firewall policer STT24050002_Alessandro-Krajcik_GGC then discard
set firewall policer STT24050005_Marc-Bergnaum_FNA if-exceeding bandwidth-limit 100m
set firewall policer STT24050005_Marc-Bergnaum_FNA if-exceeding burst-size-limit 1m
set firewall policer STT24050005_Marc-Bergnaum_FNA then discard
set firewall policer STT24050007_Monte-Anderson_GGC if-exceeding bandwidth-limit 100m
set firewall policer STT24050007_Monte-Anderson_GGC if-exceeding burst-size-limit 1m
set firewall policer STT24050007_Monte-Anderson_GGC then discard
set firewall policer STT24050008_Alana-Dooley_GGC if-exceeding bandwidth-limit 100m
set firewall policer STT24050008_Alana-Dooley_GGC if-exceeding burst-size-limit 1m
set firewall policer STT24050008_Alana-Dooley_GGC then discard
set firewall policer STT24060002_Davonte-Quigley_FNA if-exceeding bandwidth-limit 100m
set firewall policer STT24060002_Davonte-Quigley_FNA if-exceeding burst-size-limit 1m
set firewall policer STT24060002_Davonte-Quigley_FNA then discard
set firewall policer STT24060002_Davonte-Quigley_GGC if-exceeding bandwidth-limit 100m
set firewall policer STT24060002_Davonte-Quigley_GGC if-exceeding burst-size-limit 1m
set firewall policer STT24060002_Davonte-Quigley_GGC then discard
set firewall policer STT24060002_Davonte-Quigley_IPT if-exceeding bandwidth-limit 100m
set firewall policer STT24060002_Davonte-Quigley_IPT if-exceeding burst-size-limit 1m
set firewall policer STT24060002_Davonte-Quigley_IPT then discard
set firewall policer STT24060013_Ebony-Rohan_IPT if-exceeding bandwidth-limit 100m
set firewall policer STT24060013_Ebony-Rohan_IPT if-exceeding burst-size-limit 1m
set firewall policer STT24060013_Ebony-Rohan_IPT then discard
set routing-instances PNI-RT interface ge-0/0/4.202
set routing-options static route 0.0.0.0/0 next-hop 103.134.26.213
set protocols router-advertisement interface fxp0.0
