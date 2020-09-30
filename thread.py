import threading
import concurrent.futures
import time
import math


def do_some(secs):
    print("Starting..")
    for i in range(10000000):
        sqrt = math.sqrt(i)
    # time.sleep(secs)
    return "Done"+str(secs)


start = time.perf_counter()

# manual
# ts = []
# for _ in range(10):
#     t = threading.Thread(target=do_some, args=[1])
#     t.start()
#     ts.append(t)

# for t in ts:
#     t.join()

# new method
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = [executor.submit(do_some, sec) for sec in secs]

#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

# executing in order
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1, 2, 3, 4, 5]
    results = executor.map(do_some, secs)

    for r in results:
        print(r)

end = time.perf_counter()
print(f"Time : {end-start}")
