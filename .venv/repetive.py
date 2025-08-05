import time


def traffic_light():
    for _ in range(5):  # Repeat the cycle 5 times
        print("🟥 Red Light")
        time.sleep(5)

        print("🟩 Red Light")
        time.sleep(5)

        print("🟨 Yellow Light")
        time.sleep(2)


traffic_light()
