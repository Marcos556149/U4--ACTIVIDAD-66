from RepositorioProvincias import RepositorioProvincias
from VistaGeneral import Vista
from ControladorProvincias import ControladorProvincias
from ClaseObjectEncoder import ObjectEncoder
def main():
    conn= ObjectEncoder()
    repo= RepositorioProvincias(conn)
    vista= Vista()
    ctrl= ControladorProvincias(repo,vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
if __name__=='__main__':
    main()


