import subprocess
import argparse

def ping_interface(interface_name, ip_address="192.168.72.135"):
    try:
        result = subprocess.run(
            ["ping", "-I", interface_name, "-c", "1", ip_address],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        return result.returncode == 0
    except Exception as e:
        return False

def test_interfaces(num_interfaces):
    connected_count = 0

    for i in range(1, num_interfaces + 1):
        interface_name = "oaitun_ue{}".format(i)
        if ping_interface(interface_name):
            print("Interface {} is connected.".format(interface_name))
            connected_count += 1
        else:
            print("Interface {} is not connected.".format(interface_name))

    return "Connected Interfaces: {}/{}".format(connected_count, num_interfaces)


def main():
    parser = argparse.ArgumentParser(description="Test network interfaces connectivity.")
    parser.add_argument(
        "num_interfaces",
        type=int,
        help="Number of interfaces to test"
    )

    args = parser.parse_args()
    result_summary = test_interfaces(args.num_interfaces)
    print(result_summary)

if __name__ == "__main__":
    main()
