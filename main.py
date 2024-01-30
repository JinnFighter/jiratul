# This is a sample Python script.
from jiratul_service import JiratulService


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    service = JiratulService()
    print("Service created")
    service.initialize()
    if service.isInitialized:
        print("Service initialized")

    service.terminate()
    if not service.isInitialized:
        print("Service terminated")
