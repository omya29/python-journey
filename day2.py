# DAY 2 - Lists, Loops, Functions
# Written by: Om Borude

# --- PROGRAM 1: Lists ---
suspicious_ips = ["192.168.1.10", "10.0.0.5", "172.16.0.1"]

print("All IPs:", suspicious_ips)
print("First IP:", suspicious_ips[0])
print("Second IP:", suspicious_ips[1])
print("Third IP:", suspicious_ips[2])
print("Total IPs:", len(suspicious_ips))



# --- PROGRAM 2: Modifying Lists ---
blocked_ips = ["10.0.0.1", "10.0.0.2"]
print("Before:", blocked_ips)

blocked_ips.append("192.168.1.99")
print("After adding:", blocked_ips)

blocked_ips.remove("10.0.0.1")
print("After removing:", blocked_ips)


# --- PROGRAM 3: Loop through list ---
failed_logins = ["192.168.1.10", "10.0.0.5",
                 "192.168.1.10", "172.16.0.1"]

print("All failed logins:")
for ip in failed_logins:
    print("Failed from:", ip)


    print("\nWith condition:")
for ip in failed_logins:
    if ip == "192.168.1.10":
        print("SUSPICIOUS:", ip)
    else:
        print("NORMAL:", ip)



# --- PROGRAM 4: Functions ---
def greet_user(name):
    print("Welcome,", name)

greet_user("Omkar")
greet_user("Admin")
greet_user("Security Team")



# --- PROGRAM 5: Function with return ---
def check_attempts(count):
    if count >= 10:
        return "CRITICAL"
    elif count >= 5:
        return "WARNING"
    elif count >= 3:
        return "CAUTION"
    else:
        return "NORMAL"

result1 = check_attempts(12)
result2 = check_attempts(6)
result3 = check_attempts(2)

print("IP1 status:", result1)
print("IP2 status:", result2)
print("IP3 status:", result3)



# --- PROGRAM 6: Mini Threat Detector ---

def get_threat_level(attempts):
    if attempts >= 5:
        return "DANGEROUS"
    elif attempts >= 3:
        return "SUSPICIOUS"
    else:
        return "NORMAL"

ip_list = ["192.168.1.10", "10.0.0.5",
           "172.16.0.1", "8.8.8.8"]

attempts_list = [7, 2, 4, 1]

print("==============================")
print("  CLOUDSENTINEL THREAT SCAN   ")
print("==============================")

for i in range(len(ip_list)):
    ip = ip_list[i]
    attempts = attempts_list[i]
    level = get_threat_level(attempts)
    print(ip, "|", attempts, "attempts |", level)

print("==============================")
print("Scan complete.")








