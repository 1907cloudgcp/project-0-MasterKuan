from client.service.client import send_info


def transaction_service(session):
    reply = send_info("transactions", session)
    flag = reply[0]
    answer = reply[1]

    if flag == 0:
        print(answer)
        return 0

    if not answer:
        print("No transactions have been made yet")
        return 0

    try:
        for t in answer:
            print("{0}: ${1:.2f}".format(t[0], float(t[1])))
        return 1
    except ValueError:
        print("Error in viewing transaction history")
        return 0
