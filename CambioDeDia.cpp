/**
 *Definición de la función CambioDeDia
 */ 

#include "CambioDeDia.hpp"

bool CambioDeDia(Tiempo d) {
  return d.hora >= 24 && d.minuto >= 60;
}
    
