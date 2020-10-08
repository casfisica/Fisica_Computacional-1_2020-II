#include <iostream>
#include "Tiempo.hpp"
#include "CambioDeDia.hpp"

int main(){
  Tiempo t;
  t.hora = 2;
  t.minuto = 10;
  PrintTiempo(t);
  std::cout << "Cambio de dia?" << CambioDeDia(t) << std::endl;
  return 0;
}
