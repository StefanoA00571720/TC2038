//Stefano Herrejon A00571720

using namespace std;

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

int substring(string texto, string linea){

    int m = texto.length();//Filas
    int n = linea.length();//Columnas

    int ans = 0;
    int posT = 0;

    vector<vector<int>> matriz(m,vector<int>(n, 0));

    for(int i = 0;i<m;i++){


        for(int j = 0; j<n;j++){

            if(texto[i] == linea[j]){

                if(i == 0 || j == 0){

                    matriz[i][j] = 1;

                }else{

                    matriz[i][j] = matriz[i-1][j-1]+1;

                    if(matriz[i][j]>ans){
                        ans = matriz[i][j];
                        posT = i;
                    }

                }
            }
        }
    }

   // cout<<"ans : "<<ans<<" Pos de T : "<<posT<<endl;

    /*
    for(int i = 0;i<m;i++){
        for(int y = 0;y<n;y++){
            cout<<matriz[i][y]<<" ";
        }
        cout<<endl;
    }
    */

    for(int i = 1;i<=ans;i++){
        cout<<texto[posT-ans+i];
    }
    cout<<endl;

    return ans;
}


int main() {
    //Leer archivo

    ifstream archivo("PGD.txt");
    if (!archivo.is_open()) {
        cout << "Error al abrir el archivo." <<endl;
        return 1;
    }

    string dracula, linea;

    while (getline(archivo, linea)) {
        istringstream iss(linea);
        string palabra;
        while (iss >> palabra) {
            dracula = dracula + palabra;
        }
    }

    archivo.close();

    //cout<<dracula<<endl;

    string frase = "lookoutthereisDraculaouthere";
    //string frase = "aftergoingtothefarsideofthePass";
    //string frase = "helookuponthemtheyfeltfearintheirbodies";
    //string frase = "VampiresFangsBloodlust";
    //string frase = "TransylvaniaCastleCoffin";
    //string frase = "HauntingVictorianHorror";
    //string frase = "SeductionEternalNight";
    //string frase = "DraculianHordeCursedSoul";
    //string frase = "BookmadebyBramStoker";
    //string frase = "theroomlookquitewellandafter";


    cout<<"Tamaño del Substring más grande : "<<substring(dracula,frase)<<endl;

    return 0;
}
