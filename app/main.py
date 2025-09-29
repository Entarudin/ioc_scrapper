from app.src.app import Application
from app.src.container import container


def main() -> None:
    app = Application(config=container.app_config, logger=container.app_logger)
    app.start()


if __name__ == "__main__":
    main()
