#!/opt/local/bin/python

from pmix import *

def main():
    foo = PMIxClient()
    print("Testing PMIx ", foo.get_version())
    info = {PMIX_PROGRAMMING_MODEL: ('TEST', PMIX_STRING), PMIX_MODEL_LIBRARY_NAME: ("PMIX", PMIX_STRING)}
    my_result = foo.init(info)
    print("Init result ", my_result)
    if 0 != my_result:
        print("FAILED TO INIT")
        exit(1)
    # try putting something
    print("PUT")
    rc = foo.put(PMIX_GLOBAL, "mykey", (1, PMIX_INT32))
    print("Put result ", rc);
    # commit it
    print("COMMIT")
    rc = foo.commit()
    print ("Commit result ", rc)
    # execute fence
    print("FENCE")
    procs = []
    info = {}
    rc = foo.fence(procs, info)
    print("Fence result ", rc)
    # finalize
    info = {}
    foo.finalize(info)
    print("Client finalize complete")
if __name__ == '__main__':
    main()
