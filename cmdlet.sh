Get-MessageTrackingLog -Server CGMXS1 -Start "06/14/2022 09:00:00" -End "06/15/2022 17:00:00" -Sender "ataur.rahman@cg-bd.com" | ConvertTo-Csv  > "D:\Mail_logs\message_track.csv" 

Get-MessageTraceDetail -MessageTraceId ded2b70b-cc9d-46d3-aa4a-08da4eb03e3d -RecipientAddress mahbub.alum@cgbd.com


# main part start

Search-MessageTrackingReport -Identity "Abu Tareq Khan" -Recipients "mahbub.alum@cg-bd.com" -BypassDelegateChecking | ConvertTo-Csv  > "D:\Mail_logs\message_track_report.csv"
 
Search-MessageTrackingReport -Identity "Abu Tareq Khan" -Sender "mahbub.alum@cg-bd.com" -BypassDelegateChecking | ConvertTo-Csv  > "D:\Mail_logs\message_track_report_replay.csv" 

# get details of a message by messageid
Get-MessageTrackingReport -Identity "Message-Id=<a3a6650b8e7d4a2e9c86bdb4512a7ed4@cg-bd.com>,Server=cgmxs1.cg-bd.com,Internal-Id=0,Sender=1d23cf09-a36e-4b0a-91fa-1495f6753a95,Domain=cg-bd.com" -DetailLevel Verbose -BypassDelegateChecking

# main part end

