def audit_blocklists(list_a, list_b, list_c):
    universal = set(list_a & list_b & list_c)
    redundant1 = list_a & list_b
    redundant2 = list_b & list_c
    redundant3 = list_c & list_a
    redundant = set(redundant1|redundant2|redundant3)
    uniqueaset = list_a - list_b - list_c

    print(f"Universal:{universal}\nRedundant:{redundant}\nUnique A Set:{uniqueaset}")
    return (universal,redundant,uniqueaset)


audit_blocklists({"malware.exe", "virus.zip"}
, {"virus.zip", "adware.dmg"}
, {"virus.zip", "spyware.exe"}
)