//Stefano Herrejon A00571720

using namespace std;

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>


unsigned long long polynomialHash(const string& palabra) {
    const int p = 31; // Número primo para la función hash
    const int m = 1e9 + 9; // Valor máximo de m para evitar desbordamientos

    unsigned long long hash_value = 0;
    unsigned long long p_pow = 1;

    for (char c : palabra) {
        hash_value = (hash_value + (c - 'a' + 1) * p_pow) % m;
        p_pow = (p_pow * p) % m;
    }

    return hash_value;
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
            unsigned long long hash_value = polynomialHash(palabra);
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
