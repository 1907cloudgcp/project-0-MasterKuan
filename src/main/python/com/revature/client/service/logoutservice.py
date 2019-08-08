from service.client import send_info


def logout_service(session):
    reply = send_info("logout", session)
    flag = reply[0]
    answer = reply[1]

    print(answer)
    if flag == 0:
        return 0
    return 1

