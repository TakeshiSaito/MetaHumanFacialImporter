from MetaHumanFacialImporter import Presenter
from MetaHumanFacialImporter.UseCase import ImportFacialAnimUseCase
from MetaHumanFacialImporter.View import MainWindow
import importlib


def run_main():
    importlib.reload(MainWindow)
    importlib.reload(Presenter)
    importlib.reload(ImportFacialAnimUseCase)

    main_window = MainWindow.MainWindow()
    presenter = Presenter.Presenter(main_window)
    presenter.show()


if __name__ == '__main__':
    run_main()