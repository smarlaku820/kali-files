# ZEEK


Category
Description
Log Files
```
Network
Network protocol logs.
conn.log, dce_rpc.log, dhcp.log, dnp3.log, dns.log, ftp.log, http.log, irc.log, kerberos.log, modbus.log, modbus_register_change.log, mysql.log, ntlm.log, ntp.log, radius.log, rdp.log, rfb.log, sip.log, smb_cmd.log, smb_files.log, smb_mapping.log, smtp.log, snmp.log, socks.log, ssh.log, ssl.log, syslog.log, tunnel.log.

Files
File analysis result logs.
files.log, ocsp.log, pe.log, x509.log.

NetControl
Network control and flow logs.
netcontrol.log, netcontrol_drop.log, netcontrol_shunt.log, netcontrol_catch_release.log, openflow.log.

Detection
Detection and possible indicator logs.
intel.log, notice.log, notice_alarm.log, signatures.log, traceroute.log.

Network Observations
Network flow logs.
known_certs.log, known_hosts.log, known_modbus.log, known_services.log, software.log.

Miscellaneous
Additional logs cover external alerts, inputs and failures.
barnyard2.log, dpd.log, unified2.log, unknown_protocols.log, weird.log, weird_stats.log.

Zeek Diagnostic
Zeek diagnostic logs cover system messages, actions and some statistics.
broker.log, capture_loss.log, cluster.log, config.log, loaded_scripts.log, packet_filter.log, print.log, prof.log, reporter.log, stats.log, stderr.log, stdout.log.

Update Frequency	Log Name                  Description
Daily	                known_hosts.log	         List of hosts that completed TCP handshakes.
Daily	                known_services.log	 List of services used by hosts.
Daily	                known_certs.log	         List of SSL certificates.
Daily	                software.log	         List of software used on the network.
Per Session	        notice.log	         Anomalies detected by Zeek.
Per Session             intel.log	         Traffic contains malicious patterns/indicators.
Per Session             signatures.log	         List of triggered signatures.


Overall Info		Protocol Based	Detection	Observation
conn.log		http.log	notice.log	known_host.log
files.log		dns.log		signatures.log	known_services.log
intel.log		ftp.log		pe.log		software.log
loaded_scripts.log	ssh.log		traceroute.log	weird.log


```

## References
- [Zeek Scripting Language](https://try.bro.org/#/?example=hello)
