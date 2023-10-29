import yaml
import os

data = {}

# Path to the files
directory      = "userdata/"
save_directory = "ips.txt"
###################
existing_uuids = open(save_directory, "r").readlines()

for filename in os.listdir(directory):
    if filename.endswith(".yml"):
        file_path = os.path.join(directory, filename)
        print(file_path)
        with open(file_path, "r") as file:
            yaml_data = yaml.safe_load(file)
            data[filename] = yaml_data
(d.pop() for d in data.keys() if d.removesuffix(".yml") in existing_uuids)
with open(save_directory, "a") as f:
    for yaml_data in data.keys():
        uuid = yaml_data.removesuffix(".yml")
        yaml_data = data[yaml_data]
        last_account_name = yaml_data["last-account-name"]
        ip_address = yaml_data["ip-address"]
        x = yaml_data["logoutlocation"]["x"]
        y = yaml_data["logoutlocation"]["y"]
        z = yaml_data["logoutlocation"]["z"]
        f.write(
            "[%s] %s | IP: %s | X: %s, Y: %s, Z: %s\n" % (
            uuid,
            last_account_name,
            ip_address,
            x,
            y,
            z
            )
        )

