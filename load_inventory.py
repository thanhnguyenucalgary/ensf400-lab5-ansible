import ansible_runner
import json
if __name__ =="__main__":
    # Get the inventory information
    """The ansible_runner.interface.get_inventory return a tuple contain 2 elements: 
            Invertory Info in JSON String
            Warning Message in String form"""
    inventory_info_string, warning_message = ansible_runner.interface.get_inventory(action="list", inventories=["./hosts.yml"])
    #Convert string to dictionary form
    inventory_info_dict=json.loads(inventory_info_string)


    # Print the names, IP addresses
    print("\n\n\n\n")
    print("Print the names, IP addresses: ")
    # Extract and print names and IP addresses of the hosts
    for host, details in inventory_info_dict['_meta']['hostvars'].items():
        print(f"Name: {host}, IP Address: {details['ansible_host']}")   
    
   # Print group names of all hosts

    print("\n\n\n\n")
    group_list = inventory_info_dict["all"]["children"]

    # Print hosts in each group
    print("Print group names of all hosts")
    for group in group_list:
        print(f"Hosts in group {group}:")
        for host in inventory_info_dict[group]["hosts"]:
            print("\t"+host)

    # Ping all these hosts and output the results.

    """The ansible_runner.interface.run_command() function returns a tuple containing three elements: stdout, stderr, and return_code.
        stdout: This element contains the standard output of the command executed.
        stderr: This element contains the standard error output of the command executed.
        return_code: This element contains the return code of the executed command. Typically, a return code of 0 indicates success, while a non-zero return code indicates an error."""
    
    output_tuple = ansible_runner.interface.run_command(executable_cmd="ansible all:localhost -m ping") # the command to ping is "ansible all:localhost -m ping 
    stdout, stderr, return_code = output_tuple
    print(f"Response: \n{stdout}")