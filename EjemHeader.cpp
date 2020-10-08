/**
 * Programa para ilustrar el uso de los headers
 * definidos por el usuario 
 */
//Incluyo el header de la librería estándar de entrada y salida
#include <iostream> 
using namespace std;

// Incluyo el header de la librería de usuario 
#include "suma.hpp" 

// Programa
int main() 
{ 
  
  // Definimos dos números 
  int a = 2, b = 100; 
  
  // Usamos la función declarada en el header 
  cout << "a+b= " << SumaEnteros(a, b) << endl; 
}
