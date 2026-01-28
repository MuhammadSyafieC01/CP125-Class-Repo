def audit_zero_trust(baseline_set, current_log_list):
   baseline = set(baseline_set)
   log = set(current_log_list)

   authorized = set(baseline & log)
   alerts = set(log-baseline)
   inactive = set(baseline-log)

   print(f"Authorized:{authorized}\nAlerts:{alerts}\nInactive:{inactive}")

   return(authorized,alerts,inactive)

audit_zero_trust({( "u1", "192.168.1.1" ), ( "u2", "192.168.1.5" )}
, [( "u1", "192.168.1.1" ), ( "u3", "10.0.0.99" )])