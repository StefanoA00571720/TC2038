//Stefano Herrejoon

using namespace std;

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>



vector <int> sufijos(string texto){
    //Agregamos el simbolo de $
    texto.append("$");
    int n = texto.length();

    //vector vacio que llenaremos con los substrings
    vector<string> vecString;


    for(int i = 0;i<n;i++){
        //substr(indice del inicio de la cadena, longitud de la cadena)
        vecString.push_back(texto.substr(n-i-1,i+1));
    }

    sort(vecString.begin(),vecString.end());

    vector<int> respuesta(n);

    for(int i = 0;i<n;i++){
        respuesta[i] = n - vecString[i].size();
    }

    for (size_t i = 0; i < n; i++)
        respuesta[i] = n - vecString[i].size();
    
    return respuesta;
}


int main(){

    string oracion = "bcdeabcedeb";
    int n = oracion.length();

    cout << "String: " << oracion << " Suffix array: " <<endl;
    vector<int> respuesta = sufijos(oracion);

    for(int i = 0;i<=n;i++){
        cout<<respuesta[i]<<" ";
    }

    return 0;
}