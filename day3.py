#day3 : dictionaries
#written by Om borude
#Date : 31 march 2026


#program 1 :Basic Dictionaries

failed_attempts = { "192.168.1.10":7 ,
                   "192.1.1.10":2,
                   "172.16.0.1":4}
print("Dictionary",failed_attempts)
print("Ip 192.1681.10:",failed_attempts["192.168.1.10"])
print("Ip 192.1.1.10:",failed_attempts["192.1.1.10"])



#program 2 :add & Update

failed_attempts["8.8.88.8"]=1  # add new ip
failed_attempts["192.168.1.10"]=8 # update existing ip 
del failed_attempts["172.16.0.1"]   # remove ip 
print(failed_attempts)

# program 3 : loop through dictionary 

for ip in failed_attempts:
    count=failed_attempts[ip]
    print(f"IP: {ip} | Failed attempts: {count}")

# --- PROGRAM 4: Loop with Condition ---
print("\n--- Threat Detection ---")

for ip in failed_attempts:
    count = failed_attempts[ip]
    if count >= 5:
        print(f"CRITICAL: {ip} - {count} attempts")
    elif count >= 3:
        print(f" SUSPICIOUS: {ip} - {count} attempts")
    else:
        print(f"NORMAL: {ip} - {count} attempts")



# --- PROGRAM 5: Safe Access with .get() ---
print("\n--- Safe Access ---")

# This would give error if key missing:
# print(failed_attempts["1.1.1.1"])

# This is safe:
count = failed_attempts.get("1.1.1.1", 0)
print("IP 1.1.1.1 attempts:", count)

# Get with default value
new_ip_count = failed_attempts.get("10.10.10.10", 0)
print("IP 10.10.10.10 attempts:", new_ip_count)



# --- PROGRAM 6: Real Log Parser ---
print("\n--- Log Parser ---")

def parse_logs(log_text):
    """Count failed attempts per IP from log text"""
    counts = {}
    
    lines = log_text.strip().split('\n')
    for line in lines:
        if "FAILED" in line:
            parts = line.split()
            if len(parts) > 0:
                ip = parts[0]
                # The important line:
                counts[ip] = counts.get(ip, 0) + 1
    
    return counts

def show_report(counts):
    """Display threat report"""
    print("\n" + "="*40)
    print("   CLOUDSENTINEL THREAT REPORT")
    print("="*40)
    
    for ip, count in counts.items():
        if count >= 5:
            print(f" {ip} : {count} attempts - CRITICAL")
        elif count >= 3:
            print(f" {ip} : {count} attempts - SUSPICIOUS")
        else:
            print(f" {ip} : {count} attempts - NORMAL")
    
    print("="*40)
    print(f"Total suspicious IPs: {len(counts)}")

# Test data
test_logs = """192.168.1.10 FAILED login attempt
192.168.1.10 FAILED login attempt
192.168.1.10 FAILED login attempt
192.168.1.10 FAILED login attempt
192.168.1.10 FAILED login attempt
10.0.0.5 FAILED login attempt
10.0.0.5 FAILED login attempt
192.168.1.20 SUCCESS login
172.16.0.1 FAILED login attempt
172.16.0.1 FAILED login attempt
172.16.0.1 FAILED login attempt"""

results = parse_logs(test_logs)
show_report(results)



# --- PROGRAM 7: File-Based Log Parser ---
print("\n--- File-Based Log Parser ---")

# Create a test log file
with open("test_logs.txt", "w") as f:
    f.write("192.168.1.10 FAILED login\n")
    f.write("192.168.1.10 FAILED login\n")
    f.write("192.168.1.10 FAILED login\n")
    f.write("10.0.0.5 FAILED login\n")
    f.write("172.16.0.1 SUCCESS login\n")
    f.write("172.16.0.1 FAILED login\n")
    f.write("172.16.0.1 FAILED login\n")

def parse_file(filename):
    """Read log file and count failed attempts"""
    counts = {}
    
    with open(filename, 'r') as file:
        for line in file:
            if "FAILED" in line:
                parts = line.split()
                if len(parts) > 0:
                    ip = parts[0]
                    counts[ip] = counts.get(ip, 0) + 1
    
    return counts

file_results = parse_file("test_logs.txt")
show_report(file_results)