from hostp2pd import HostP2pD
import time
print("wifi p2p")
with HostP2pD() as hostp2pd:
    time.sleep(40)
    if hostp2pd.addr_register:
        print("Station addresses:")
        for i in hostp2pd.addr_register:
            print("  {} = {:35s} ({})".format(i,
                    hostp2pd.addr_register[i],
                    (hostp2pd.dev_type_register[i]
                        if i in hostp2pd.dev_type_register
                        else "(unknown device type)")
                )
            )

print("Completed.")


#  This works on Linux systems only. My machine does not support it. 