//Stefano Herrejon A00571720

using namespace std;

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

uint32_t murmur3Hash(const string &word) {
  const uint32_t seed = 0; // Seed value

  uint32_t hashValue = seed;
  const uint32_t c1 = 0xcc9e2d51;
  const uint32_t c2 = 0x1b873593;
  const uint32_t r1 = 15;
  const uint32_t r2 = 13;
  const uint32_t m = 5;
  const uint32_t n = 0xe6546b64;

  for (size_t i = 0; i < word.length(); ++i) {
    uint32_t k = word[i];
    k *= c1;
    k = (k << r1) | (k >> (32 - r1));
    k *= c2;

    hashValue ^= k;
    hashValue = ((hashValue << r2) | (hashValue >> (32 - r2))) * m + n;
  }

  hashValue ^= word.length();
  hashValue ^= hashValue >> 16;
  hashValue *= 0x85ebca6b;
  hashValue ^= hashValue >> 13;
  hashValue *= 0xc2b2ae35;
  hashValue ^= hashValue >> 16;

  return hashValue;
}

int main() {
    //Leer archivo

    ifstream archivo("PGD.txt");
    if (!archivo.is_open()) {
        cout << "Error al abrir el archivo." <<endl;
        return 1;
    } else {
        cout << "Todo Bien" <<endl;
    }

    string linea;

    map<long long, pair<string, int>> miMapa;

    while (getline(archivo, linea)) {
        istringstream iss(linea);
        string palabra;
        while (iss >> palabra) {
            unsigned long long hash_value = murmur3Hash(palabra);
            miMapa[hash_value].first = palabra;
            miMapa[hash_value].second += 1;
        }
    }

    archivo.close();

       // Copiar los elementos del mapa a un vector para ordenarlos
    vector<pair<long long, pair<string, int>>> vectorDePares(miMapa.begin(), miMapa.end());

    // Ordenar el vector en función del valor del numero
    sort(vectorDePares.begin(), vectorDePares.end(), [](const auto& a, const auto& b) {
        return a.second.second > b.second.second; // Ordenar
    });

    // Iterar a través del vector para mostrar los resultados

    long long repeticion = 1;
    for(const auto&par : vectorDePares){

        cout<<repeticion<<". "<<par.second.first<<" #: "<<par.second.second<<endl;
        repeticion++;
    }
  

    return 0;
}
