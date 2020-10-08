/**
 *Definición de la función PrintTiempo
 */

#include <iostream>
#include "Tiempo.hpp"

void PrintTiempo(Tiempo t){
  std::cout << "Hora: " << t.hora << " Minuto: " << t.minuto << std::endl;
}
