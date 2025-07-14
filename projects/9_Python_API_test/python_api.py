#/home/ubuntu/k8s-env/bin/python3

from kubernetes import client, config, watch

#load authentication
config.load_kube_config()

api = client.CoreV1Api()

def show_menu():
    print("Select an option: ")
    print("1. List All Pods")
    print("2. List All Services")
    print("3. Liast All Nodes ")
    print("Exit ")

while True:
    show_menu()
    choice = input("Enter our Choice: ")

    if choice == "1":
       pods = api.list_pod_for_all_namespaces()
       for pod in pods.items:
           print("%s: %s" % (pod.metadata.namespace,pod.metadata.name))

    elif choice == "2":
       services = api.list_service_for_all_namespaces()
       for svc in services.items:
           print("%s: %s" % (svc.metadata.namespace,svc.metadata.name))

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
