import ansible_runner
import requests

if __name__ == "__main__":
    playbook_name = "hello.yml"

    
    #Run the playbook
    playbook_command = "ansible-playbook"+ " "+ playbook_name
    output = ansible_runner.interface.run_command(executable_cmd=playbook_command)

    #Print the output
    response, error_string, return_code = output
    print("\n"*4)
    print("Output: "+response)
    print("\n"*4)
    for i in range(3):
        response = requests.get("http://0.0.0.0")
        print("This is the message:", response.text)

    


